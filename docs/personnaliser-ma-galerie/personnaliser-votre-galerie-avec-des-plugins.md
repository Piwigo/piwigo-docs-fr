# Personnaliser votre galerie avec des plugins

Vous trouverez sur cette page quelques plugins permettant de personnaliser l’apparence et les fonctionnalités de votre galerie.

Vous trouverez d’autres plugins de personnalisation pour votre galerie en lisant les articles suivants :

[Les albums sur votre galerie](../naviguer-sur-votre-galerie-piwigo/les-albums-sur-votre-galerie)

[La page Photo sur votre galerie](../naviguer-sur-votre-galerie-piwigo/la-page-photo-sur-votre-galerie)

[Les tags sur votre galerie](../naviguer-sur-votre-galerie-piwigo/les-tags-sur-votre-galerie)

## PWG Stuff : ajouter des blocs configurables sur votre galerie

Le plugin **PWG Stuffs** offre diverses options pour ajouter des blocs configurables à votre galerie. 

Ces blocs viennent enrichir les pages existantes. C’est donc un plugin très complet pour customiser votre galerie, qui permet notamment de personnaliser l’affichage en fonction des utilisateurs.

Il est notamment utilisé pour :

- Ajouter un nuage de mots-clés sur la page d’accueil
- Ajouter une zone de connexion sur la page d’accueil
- etc.

Cliquez ci-dessous pour lire la documentation complète de PWG Stuff.

[PWG Stuffs : ajouter des blocs sur votre galerie](personnaliser-votre-galerie-avec-des-plugins/pwg-stuff-ajouter-des-blocs-sur-votre-galerie)

## Fotorama : un autre diaporama pour votre galerie

Le plugin **Fotorama** permet de remplacer le lecteur diaporama utilisé par défaut sur votre galerie Piwigo par un autre diaporama.

Il dispose de diverses options paramétrables dans la configuration du plugin.

![Diaporama plein écran avec Fotorama](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-7d9727bc.png)

Diaporama plein écran avec Fotorama

## Extended Description : de nombreuses options pour personnaliser votre galerie

Le plugin Extended Description offre de nombreuses possibilités. Il est notamment utilisé pour traduire en plusieurs langues les titres et descriptions des albums et des photos [comme expliqué dans cet article](gerer-les-langues-disponibles-sur-votre-galerie).

Mais il offre de nombreuses autres possibilités.

Il permet en effet de gérer des balises que vous pouvez insérer n’importe où dans votre galerie.

Cela peut vous permettre :

- De gérer deux descriptions différentes pour un album (une courte affichée sur la liste des albums et une longue sur la page album)
- D’insérer un album ou une photo dans n’importe quel champ texte de votre galerie
- D’insérer un carrousel (ou diaporama) dans n’importe quel champ texte de votre galerie
- De masquer un album sur la page de l’album parent ou dans le menu
- De masquer une photo sur la page d’un album
- De rediriger un album vers n’importe quelle URL
- De rediriger un élément vers une image, un album, ou une page de recherche
- D’insérer un lien de connexion à la galerie où vous le souhaitez.

Une fois que vous avez installé Extended Description, à côté des champs de saisie vous verrez apparaître une icône en forme de point d’interrogation : cliquez dessus pour afficher toutes les options du plugin.

Nous les avons repris intégralement ci-dessous.

