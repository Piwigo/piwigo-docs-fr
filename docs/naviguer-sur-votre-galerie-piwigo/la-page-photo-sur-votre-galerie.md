# La page Photo sur votre galerie

À partir du moment où l’on accède à un fichier (image ou autre) sur la galerie Piwigo, depuis un album, une recherche ou tout autre moyen, on accède à la page Photo.

Cette page permet de visualiser une photo, ses informations et d’effectuer un certain nombre d’actions sur ce fichier.

Dans cet article nous verrons comment la page Photo est structurée, quelles fonctionnalités sont disponibles, quelles sont les options de personnalisation possible, en standard ou avec des plugins.

<aside>
⚠️ Remarque : la plupart des captures d’écran présentées dans cet article montrent une galerie utilisant le thème Modus. Suivant le thème de votre galerie, la présentation des informations et les icônes utilisées ne sont pas forcément les mêmes.

</aside>

## Structure de la page Photo

Quel que soit le thème de votre galerie, la page Photo contient toujours les mêmes éléments, en plus du menu et du pied de page qui sont affichés sur toutes les pages :

- Un fil d’ariane, qui permet de voir où ce situe cette photo dans l’arborescence des albums, et de naviguer dans cette arborescence ;
- Une barre d’outils, avec des icônes permettant d’effectuer certaines actions sur la photo ;
- Des flèches de navigation, permettant de naviguer de photo en photo au sein de l’album ;
- Les informations (propriétés, métadonnées) de la photo;
- La photo elle-même (avec le cas échéant, sa description);
- Une zone de commentaire (si les commentaires sont activés sur la galerie).

Vous pouvez voir ci-dessous comment la page Photo est structurée avec le thème par défaut (Modus).

![page-photo.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-dc110086.png)

Si vous utilisez un autre thème, comme Bootstrap Darkroom par exemple, l’organisation de la page sera différente mais on retrouvera bien les mêmes éléments.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-868f1e36.png)

### Naviguer avec les flèches

Sur la page Photo, vous avez la possibilité de naviguer au sein d’une sélection de photos grâce à des icônes en forme de flèches.

Avec le thème Modus, ces flèches s’affichent en haut à droite de la page.

![flèches.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-4f13cf73.png)

La sélection de photos dépend du chemin que vous avez pris pour accéder à la photo :

- Si vous venez de la page album, les flèches permettent de voir toutes les photos de l’album
- Si vous avez cliqué sur un tag, les flèches permettent de voir toutes les photos associées au même tag
- Si vous venez d’une recherche, les flèches permettent de naviguer au sein des résultats de votre recherche
- etc

Les flèches droite et gauche permettent de visualiser la photo suivante et la photo précédente.

La flèche vers le haut permet de revenir à la page précédente (album, tag, recherche, etc.)

### Propriétés et métadonnées

La page Photo affiche certaines propriétés et métadonnées de votre fichier.

Avec le thème Modus, cette section s’affiche à droite de la photo.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-8c892489.png)

Pour en savoir plus sur les propriétés et métadonnées, et pour savoir :

- comment choisir lesquelles afficher ou pas sur votre galerie
- comment définir l’ordre d’affichage des propriétés
- comment afficher ou pas les métadonnées
- comment créer des propriétés personnalisées
- etc

Alors lisez [l’article sur les propriétés et métadonnées](/importer-et-gerer-les-photos/gerez-les-proprietes-et-metadonnees-de-vos-fichiers).

### Commentaires

Si vous avez activé les commentaires sur votre galerie, une zone de commentaires s’affiche sur la page Photo.

Pour en savoir plus, lisez [l’article sur la gestion des commentaires](/les-commentaires-et-notes/commentaires-options-avancees).

### Actions disponibles sur une photo

La barre d’outils vous donne accès à différentes fonctionnalités. 

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-036c3e5c.png)

**Modifier la taille de photo affichée**

La première icône permet de choisir la taille de la photo affichée, parmi les tailles disponibles sur la galerie.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-901fedf6.png)

Pour savoir comment définir les tailles de photos disponibles sur la galerie, lisez le chapitre [Gérer les tailles de fichiers disponibles sur votre galerie](/naviguer-sur-votre-galerie-piwigo/la-page-photo-sur-votre-galerie).

**Lancer un diaporama**

