# Créer et gérer les tags

Les tags sont un outil essentiel pour organiser votre photothèque et faciliter vos recherches de contenu. Comment les créer et les organiser dans Piwigo ?

## Comment créer des tags ?

Il existe plusieurs manières de créer des tags. Vous pouvez les créer vous-même dans l’administration de Piwigo ; ils peuvent également être importés depuis votre ordinateur si vous utilisez déjà un système de mots-clés pour classer vos photos, ou depuis un logiciel tiers comme Lightroom. 

Pour en savoir plus sur l’import de photo, [lisez cet article](../importer-et-gerer-les-photos/importer-des-photos-dans-piwigo).

### Créer un tag dans l’administration

Pour créer un tag, rendez-vous dans l’administration, cliquez sur le menu de gauche sur Photos > Tags.

Vous arrivez sur le gestionnaire de tags, qui liste les tags existants, permet de les modifier et d’en créer de nouveaux.

![fr-liste-tags.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-12b57083.png)

Pour créer un tag, cliquez sur “Ajouter un tag”, saisissez le libellé du tag et cliquez sur le bouton + ou appuyez sur la touche “Entrée” de votre clavier. Le tag est créé.

![fr-tag-creer.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-007c569a.png)

Vous pouvez également créer un tag directement à chaque fois que vous avez la possibilité d’affecter un tag à une photo :

- depuis l’éditeur de photo
- depuis le gestionnaire de lot

### **Add tags mass :** Créer une liste de tags en masse

Si vous avez besoin d’importer dans votre Piwigo une liste de tags existants ou de créer rapidement plusieurs tags, il suffit d’activer le plugin “Add tags mass”.

!!! info 
    Si vous êtes client d’une offre Piwigo Cloud, ce plugin n’est accessible qu’à partir de l’offre Équipe.

Une fois ce plugin activé, rendez vous dans la configuration du plugin pour ajouter des tags en masse.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-8833fa8e.png)

Il suffit d’ajouter des tags les uns à la suite des autres, ligne par ligne, dans le formulaire et de cliquer sur Valider pour les enregistrer.

!!! info
    Vous pouvez copier coller une liste de tags dans ce formulaire depuis un tableur (Excel par exemple).

### Importer les tags depuis vos mots-clés IPTC

Peut-être que vos photos sont déjà taguées avec des mots-clés, ajoutés depuis un logiciel de traitement photo comme Lightroom.

Ces mots-clés font partie des métadonnées IPTC de vos photos, et peuvent être importés dans Piwigo sous forme de tags.

C’est le cas par défaut : si vous souhaitez modifier cette configuration, vous devez contacter le support si vous êtes client d’une offre Piwigo Cloud.

!!! Warning "Attention" 
    Piwigo ne prend pas en charge l’import des tags que vous pouvez associer à une photo depuis le Finder de Mac OS.

    ![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-f06a63cd.png)

## Comment associer des tags à mes photos ?

### Associer des tags depuis l’éditeur de photo

Pour modifier les tags d’une photo de façon unitaire, il vous suffit de modifier cette photo.

L’éditeur de photo permet d’ajouter un ou plusieurs tags à une photo grâce au champ Tags.

[En savoir plus sur l’édition de photos](../importer-et-gerer-les-photos/modifier-ou-supprimer-une-photo)

Lorsque vous cliquez dans la zone de saisie, la liste déroulante des tags apparaît. Pour chercher un tag en particulier, il suffit de saisir quelques caractères : la liste se rafraîchit immédiatement pour afficher uniquement les tags correspondant à votre saisie.

![fr-tag-photo.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-ecf2e2eb.png)

Cliquez sur un tag pour l’associer à votre photo : il apparaît à présent en orange.

![fr-tag-photo-2.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-54358627.png)

Pour enlever un tag de la photo en cours d’édition, cliquez sur la croix à côté du nom du tag. Cela ne supprime pas le tag de votre photothèque : il reste utilisable pour d’autres photos.

Vous pouvez continuer ainsi et associer plusieurs tags à votre photo.

Si vous souhaitez créer un nouveau tag, il suffit de saisir le nom du tag dans la zone de saisie. L’option “Créer …” apparaît : cliquez dessus ou appuyez sur la touche Entrée de votre clavier pour créer un nouveau tag.