- **Voir la doc complète du plugin Extended Descriptions**
    
    **Descriptions multilingues**
    
    Les descriptions multilingues se font entre les balises `[lang=xx]` et `[/lang]`, ou xx est le code de la langue (par exemple fr, en, es, ...)
    
    ```html
    [lang=en]Default description[/lang]
    [lang=fr]Description en français[/lang]
    [lang=de]Deutsche Beschreibung[/lang]
    ```
    
    **Balise *default***
    
    La description par défaut sera utilisée si la description dans la langue de l'utilisateur n'est pas définie.
    Si `[lang=default]` n'existe pas, tout ce qui est situé en dehors des balises de langues sera considéré comme description par défaut.
    
    ```html
    [lang=default]Default description[/lang]
    [lang=fr]Description en français[/lang]
    
    // OR
    
    Default description
    [lang=fr]Description en français[/lang]
    ```
    
    **Balise *all***
    
    tout ce qui est situé entre les balises `[lang=all]` et `[/lang]` sera inclus dans la description, quelle que soit la langue de l'utilisateur.
    Ceci est particulièrement pratique pour inclure du code HTML ou Javascript dans une description.
    
    ```html
    [lang=all]<p>[/lang]
      [lang=default]Default description[/lang]
      [lang=fr]Description en français[/lang]
      [lang=de]Deutsche Beschreibung[/lang]
    [lang=all]</p>[/lang]
    ```
    
    **Descriptions étendues**
    
    Les balises de description étendue permettent d'avoir une description réduite pour la présentation d'un album, une description étendue pour la description qui s'affiche sur la page de l'album, ou deux descriptions différentes sur la page de l'album.
    
    **<!--more-->**
    
    Seule la description réduite sera affichée pour la présentation de l'album. Sur l'album lui-même, la description sera la description réduite + la description détaillée.
    
    ```html
    description réduite <!--more--> description détaillée
    ```
    
    **<!--complete-->**
    
    Seule la description réduite sera affichée pour la présentation de l'album. Par contre, sur l'album lui-même, la description sera uniquement la description détaillée, soit 2 descriptions différentes.
    
    ```html
    description réduite <!--complete--> description détaillée
    ```
    
    **<!--up-down-->**
    
    Seule la description haute sera affichée pour la présentation de l'album. Sur l'album lui-même, la description haute sera affichée au-dessus des miniatures, alors que la description basse sera affichée au-dessous (à l'emplacement normal de la description).
    
    ```html
    description haute <!--up-down--> description basse
    ```
    
    **Insérer un album ou une photo
    \[photo id=xx\]**
    
    Cette balise permet d'insérer une photo de n'importe quelle taille.**Options:**
    • `id` le numéro de la photo
    • `album` (facultatif) le numéro de l'album parent
    • `size` (facultatif) la taille de la photo, parmi *(SQ, TH, XXS, XS, S, M, L, XL, XXL)*
    • `html` (facultatif) si `false`, la balise ne retourne que l'URL de la photo, sans HTML
    • `link` (facultatif) si `true`, la photo est cliquable, vers sa page
    
    ```html
    [photo id=46]
    
    [photo id=46 album=22 size=M html=true link=true]
    ```
    
    **\[random album=xx\]**
    Il y a les mêmes options, sauf que la photo ou les photos sont prises aléatoirement dans toute la galerie ou dans `album`.
    Pour afficher plusieurs images utiliser l'option:
    • `nb_images` (optional) le nombre d'images à afficher
    
    ```html
    [random]
    
    [random album=123 size=M html=yes link=yes]
    
    [random album=123 size=M html=yes link=yes nb_images=8]
    ```
    
    **\[cat=xx\]**
    
    Cette balise permet d'insérer un album dans la description, avec `xx` le numéro de l'album.
    
    **Insérez un carrousel
    \[slider album=xx\]**
    Permet d'insérer un diaporama.**Options:** (vous devez renseigner `album` OU `list`)
    • `album` (facultatif) album source
    • `nb_images` (facultatif) nombre maximal de photos dans le diaporama
    • `random` (facultatif) choisir les photos aléatoirement dans l'album
    • `list` (facultatif) une liste de photos séparées par une virgule
    • `size` (facultatif) la taille des photos, parmi *(SQ, TH, XXS, XS, S, M, L, XL, XXL)*
    • `speed` (facultatif) la vitesse du diaporama (en secondes)
    • `title` (facultatif) afficher le nom de la photo
    • `effect` (facultatif) effet de transition (voir [la doc de NivoSlider](http://docs.dev7studios.com/jquery-plugins/nivo-slider#jumpNav-5))
    • `arrows` (facultatif) afficher les flèches de navigations
    • `elastic` (facultatif) adapter la taille du diaporama à chaque photo
    • `control` (facultatif) afficher la barre de navigation, peut aussi valoir `thumb`
    • `thumbs_size` (facultatif) taille des miniatures en pixel si `control=thumb`
    
    ```html
    [slider album=123]
    
    [slider list=46,47,52]
    
    [slider album=123 nb_images=10 random=false size=M speed=3 title=false effect=fade arrows=true elastic=false control=true thumbs_size=80]
    ```
    
    **Masquer un élément**
    
    **Masquer un album**
    
    Utilisez la balise `<!--hidden-->` dans le nom de l'album :
    • celui-ci ne sera plus affichée sur la page de l'album parent
    • il reste visible dans le menu des albums
    
    **Masquer un album dans le menu**
    
    Utilisez la balise `<!--mb-hidden-->` dans le nom de l'album :
    • celui-ci ne sera plus affichée dans le menu des albums
    • il reste visible sur la page de l'album parent
    
    **Masquer une photo**
    
    Utilisez la balise `<!--hidden-->` dans le nom de la photo :
    • celle-ci ne sera plus affichée sur la page des vignettes
    • elle reste néanmoins visible au sein de l'album
    
    **Rediriger un élément**
    
    **\[redirect http://piwigo.org\]**
    Insérez cette balise dans la description d'un album afin de le rediriger vers l'URL de votre choix.
    
    **\[redirect img=xx\]**
    Redirige vers une photo de votre galerie où `xx` est l'identifiant de celle-ci; vous pouvez également préciser l'identifiant de l'album après le numéro de la photo : `xx.ccc`.
    
    **\[redirect cat=xx\]**
    Redirige vers un album de votre galerie où `xx` est l'identifiant de celui-ci.
    
    **\[redirect search=xx\]**
    Redirige vers une page de recherche de votre galerie où `xx` est l'identifiant de la page de recherche.
    
    **Lien de connexion & block authentifié
    \[login-link\]**
    Ce tag permet d'ajouter n'importe où un lien de connexion avec redirection automatique vers la page courante.**Options:**
    • `html` (facultatif) si `false`, la balise ne retourne que l'URL du lien, sans HTML
    • `text` (facultatif) texte du lien, peut contenir des tags `[lang]`
    
    ```html
    [login-link]
    
    [login-link html=true text="log in[lang=fr]connectez-vous[/lang]"]
    ```
    
    **\[logged\]**
    Affiche un block de texte selon si l'utilisateur est connecté ou pas.
    
    ```html
    [logged=true] Welcome back [/logged]
    [logged=false] Please log in [/logged]
    ```
    

## Perso Footer : Personnaliser le pied de page de votre galerie

Par défaut, le pied de page, ou “footer” de votre galerie affiche un texte de présentation de Piwigo, ainsi qu’un lien de connexion/déconnexion et un lien pour envoyer un email au webmaster de la galerie (abonnés [Piwigo Cloud](http://piwigo.org) uniquement).

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-3494b9f3.png)

Vous pouvez ajouter du contenu à ce footer grâce au plugin **Perso Footer**.

La configuration de ce plugin vous donne accès à un bloc de saisie de texte où vous pouvez insérer du texte simple ou du code HTML.

Si vous installez en plus le plugin FCK Editor, qui ajoute aux zones de saisie de texte un éditeur visuel pour mettre en forme le texte, vous pourrez facilement créer un pied de page personnalisé.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-bc553697.png)

## Personal Favicon : Personnaliser l’icône de votre galerie dans le navigateur

Par défaut, le favicon de votre galerie Piwigo, c’est à dire l’icône qui s’affiche dans le navigateur, est l’icône de Piwigo Cloud.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-8435a237.png)

Vous pouvez personnaliser cette icône en activant le plugin **Perso Favicon**.

Une fois ce plugin activé, rendez vous dans sa page de configuration.

Vous pouvez télécharger sur Piwigo un fichier (extension .ico, maximum 5ko) qui viendra remplacer l’icône par défaut.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-f4da6a9b.png)

## OpenStreetMap : Géolocaliser vos photos sur une carte interactive

Le plugin OpenStreetMap, qui se base sur le projet cartographique libre [OpenStreetMap](https://www.openstreetmap.fr/), permet d’afficher vos photos sur une carte en fonction de leurs coordonnées GPS.

Vous pouvez voir ici un exemple de galerie qui intègre la géolocalication avec OpenStreetMap : [https://laseineavelo.piwigo.com/](https://laseineavelo.piwigo.com/)

La carte peut être affichée :

- Sur la page d’accueil de Piwigo
    
    ![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-d2a16cc9.png)
    
- Sur la page d’un album
    
    ![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-6bc04021.png)
    
- Sur la page d’une photo
    
    ![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-f96d2565.png)
    

De plus, le plugin peut ajouter une page disponible depuis le menu de la galerie, qui ouvre une carte en plein écran.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-2b4cf86b.png)

Lorsque l’on clique sur un point d’intérêt sur la carte, on affiche la photo associée ainsi que les informations disponibles, comme le titre de la photo ou encore son auteur. Un clic sur l’image ouvre la page de la photo.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-97a6b88e.png)

Dans l’administration, lorsque vous éditez une photo, un onglet OpenStreetMap permet de visualiser les coordonnées géographiques de l’image et si nécessaire, de les modifier.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-7455d07b.png)

Il est également possible de modifier les coordonnées GPS d’un lot d’image dans la gestion par lots.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-d0df2bd7.png)

