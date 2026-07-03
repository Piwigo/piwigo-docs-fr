# Gérer les contributeurs (plugin Community)

## Pourquoi utiliser le plugin Community ?

Par défaut, dans Piwigo, seuls les administrateurs ont le droit d’importer du contenu dans votre photothèque.

Or, parfois, vous souhaitez autoriser certains utilisateurs à importer des fichiers, sans pour autant leur donner un statut d’administrateur. Quelques exemples dans le cadre d’une organisation :

- Vous travaillez avec un photographe, et pour gagner du temps, vous souhaitez qu’il envoie son dernier shooting directement sur Piwigo pour faire le tri, plutôt que passer par un CD ou un transfert de fichiers ;
- Certains membres de votre équipe sont chargés de créer des fichiers (photos retouchées, créations graphiques, brochures…) ; vous ne voulez pas qu’ils soient obligés de passer par un administrateur pour les ajouter à Piwigo, mais vous ne souhaitez pas non plus leur donner les droits d’administration.
- Des utilisateurs sur le terrain doivent envoyer des photos prises sur site (agents de maintenance, chefs de chantier, responsables de site…). Leur permettre de les ajouter directement à Piwigo fait gagner du temps à tout le monde (surtout s’ ils utilisent [l’application mobile Piwigo](../les-applications-mobiles) pour iOS ou Android !).

Si vous utilisez Piwigo dans un contexte familial, amical ou dans un club, vous pouvez également donner à d’autres personnes la possibilité d’envoyer leurs photos sur votre Piwigo.

Tous ces utilisateurs qui ne sont pas administrateurs mais ont le droit d’importer du contenu dans Piwigo sont ce que nous appelons ici les **contributeurs**.

Pour activer cette fonctionnalité, vous devez activer le plugin Community.

!!! Warning "Attention"
    Si vous êtes client d’une offre Piwigo Cloud, ce plugin n’est accessible qu’à partir de l’offre Équipe.


## Définir les utilisateurs habilités à ajouter des photos et leurs autorisations

Une fois le plugin Community activé, vous devez vous rendre dans la configuration du plugin en cliquant sur “Configuration”.

![fr-community-configuration.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-ddf54f7a.png)

Le premier onglet permet de définir les autorisations et options de Community.

Par défaut, une autorisation a été créée, qui permet à tous les utilisateurs enregistrés d’être contributeurs.

Vous pouvez modifier cette autorisation en cliquant sur l’icône d’édition, ou la supprimer en cliquant sur l’icône de suppression (la croix).

![fr-community-default.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-ed92b6af.png)

Vous pouvez également ajouter une nouvelle autorisation en cliquant sur “Ajouter une permission”.

Lorsque l’on clique sur “Ajouter une nouvelle permission”, on accède aux différentes options possibles.

![fr-community-new.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-9db64521.png)

**Qui ?**

Définissez ici qui a le droit d’ajouter des photos depuis la galerie :

- N’importe quel visiteur (même anonyme)
- N’importe quel utilisateur enregistré
- Un utilisateur en particulier : vous pouvez alors choisir l’utilisateur en question
- Un groupe d’utilisateur en particulier : vous pouvez créer un groupe Contributeurs, ce qui est le plus pratique. [En savoir plus sur les groupes d’utilisateurs](les-groupes-dutilisateurs)

**Où ?**

Choisissez ici dans quel espace de la galerie les contributeurs peuvent ajouter des photos :

- Dans la galerie toute entière (n’importe quel album)
- Dans un album en particulier

!!! info
    Par défaut, l’activation du plugin Community crée un nouvel album “Community”. Vous pouvez choisir que les photos des contributeurs aillent dans cet album, pour qu’un administrateur les trie et les valide.


Si vous cochez “appliquez aux sous-albums”, les utilisateurs auront le droit d’ajouter des photos dans l’album choisi ET dans ses sous-albums.

Si vous cocher “possibilité de créer des albums”, les utilisateurs auront le droit de créer un nouvel album au moment de l’ajout de photo.

**Quel degré de confiance ?**

Vous avez le choix entre deux options :

- confiance faible : les photos ajoutées par les contributeurs devront être validées par un administrateur avant d’être visibles sur la galerie.
- confiance élevée : les photos ajoutées par les contributeurs seront directement visibles sur la galerie.

**Autres options**

Vous pouvez enfin :

- limiter le nombre de photos que les contributeurs auront le droit d’ajouter (limite par utilisateur)
- limiter l’espace disque pris par les photos ajoutées par les contributeurs (limite par utilisateur)

Par défaut, ces valeurs sont illimitées.

Cliquez sur Ajouter : l’autorisation a été créée.

Si vous souhaitez gérer différents types de contributeurs, avec des droits différents, vous devrez créer plusieurs autorisations.

**Création automatique d’un album par contributeur**

Si vous le souhaitez, Piwigo peut créer un nouvel album automatiquement pour chaque contributeur à sa première connexion.

Pour cela, rendez-vous dans l’onglet Configuration de la configuration du plugin Community.

![fr-community-config.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-a1bc9f4d.png)

Si vous cochez cette option, vous pouvez définir dans quel album seront créés les albums spécifiques à chaque contributeur.

## Pour les contributeurs : comment ajouter des photos sur Piwigo avec Community ?

Les utilisateurs habilités à ajouter des photos sur la galerie ont accès à un nouveau point de menu “Ajouter des photos” sous le menu “Explorer”.

![fr-community-menu.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-652c6497.png)