L’icône en forme de bouton “Lecture” permet de lancer un diaporama pleine page, qui navigue parmi les photos de votre sélection.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-c1653cb8.png)

**Afficher les métadonnées**

L’icône en forme d’appareil photo permet d’afficher ou masquer les métadonnées de votre photo dans le panneau latéral des propriétés. En savoir plus sur [l’affichage des métadonnées](/importer-et-gerer-les-photos/gerez-les-proprietes-et-metadonnees-de-vos-fichiers)

**Télécharger la photo**

L’icône en forme de disquette permet de télécharger la photo sur votre ordinateur.

Par défaut, la photo téléchargée est l’originale.

Si vous avez activé le plugin **Download by Size,** l’utilisateur doit choisir au préalable la taille de la photo qu’il télécharge.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-3fe425a1.png)

Si la permission utilisateur “Téléchargement” est désactivée sur votre profil, l’original de la photo n’est pas disponible. Vous ne voyez les tailles rendues disponibles sur votre galerie. Ainsi, vous pouvez n’afficher sur votre galerie que des versions basse définition de vos photos si vous le souhaitez.

Si vous souhaitez désactiver complètement le bouton “Télécharger” sur votre galerie, rendez vous dans l’administration, menu Configuration > Options, onglet Afficher, Section “Page de la photo” et décochez la case *Activer l’icône “Télécharger ce fichier”.*

**Ajouter la photo à vos favoris**

L’icône en forme de coeur permet d’ajouter la photo à vos favoris. Vous pouvez retrouver vos favoris dans la page Mes favorites disponibles via le menu Explorer (ou Découvrir si vous utilisez le thème Bootstrap Darkroom). [En savoir plus sur les favoris](/naviguer-sur-votre-galerie-piwigo/gerer-ses-favoris)

**Choisir la photo comme représentante de cet album (administrateurs uniquement)**

L’icône en forme de trophée est visible uniquement aux administrateurs. Elle permet de choisir que la photo en cours deviennent la représentante de l’album.

**Éditer la photo (administrateurs uniquement)**

L’icône en forme de crayon est visible uniquement aux administrateurs. Elle permet d’accéder à l’écran de modification de la photo en cours dans l’administration de Piwigo.

**Ajouter la photo au panier (administrateurs uniquement)**

L’icône en forme de caddie est visible uniquement aux administrateurs. Elle permet d’ajouter la photo à son panier. Le panier est ensuite accessible dans l’administration pour effectuer des actions en masse via le [gestionnaire de lots](/importer-et-gerer-les-photos/gestion-par-lot-modifier-et-gerer-une-selection-de-photos).

## Gérer les tailles de fichiers disponibles sur votre galerie

Pour définir les tailles de photos disponibles sur votre galerie, rendez vous dans l’administration, menu Configuration > Options, onglet Tailles de photos.

Par défaut, Piwigo propose plusieurs tailles de fichiers. En réalité, Piwigo n’importe que le fichier original, mais il peut générer les autres tailles à la demande des utilisateurs, selon les tailles que vous aurez activées.

