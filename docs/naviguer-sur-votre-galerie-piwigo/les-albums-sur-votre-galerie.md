# Les albums sur votre galerie

Sur une galerie Piwigo, la navigation la plus courante se fait par album. Pour rappel, dans Piwigo, une photo est forcément placée dans un album, qui peut être considéré comme un répertoire ou comme une catégorie.

Les albums sont organisés en arborescence et peuvent contenir des sous-albums, qui eux-même peuvent contenir des sous-albums, etc.

À partir du moment où vous cliquez sur un album dans votre galerie, vous accédez à la page Album. 

Dans cet article nous verrons comment naviguer dans les albums, comment la page Album est structurée, quelles fonctionnalités sont disponibles, et quelles sont les options de personnalisation possibles, en standard ou avec des plugins.

!!! Warning "Attention"
    Remarque : la plupart des captures d’écran présentées dans cet article montrent une galerie utilisant le thème Modus. En fonction du thème utilisé par votre galerie, la présentation des informations et les icônes utilisées ne sont pas forcément les mêmes.


Pour en savoir plus sur les albums, lisez cette série d’articles :

[Organiser les albums](../organiser-les-albums)

## Préambule

Sur votre galerie, les différentes pages qui listent des photos (résultat d’une recherche, liste des photos associées à un tag, page “Mes photos” ou “Les plus vues”…) adoptent toute la même présentation que la page Album.

Les fonctionnalités de la page Album sont donc, grosso modo, les mêmes que les autres pages qui listent des photos.

![Page d’un album](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-fbbf21c8.png)

Page d’un album

![Page d’un tag](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-313b39a0.png)

Page d’un tag

![Page de résultats d’une recherche](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-26b9269c.png)

Page de résultats d’une recherche

## Les albums sur votre galerie

Lorsque vous arrivez sur l’accueil de votre galerie, vous visualisez la liste des albums de premier niveau, ou albums à la racine de votre arborescence.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-9cf59e80.png)

Les albums qui apparaissent sont : 

- Tous les albums publics
- Tous les albums privés que vous avez le droit de voir, si vous êtes connecté. [En savoir plus sur les permissions](../organiser-les-albums/permissions-et-visibilite-des-albums)

!!! info
    Par défaut, la page d’accueil affiche 12 albums par page. Vous pouvez naviguer dans vos albums grâce à la pagination en bas de page. Si vous souhaitez modifier le nombre d’albums affichés par page, rendez-vous dans l’administration, Configuration > Options, onglet Afficher.


En cliquant sur un album, vous accédez à la page de l’Album.

Le contenu de celle-ci diffère en fonction du contenu de l’album : soit il contient directement des photos (ou d’autres fichiers), soit il continent des sous-albums.

!!! info
    Pour comprendre les notions d’albums et sous-albums, [lisez cet article](../organiser-les-albums/albums-et-sous-albums-presentation). Il est possible qu’un album contienne à la fois des sous-albums et des fichiers, mais on le déconseille.


## Album avec des sous-albums

Si l’album contient des sous-albums, alors la page de cet album racine affiche les vignettes de ces sous-albums, et ainsi de suite.

Le chemin de navigation (ou fil d’ariane) en haut à gauche vous permet de visualiser à quel niveau d’arborescence vous êtes.

![Exemple : un album Bâtiments avec deux sous-albums Eglises et Maisons.](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-de43a71e.png)

Exemple : un album Bâtiments avec deux sous-albums Eglises et Maisons.

La barre d’outils vous propose plusieurs actions possibles, en fonction de vos droits utilisateurs, de votre thème, et en fonction du paramétrage de votre galerie. 

Vous pouvez notamment afficher à plat, tous les fichiers de l’album, tous sous-albums confondus, en cliquant sur l’icône adéquate (elle diffère suivant votre thème). Vous pourrez revenir à l’affichage par défaut en cliquant sur l’icône en forme de diagramme en arborescence.

## Affichage des photos sur la page Album

Si l’album ne contient pas des sous-albums, mais directement des photos, la page album affiche les vignettes des photos de l’album.

Si vous avez de nombreux fichiers dans cet album, des liens de pagination apparaissent en bas, et permettant de naviguer au sein de votre album.

![fr-liste-photos-album.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-d4e3c04b.png)

