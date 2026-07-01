# Problèmes de génération des vignettes et des miniatures

!!! info
    Lire aussi : [Importer des photos dans Piwigo](../importer-et-gerer-les-photos/importer-des-photos-dans-piwigo)

Lorsque vous téléchargez des fichiers sur Piwigo, tout un processus se met en route. Les fichiers sont téléchargés sur le serveur mais aussi enregistrés dans la base de données, et d'autres fichiers sont générés à la volée :

- plusieurs fichiers sont créés lorsque Piwigo génère plusieurs tailles de votre image, y compris les vignettes qui seront affichées dans votre galerie ;
- pour certains formats de fichiers (vidéos, PDF,...) des images sont générées pour être affichées à la place du fichier source dans votre galerie : c'est ce que nous appelons parfois des “représentants”, ou miniatures.

La génération des tailles multiples et des miniatures peut échouer si quelque chose n'est pas configuré correctement sur votre serveur. En effet, Piwigo utilise des librairies externes pour faire ce travail.

Si vous gérez vous-même votre serveur, vous allez devoir investiguer pour résoudre ce problème : c'est ce que nous allons expliquer dans cet article.

!!! Warning "Attention"
    Cet article s'adresse uniquement aux webmasters d'une bibliothèque Piwigo auto-hébergée. Si vous êtes client de Piwigo Cloud, vous n'êtes pas concerné : l'environnement d'hébergement sur Piwigo Cloud est optimisé.


## 1- Problèmes de génération de vignettes de photos

Vous avez importé des photos dans un album, mais vous ne voyez pas les images sur votre galerie Piwigo ? Cela peut être dû à un problème de génération de vignettes.

Pour vous en assurer, rendez-vous dans l’administration, menu “Gestion par lots”, et sélectionnez votre album. Une fois le filtre validé, des vignettes devraient apparaître. Si vous voyez « Aucune photo sélectionnée parmi les 12 photos du lot » mais des carrés vides, c'est qu'il y a un problème de vignettes.

### Vérifier si une erreur est renvoyée par l'url i.php

!!! info
    Piwigo a un système de génération automatique des miniatures et autres images retaillées. Piwigo appelle le fichier i.php pour générer les images retaillées dans `./_data/i/`, puis une fois que l'image retaillée a été générée dans ce cache, Piwigo appelle directement l'image retaillée depuis `./_data/i/`. Ainsi plusieurs problèmes peuvent apparaître : surcharge serveur, image trop grosse/lourde ou avec une mauvaise extension de fichier, pas assez de permission sur les fichiers/dossiers…

Dans la Gestion par lots, faites un clic droit sur une image qui a échoué puis « Afficher l'image » ou « copier l'url de l'image », à partir de votre navigateur. Vous pouvez également essayer d'afficher le code source de la page (Ctrl+U en général) et rechercher (Ctrl+F) une url avec « i.php ». Allez ensuite à cette url avec votre navigateur et notez tout message d'erreur affiché.

Voici les messages d'erreur que vous pouvez trouver :