![](https://s3.amazonaws.com/helpscout.net/docs/assets/61e7cec9c1b8c85d97faea30/images/62385306ab585b230a8a2de9/file-hyfKHnjnF0.png)

### **A quoi servent les différentes tailles de fichiers ?**

- Les tailles Carré, Miniature et Moyen sont utilisées par Piwigo pour l'affichage des photos dans la galerie. C'est pourquoi vous ne pouvez pas les décocher.
- Les autres tailles peuvent être désactivées en les décochant. Sur votre galerie Piwigo, les utilisateurs pourront choisir la taille du fichier affiché sur leur écran parmi les formats disponibles.

Pour en savoir plus sur les différents formats, et éventuellement, les personnaliser, cliquez sur "Montrer les détails" (à droite de la page). Vous pouvez alors, pour chaque format :

- Voir la taille générée par Piwigo, par défaut
- Personnaliser cette taille en cliquant sur "édition" en face de chaque format
- Personnaliser la qualité d'image (par défaut, 95%)
- Rétablir les valeurs par défaut : cela permet d'annuler les modifications faites précédemment et de revenir sur les paramètres par défaut de Piwigo

![](https://s3.amazonaws.com/helpscout.net/docs/assets/61e7cec9c1b8c85d97faea30/images/6238533f2ce7ed0fb0917ac3/file-Kr8T7PoSY0.png)

### **Pourquoi personnaliser les tailles d'images disponibles ?**

Cela peut être utile pour divers besoins.

Exemple : pour votre site Internet, vous avez une taille standard de photo utilisée sur toutes les pages, de 700 pixels de large. Les mêmes photos, dans votre newsletter, doivent faire 400 pixel de large.

Vous pouvez personnaliser la taille XS en choisissant une largeur de 400 px, et la taille S en mettant une largeur de 700 px.

Ainsi, les utilisateurs de votre photothèque savent que pour votre site Internet, ils doivent télécharger la version S d'une photo, et pour la newsletter, la version XS.

Si vous avez activé sur votre galerie le plugin **Download by size**, le bouton de téléchargement sur la galerie permettra à l’utilisateur de choisir la taille du fichier au téléchargement.

Pour personnaliser la taille d'un des formats de fichiers, vous devez au préalable avoir cliqué sur "montrer les détails" dans la page Configuration > Tailles de photos.

En face du format que vous souhaitez modifier, cliquez sur "édition". Vous pouvez alors modifier la largeur, et la hauteur maximum du format choisi.

![](https://s3.amazonaws.com/helpscout.net/docs/assets/61e7cec9c1b8c85d97faea30/images/623856772ce7ed0fb0917ae9/file-QDaIMMz4Ox.png)

Si vous cochez "Retailler", votre fichier sera automatiquement "découpé" par Piwigo pour correspondre aux tailles choisies.

<aside>
⚠️ Attention : en faisant ce choix, vous risquez de perdre une partie de votre fichier.

</aside>

Une fois que vous avez terminé la personnalisation des tailles de fichier, n'oubliez pas de cliquer sur "Enregistrer les paramètres" pour sauvegarder votre configuration.

## Options de la page Photo

### Actions et propriétés affichées sur la page Photo

Vous pouvez définir dans l’administration de Piwigo quelles actions sont disponibles via la barre d’outil, et quelles propriétés sont affichées sur la page Photo, et d’autres options de personnalisation de cette page.

Pour en savoir plus lisez l’article sur les [options de personnalisation de votre galerie](/personnaliser-ma-galerie/options-de-personnalisation-de-votre-galerie).

Pour plus d’informations sur la personnalisation de l’affichage des propriétés et métadonnées, lisez l’article sur [les propriétés et métadonnées](/importer-et-gerer-les-photos/gerez-les-proprietes-et-metadonnees-de-vos-fichiers).

### **Ajouter un filigrane à vos photos**

Lorsque vous importez une photo dans Piwigo, Piwigo peut ajouter automatiquement un filigrane, c'est à dire une image qui va s'afficher "par dessus" votre photo.

**Pourquoi ajouter un filigrane à mes photos ?**

Ajouter un filigrane aux photos sur la galerie est utile lorsque vous souhaitez protéger vos droits d'auteurs. 

Avec un filigrane, vos photos seront visibles sur votre galerie, mais l'original ne sera pas téléchargeable. Cette option est souvent utilisée par les photographes qui veulent présenter leur travail sur leur galerie Piwigo mais veulent se protéger d'une violation de leur copyright.

**Comment ajouter un filigrane à mes photos ?**

Rendez vous dans l'administration, et dans le menu de gauche, cliquez sur Configuration > Options. 

Cliquez ensuite sur l'onglet "Filigrane". Cet écran permet de choisir un fichier image qui sera ajoutée à toutes les photos sur votre galerie, et de configurer un certain nombre d'options d'affichage de ce filigrane.

![](https://s3.amazonaws.com/helpscout.net/docs/assets/61e7cec9c1b8c85d97faea30/images/62385b962ce7ed0fb0917b19/file-gEvMZ1x3ir.png)

Pour voir ce que cela donne, vous pouvez faire le test avec un des fichiers fournis par Piwigo.

A côté de "Sélectionner un fichier", choisissez par exemple Owned.png. Vous pouvez modifier l'emplacement du filigrane (au milieu de l'image ou dans un des coins de l'image). Choisissons par exemple "Coin inférieur droit".

![](https://s3.amazonaws.com/helpscout.net/docs/assets/61e7cec9c1b8c85d97faea30/images/62385cd4c1688a6d26a778ce/file-9SjLEPs0mU.png)

Enregistrez les paramètres : sur votre galerie, toutes les photos sont affichées avec ce filigrane en bas à droite.

![](https://s3.amazonaws.com/helpscout.net/docs/assets/61e7cec9c1b8c85d97faea30/images/62385d15ab585b230a8a2e34/file-pfWauJmyLS.png)

Bien sûr, vous pouvez ajouter votre propre filigrane.

On recommande pour cela un fichier PNG sur fond transparent.

## Personnaliser la page Photo avec des plugins

Voici une sélection de plugins permettant d’ajouter des fonctionnalités à la page Photo.

### Custom Download Link : Ajouter un gros bouton de téléchargement

Le plugin Custom Download Link ajoute un gros bouton de téléchargement sur la page Photo.

![custom-download link.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-01a10007.png)

Ce bouton permet de télécharger directement l’original de la photo. Il ne s’affiche pas si l’utilisateur connecté n’a pas le droit “Téléchargement” activé sur son profil.

### Download by size : Choisir la taille du fichier téléchargé

On en a déjà parlé précédemment dans cet article : le plugin **Download by Size** vous permet d’offrir aux utilisateurs la possibilité de choisir la taille de photo téléchargée lorsqu’ils cliquent sur l’icône “Télécharger”. 

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-3fe425a1.png)

### Private Share : Partager une photo par un lien sécurisé par email

Le plugin **Private Share** permet aux utilisateurs habilités de générer un lien de partage d’une photo et de l’envoyer par email. Ce qui est très utile avec ce plugin, c’est qu’il vous permet de partager une photo présente dans un album privé, même avec des personnes n’ayant pas de compte Piwigo.

Une fois ce plugin activé, vous devez d’abord définir quels utilisateurs ont le droit de l’utiliser. Pour cela rendez vous dans la configuration du plugin. Le premier onglet vous permet de définir quels sont les groupes d’utilisateurs qui ont le droit de l’utiliser. [En savoir plus sur les groupes d’utilisateurs](/les-utilisateurs/les-groupes-dutilisateurs)

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-1a1a92dd.png)

Les utilisateurs habilités verront dans votre galerie Piwigo une icône “Partager” sur chaque photo.

![private-share.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-0613b9fa.png)

Si on clique sur cette icône, une fenêtre apparaît. Elle permet de saisir l’adresse email à laquelle on souhaite envoyer cette photo, et la durée de validité du lien (1 semaine, 2 semaines, 1 mois, ou 3 mois).

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-5480cef8.png)

Le destinataire reçoit un email contenant un lien permettant de visualiser la photo.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-85baf7de.png)

Le lien généré est parfaitement sécurisé et ne donne accès qu’à cette photo : le destinataire n’a aucun moyen d’accéder au reste de la galerie.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-2cc6cccb.png)

À tout moment, via la configuration du plugin (onglet Activité), les administrateurs peuvent contrôler l’historique d’utilisation de Private Share : ils peuvent voir les liens partagés, les destinataires, la date de partage et d’expiration, et choisir de faire expirer le lien de partage si nécessaire.

![privateshare-admin.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-6ef56631.png)

### Loupe : Pouvoir zoomer sur une photo

Le plugin **Loupe** permet aux visiteurs d’agrandir ou de zoomer sur un détail d’une photo en passant la souris dessus.

Une fois ce plugin activé, quand l’utilisateur passe sa souris sur une photo, le curseur se transforme en loupe. On peut zoomer et dézoomer à l’aide du curseur de la souris.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-919ba2f5.png)