Si vous souhaitez supprimer la pagination et afficher l’intégralité des photos sur la page album, vous pouvez activer le plugin **RV Thumb Scroller**. Ce plugin charge les photos progressivement au fur et à mesure que l’utilisateur scrolle sur la page.

!!! info
    Pour modifier le nombre de photos affichées sur une page album, rendez vous dans vos [préférences utilisateur](../les-utilisateurs/creer-et-gerer-les-utilisateurs) ; vous pouvez y accéder en cliquant sur le menu “Personnaliser” sur la galerie, ou en modifiant votre profil utilisateur dans l’administration.


## La barre d’outils de la page Album

La barre d’outils vous donne accès à plusieurs fonctionnalités.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-6b027860.png)

!!! info
    Remarque : Les icônes et fonctionnalités disponibles sur votre galerie dépendent du thème que vous avez choisi, de la configuration de Piwigo, des plugins activés... Les exemples présentés sur cette page présentent les possibilités par défaut du thème [Modus](../les-themes/le-theme-modus). Si vous utilisez le thème [Bootstrap Darkroom](../les-themes/le-theme-bootstrap-darkroo), par exemple, les fonctionnalités disponibles sont globalement les mêmes, mais les icônes sont légèrement différentes.


### **Modifier l’ordre de tri des photos**

Vous pouvez modifier l’ordre de tri par défaut en cliquant sur l’icône “Tri” : ainsi vous pouvez trier vos photos par date d’ajout, par ordre alphabétique, par nombre de visites…

![fr-modifier-tri-album.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-227d4fed.png)

!!! info
    Pour modifier l’ordre de tri par défaut, rendez-vous dans l’administration, menu Configuration > Options.


### **Modifier la taille des photos affichées**

Pour modifier la taille des vignettes affichées à l’écran, vous pouvez cliquer sur l’icône “Taille”.

![fr-modifier-taille-photos-album.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-e0f063d4.png)

Exemple d’affichage avec la taille “Miniature” :

![fr-liste-photos-miniature.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-5b97b6ba.png)

### Ajouter au panier (administrateurs uniquement)

Si vous êtes administrateur, l’icône représentant un chariot permet d’ajouter toutes les photos de l’album à votre panier. Vous retrouverez ensuite ce panier dans l’administration, et pourrez agir sur ces photos, via le [gestionnaire de lots](../importer-et-gerer-les-photos/gestion-par-lot-modifier-et-gerer-une-selection-de-photos).

### Éditer l’album (administrateurs uniquement)

Si vous êtes administrateur, l’icône représentant un outil permet de vous rendre dans l’administration pour [modifier l’album](../organiser-les-albums/modifier-un-albu).

### **Afficher les photos en mode Calendrier**

Si vous voulez afficher les photos en fonction de leur date d’ajout, cliquez sur l’icône représentant un Calendrier. Vous pourrez alors filtrer vos photos en fonction de l’année et du mois auxquelles elles ont été ajoutées à Piwigo.

![fr-liste-photos-vue-calendrier.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-60032677.png)

Si vous cliquez sur l’icône représentant un appareil photo, vous pourrez filtrer les photos en fonction de leur date de création (et non plus de la date d’ajout à Piwigo).

![fr-liste-photos-date-creation.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-610d1078.png)

Pour retourner à la vue normale, cliquez sur l’icône en forme de diagramme en arborescence.

### Lancer un diaporama

Cliquer sur l’icône “Lecture” dans la barre d’outils permet de lancer un diaporama plein écran.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-aff0b0c8.png)

### Description de l’album

Lorsque vous modifiez un album dans l’administration, vous pouvez choisir de saisir une description pour cet album.

Celle-ci s’affichera sur la page album et sur la liste des albums (en fonction des thèmes et de leur configuration).

Si vous utilisez le thème Modus, par défaut la description s’affichera en haut de la page Album.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-3b7f3cad.png)

## Options de la page Album

### Définir les actions disponibles dans la page Album

Vous pouvez personnaliser l’affichage de certaines fonctionnalités sur la page album via le menu Configuration > Options de l’administration de Piwigo.

Dans l’onglet “Afficher”, vous pouvez personnaliser les actions disponibles via la barre d’outils de la page Album :

