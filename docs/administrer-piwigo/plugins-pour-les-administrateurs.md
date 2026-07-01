# Plugins pour les administrateurs

En plus des fonctionnalités d’administration classiques de Piwigo, certaines options supplémentaires sont disponibles via des plugins.

On en fait le tour sur cette page.

## Admin Tools : Administrer Piwigo depuis votre galerie

Le plugin **Admin Tools** permet aux administrateurs d'effectuer certaines tâches d'administration directement depuis la galerie (édition de photo, d'album...).

Une fois le plugin Admin Tools activé, vous verrez apparaître une nouvelle barre de navigation sur votre galerie lorsque vous êtes connecté en tant qu’administrateur.

![fr-admin-tools.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-f562c802.png)

Cette barre d’outils permet d’accéder aux principales pages d’administration depuis votre galerie.

Depuis la page d’une photo, vous avez également accès à des raccourcis vers des actions d’administration qui apparaissent :

- éditer la photo
- choisir la photo comme représentante de l’album
- ajouter au panier

![fr-admin-tools-2.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-3d8cf4b4.png)

Une fenêtre d’édition rapide permet de modifier les informations principales de la photo sans passer par l’administration.

Les mêmes fonctionnalités sont accessibles depuis les pages des albums.

Enfin, d’autres outils sont accessibles à droite de la barre Admin Tools :

![fr-admin-tools-3.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-054800fc.png)

- Voir en tant que : pour voir la galerie depuis le point de vue d’un autre utilisateur
- Changement de thème rapide
- Changement de langue rapide
- Les autres options ne seront utilisées que par les développeurs.

## Admin Messages : Ajouter un message d’accueil dans l’administration

!!! info
    Si vous êtes client d’une offre Piwigo Cloud, ce plugin n’est accessible qu’à partir de l’offre Équipe.

Le plugin **Admin Messages** permet aux administrateurs d'ajouter des messages sur l'accueil de l'administration de Piwigo (pour communiquer avec les autres administrateurs).

Les messages sont affichés sur le tableau de bord, en bas de la page.

Pour chaque message, on affiche le nom de l’administrateur, la date et le message.

![fr-admin-messages.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-06937cb2.png)

## **Protect Notification : Changer l’expéditeur des emails de notification**

Parfois, il arrive que les emails de notification envoyés par Piwigo arrivent en SPAM. Cela vient du fait qu’ils sont envoyés par l’adresse email de l’administrateur principal (webmestre). Si votre serveur (ou le serveur Piwigo Cloud) n’a pas le droit d’envoyer des emails depuis cette adresse mail, les emails sont considérés comme non sécurisés.

Pour régler ce problème, vous pouvez installer le plugin **Protect Notif**.

Une fois ce plugin activé, tous les emails de notifications envoyés par Piwigo seront expédiés depuis une fausse adresse du type “no-reply@[`mygallery.com`](http://mygallery.com)” (remplacez `mygallery.com` par votre nom de domaine).

En conséquence, les emails de notification seront correctement distribués.

!!! info
    Depuis février 2024, Protect Notif est activé par défaut sur tous les nouveaux comptes créés sur Piwigo Cloud.

## Download Limits : Limiter le nombre de téléchargements par jour

!!! info
    Si vous êtes client d’une offre Piwigo Cloud, ce plugin n’est accessible qu’à partir de l’offre Entreprise.

Le plugin **Download Limits** permet aux administrateurs de limiter le nombre de téléchargements par jour sur leur galerie.

!!! Warning "Attention"
    Le nombre de téléchargements maximum n’est pas paramétrable dans l’interface de Piwigo mais dans un fichier de configuration. Si vous êtes un client Piwigo Cloud, contactez le support pour le mettre en place.

## Export Data : Exporter les données de votre Piwigo

!!! info
    Si vous êtes client d’une offre Piwigo Cloud, ce plugin n’est accessible qu’à partir de l’offre Équipe.


Le plugin **Export Data** permet aux administrateurs d’exporter les données de Piwigo vers un tableur.

Les données exportables sont les suivantes :

- Albums
- Photos
- Commentaires
- Téléchargements

Les données sont exportées dans un fichier .CSV.

## FCK Editor : Ajouter un éditeur WYSIWYG à Piwigo

Le plugin **FCK Editor** permet d’ajouter un éditeur HTML avec des options de mise en forme sur la plupart des zones de saisies de l’administation de Piwigo :

- Champs “Description” des albums et des photos
- Pages personnalisées (disponibles avec le plugin **Additional Pages**)
- Blocs personnalisés (disponibles avec le plugin **PWG Stuff**)

Ci-dessous on peut voir comment mettre en forme la description d’une photo avec FCK Editor.

![fr-fck-editor.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-cd3807b4.png)

Par défaut, la version basique de FCK Editor est affichée sur la plupart des pages : les fonctionnalités proposées sont donc limitées. Mais il est possible d’activer davantage de fonctionnalités comme le montre la capture ci-dessous.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-93cd3f42.png)

Comment activer toutes ces fonctionnalités ?

- Si votre Piwigo est hébergé sur Piwigo Cloud, contactez le support.
- Si vous hébergez vous-même Piwigo, suivez le tutoriel ci-dessous.
    - Cliquez ici pour afficher le tutoriel
        
        La configuration de FCK Editor se trouve dans le fichier `*plugins/FCKEditor/fckeditor.tpl`.*
        
        Editez ce fichier et recherchez le code suivant :
        
        ```jsx
        CKEDITOR.config.toolbar_Basic =
        [
          ["Source"],["Bold","Italic","Underline"],
          ["JustifyLeft","JustifyCenter","JustifyRight","JustifyBlock"],
          ["Styles","Format","Font","FontSize"],
          ["Link","Unlink","ShowBlocks"]
        ];
        ```
        
        Remplacez cet extrait de code par le code suivant :
        
        ```jsx
        CKEDITOR.config.toolbar_Basic =
        [
            ['Source','-','Save','NewPage','Preview','-','Templates'],
            ['Cut','Copy','Paste','PasteText','PasteFromWord','-','Print', 'SpellChecker', 'Scayt'],
            ['Undo','Redo','-','Find','Replace','-','SelectAll','RemoveFormat'],
            ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField'],
            '/',
            ['Bold','Italic','Underline','Strike','-','Subscript','Superscript'],
            ['NumberedList','BulletedList','-','Outdent','Indent','Blockquote'],
            ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
            ['Link','Unlink','Anchor'],
            ['Image','Flash','Table','HorizontalRule','Smiley','SpecialChar','PageBreak'],
            '/',
            ['Styles','Format','Font','FontSize'],
            ['TextColor','BGColor'],
            ['Maximize', 'ShowBlocks','-','About']
        ];
        ```
        

## LocalFiles Editor : Ajouter du code personnalisé

Le plugin **LocalFiles Editor** vous permet de modifier des fichiers de Piwigo directement depuis l’administration.

!!! Warning "Attention"
    Cette fonctionnalité est réservée aux utilisateurs avertis !

Pour les clients Piwigo Cloud, ce plugin permet uniquement d’ajouter du code CSS personnalisé.

Pour les autres utilisateurs qui hébergent eux-mêmes Piwigo, ce plugin permet de modifier d’autres fichiers (configuration locale, fichiers de langue, etc). 

[En savoir plus sur LocalFiles Editor](../hebergez-votre-piwigo/modifier-la-configuration-locale-avec-localfiles-editor)

## Rightclick : Désactiver le clic droit sur les photos

Vous souhaitez empêcher les visiteurs de votre galerie de pouvoir télécharger les photos de votre galerie ?

Vous pouvez d’abord interdire le téléchargement aux utilisateurs invités (anonymes) ou à certains utilisateurs, dans la gestion des utilisateurs [comme expliqué dans cet article](../les-utilisateurs/creer-et-gerer-les-utilisateurs). Si vous désactivez le téléchargement, l’icône de téléchargement ne s’affichera pas.

Mais les visiteurs pourront toujours télécharger les photos en effectuant un clic droit > Enregistrer l’image sous.

Pour désactiver cette possibilité, il suffit d’activer le plugin **Rightclick**.

![fr-rightclick.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-1f381cda.png)

Une fois ce plugin activé, le clic droit sur les images sera désactivé sur votre galerie (sauf pour les administrateurs).

## Piwishack : Intégrer une photo sur une page web

Vous avez besoin d’intégrer vos photos Piwigo sur d’autres sites ?

Avec le plugin **Piwishack**, vous pouvez générer pour chaque photo un code HTML qui permettra d’embarquer votre photo sur une page web.

Une fois le plugin Piwishack activé, une nouvelle icône apparaîtra sur votre galerie au dessus des photos.

![fr-piwishak.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-f51f198c.png)

Un clic sur cette icône ouvre une fenêtre qui permettra de récupérer plusieurs codes.

Le premier onglet génère plusieurs codes HTML permettant d’embarquer la photo sur une page web.

![fr-piwishack2.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-d2a9deee.png)

 Voici les différentes options disponibles :

- Afficher la miniature sans lien
- Afficher la miniature avec un lien vers la photo dans votre galerie
- Afficher la miniature avec un lien direct vers la photo
- Afficher la vue normale (photo à la taille normale) sans lien
- Afficher la vue normale (photo à la taille normale) avec un lien vers la photo dans votre galerie

Le deuxième onglet génère plusieurs codes au format BBcode (utilisés principalement sur des forums de discussions), avec les mêmes options.

Il est enfin possible de générer des codes personnalisés.

## Stop Spammers : Lutter contre le SPAM

Le plugin **Stop Spammers** met en place un contrôle antispam sur votre galerie. S’il n’est pas activé, pensez à le faire.

## AntiAspi : Bannir des adresses IP de votre galerie

Le plugin AntiAspi a pour objectif de protéger votre galerie des robots ou utilisateurs malveillants qui pourraient attaquer votre site, notamment pour “aspirer” son contenu.

La configuration du plugin permet de définir des critères qui déclenchent le bannissement de l’adresse IP qui visite votre site, par exemple :

- Bannir l’adresse IP si 20 pages différentes ont été visitées en 10 secondes
- Bannir l’adresse IP si la même page a été vue 15 fois en 30 secondes
- etc.

Ces critères sont paramétrables.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-94e31b70.png)

