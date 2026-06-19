# Importer des photos dans Piwigo

Il existe différentes possibilités pour importer des fichiers dans Piwigo. 

!!! info
    Nous parlons le plus souvent de photos, mais ce qui est valable pour les photos est valable en général pour n'importe quel type d'image, de vidéo, ou de document (voir l'article : [Les différents formats de fichiers dans Piwigo](/importer-et-gerer-les-photos/les-differents-formats-de-fichiers)).


Cet article vous permet de découvrir comment ajouter des fichiers :

- depuis l'administration de Piwigo
- depuis votre galerie (pour les utilisateurs non administrateurs)
- depuis d'autres sources

!!! Warning "Attention"
    Certaines options comme l’import FTP ne sont disponibles que pour les utilisateurs qui hébergent eux-mêmes leur Piwigo.


## **Importez des photos depuis l'administration de Piwigo**

Pour importer des photos (ou tout autre type de fichier) depuis l'administration de Piwigo, rendez-vous dans l'administration.

Sur le menu de gauche, sélectionnez Photos > Ajouter. Vous arrivez sur la page d'Ajout de photo.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-1f6768b7.png)

### Choisir l’album de destination de vos photos

Pour importer des fichiers dans Piwigo, vous devez d'abord choisir un album en cliquant sur l’icône à côté de "Choisir un album". Cela ouvre une fenêtre qui liste les  les albums existants. Les albums avec des sous-albums apparaissent avec une flèche sur la gauche, vous pouvez dérouler l’arborescence en cliquant sur la flèche. Vous pouvez recherche l’album de votre choix par nom.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-88fd9280.png)

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-4628dcb6.png)

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-4d44166a.png)

Cliquez sur le + à côté d’un album pour le sélectionner.

Vous pouvez également créer un nouvel album en cliquant sur “Mode Création”. Choisissez l’album parent dans la liste pour créer un sous-album, ou cliquez sur “Créer un album racine” pour créer un album au premier niveau de votre espace Piwigo. Donnez un nom à l’album, choisissez si vous souhaitez l’afficher au début ou à la fin de la liste des albums, et cliquez sur “Créer et sélectionner”.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-42d1d0c4.png)

### Importer les fichiers dans Piwigo

Une fois l'album choisi, vous avez deux possibilités pour importer des fichiers depuis votre ordinateur :

- Cliquer sur le bouton Ajouter des photos, et sélectionner les fichiers souhaités sur votre ordinateur.
- Glisser et déposer des fichiers directement depuis un dossier de votre ordinateur vers la zone grise, comme on le voit sur l'exemple ci-dessous.

