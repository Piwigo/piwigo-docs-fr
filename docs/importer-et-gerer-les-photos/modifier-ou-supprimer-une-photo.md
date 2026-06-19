# Modifier ou supprimer une photo

En tant qu’administrateur de Piwigo, vous pouvez à tout moment avoir besoin de modifier une image ou un autre type de fichier.

Si vous cherchez à modifier un fichier en particulier, le plus simple est de passer par votre galerie !

Une fois que vous êtes sur la page de votre photo, cliquez sur le bouton en forme de crayon dans la barre d’outil.

![fr-edition-photo-galerie.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-b4679b47.png)

!!! info
    En fonction de votre thème, le bouton n’apparaîtra pas toujours au même endroit. Si vous ne voyez pas le bouton d’édition sur votre galerie, et que vous êtes bien administrateur, alors c’est que ce bouton a été masqué. Pour l’afficher, rendez vous dans l’administration de Piwigo, sur la page Configuration > Options, onglet “Afficher”, section “Page de la photo”, et cochez “Activer l’icône Éditer la photo”. [En savoir plus sur la configuration de Piwigo](/personnaliser-ma-galerie/options-de-personnalisation-de-votre-galerie)


La page d’édition de la photo s’ouvrira alors, ce qui vous permettra de modifier ses informations.

!!! info
    Vous pouvez également modifier une photo depuis l’administration, notamment depuis l’écran de [gestion par lot](/importer-et-gerer-les-photos/gestion-par-lot-modifier-et-gerer-une-selection-de-photos).


![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-2825e1e2.png)

## Aperçu, télécharger, supprimer, synchroniser les métadonnées

Lorsque vous êtes dans l’administration, sur la page d’édition d’une photo, une miniature de votre fichier apparaît sur la gauche.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-e6d936d3.png)

Depuis cette zone, plusieurs actions sont possibles :

- Agrandir la photo : pour cela, cliquer sur l’icône “agrandir”
- Afficher la photo sur votre galerie : pour cela, passez la souris sur l’image et cliquez sur le bouton “ouvrir dans la galerie” ; la page de cette photo sur votre galerie s’affichera dans un nouvel onglet
- Télécharger la photo : pour cela cliquez sur la 2ème icône, avec une flèche ; la version originale du fichier sera téléchargée sur votre ordinateur.
- Voir l’historique des visites de cette photos : pour cela cliquez sur l’icône en forme de graphique ;
- Synchroniser les métadonnées : pour cela cliquez sur la 4ème icône, avec deux flèches ; cela n’est utile que si des modifications ont été faites dans la configuration des métadonnées. [En savoir plus sur les métadonnées](/importer-et-gerer-les-photos/gerez-les-proprietes-et-metadonnees-de-vos-fichiers)
- Supprimer la photo : pour cela cliquez sur la 5ème icône représentant une poubelle.

## Les métadonnées de votre fichier

En haut à droite de l’éditeur de photo sont affichées certaines métadonnées de votre fichier (nom de fichier, taille et poids, format) ainsi que d’autres informations non modifiables depuis cet écran (date d’import, utilisateur de l’import, nombre de visites…).

![fr-editeur-photo-infos.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-415a97b6.png)

Les métadonnées sont des informations associées à vos photos et récupérées automatiquement depuis les métadonnées du fichier sources (pour en savoir plus, lisez l’article [Gérez les propriétés et métadonnées de vos fichiers](/importer-et-gerer-les-photos/gerez-les-proprietes-et-metadonnees-de-vos-fichiers)).

## Modifier les propriétés de votre fichier

Dans la partie droite de l’écran apparaissent les propriétés de votre fichier, que vous pouvez modifier : titre, description, auteur, date de création…

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-b781d625.png)

!!! Warning "Attention"
    N’oubliez pas de cliquer sur le bouton “Enregistrer les paramètres” pour sauvegarder vos modifications !


Pour en savoir plus sur les propriétés de vos fichiers, leur rôle, comprendre pourquoi et comment les modifier, et découvrir des options avancées, lisez l’article [Gérez les propriétés et métadonnées de vos fichiers](/importer-et-gerer-les-photos/gerez-les-proprietes-et-metadonnees-de-vos-fichiers).

## Modifier le centre d’intérêt d’une photo

La page d’édition d’une photo comporte un deuxième onglet : **Centre d’intérêt**.

Cet onglet permet de définir la partie la plus importante de votre photo, qui sera mise en avant lorsque la photo est retaillée, par exemple au format carré.

En haut de la page, vous voyez à quoi ressemble votre photo une fois retaillée au format carré, et en dessous, l’original. 

Parfois, le format carré ne convient pas car Piwigo coupe automatiquement une partie importante de votre image. Dans l’exemple ci-dessous, nous ne souhaitons pas que la photo soit coupée à droite.

![fr-centre-interet-photo.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-11badb30.png)

Pour modifier le centre d’intérêt, sur la photo affichée en dessous de la miniature, sélectionnez la zone la plus intéressante de votre photo à l’aide de votre souris, puis cliquez sur Valider.

![fr-modifier-centre-interet.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-3d1ee023.png)

Le format carré est mis à jour en fonction de vos modifications. 

C’est particulièrement utile si votre galerie affiche les miniatures des photos dans un format différent de l’original, par exemple en paysage alors que la photo originale est en portrait. C’est le cas avec le thème [**Bootstrap Darkroom**](/les-themes/le-theme-bootstrap-darkroo) par exemple.

## Photo Update : remplacer un fichier sans modifier ses propriétés

Depuis l’écran d’édition de la photo, il est possible de ré-importer un fichier pour remplacer le fichier d’origine, tout en conservant les propriétés de la photo.

Pour cela, vous devez installer le plugin **Photo Update**.

Une fois ce plugin activé, un nouvel onglet “Mettre à jour” s’ajoute dans l’écran d’édition de photo. Cet onglet permet d’importer un nouveau fichier pour remplacer le fichier existant.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-9cab24a1.png)

Il permet également également de mettre à jour l’image représentative d’un fichier non image (vidéo, audio, document…).

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-9ae534a3.png)

## Rotate Image: Faire pivoter une photo

Depuis l’écran d’édition de la photo, il est possible de de faire pivoter une photo si elle n’est pas dans le bon sens.

Pour cela, vous devez installer le plugin **Rotate Image**.

Une fois ce plugin activé, un nouvel onglet “Pivoter” s’ajoute dans l’écran d’édition de photo.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-4c71679e.png)

Sommaire de l’article

---

← Précédent

[Les différents formats de fichiers](/importer-et-gerer-les-photos/les-differents-formats-de-fichiers)

Suivant →

[Gestion par lot : Modifier et gérer une sélection de photos](/importer-et-gerer-les-photos/gestion-par-lot-modifier-et-gerer-une-selection-de-photos)
