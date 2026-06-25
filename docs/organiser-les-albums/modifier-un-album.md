# Modifier un album

## Modifier un album depuis l’administration

Pour modifier un album dans l’administration de Piwigo, rendez vous sur la liste des albums depuis le menu Albums > Gérer.

Depuis la liste des albums, cliquez sur l’icône “Editer l’album” dans la liste. Une nouvelle page s’ouvre : celle de l’éditeur d’album.

![fr-editer-album-admin.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-512d7f03.png)

## Modifier un album depuis votre galerie

Vous pouvez également modifier un album depuis votre galerie si vous êtes administrateur.

Pour cela, rendez vous sur la page de l’album et cliquez sur l’icône “Editer l’album”.

En fonction de votre thème, cette icône pourra prendre la forme d’une clé à molette ou encore d’un crayon. Vous serez redirigé vers la fenêtre d’édition de l’album dans l’administration.

## Voir et modifier les propriétés d’un album

L’écran de modification d’un album vous offre de nombreuses possibilités.

<aside>
🆕 Les captures d’écran ci-dessous présentent la nouvelle version de l’éditeur d’album, disponible depuis la version 14 de Piwigo

</aside>

Penchons-nous d’abord sur le premier onglet “Propriétés”.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-2be2df5c.png)

### **Voir les informations de l’album**

L’écran affiche des informations sur votre album.

En en-tête de la page, vous retrouver le nom de l’album et son emplacement dans l’arborescence à gauche, ainsi que l’ID (identifiant unique) de l’album à droite.

Vous pouvez ensuite visualiser des informations sur l’album : date de création, de dernière modification, nombre de photos, nombre de sous-albums.

### **Modifier les propriétés de l’album**

L’onglet Propriétés permet de modifier différentes informations sur votre album.

- Modifier le nom de votre album
- Modifier la description de votre album

Si vous ajoutez une description à votre album, elle apparaîtra en-tête des photos de l’album sur votre galerie, comme dans l’exemple ci-dessous.

![fr-album-description.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-0b4b355b.png)

- Ajouter ou modifier un album parent à votre album

Vous pouvez ainsi déplacer un album à l’intérieur d’un autre album, le transformant ainsi en sous-album ; ou à l’inverse, déplacer un sous-album “à la racine” de votre galerie.

- Modifier la miniature / représentante de l’album

Par défaut, Piwigo choisit une image aléatoire parmi les photos d’un album pour “représenter” cet album dans les listes. On appelle cette photo la miniature de l’album.

Lorsque vous modifiez un album dans l’administration, vous pouvez modifier la miniature associée à cet album sur votre galerie, en passant la souris sur l’image et en cliquant sur “changer la miniature”. Piwigo fera défiler la liste des photos de cet album, jusqu’à ce que vous trouviez celle qui vous convient.

Vous pouvez également visiter la page d’une photo sur la galerie, et cliquer sur l’icône “choisir comme représentante de cet album”.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-3d45d5eb.png)

Si vous souhaitez qu’une photo en particulier illustre votre album, vous pouvez enfin éditer cette photo et choisir l’album qu’elle représente grâce au champ “Représentation des albums”. Avec cette fonctionnalité, vous pouvez ainsi choisir comme représentante d’un album une photo qui n’est même pas présente dans cet album ! [En savoir plus](../importer-et-gerer-les-photos/gerez-les-proprietes-et-metadonnees-de-vos-fichiers) 

### **Autoriser ou interdire les commentaires**

En bas de l’écran d’édition d’album, vous avez la possibilité d’autoriser ou interdire les commentaires pour les photos présentes dans cet album.

Pour gérer les commentaires dans les sous-albums, cliquer sur l’icône représentant 3 points en haut à droite.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-02970173.png)

[En savoir plus sur les commentaires](../les-commentaires-et-notes/commentaires-options-avancees)

### **Autres actions disponibles sur l’album**

Depuis la barre d’outils à droite, vous avez accès à plusieurs options.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-74b54b7e.png)

- Gérer les photos de l’album : cette icône vous permet de modifier en lot les photos de votre album. [En savoir plus sur la gestion par lot](../importer-et-gerer-les-photos/gestion-par-lot-modifier-et-gerer-une-selection-de-photos)
- Ajouter des photos : cette icône permet d’ajouter de nouveaux fichiers dans votre album
- Gérer les sous-albums : cette icône vous amène à la liste des albums, si vous avez besoin de modifier les sous-albums présents dans votre album
- Supprimer l’album : cette icône vous permet, au choix, de supprimer l’album et son contenu, ou de supprimer uniquement l’album (les photos qu’il contient seront alors considérées dans Piwigo comme “orphelines”).

