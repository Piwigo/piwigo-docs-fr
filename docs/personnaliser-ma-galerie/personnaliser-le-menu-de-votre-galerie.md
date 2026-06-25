# Personnaliser le menu de votre galerie

Comment personnaliser la barre de menu de votre galerie, modifier l’arborescence et ajouter de nouveaux points de menu ? On vous explique tout dans cet article.

## Présentation du menu par défaut sur Piwigo

Par défaut, toutes les galeries sont créées avec le même menu de navigation. Ce qu’on appelle **le menu** représente les liens affichés dans le bandeau en haut de toutes les pages de la galerie.

![Le menu de navigation avec le thème Modus](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-7c359159.png)

Le menu de navigation avec le thème Modus

![Le menu de navigation avec Bootstrap Darkroom](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-04efd459.png)

Le menu de navigation avec Bootstrap Darkroom

Vous remarquez avec les précédents exemples : 

- que les points de menus affichés ne sont pas les mêmes en fonction du thème utilisé sur votre galerie ;
- que le menu n’est pas le même suivant que l’on soit connecté en tant qu’utilisateur ou pas.

Certains points de menu ouvrent une liste avec des sous-menus :

- Le lien Albums affiche la liste des albums avec, pour chacun, le nombre de photos qu’il contient.
- Le menu “Tags liés” affiche la liste des tags et permet de rechercher une photo par tag.
- Le menu Explorer (sur Modus) ou Découvrir (sur bootstrap Darkroom) liste de nombreux sous-menus.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-8da67781.png)

## Personnaliser le menu : options de base

Pour personnaliser le menu de navigation sur votre galerie, rendez-vous dans l’administration, menu Configuration > Menus.

Cette page permet de visualiser les liens dans le menu, de les réorganiser, et de masquer certains.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-ebbefd41.png)

Il est important de comprendre à quoi correspond chaque ligne sur cette page :

- La ligne “Spéciales” correspond à une liste de liens disponibles quand on clique sur le point de menu “Explorer” sur Modus et “Découvrir” sur bootstrap Darkroom. Les pages “spéciales” sont les pages suivantes :
    - Mes favorites (pour les utilisateurs connectés)
    - Plus vues
    - Mieux notés
    - Photos récentes
    - Albums récents
    - Photos au hasard
    - Calendrier

![Les blocs “Menu” et “Spéciales” sur une galerie avec le thème Modus](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-27d5f318.png)

Les blocs “Menu” et “Spéciales” sur une galerie avec le thème Modus

- La ligne “Menu” correspond à une autre liste de liens disponibles quand on clique sur le point de menu “Explorer” sur Modus et “Découvrir” sur bootstrap Darkroom. Le bloc “Menu” regroupe les liens suivants :
    - Tags
    - Recherche
    - Commentaires
    - Notifications
- La ligne “Albums liés” ne s’affiche que sur la page d’une photo
- La ligne “Liens” correspond aux liens externes qui peuvent être ajoutés dans la configuration de Piwigo (avec [LocalFile Editor](../hebergez-votre-piwigo/modifier-la-configuration-locale-avec-localfiles-editor) si votre Piwigo est auto-hébergé, ou avec le plugin [Advanced Menu Manager](personnaliser-le-menu-de-votre-galerie))

Pour modifier l’ordre d’affichage des points de menus, il suffit de procéder par “drag and drop” (glisser-déposer) et d’enregistrer les paramètres.

![menu.gif](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-59093a15.gif)

Vous pouvez également cocher “Masquer” si vous souhaitez masquer un élément dans le menu.

## Personnaliser le menu avec des plugins

Plusieurs plugins permettent d’aller plus loin dans la personnalisation de votre menu.

### Advanced Menu Manager : personnalisation avancée du menu

Le plugin Advanced Menu Manager offre des options supplémentaires pour la personnalisation de votre menu de navigation. Une fois activé, rendez vous dans la page de configuration du plugin. 

5 onglets sont à votre disposition.

**Onglet “Gestion du menu”**

Cet onglet permet, comme sur la page de configuration du menu dans l’administration, de réordonner les points de menu en “drag and drop”. Il permet également modifier la visibilité de certains points de menu en fonction des utilisateurs :

- par [statut utilisateur](../les-utilisateurs/les-statuts-utilisateurs) dans la colonne de gauche (administrateur, webmaster, visiteur, invité…)
- par [groupe d’utilisateurs](../les-utilisateurs/les-groupes-dutilisateurs) dans la colonne de droite

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-6a0ce627.png)

Sur ce même onglet, en cliquant sur “Contenu des menus “Menu” et “Spéciales”, vous pouvez personnaliser les pages affichées dans les blocs “Menu” et “Spéciales” (voir paragraphe précédent).

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-2bf3f886.png)

Sur cette page, vous pouvez donc réordonner les liens dans ces deux blocs de menus, mais également cliquer sur le cadenas pour définir la visibilité de ces liens par statut utilisateur et par groupe utilisateur.

**Onglet “Liens”**

Cet onglet permet d’ajouter des liens externes qui seront insérés dans le groupe “Liens” (par exemple, si vous souhaitez intégrer un lien vers votre site web sur votre galerie).

Vous pouvez ici :