L’onglet Adresses IP de la configuration du plugin AntiAspi permet de visualiser l’historique des adresses IP bannies, et d’ajouter des adresses IP toujours autorisées (liste blanche).

## Cookie consent : ajouter une bannière de consentement

Le plugin **Cookie Consent** permet d’ajouter une bannière sur votre site invitant les visiteurs à valider leur consentement aux cookies de base que peut laisser votre galerie sur leur ordinateur.

Il peut être également utilisé pour inviter les visiteurs à déclarer leur consentement aux conditions d’utilisation de votre galerie.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-14b10821.png)

Le texte, le texte du bouton ainsi que le lien sont paramétrables.

L’acceptation est enregistrée sous la forme d’un cookie dont vous pouvez choisir la durée de validité.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-9d6c6d2a.png)

!!! Warning "Attention"
    Si votre galerie utilise des cookies tiers comme ceux de Google Analytics, ce type de bannière n’est pas suffisante pour recueillir le consentement de vos visiteurs car elle est uniquement informative (l’utilisateur n’a pas la possibilité de refuser les cookies, ni de révoquer son consentement).

## Les plugins pour le SEO de votre galerie

Si votre galerie est publique, vous souhaitez sans doute que ses pages soient visibles sur Google et les autres moteurs de recherche.