De nombreuses options de paramétrage sont disponibles dans la configuration du plugin. Vous pouvez notamment modifier l’apparence de la carte, sa taille, activer ou pas son emplacement…

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-8d4fc096.png)

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-f72fd449.png)

Vous pouvez même créer votre style personnalisé pour les couleurs de votre carte ainsi que pour les épingles représentant les photos.

## Header Manager : gérer facilement la bannière de votre galerie

Il existe plusieurs moyens d’ajouter une bannière à votre galerie Piwigo.

La plus basique est disponible depuis l’administration, menu Configuration>Options, onglet Général, section Paramètres de base. Vous pouvez à cet endroit saisir un code HTML pour votre bannière.

Le plugin **Header Manager** vous donne plus d’options pour paramétrer votre bannière.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-e6afe999.png)

Ce plugin permet :

- d’uploader une ou plusieurs images ou d’en choisir une parmi les photos de votre galerie
- de retailler en ligne votre image pour créer votre bannière
- De personnaliser votre bannière :
    - Afficher seulement une image
    - Afficher le titre de votre galerie au dessus de l’image (en transparence)
    - Afficher l’image et le texte de votre choix
    - De choisir si la bannière s’affiche ou pas sur la page des photos
    - De faire tourner plusieurs bannières de façon aléatoire
    - De mettre en place des bannières spécifiques par album