- Activer l’icône “Ordre de tri”
- Activer l’icône “Afficher à plat les photos des albums et sous-albums”
- Activer l’icône “Afficher un calendrier par date d’ajout”
- Activer l’icône “Afficher un calendrier par date de création”
- Activer l’icône “Diaporama”
- Activer l’icône “Tailles de photo”
- Activer l’icône “Éditer l’album” (visible uniquement par les administrateurs)
- Activer l’icône “Ajouter au panier” (visible uniquement par les administrateurs)

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-f1927e8d.png)

### Options liées aux thèmes

En fonction du thème utilisé par votre galerie, vous avez accès à d’autres options de mise en forme de votre page Album.

Visitez la documentation de votre thème pour en savoir plus :

- [Documentation de Modus](../les-themes/le-theme-modus)
- [Documentation de Bootstrap Darkroom](../les-themes/le-theme-bootstrap-darkroo)

### Modifier le nombre de photos affichées sur la page Album

Par défaut, Piwigo affiche 15 miniatures sur la page d’un album, mais vous pouvez en afficher plus (ou moins).

Pour modifier le nombre de photos affichées sur une page album, rendez-vous dans vos préférences utilisateur ; vous pouvez y accéder en cliquant sur le menu “Personnaliser” sur la galerie, ou bien en modifiant votre profil utilisateur dans l’administration.

[En savoir plus sur les préférences](../les-utilisateurs/creer-et-gerer-les-utilisateurs)

## Personnaliser la page Album avec des plugins

### **Comments on albums : Afficher** des commentaires sur les albums

Par défaut, Piwigo permet aux visiteurs de votre galerie de publier des [commentaires](../les-commentaires-et-notes/gerer-les-notes-votes) sur les photos, mais pas sur les albums.

Si vous souhaitez activer cette option, il suffit d’activer le plugin **Comments on albums**.

[En savoir plus](../les-commentaires-et-notes/gerer-les-notes-votes)

### Batch Downloader : Télécharger tous les fichiers d’un album (ou d’une sélection) au format zip

Le plugin **Batch Downloader** permet aux utilisateurs habilités de télécharger en un clic un fichier .zip contenant un lot de fichiers. C’est notamment possible depuis la page d’un album.

Une fois le plugin activé, une nouvelle icône apparaîtra dans la barre d’outil de la page d’un album. Cet icône permet de télécharger tous les fichiers de la sélection.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-570f1c4d.png)

Cette icône ne sera pas seulement disponible depuis la page d’un album, mais sur toutes les pages qui liste des photos :

- Résultats d’une recherche
- Liste des photos associées à un ou plusieurs tags
- Page “Mes favorites”
- etc.

Un clic sur l’icône permet de choisir la taille des photos téléchargées, en fonction des tailles de photos disponibles sur votre galerie.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-97d8cce9.png)

Une fois la taille choisie, le téléchargement est lancé. 

L’utilisateur peut à tout moment retrouver l’historique des fichiers téléchargés depuis le menu “Téléchargements” qui est apparu sur la galerie.

Cette page récapitule les fichiers téléchargés, permet d’annuler le téléchargement, et de télécharger le fichier sur votre ordinateur en cliquant sur le lien “Archive (prête)”

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-3ccd38b3.png)

La configuration du plugin Batch Downloader vous donne accès à une page avec deux onglets :

**Historique**

Cette page affiche l’historique des téléchargements via le plugin Batch Downloader. Vous pouvez ainsi voir :

- l’utilisateur ayant demandé le téléchargement
- le lot téléchargé
- la date
- la taille
- le nombre de photos
- le statut

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-cadf116f.png)

**Configuration**

L’onglet configuration permet de gérer de façon précise les possibilités offertes sur votre galerie.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-d12526fd.png)