### Social Buttons : Boutons de partage sur les réseaux sociaux

Le plugin **Social Buttons** permet d’afficher des boutons de partage sur les réseaux sociaux sur votre page Photo.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-43504c10.png)

Pour un affichage optimal, voici les options que nous vous conseillons d’utiliser dans la page Configuration du plugin Social Buttons.

- Position des boutons sur la page : Haut ou Bas
- Afficher les boutons : uniquement sur les photos
- Taille des photos partagées : nous vous conseillons de ne pas partager l’original mais un format de taille inférieure
- Mode léger : Activer (Si vous désactivez le mode léger, des cookies seront installés sur l’ordinateur de vos visiteurs pour activer leur tracking par les plateformes. De plus, le mode léger est plus élégant).

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-4197d8ca.png)

<aside>
ℹ️ Si vous utilisez le thème Bootstrap Darkroom, vous n’avez pas besoin d’utiliser ce plugin, puisque le thème intègre déjà des boutons de partage sur les réseaux sociaux.

</aside>

### Back2Front : Gérer des images recto-verso

Le plugin **Back2Front** permet d’afficher, sur la page Photo, une version alternative de la même photo ; il est généralement utilisé pour des images recto-verso.

Par exemple, il a été utilisé pour des galeries de cartes postales, ou de cartes à collectionner.