- Ajouter un ou plusieurs liens externes
- Renommer le nom du point de menu “Liens” affiché sur votre galerie, dans chaque langue
- Autres options

**Onglet “Image aléatoire”**

Le plugin Advanced Menu Manager ajoute un point de menu “Une image au hasard” sur votre galerie. Ce lien permet d’afficher une image choisie aléatoirement lorsque l’on passe la souris dessus.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-b98d98ea.png)

Dans l’onglet “Image aléatoire”, vous pouvez personnaliser le titre de ce bloc dans le menu, les données affichées, ainsi que la visibilité de ce bloc dans certains albums uniquement.

**Onglet “Menu personnalisé”**

 Cet onglet vous permet d’ajouter les points de menu de votre choix dans le menu.

**Onglet “Album ⇒ Menu”**

Cet onglet permet de créer des points de menu à partir d’un album. 

C’est utile si vous souhaitez mettre en avant un album en particulier dans le menu de navigation.

### RV Menu Tree : Naviguer dans l’arborescence des albums

Le plugin RV Menu Tree modifie le fonctionnement du point de menu “Albums” sur votre galerie.

Il permet de naviguer dans l’arborescence des sous-albums, ce qui n’est pas proposé par défaut.

![Menu “Albums” avec le thème Modus par défaut](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-2f0c849c.png)

Menu “Albums” avec le thème Modus par défaut

![Menu “Albums” avec le thème Modus AVEC RV Menu Tree](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-d2567eb3.png)

Menu “Albums” avec le thème Modus AVEC RV Menu Tree

### See my photos : Ajout d’un menu “Mes photos”

Le plugin **See My Photos** permet d’ajouter un point de menu “Mes photos” sur la galerie, disponible au sein du bloc “Spéciales”.

!!! Warning "Attention"
    Si vous êtes client d’une offre piwigo.com, ce plugin n’est accessible qu’à partir de l’offre Équipe.


Ce lien permet à un utilisateur de voir toutes les photos qu’il a lui même importées dans Piwigo. C’est particulièrement utile lorsque vous utilisez le plugin [Community](../les-utilisateurs/gerer-les-contributeurs-plugin-community).

### See photos by user : Ajout d’un menu “Utilisateurs”

Le plugin **See photos by user** permet aux visiteurs de la galerie de filtrer facilement les photos en fonction de l’utilisateur qui les a ajoutées.

!!! Warning "Attention"
    Si vous êtes client d’une offre piwigo.com, ce plugin n’est accessible qu’à partir de l’offre Équipe.


Vous pouvez affiner les paramètres de ce plugin depuis sa page de configuration dans l’administration :

- choisir un nombre minimum de photos à partir duquel on affiche un utilisateur sur la galerie
- choisir le nombre maximum d’utilisateurs à afficher sur la page
- choisir l’ordre de classement des utilisateurs sur la page (ordre alphabétique, nombre de photos…)
- choisir l’emplacement de la page sur la galerie :
    - Menu “Voir les photos par utilisateur” sous “Explorer”
    - ou bien ajout d’un Menu “Utilisateurs” au niveau du menu principal, avec un sous-menu correspondant à chaque utilisateur
- choisir le mode de filtrage des utilisateurs sur la galerie :
    - affichage d’un nuage d’utilisateurs classique
    - affichage d’un nuage d’utilisateur animé et en couleur
    - affichage d’une liste déroulante d’utilisateurs

Ci-dessous, on peut voir un exemple de page “Utilisateurs” avec les options d’affichage d’un menu “Utilisateurs” et d’affichage des utilisateurs sous la forme d’un nuage classique. 

![fr-see-photo-by-user.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-6d809fcc.png)

!!! Warning "Attention"
    Ce plugin n’est que partiellement compatible avec le thème bootstrap Darkroom.


### Menu Random Photo : ajout d’une photo aléatoire

Le plugin **Menu Random Photo** permet d’ajouter un point de menu qui affiche une image choisie aléatoirement dans Piwigo.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-3eb0c512.png)

Cette fonctionnalité est également présente dans le plugin Advanced Menu Manager.

### Menu Tags

Le plugin **Menu Tags** ajoute un menu “Tags” sur toutes les pages qui n’ont aucun tags liés.

Si vous activez ce plugin, le menu “Tags liés” s’affichera toujours sur la page d’un album (il affichera uniquement les tags liés aux photos de cet album).

Mais sur la page d’accueil, à la place du menu “Tag liés”, on affichera un menu “Tags” qui affiche tous les tags de votre galerie, avec une taille proportionnelle à leur taux d’utilisation.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-c813024c.png)

[En savoir plus sur les tags sur votre galerie](../naviguer-sur-votre-galerie-piwigo/les-tags-sur-votre-galerie)

### **Upload 1 Menu : ajout d’un menu “Ajoutez des photos”**

!!! Warning "Attention"
    Si vous êtes client d’une offre piwigo.com, ce plugin n’est accessible qu’à partir de l’offre Équipe.


Lorsque le plugin [Community](../les-utilisateurs/gerer-les-contributeurs-plugin-community) est activé, le plugin **Upload 1 Menu** permet d’afficher le menu “Ajouter des photos” au niveau du menu principal de la galerie, à côté du menu “Explorer”.

![fr-community-uploadmenu1.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-29ba55aa.png)