- Qui a le droit de télécharger des photos en lot
- Quel type de lot de photo peut être téléchargé (albums uniquement, ou également les pages “Spéciales” (plus vues, mieux notées…)
- La taille des photos autorisée en téléchargement

Vous pouvez également définir des règles sur le temps de conservation des archives sur le serveur, le nombre maximum de photos par lot, la taille maximale de chaque archive…

Les fonctionnalités avancées listent les options qui sont modifiables via le fichier de configuration de Piwigo.

Vous pouvez les modifier grâce à [Localfile Editor](../hebergez-votre-piwigo/modifier-la-configuration-locale-avec-localfiles-editor) si vous travaillez sur un Piwigo auto-hébergé ; si vous êtes clients d’une offre Piwigo Cloud, contactez le support pour modifier l’un de ces paramètres.

### ShareAlbum : partager un lien sécurité vers un album

Le plugin **ShareAlbum** permet aux utilisateurs habilités de générer un lien de partage vers cet album. Ce qui est très utile avec ce plugin, c’est qu’il vous permet de partager le contenu d’un album privé, même avec des personnes n’ayant pas de compte Piwigo.

Une fois ce plugin activé, vous trouverez dans votre galerie Piwigo une icône “Partager” sur chaque album.

![sharealbum.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-8fb407d2.png)

Si vous cliquez sur cette icône, un bouton “Partager cet album” apparaît.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-d61bf386.png)

Une fois l’album partagé, cliquez à nouveau sur l’icône pour visualiser le lien de partage. 

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-96c8bc9b.png)

Une fois que vous n’en avez plus besoin, vous pouvez annuler le lien de partage : il ne sera alors plus accessible.

Vous pouvez également cliquer sur “Renouveler le lien” pour générer un nouveau lien (le lien précédemment généré ne sera plus accessible).

Si vous utilisez Piwigo dans le cadre d’une entreprise, c’est très utile lorsque vous avez besoin de partager ponctuellement le contenu d’un album avec une personne externe à votre organisation (un client, un partenaire, un journaliste,…).

La configuration du plugin ShareAlbum vous donne accès à deux onglets :

**Onglet Configuration**

Cet onglet donne accès aux options de configuration de ShareAlbum.

- Cacher les menus pour les visiteurs : si cette option est activée, le lien de partage n’affichera que les contenus de l’album, sans le menu de navigation en haut de l’écran. Si vous activez cette option, vous pouvez choisir d’afficher ou non un menu de connexion sur la page partagée.
- Activer l’auto-login
- Remplacer les liens de la barre de navigation par le nom de l’album uniquement : permet de masquer l’arborescence de l’album
- Partager également les sous-albums : permet de définir si le partage d’un album donne également accès à ses sous-albums ou pas
- Autoriser la création de partages par des utilisateurs non-admin : permet d’autoriser des utilisateurs non admin de créer des liens de partage

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-e08db929.png)

**Onglet Shared Albums**

Le deuxième onglet permet de voir l’historique des liens de partage générés par le plugin ShareAlbum. Vous pouvez voir qui a créé des liens, le nombre de fois où ces liens ont été visités, l’album associé, renouveler et supprimer des liens de partage existants.

Vous pouvez également créer des liens de partage depuis cet écran, sans passer par votre galerie.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-4712afd8.png)

### GThumb+ : Afficher un patchwork de miniatures

Par défaut, sur les pages Album et les autres pages listant des photos sur votre galerie, les miniatures sont affichées sous la forme d’une grille ; toutes les miniatures ont la même hauteur.

Le plugin Gthumb+ permet de les afficher sous la forme d’un patchwork avec des hauteurs variables.

![Affichage par défaut](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-899b459f.png)

Affichage par défaut

![Affichage avec Gthumb+](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-e84c582e.png)

Affichage avec Gthumb+

La configuration du plugin vous permet de personnaliser les options par défaut, comme :

- Hauteur maximum des miniatures
- Marge entre les miniatures
- Nombre de miniatures par page
- etc.

### Image Preview : afficher les miniatures au survol

!!! Warning "Attention"
    Attention ! Si vous utilisez le thème Modus, pour utiliser le plugin Image Preview, vous devrez au préalable activer le plugin **Gthumb+** (voir chapitre précédent).


Le plugin **Image Preview** permet ****d’agrandir les miniatures des photos lorsque l’on passe la souris dessus, depuis la page Album ou toute autre page de liste sur la galerie.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-8f50808b.png)

La configuration du plugin permet de définir la taille de l’image affichée (par défaut : maximum 400 px de largeur et 600 px de hauteur).

Vous pouvez choisir également d’afficher ou non le nom de l’image, d’appliquer un effet de transparence au survol, et de pré-charger les images (déconseillé pour des raisons de performances).