Pour en savoir plus sur la création des bannières, avec ou sans ce plugin, lisez cet article :

[Ajouter une bannière personnalisée à votre galerie](ajouter-banniere-personnalisee-piwigo)

## Paypal Shopping Cart : Vendre des photos sur votre galerie avec Paypal

Vous souhaitez vendre des tirages photo, par exemple, sur votre galerie ?

C’est possible avec le plugin **Paypal Shopping Cart.**

Pour utiliser ce plugin, vous devez au préalable créer un compte Paypal.

**Ce compte doit utiliser la même adresse email que le webmaster de votre galerie.**

La configuration du plugin Paypal Shopping Cart permet de paramétrer :

- La devise utilisée sur votre site
- L’activation du panier Paypal pour toute la galerie ou seulement certains albums
- La gestion de tarifs différents en fonction des tailles de photos
- Le montant des frais d’envoi (fixes)

Une fois ces éléments paramétrés, un bouton “Ajouter au panier” sera ajouté sur les pages des photos dans les albums concernés.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-f77a886b.png)

L’ajout d’une photo au panier ouvre une page de paiement Paypal ; mais le visiteur peut retourner sur votre galerie, et ajouter d’autres photos à son panier.

Une fois qu’il a terminé ses achats, il peut payer la commande sur Paypal.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-7ca2ec7e.png)