Enfin, pour ouvrir votre album directement dans la galerie, cliquez sur le bouton en bas à gauche “Ouvrir dans la galerie”.

### **Verrouiller un album**

En bas de l’écran d’édition d’album, vous avez la possibilité de verrouiller un album.

!!! info
    Un album verrouillé est inaccessible sur la galerie, sauf pour les administrateurs. Le plus souvent, le statut verrouillé est utilisé lorsqu’un album n’est pas encore prêt à être rendu public sur la galerie, parce qu’un administrateur est en train de travailler dessus (préparation avant publication, maintenance…). C’est donc un statut “de travail”, temporaire.


Vous pouvez également verrouiller / déverrouiller une liste d’albums depuis le menu Albums > Propriétés > Verrouiller.

## Modifier l’ordre des photos dans un album

Quand vous éditez un album, le deuxième onglet “Ordre des photos” permet de modifier l’ordre des photos telles qu’elles s’affichent dans votre album.

!!! info
    Par défaut Piwigo classe les photos de la façon suivante : par date d’ajout (du plus récent au plus ancien), PUIS par nom du fichier (de A à Z), PUIS par identifiant (du plus petit au plus grand). Vous pouvez modifier ce paramètre dans les options de configuration de Piwigo. [En savoir plus](../personnaliser-ma-galerie/options-de-personnalisation-de-votre-galerie)


### **Modifier manuellement l’ordre des photos**

La première section “ordre manuel” vous permet de réorganiser comme bon vous semble l’ordre des photos par cliqué-glissé. Cliquez sur une photo et maintenez le clic : en déplaçant votre souris, vous pouvez déplacer la photo là où vous le souhaitez. Relâchez le clic lorsque votre photo est au bon endroit.

![fr-ordre-photos-manuel.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-137f96ef.png)

### **Modifier automatiquement l’ordre des photos**

La deuxième section “Ordre de tri” permet de modifier automatiquement l’ordre d’affichage des photos.

![fr-ordre-photo-auto.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-db6b9008.png)

Vous avez 3 options :

- Ordre de tri par défaut : c’est l’ordre de tri appliqué quand vous n’avez rien modifié. Dans ce cas les photos sont affichées par date et heure d’ajout à Piwigo.
- Ordre manuel : si vous avez déjà modifié manuellement l’ordre des photos dans votre album, cette option est automatiquement sélectionnée.
- Ordre automatique : si vous choisissez cette option, vous pourrez choisir d’appliquer un ordre automatique, parmi de nombreuses options comme le montre l’image ci-dessous.
    
    ![fr-ordre-photo-auto-2.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-15c37f9c.png)
    

Si vous le souhaitez, vous pouvez combiner plusieurs options, par exemple : classez les photos, par date d’ajout (du plus ancien au plus récent), PUIS par nom du fichier (de A à Z).

![fr-ordre-photo-auto-3.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-c4b50d55.png)

N’oubliez pas de cliquer sur Enregistrer les paramètres pour sauvegarder votre choix !

L’ordre de tri choisi peut être appliqué aux sous-albums (si votre album en a) en cochant la case à côté du bouton d’enregistrement.

### **Reset Manual Order**

Vous souhaitez classer les photos au sein d’un album en choisissant un ordre de tri automatique, mais en y apportant des modifications ? Pour cela vous pouvez activer le plugin **Reset Manual Order**.

Ce plugin ajoute une option “Réinitialiser l’ordre manuel avec l’ordre automatique en cours”. Cela applique à votre album un ordre de tri automatique, sur lequel ensuite vous pouvez effectuer des modifications manuellement.

## Modifier les permissions sur un album

Le troisième onglet de l’éditeur d’album est sans doute le plus important : il permet en effet de définir qui a le droit de visualiser cet album et son contenu sur votre galerie !

![fr-album-permissions.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-4df2ba8e.png)

Pour tout comprendre sur la gestion des permissions sur les albums, lisez l’article suivant :

[Permissions et visibilité des albums](permissions-et-visibilite-des-albums)

## Envoyer une notification sur un album

L’onglet Notification permet d’envoyer un email contenant un lien vers l’album à un ou plusieurs utilisateurs, ou même à tous les utilisateurs d’un groupe.

![fr-notif-album.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-5996131d.png)

Les personnes concernées recevront un email contenant un lien vers l’album, accompagné de votre message.

![fr-notif-album.email.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-63560b26.png)

!!! info
    Attention : avant d’envoyer une notification, pensez à vérifier que les utilisateurs ont bien accès à cet album dans l’onglet Permissions.