![fr-tag-photo3.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-c64ce62f.png)

!!! info
    Pensez bien à enregistrer vos modifications pour qu’elles soient appliquées à votre photo !

### Associer des tags à des photos en masse avec le gestionnaire de lot

En général, on va préférer taguer des photos en masse plutôt que le faire de façon unitaire :

- Soit après avoir importé un lot de photos dans Piwigo
- Soit pour mettre à jour une liste de photos correspondant à un critère (photos d’un album, sélection de photo dans votre Panier…)

Vous pouvez le faire facilement en passant par la [Gestion par Lot.](../importer-et-gerer-les-photos/gestion-par-lot-modifier-et-gerer-une-selection-de-photos)

Une fois votre sélection effectuée, vous pouvez choisir l’action “Ajouter les tags”. Elle permet d’associer à un lot de photos des tags existants ou un nouveau tag créé à la volée.

En mode global :

![fr-tags-lot.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-3f4c1b18.png)

En mode unitaire :

![fr-tags-lot-unitaire.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-0ded31b2.png)

### Supprimer les tags de photos en masse avec le gestionnaire de lot

Le gestionnaire de tags permet aussi de retirer les tags d’une liste de photos.

Pour cela, choisissez l’action “Supprimer les tags” et choisissez les tags que vous ne souhaitez plus affecter à la sélection de photos.

Cela ne supprime pas les tags de votre photothèque : ils restent utilisables pour d’autres photos.

## Gérer et modifier les tags

Pour gérer, modifier, supprimer les tags de votre photothèque, rendez vous dans l’écran de gestion de tags en cliquant sur le menu Photos > Tags.

![fr-liste-tags.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-12b57083.png)

Un moteur de recherche permet de trouver un tag facilement : utile lorsque vous en avez beaucoup !

Lorsque vous cliquez sur les 3 points à côté d’un tag, vous voyez apparaître le nombre de photos auxquelles ce tag est associé, ainsi qu’une liste d’actions disponibles.

![fr-tags-manage.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-3cd9d18a.png)

- Voir dans la galerie : affiche toutes les photos associées à ce tag dans votre galerie Piwigo
- Gérer les photos : permet de gérer / modifier les photos associés à ce tags via le gestionnaire de lot
- Éditer : permet de renommer le tag
- Dupliquer : crée une copie du tag
- Supprimer : permet de supprimer le tag

### **Modifier des tags en masse : mode sélection**

Pour modifier une liste de tags en masse, vous devez passer en mode sélection en cliquant sur le bouton “Mode sélection” à droite de l’écran.

Cette fonctionnalité permet :

- de supprimer en masse une liste de tags
- de fusionner des tags (utile en cas de doublons)

Cliquez sur les tags à modifier : ils apparaissent les uns après les autres dans une liste à droite de l’écran.

![fr-gestion-tags-selection.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-6403656f.png)

En cas d’erreur, vous pouvez retirer un tag de la liste sélectionnée en cliquant sur la croix à côté de son nom.

![fr-gestion-tags-selection2.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-6af46912.png)

En haut de l’écran, les boutons Tout / Rien / Inverser vous permettent d’aller plus vite dans la sélection si vous avez de nombreux tags à gérer.

- Cliquer sur “Tout” ajoute tous les tags de l’écran à votre liste de sélection
- Cliquer sur “Rien” vide votre liste de sélection
- Cliquer sur “Inverser” ajoute à la sélection tous les tags, sauf ceux actuellement sélectionnés.

Une fois votre sélection de tags terminée, cliquez sur l’action de votre choix :

- Fusionner : tous les tags sélectionnés seront fusionnés en un seul (vous devrez choisir quel libellé de tag conserver)
- Supprimer : tous les tags sélectionnés seront supprimés.

## À lire aussi : Les tags sur votre galerie

Lisez cet article pour découvrir comment utiliser les tags sur votre galerie, ainsi que des options et plugins pour aller plus loin dans l’utilisation des tags.

[Les tags sur votre galerie](../naviguer-sur-votre-galerie-piwigo/les-tags-sur-votre-galerie)