1. “source not found” : vérifiez par Ftp si l'image source/d'origine existe bien (dans upload ou galleries, c'est marqué dans l'url après “i.php?”. D'ailleurs, si ce chemin est faux, postez sur le forum) et si les permissions sur les fichiers et dossiers sont suffisantes (Chmod : 755 folders, 644 files). Si cela ne marche toujours pas, vérifiez que l'utilisateur système Php a assez de droits sur votre serveur (contactez votre hébergeur)
2. “dir create error” : vérifiez par Ftp si les permissions sur les fichiers et dossiers sont suffisantes (Chmod : 755 folders, 644 files). Si cela ne marche toujours pas, vérifiez que l'utilisateur système Php a assez de droits sur votre serveur (contactez votre hébergeur)
3. “Empty array while parsing Sizing” “Sizing arr” “Invalid chars in request”… : un thème ou plugin ne marche pas correctement : assurez-vous qu'ils soient à jour et compatibles avec votre version de Piwigo.
4. 404 error page : le fichier i.php est manquant. Téléchargez le package complet depuis piwigo.org, extrayez les fichiers et uploadez les par Ftp en écrasant les fichiers existants (vous ne perdrez aucune configuration).
5. 403 error page : vérifiez les permissions de i.php. Chmod : 755 dossiers, 644 fichiers.
6. “500 Internal error page” ou “PHP Fatal Error: Allowed memory size of …” : plusieurs problèmes peuvent générer ces erreurs. Si quelques images sont générées et d'autres non, cela peut être du à une surcharge temporaire de votre serveur : attendez ou contactez votre hébergeur. Il est aussi possible que la mémoire allouée à Php soit insuffisante pour les images que vous avez uploadées : augmentez ou demandez à votre hébergeur d'augmenter memory_limit. Si la librairie graphique est GD, nous recommandons fortement l'utilisation de Imagemagick à la place : lisez le paragraphe au sujet d'Imagemagick plus bas.

Pas de message d'erreur ?

1. Avec le plugin Localfiles Editor, ajoutez cette ligne `$conf['enable_i_log']` = true;” à la configuration locale. Ensuite essayez de générer des images via le Gestionnaire par Lot. Une fois ceci fait, allez chercher par Ftp le fichier _data/tmp/i.log et ouvrez le afin de vérifier la présence éventuelle d'erreurs.
2. Vous pouvez aussi lire les instructions ci-dessus pour “500 Internal error page” et utiliser **Imagemagick**.

### Installer Imagemagick

**GD Graphics Library** et **ImageMagick** sont deux bibliothèques open source pour la génération d'images dynamiques. Vous pouvez rencontrer des problèmes avec la génération de vignettes (entre autres) si votre serveur utilise la bibliothèque graphique GD.

C'est pourquoi nous vous recommandons de passer à **ImageMagick**. ImageMagick est disponible dans la plupart des hébergements mutualisés. 

Tout d'abord, Imagemagick doit être installé si ce n'est pas déjà fait. Ensuite, vous pouvez indiquer à Piwigo où se trouvent les fichiers.

Pour ce faire, ajoutez les variables suivantes avec Localfiles Editor. Vous devez d'abord demander à votre hébergeur le chemin vers les binaires d'ImageMagick.

```php
// Library used for image resizing. Value could be 'auto', 'imagick',
// 'ext_imagick' or 'gd'. If value is 'auto', library will be choosen in this
// order. If choosen library is not available, another one will be picked up.
$conf['graphics_library'] = 'ext_imagick';
// If library used is external installation of ImageMagick ('ext_imagick'),
// you can define imagemagick directory.
$conf['ext_imagick_dir'] = '/usr/local/bin/';//À changer selon votre installation!
```

Pour vérifier quelle bibliothèque graphique est utilisée dans votre environnement, vous pouvez aller dans l'administration, menu Outils > Maintenance, et aller sur l'onglet Environnement.

![ext-image-magick.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-7b656060.png)

!!! Warning "Attention"
    Attention ! Il est possible que votre serveur n’utilise pas ImageMagick mais Imagick, une fonctionnalité PHP qui “encapsule” ImageMagick, mais qui ne permet pas de générer les prévisualisations pour certains formats de fichiers. Assurez vous bien d’utiliser **External Image Magick.**

## 2- Problèmes de génération de miniatures vidéo

Vous pouvez télécharger des vidéos sur votre Piwigo en utilisant le plugin VideoJS et en ajoutant du code à votre configuration locale [(comme expliqué ici).](../importer-et-gerer-les-photos/les-differents-formats-de-fichiers)

Mais ce plugin a besoin de la bibliothèque **ffmpeg** pour fonctionner correctement. Si elle n'est pas installée sur votre serveur, Piwigo ne pourra pas exécuter la commande qui génère les vignettes.

Dans ce cas, il peut y avoir deux conséquences :

- Soit la vidéo est ajoutée à votre galerie mais aucune image n'est générée, elle est donc représentée par une icône par défaut ;
- Soit la vidéo n'est pas du tout ajoutée à votre galerie.

Donc, si vous voulez que les vidéos fonctionnent correctement sur votre Piwigo, vous devez vérifier si ffmpeg est installé. Si c'est le cas, c'est bon : il suffit d'indiquer à Piwigo où se trouvent les fichiers.

Pour ce faire, ajoutez les variables suivantes avec Localfiles Editor. Vous devez d'abord demander à votre hébergeur le chemin vers les binaires de ffmpeg, et remplacer le code par le chemin sur votre propre serveur.

```php
$conf['ffmpeg_dir'] = '../../apps/ffmeg/';
```

Si vous avez besoin de plus de support technique sur ce sujet, consultez la [documentation VideoJS sur GitHub](https://github.com/Piwigo/piwigo-videojs/wiki/How-to-add-videos#step-2-install) : vous y trouverez des instructions détaillées sur l'installation de **ffmpeg**.

!!! Warning "Attention"
    Si **ffmpeg** n'est pas disponible sur votre hébergement web, vous ne pouvez pas importer correctement des vidéos sur votre Piwigo. Nous vous recommandons de changer d'hébergeur.

## 3- Problèmes de génération de vignettes PDF, PSD, HEIC et autres formats

Vous pouvez télécharger des fichiers PDF sur Piwigo, [comme expliqué ici](../importer-et-gerer-les-photos/les-differents-formats-de-fichiers).

Piwigo génère une vignette pour représenter votre fichier PDF, en extrayant la première page du fichier et en la convertissant en image.

Mais parfois, après avoir téléchargé un fichier PDF sur Piwigo, vous verrez une icône à la place de la vignette, comme dans l'exemple ci-dessous.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-a8dd8b8f.png)

Sur votre galerie, votre PDF sera également affiché avec cette icône par défaut.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-60382354.png)

Dans ce cas, le fichier est correctement téléchargé sur Piwigo, et peut être téléchargé en cliquant sur l'icône « Télécharger le fichier ». Mais les vignettes ne sont pas générées correctement.

Pour régler ce problème, vérifiez si la bibliothèque **External** **ImageMagick** est installée et, le cas échéant, déclarez son chemin dans la configuration locale (comme expliqué dans un chapitre précédent de cette page).

Ce problème ne concerne pas que les PDF : il empêche également de générer des vignettes pour les fichiers PSD, AI, TIF, TIFF, et HEIC.