### Lightbox : Afficher la photo dans une popin plutôt que sur la page Photo

Par défaut, lorsque vous cliquez sur une photo dans un album, vous êtes redirigé vers la page de cette photo.

Le plugin **Lightbox** modifie le comportement de Piwigo : une fois que vous l’avez activé, lorsque vous cliquez sur une photo, elle s’affiche dans une pop in (pop up modale) au-dessus de la page Album, comme vous le voyez dans l’exemple ci-dessous.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-0068cdc1.png)

Des flèches permettent de naviguer au sein de l’album.

Les options de configuration du plugin permettent de personnaliser certains paramètres :

- Afficher ou non le titre de l’image
- Permettre d’accéder à la page photo en cliquant sur le titre de l’image
- Afficher ou non les flèches de navigation
- Personnalisation du look de la lightbox (fond clair ou foncé…)
- Dimensions de la lightbox.

### Permalink Generator : personnaliser l’URL d’une page Album

Par défaut, lorsque vous créez un nouvel album, intitulé par exemple “Shooting”, son URL (adresse web) à la forme suivante : [monpiwigo.com/index?/category/XX_shooting](http://monpiwigo.com/index?/category/XX_shooting) (XX étant l’identifiant de cet album dans la base de données Piwigo)

Si vous modifiez le nom de l’album, son URL changera également.

Le plugin **Permalinks Generator** permet de générer des URL uniques pour vos albums, qui resteront valides même si vous changez leur nom.

Une fois le plugin activé, rendez-vous dans sa configuration et cliquez sur “Générer les permaliens”. Vous constaterez que les URL de vos albums ont changé et ont désormais le format monpiwigo.com/index?/category/shooting. 

Si vous modifiez le nom de l’album, l’URL restera la même.

### Quick Fav : ajouter une photo à ses favoris depuis la page Album

Avec Piwigo, il est possible pour chaque utilisateur d’ajouter une photo à ses favoris pour la retrouver plus tard. Par défaut, c’est uniquement possible depuis la page d’une photo.

Le plugin **Quick Fav** permet d’ajouter une photo en clic depuis sa vignette, sur la page Album ou une autre page de liste.

!!! Warning "Attention"
    Attention ! Ce plugin est pour le moment uniquement compatible avec le thème Bootstrap Darkroom. Par ailleurs, il n’est accessible que pour les clients d’une offre [Piwigo Cloud](https://piwigo.org) (ce sera corrigé prochainement).


Une fois ce plugin activé, lorsque l’on passe la souris sur une photo, un coeur apparaît : un clic sur ce coeur ajoute la photo aux favoris de l’utilisateur.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-50f3baef.png)

Lorsque vous passez la souris sur un favori, le coeur apparaît comme plein. Cliquez à nouveau dessus pour retirer la photo de vos favoris.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-3c93a57e.png)

### Ajouter un album entier à ses favoris avec Quick Fav

Il est également possible, avec le plugin **Quick Fav**, d’ajouter un album entier à ses favoris.

Depuis une page qui liste des albums, vous voyez apparaître la même icône que sur une liste de photos, qui permet en un clic d’ajouter le contenu d’un album à ses favoris.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-7ec0edd3.png)

### Thumbnail Tooltip : personnaliser l’infobulle affichée sur la miniature d’une photo

Sur la page d’un album, lorsque l’on passe la souris sur une photo, on affiche dans une infobulle certaines informations sur la photo (titre, nombre de visites…).

Il est possible de personnaliser le contenu de cette infobulle avec le plugin **Thumbnail Tooltip**.

!!! Warning "Attention"
    Attention : le thème Modus d’affiche pas d’infobulle sur la page Album. Ainsi, le plugin Thumbnail Tooltip n’est pas compatible avec Modus.


Une fois ce plugin activé, rendez vous dans sa configuration pour définir ce que vous souhaitez afficher dans l’infobulle, et dans quel ordre.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-427cbc69.png)

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-9d4628f4.png)

Sommaire de l’article

### RV Thumb Scroller : supprimer la pagination sur la page Album

Le plugin **RV Thumb Scroller** permet de désactiver la pagination sur la page Album.

Si vous l’activez, les miniatures des photos se chargeront progressivement au scroll sur la page, quel que soit le nombre de photos dans l’album.