!!! info
    Remarque : le menu “Ajouter des photos” peut être affiché au niveau du menu principal, à droite du menu “Explorer”. Pour cela, installez le plugin Upload 1 Menu. Ce plugin est réservé aux détenteurs d’un abonnement Equipe, Entreprise ou VIP.


Le menu Ajouter des photos permet d’accéder à la page d’ajout de photos.

![fr-community-formulaire.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-2109431b.png)

L’utilisateur a la possibilité :

- de choisir l’album dans lequel ajouter les photos (seuls les albums autorisés sont accessibles)
- de créer un nouvel album (si il en a le droit)
- d’ajouter des photos depuis sont ordinateur (en cliquant sur Ajouter des photos ou par un glisser déposer)
- de définir les propriétés des photos (Titre, Auteur, Description) en cliquant sur “Définir les propriétés de la photo”

Le bouton “Démarrer le transfert” envoie les photos vers Piwigo.

En fonction du niveau de confiance choisi lors de la création de l’autorisation de l’utilisateur, les photos seront soit :

- Visible tout de suite sur la galerie
- Soumise à la validation d’un administrateur

### Voir et modifier les photos ajoutées en tant que contributeur

En tant que contributeur, vous avez accès à un menu “Edit photos” sous le menu principal “Explorer”.

Cette page vous permet de voir les photos que vous avez ajoutées. Celles qui sont toujours en attente de validation affichent le libellé “En attente”.

![fr-community-edit-photos.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-a74fa75d.png)

Cette page vous permet de supprimer des photos ajoutées, et de leur ajouter des tags.

Pour éditer des photos, cliquer sur les photos souhaitées pour les ajouter à la sélection, ou utiliser les boutons Tout/Rien/Inverser pour une sélection multiple.

Ensuite, cliquez sur la liste déroulante “Action” pour choisir l’action à effectuer :

- Supprimer les photos sélectionnées
- Ajouter des tags

![fr-community-edit-photos-2.png.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-9d7acf7e.png)

## Pour les administrateurs : comment valider les photos ajoutées par les contributeurs via Community ?

Si vous avez choisi l’option “confiance faible” dans les paramètres du plugin Community (voir premier chapitre de cette page), les photos ajoutées par les utilisateurs doivent être validées par un administrateur avant d’être publiées sur la galerie.

Il existe plusieurs moyens de voir les photos à valider par un administrateur.

### Notification par email

Les administrateurs reçoivent un email à chaque fois que des photos sont ajoutées. Cet email contient un lien permettant directement de vérifier et valider les photos.

![fr-email-validation-community.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-d1078599.png)

### Dashboard de Piwigo

Lorsque des photos sont en attente de validation, les administrateurs en sont informés par un bandeau visible depuis la page d’accueil de l’administration de Piwigo (le dashboard).

### Valider les photos en attente

Depuis le lien envoyé par email ou accessible depuis l’accueil de l’administration, vous êtes redirigé vers les paramètres de Community, onglet “Photos en attente”.

Cet onglet liste les photos en attente de validation.

![fr.community-validation.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-33137fff.png)

Pour chaque photo, vous pouvez voir ses paramètres, l’agrandir en cliquant sur “Zoom” et l’éditer en cliquant sur “Editer”. Vous pouvez ainsi ajuster les propriétés de l’image (titre, description, album, tags…) avant de la mettre définitivement en ligne.

Vous pouvez enfin ajuster le niveau de confidentialité des photos grâce à la liste déroulante en dessous du texte “Qui peut voir ces photos” ? (en savoir plus sur les [niveaux de confidentialité](les-niveaux-de-confidentialite)). Si vous n’utilisez pas les niveaux de confidentialité sur votre galerie, laissez la liste déroulante sur “Tout le monde”.

Ensuite, il suffit de cocher les photos et de cliquer sur “Valider” (mettre en ligne les photos) ou “Rejeter” (refuser la mise en ligne des photos).

## Les plugins complémentaires au plugin Community

Certains plugins sont utiles pour les galeries Piwigo qui utilisent le plugin Community : en voici la liste.

!!! info
    Si vous êtes client d’une offre Piwigo Cloud, ces plugins ne sont accessibles qu’à partir de l’offre Équipe.


### Upload 1 Menu

Ce plugin permet d’afficher le menu “Ajouter des photos” au niveau du menu principal de la galerie, à côté du menu “Explorer”.

![fr-community-uploadmenu1.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-29ba55aa.png)

### See My Photos

Ce plugin permet d’ajouter un menu “Mes photos” sur la galerie. Ainsi, chaque utilisateur peut facilement visualiser les photos qu’il a ajoutées à la galerie, sous albums confondus.

[En savoir plus](../personnaliser-ma-galerie/personnaliser-le-menu-de-votre-galerie)

### See photos by user

Ce plugin permet aux visiteurs de la galerie de filtrer facilement les photos en fonction de l’utilisateur qui les a ajoutées.

[En savoir plus](../personnaliser-ma-galerie/personnaliser-le-menu-de-votre-galerie)

### Photo added by

Ce plugin permet d’afficher sur la page d’une photo l’identifiant de l’utilisateur qui l’a ajoutée sous le champ “Photo ajoutée par”.

![fr-photo-ajoutee-par.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-d13b9bef.png)

La configuration du plugin permet de définir à quel endroit on souhaite afficher cette information (par défaut, juste avant “Albums”).

Si le plugin “See photos by user” est activé, il est possible de rendre le nom de l’utilisateur cliquable, pour permettre d’accéder à la page listant toutes les photos ajoutées par cet utilisateur.