Les plugins ci-dessous sont utiles si vous souhaitez améliorer le référencement naturel (SEO) de votre galerie Piwigo.

### Title : personnaliser la balise Title des pages du site

Ce plugin permet de personnaliser la balise meta “Title” de toutes les pages de votre galerie.

Vous pouvez personnaliser les balises Title des pages principales depuis la configuration du plugin.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-7ccaed61.png)

Vous pouvez par ailleurs modifier la balise meta Title de chaque photo et de chaque album sur la page d’édition, avec les autres propriétés.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-1d3ecfea.png)

### Meta : personnaliser les meta des pages du site

Outre la meta Title, personnalisable grâce au plugin **Title**, d’autres balises liées au SEO (référencement naturel) peuvent être paramétrées dans Piwigo, grâce au plugin **Meta**.

Les meta gérées par ce plugin sont les suivantes :

- author
- description
- keywords
- robots

Vous pouvez définir certaines balises de méta de façon globale sur toutes les pages du site, dans le premier onglet de la configuration du plugin.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-26dd56c7.png)

La balise **robots**, notamment, vous permet de définir si vous souhaitez ou pas que votre site soit indexé sur les moteurs de recherche :

- si vous souhaitez que votre galerie ne soit pas référencée, saisissez `noindex`
- si vous souhaitez que votre galerie soit référencée, saisissez `index`