Quand ce plugin est activé, sur la page d’édition d’une photo dans l’administration, vous pouvez définir si cette image est le verso d’une autre image (le recto) en précisant l’identifiant du recto. Vous pouvez choisir si le verso doit être masqué de l’album.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-60242e34.png)

Lorsqu’un verso a été défini pour une photo, un bouton “Voir le verso” apparaît sur la page Photo. Quand on clique sur ce bouton, l’image correspondant au Verso est alors affichée.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-fcda53ba.png)

### **AlwaysShowMetadata : Toujours afficher les métadonnées des fichiers**

Par défaut, les métadonnées sont masquées sur la page Photo de votre galerie : il faut cliquer sur une icône pour les faire apparaître.

Si vous souhaitez qu’elles soient toujours affichées, alors installez le plugin **AlwaysShowMetadata.**

Pour en savoir plus sur les métadonnées, [lisez cet article](/importer-et-gerer-les-photos/gerez-les-proprietes-et-metadonnees-de-vos-fichiers).

### Rightclick : Interdire le clic droit sur la page Photo

Si vous souhaitez empêcher les visiteurs d’effectuer un clic droit sur une photo pour la télécharger, vous pouvez installer le plugin **rightClick**.

Une fois ce plugin activé, le clic droit sera inopérant sur la page Photo, mais également sur d’autres pages, sauf pour les administrateurs.

<aside>
⚠️ Attention : ce plugin ne garantit pas une sécurité totale de vos images. Seul le fait de mettre vos albums en mode privé protège vos photos.

</aside>

### Hide title : Masquer le nom de la photo dans le fil d’Ariane

Par défaut, le fil d’Ariane affiché sur la page Photo affiche le nom de la photo.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-9ea4ec5a.png)

Pour le masquer, il suffit d’activer le plugin **Hide Title on Browse Path.**

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-4f00672d.png)

### Automatic size : Taille de fichier automatique en fonction de la taille de l’écran

Le plugin **Automatic Size** permet d’adapter la taille de fichier affichée par défaut en fonction de la taille de l’écran de l’utilisateur. Il a été prévu pour les galeries utilisant le thème **Elegant**.

Ce plugin n’est **pas utile si votre galerie utilise le thème Modus**, car Modus prend déjà en charge par défaut l’affichage automatique de la taille adaptée à la résolution de votre écran.

De plus, ce plugin n’est pas compatible avec le thème **Bootstrap Darkroom**.

### Color Palette : extraire les couleurs de la photo

Le plugin **Color Palette** permet d’extraire automatiquement les couleurs d’une photo et de rechercher des photos par couleur.

Une fois ce plugin activé, sur chaque photo de votre galerie, vous retrouverez la palette de couleurs présentes sur cette photo.

![color-palette.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-6f5d63db.png)

En cliquant sur une ou plusieurs couleurs sur la palette, vous pouvez rechercher toutes les photos de votre galerie qui contiennent les mêmes couleurs.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-cd29f5e6.png)

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-5ce383be.png)

La page de configuration du plugin permet de paramétrer certaines options, comme le nombre de couleurs extraites par palette.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-1c49eb35.png)

<aside>
ℹ️ Attention ! L’activation du plugin ne génère pas les palettes sur chaque image de votre photothèque. La palette d’une photo est générée lorsqu’elle est affichée pour la première fois après l’activation du plugin. Au début, la recherche par couleur donnera donc peu de résultats puisque les palettes de vos photos n’auront pas encore été générées.

</aside>

Sommaire de l’article

---

← Précédent

[Les albums sur votre galerie](/naviguer-sur-votre-galerie-piwigo/les-albums-sur-votre-galerie)

Suivant →

[Les tags sur votre galerie](/naviguer-sur-votre-galerie-piwigo/les-tags-sur-votre-galerie)