![](https://s3.amazonaws.com/helpscout.net/docs/assets/61e7cec9c1b8c85d97faea30/images/622b252fc1e53608cf9e762f/file-TNIliqYNyQ.gif)

Au fur et à mesure, vos fichiers s'affichent à l'écran. Ils sont dans une sorte de file d'attente. Vous pouvez visualiser leur nom, et leur taille. Si vous souhaitez finalement ne pas importer l'un des fichiers, il suffit de cliquer sur la croix à droite.

![](https://s3.amazonaws.com/helpscout.net/docs/assets/61e7cec9c1b8c85d97faea30/images/622b25bcc1e53608cf9e7633/file-Ycg0YJmaHg.png)

Une fois que vous êtes satisfait, cliquez sur le bouton "Démarrer le transfert".

Au fur et à mesure que Piwigo importe vos fichiers, ils disparaissent de la liste. Une fois l'import terminé, vous pouvez choisir

- de modifier par lot les propriétés des photos en cliquant sur "Gérer ce lot de photos"
- ou d'ajouter d'autres fichiers en cliquant sur "Ajouter d'autres photos"

![](https://s3.amazonaws.com/helpscout.net/docs/assets/61e7cec9c1b8c85d97faea30/images/622b270cc1688a6d26a74394/file-ejk1UpCsn2.gif)

## Détecter les doublons à l’import

Lorsque vous importer des fichiers dans Piwigo, Piwigo peut détecter les doublons et ne pas les importer.

Lors de l'ajout de photos, si vous importez un fichier identique à un fichier déjà présent dans votre Piwigo, alors Piwigo va associer le fichier existant à l'album d'import, mais ne va pas dupliquer le fichier.

Vous pouvez activer ou désactiver cette option depuis l’administration, menu Configuration > Options, onglet Général, section Divers.

![detection-doublons.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-45b4ca88.png)

## **Redimensionner les photos à l'import**

Pour configurer la taille des fichiers importés sur votre galerie, rendez-vous dans l'administration, et dans le menu de gauche, cliquez sur Configuration > Options. Cliquez ensuite sur l'onglet "Tailles de photos".

![](https://s3.amazonaws.com/helpscout.net/docs/assets/61e7cec9c1b8c85d97faea30/images/62384f232ce7ed0fb0917a8f/file-bYE5frbO56.png)

Par défaut, Piwigo importe le fichier dans sa taille originale.

Si vous le souhaitez, vous pouvez demander à Piwigo de redimensionner automatiquement les fichiers au moment de l'import.

**❓ Pourquoi redimensionner les photos à l'import ?**

Cela peut être utile, si vous avez des photos originales dans une très haute résolution, et que vous n'avez pas besoin d'afficher vos photos dans leur résolution optimale sur votre photothèque. Les avantages sont les suivants :

- Cela diminue la taille des fichiers, et donc vos besoins en espace de stockage
- Cela réduit les besoins en ressources du serveur

En revanche, on déconseille de redimensionner les photos si Piwigo est l'endroit où vous centralisez le stockage de vos fichiers. En redimensionnant les fichiers, vous perdez en qualité. Si vous envoyez vers Piwigo une version dégradée de vos images, veillez à conserver les originaux dans un autre espace sécurisé (par exemple, sur un disque dur avec une sauvegarde).

Pour automatisez le redimensionnement de vos photos, dans la page Configuration > Tailles de photos, cochez la case "Redimensionner après transfert". Vous pouvez choisir :

- La largeur maximum de vos photos (en pixels)
- La hauteur maximum de vos photos (en pixels)
- La qualité d'image après redimensionnement (en pourcentage)

![](https://s3.amazonaws.com/helpscout.net/docs/assets/61e7cec9c1b8c85d97faea30/images/62384f57c1e53608cf9eabc5/file-coYVOF7nhB.png)

## Mettre à jour les fichiers après un import

Lorsque vous venez d’importer un lot de fichiers dans Piwigo, vous avez la possibilité d’éditer leurs propriétés dans la foulée, en cliquant “Gérer ce lot de photos”.

![fr-gerer-lot-photo-import.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-474880d2.png)

Cela a pour effet d’ajouter la sélection dans votre panier. Vous arrivez alors sur la page “Gestion par lot”, filtrée sur les photos que vous venez d’importer.

Vous avez la possibilité d’apporter des modifications aux fichiers de votre import :

- soit en lot, en restant sur l’onglet en cours (Mode global)
- soit unitairement, fichier par fichier, en cliquant sur l’onglet “Mode unitaire”.

![fr-edition-photos-import.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-92097be6.png)

Pour comprendre comment utiliser la gestion par lot, [lisez cet article](/importer-et-gerer-les-photos/gestion-par-lot-modifier-et-gerer-une-selection-de-photos).

## **Importez des photos depuis votre galerie**

Vous souhaitez qu'un utilisateur puisse ajouter des photos dans Piwigo, sans être administrateur ? C'est possible avec le plugin Community.

Ce plugin permet de donner le droit aux utilisateurs non administrateurs d'ajouter des photos dans Piwigo, depuis une page dédiée de votre galerie.

[Consultez la documentation de Community](/les-utilisateurs/gerer-les-contributeurs-plugin-community)

## **Importez des fichiers depuis votre téléphone mobile**

Vous pouvez connecter votre téléphone ou votre tablette à Piwigo pour y créer des albums et ajouter des photos et vidéos vers votre galerie. Pour cela, installez une des [applications mobiles](/les-applications-mobiles) officielles Piwigo.

## **Importez des fichiers depuis un répertoire de votre ordinateur avec Piwigo Remote Sync**

Il est possible de synchroniser automatiquement un répertoire de votre ordinateur avec Piwigo, et même d'ajouter une arborescence complète de répertoires.

A chaque fois que vous lancerez la synchronisation, seules les nouvelles photos seront ajoutées.

Pour cela, vous devez installer l’application [Piwigo Remote Sync](https://piwigo.org/ext/extension_view.php?eid=851) sur votre ordinateur. Ce logiciel est compatible Mac, Windows et Linux.

Pour en savoir plus, lisez la documentation dédiée en cliquant sur le lien ci-dessous :

[Documentation : Piwigo Remote Sync](/importer-et-gerer-les-photos/importer-des-photos-dans-piwigo/documentation-piwigo-remote-sync)

## **Importez et synchronisez un répertoire de votre ordinateur en FTP**

Si vous utilisez un Piwigo hébergé sur votre propre serveur, et non un Piwigo hébergé sur piwigo.com, vous pouvez synchroniser un répertoire de votre ordinateur avec votre galerie.

Pour cela, vous aurez besoin d’un logiciel client FTP.

Pour en savoir plus, lisez l’article ci-dessous.

[Import et synchronisation de photos FTP](/hebergez-votre-piwigo/import-et-synchronisation-de-photos-ftp)

## **Importez des fichiers depuis Adobe Lightroom**

Si vous utilisez le gestionnaire de photos Adobe Lightroom, vous pouvez installer un plugin qui vous permettra de transférer vos photos directement vers votre Piwigo. Ce plugin n’est pas développé par Piwigo. Il est vendu 15$ par son concepteur.

[Rendez-vous sur cette page pour en savoir plus](https://alloyphoto.com/plugins/piwigo/)

Une documentation du plugin Lightroom pour Piwigo existe, mais attention : elle date de la version 1.6.2 r1034 du plugin. Nous en sommes aujourd’hui à la version 3.1.0 (publiée en octobre 2021), elle peut donc être incomplète.

[Documentation : Plugin Piwigo pour Lightroom](/importer-et-gerer-les-photos/importer-des-photos-dans-piwigo/documentation-plugin-piwigo-pour-lightroo)

## **Importez des fichiers depuis Digikam**

[Digikam](https://www.digikam.org/) est un logiciel libre de gestion de photos compatible Linux, Windows et Mac. Il dispose d’un plugin d’export vers Piwigo qui permet de transférer des photos depuis Digikam vers Piwigo.

[Rendez-vous sur cette page pour en savoir plus](https://docs.digikam.org/en/export_tools/piwigo_export.html)

## **Importez des fichiers depuis Shotwell**

[Shotwell](https://wiki.gnome.org/Apps/Shotwell) est un gestionnaire de photos open source pour Linux. Il est installé par défaut sur Ubuntu et Fedora. Un plugin pour Shotwell permet d’exporter des photos vers Piwigo.

[Télécharger le connecteur sur GitHub](https://github.com/guillaumev/piwigoshotwell)

## Importez des photos depuis votre compte Flickr

Vous avez des photos sur un compte Flickr et vous souhaitez les importer sur Piwigo ? C’est possible !

Pour cela, installez le plugin Flickr2Piwigo.

!!! info
    Si vous utilisez Piwigo sur votre propre hébergement, vérifiez bien que vous avez la dernière version du plugin.

La page de configuration du plugin explique les différentes étapes pour connecter votre Piwigo à Flickr.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-61e52c7a.png)

Vous devez tout d’abord vous connecter à votre compte Flickr et vous rendre sur [cette page](https://www.flickr.com/services/apps/create/apply/) pour créer votre clé API.

Sur la première page, choisissez l’option “Demander une clé non commerciale”.

Sur la page suivante, remplissez les champs Nom et Description de votre clé, par exemple comme ci-dessous. Cochez bien les deux cases pour accepter les conditions et cliquez sur “Soumettre”.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-5afbb653.png)

Flickr va alors vous afficher deux chaînes de caractères : “Clé” et “Secret”.

Retournez dans la configuration du plugin Flickr2Piwigo, et coller ces deux chaînes de caractères dans les champs “Clé API” et “Secret API”. Enregistrez les paramètres.

Toujours dans la configuration du plugin, allez dans l’onglet “Importation et cliquez sur “Connexion”. Vous allez être redirigé vers une page Flickr. Cliquez sur ”OK, je l’autorise”.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-b552d385.png)

Ça y est, vous êtes connecté !

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-5d90af2f.png)

Vous avez alors la possibilité de :

- Lister vos albums Flickr et choisir, pour chaque album, quelles photos vous souhaitez importer dans Piwigo ;
- Importez toutes les photos de votre compte Flickr.

### Lister vos albums Flickr

Si vous choisissez cette option, la liste des albums de votre compte Flickr va s’afficher. Cliquer sur un album pour choisir les photos à importer dans Piwigo. Vous pouvez cocher les photos à importer et choisir dans quel album les importer. Vous pouvez également choisir ou pas d’importer les données de description de vos photos depuis Flickr vers Piwigo (nom de la photo, auteur, date de création, tags…)

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-0f1b0419.png)

### Importer toutes les photos de votre compte Flickr

Si vous choisissez cette option, vous allez pouvoir choisir de recréer tous vos albums Flickr dans Piwigo, ou bien d’importer toutes les photos de Flickr dans l’album de votre choix. Vous pouvez également choisir ou pas d’importer les données de description de vos photos depuis Flickr vers Piwigo (nom de la photo, auteur, date de création, tags…)

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-529cb532.png)

Et voilà !

Comme vous pouvez le voir, importer les photos depuis votre compte Flickr dans Piwigo, c’est très facile 🙂

Sommaire de l’article

---

Suivant →

[Les différents formats de fichiers](/importer-et-gerer-les-photos/les-differents-formats-de-fichiers)