Concernant la meta **Description**, nous vous conseillons de la paramétrer page par page. C’est une information importante pour le SEO puisqu’elle apparaît dans les résultats des moteurs de recherche.

![meta.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-f2f860b7.png)

Vous pouvez modifier la meta description de chaque photo et de chaque album sur la page d’édition, avec les autres propriétés.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-f600f1d6.png)

L’onglet “Métadonnées personnelles” de la configuration du plugin permet d’ajouter des balises meta personnalisées.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-c8ed7040.png)

### Meta Open Graph : personnaliser les balises meta open graph pour les réseaux sociaux

Les meta Open Graph permettent de personnaliser le contenu de la prévisualisation qui s’affiche lorsque l’on partage une page d’un site sur les réseaux sociaux.

Par défaut, ces données ne sont pas renseignées sur Piwigo. Si vous partagez le lien de votre galerie, le titre qui s’affichera sera le titre de la galerie, accompagné d’une photo prise au hasard.

Pour personnaliser ces balises meta sur votre galerie Piwigo, vous pouvez installer le plugin **Meta Open Graph**.

La configuration de ce plugin permet de personnaliser les meta open graph pour chacune des pages de votre galerie.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-6d7cb811.png)

Choisissez une page, par exemple l’accueil, et cliquez sur “édition des métadonnées Open Graph”.

Saisissez un titre, une description, et choisissez la photo qui doit représenter la page (via la liste déroulante ou en saisissant dans le champ “Métadonnées Open Graph lien de image” l’identifiant de la photo choisie.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-123dff58.png)

Cliquez sur “Sauvegardez”.

À présent, si vous partagez la page sur un réseau social (comme Facebook), la prévisualisation tiendra compte des balises meta que vous avez saisies.

![metadata-opengraph.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-7b8368e5.png)

Pour chaque photo et chaque album, vous pouvez renseigner des balises meta personnalisées dans l’administration, sur la page d’édition de la photo ou de l’album.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-632b0020.png)

L’onglet Configuration de la page de configuration du plugin permet de définir des paramètres par défaut.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-ba7b9adc.png)

Cela permet, entre autres : 

- de pouvoir définir une image spécifique pour les méta de vos albums et de vos photos (par défaut, on affichera la photo et la représentante de l’album)
- de définir un album dans lequel aller choisir une photo aléatoire pour la balise meta image lorsqu’elle n’est pas définie
- de choisir la taille de la photo utilisée
- de définir la langue utilisée par défaut
- de définir le nom de votre site
- de saisir un identifiant d’app id Facebook
- de définir le type de carte affiché lors d’un partage du Twitter (Twitter Card)
- de saisir votre identifiant Twitter si vous en avez un

[En savoir plus sur les meta open graph Facebook](https://developers.facebook.com/docs/sharing/opengraph/using-objects?locale=fr_FR)

[En savoir plus sur les Twitter card](https://developer.twitter.com/en/docs/twitter-for-websites/cards/guides/getting-started)

## Plugins pour ajouter du code personnalisé sur votre galerie

Il existe deux plugins permettant d’ajouter du code personnalisé sur votre galerie Piwigo. 

Il est intéressant de connaître les deux car il peuvent fonctionner en parallèle.

Ainsi, vous pouvez par exemple ajouter du code dans la balise <head> avec le premier, et dans le footer de votre site (avant la fermeture de la balise <body>) avec le second.

### **Add < head > element : Ajouter du code dans la balise <head>**

Le plugin **Add < head > element** permet d’ajouter du code (un script javascript par exemple) dans la balise <head> de votre galerie. Vous pouvez choisir d’activer ce code sur la galerie, l’administration, ou les deux.

### Statistics**: Ajouter du code dans la balise <head> ou le footer**

Conçu pour insérer un code de suivi d’un outil statistique externe (comme Matomo ou Google Analytics) sur votre galerie, le plugin Statistics permet également d’ajouter du code pour un autre usage.

Il permet de saisir le code souhaité et de choisir si on l’insère dans le header du site, dans le footer, ou les deux.

L’option “Exclure l'administrateur des statistiques” permet de ne pas activer le code saisi quand un administrateur est connecté.

L’option “Exclure l'utilisateur non connecté des statistiques” permet de ne pas activer le code saisi quand le visiteur de la galerie n’est pas connecté.
