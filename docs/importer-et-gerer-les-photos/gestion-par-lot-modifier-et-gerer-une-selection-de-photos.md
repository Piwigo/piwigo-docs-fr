# Gestion par lot : Modifier et gérer une sélection de photos

**Comment modifier, supprimer, mettre à jour une sélection de fichiers en masse dans Piwigo ?**

C’est le but de la fonctionnalité de Gestion par lot.

Le gestionnaire de lots permet de sélectionner une série de fichiers selon divers critères pour les modifier ou bien les supprimer.

Vous avez également la possibilité de créer une sélection de photos en naviguant sur votre galerie grâce au panier, et de les modifier ensuite dans l’administration.

Le gestionnaire de lot est une des fonctionnalités les plus puissantes de Piwigo, qui vous fera gagner un temps infini, alors prenez le temps de l’apprivoiser !

## Gestion par lot : Présentation

Pour accéder au menu Gestion par lot, rendez-vous dans l’administration et sur le menu de gauche, rendez-vous dans Photos > Gestion par lot.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-5c5d6532.png)

Cet écran comporte deux onglets : 

- Mode global (par défaut)
- Mode unitaire

L’onglet Mode global vous permet de choisir une sélection de photos depuis de nombreux critères et de leur appliquer une modification en masse.

Cet écran est conçu en 3 parties :

- Filtre : cette section permet de créer une sélection de fichiers que vous souhaitez mettre à jour, en combinant des filtres selon de nombreux critères disponibles.
- Sélection : cette section affiche la sélection résultant de vos critères de filtrage, et vous permet de l’affiner en cochant / décochant certains fichiers.
- Action : cette section permet de choisir l’action à appliquer à votre sélection.

## Gestion par lot : Utilisation des Filtres

Par défaut, le dernier filtre utilisé est appliqué. Souvent, il s’agit du dernier import.

En cliquant sur la croix, vous pouvez supprimer ce filtre.

![fr-gestion-lot-filtre.gif](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-087b32cc.gif)

En cliquant sur “Ajouter un filtre”, vous allez pouvoir choisir le ou les critères de filtrage de votre sélection, parmi les critères disponibles.

![fr-gestion-lot-filtre-choix.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-bae8066e.png)

Lorsque vous ajoutez un filtre, les photos correspondant à ce filtre ne sont pas automatiquement affichées : pour visualiser le résultat de votre sélection, vous devez cliquer sur “Rafraîchir le lot de photos”.

### **Filtrer les photos par album**

Le filtre Album permet de choisir un album dont vous souhaitez afficher les fichiers. 

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-3a0e2ad6.png)

Pour sélectionner un album, cliquez sur le bouton : cela ouvre la fenêtre de recherche d’album.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-fd10abfa.png)

Utilisez le moteur de recherche ou naviguez dans la liste et cliquez sur le + pour choisir l’album.

Une fois l’album choisi, vous pouvez choisir d’inclure dans votre sélection les photos contenues dans ses albums enfants, en cochant “inclure les sous-albums”.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-484a72ce.png)

### **Filtrer les photos par tag**

Le filtre Tag permet de filtrer les photos par Tag. Vous pouvez saisir plusieurs tags, et choisir :

- de n’afficher que les fichiers associé à TOUS les tags choisis (tous les tags)
- ou d’afficher les fichiers associés à au moins un des tags choisis (n’importe quel tag)

![fr-gestion-lot-filtre-tag.png.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-becb58da.png)

### **Filtrer les photos par niveau de confidentialité**

Le filtre Niveau de confidentialité permet de n’afficher que les fichiers associés à un niveau de confidentialité donné :

- Tout le monde
- Contacts
- Amis
- Famille
- Admins

L’option “inclure les photos d’un niveau de confidentialité inférieur” permet d’imbriquer plusieurs niveaux de confidentialité.

![fr-gestion-lot-filtre-confid.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-ca6b983e.png)

Exemple : si on choisit le niveau de confidentialité “Amis” et que l’on coche cette option, on affichera les photos associées aux niveaux de confidentialité “Amis” ET “Contacts”.

Pour comprendre le fonctionnement des niveaux de confidentialité, [lisez cet article](../les-utilisateurs/les-niveaux-de-confidentialite).

### **Filtrer les photos par dimensions**

Le filtre Dimensions permet de filtrer les photos en fonction de leurs dimensions :

- largeur
- hauteur
- ratio largeur / hauteur (format)

![fr-gestion-lot-filtre-dimensions.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-be3f2576.png)

Pour choisir la fourchette de votre choix, vous n’avez qu’à déplacer les curseurs comme dans l’exemple ci-dessus.

Si vous souhaitez un format d’image précis (portrait, paysage, carré, diaporama), cliquez sur le libellé correspondant : le ratio sera automatiquement mis à jour.

### **Filtrer les photos par poids**

Le filtre Poids permet de filtrer les photos en fonction de leurs poids en Mo (mega octets).

![fr-gestion-lot-filtre-poids.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-83d0b253.png)

### **Rechercher une photo par mot-clé**

Le filtre “Recherche” permet d’afficher un moteur de recherche texte.

![fr-gestion-lot-filtre-recherche.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-b2f7ed50.png)

Il fonctionne de la même manière que le moteur de recherche de votre galerie. 

Cliquez sur "Conseils de recherche" pour découvrir des fonctions de recherche puissantes.

### **Filtrer les photos avec les filtres prédéfinis**

Piwigo propose par défaut de nombreux filtres prédéfinis qui correspondent à un usage fréquent de Piwigo. 

Voici les filtres disponibles en standard :

- Afficher le dernier import : afficher les dernières photos importées (vous pouvez aussi cliquer sur le menu Photos > Photos récentes pour afficher le dernier import)
- Doublons : cela permet de trouver toutes les photos en doublon (qui ont le même nom) sur votre photothèque afin de les dédoublonner
- Favorites : permet de retrouver les photos ajoutées dans vos favoris sur la galerie
- Panier : permet de retrouver toutes les photos ajoutées à votre “Panier” (vous pouvez aussi cliquer sur le menu Photos > Panier, voir chapitre Panier)
- Sans albums (orphelines) : cela permet de retrouver les photos de votre galerie qui ne sont ajoutées à aucun album, et ne sont donc pas visibles
- Sans tag
- Tout : affiche toutes les photos de votre photothèque

![fr-gestion-lot-filtres-predefinis.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-3026d40d.png)

### **Combiner plusieurs filtres**

Il est tout à fait possible de combiner plusieurs filtres.

Une fois votre premier filtre sélectionné, cliquez à nouveau sur “Ajouter un filtre” : les filtres se combinent.

![fr-gestion-lot-filtres-combinés.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-7e801bc5.png)

### **Batch Manager Prefilters: Ajouter de nouveaux filtres prédéfinis au gestionnaire de lots**

Pour ajouter de nouveaux filtres prédéfinis, installez le plugin **Batch Manager Prefilters**.

Il ajoute les filtres suivants :

- Fichiers associés à plusieurs albums
- Fichiers associés à un seul album
- Fichiers avec auteur
- Fichiers sans auteur
- Fichiers avec tags
- Fichiers sans date de création
- Fichiers sans titre

Vous pouvez également installer le plugin **Batch Manager, Photo Description**, pour ajouter le filtre prédéfini “Sans description”. 

Vous pourrez ainsi en un clin d’oeil visualiser les photos pour lesquelles aucune description n’a été saisie.

### **Batch Manager Added By : Rechercher une photo par utilisateur**

Pour filtrer les photos en fonction de l’utilisateur qui les a importées dans Piwigo, vous devez installer le plugin **Batch Manager, Added By**.

!!! info
    Si vous êtes client d’une offre Piwigo Cloud, ce plugin n’est accessible qu’à partir de l’offre Équipe.


Une fois activé, ce plugin ajoute un nouveau filtre dans la gestion par lot “Ajouté par”.

## Gestion par lot : Votre sélection

Une fois que vous avez appliqué vos filtres et cliqué sur “Rafraîchir le lot de photos”, les photos correspondant à votre recherche s’affichent dans la zone “Votre sélection”.

Par défaut, 20 fichiers sont affichés à l’écran. Vous pouvez naviguer dans votre sélection grâce aux liens de pagination ou aux flèches en bas à droite ; vous pouvez également augmenter la quantité de fichiers affichés à l’écran en cliquant sur 50, 100 ou Tout en bas à gauche.

![fr-selection-photos-import.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-fc8c0a39.png)

Pour sélectionner les fichiers à modifier, vous pouvez tout simplement cliquer sur chaque fichier à éditer. Vous pouvez également cliquer sur :

- “Toute la page” pour sélectionner tous les fichiers visibles à l’écran
- “Tout le lot” pour sélectionner tous les fichiers de votre sélection
- “Inverser” pour sélectionner tous les fichiers sauf ceux sur lesquels vous avez cliqué
- “Rien” pour désélectionner les fichiers sélectionnés

Les fichiers sélectionnés sont mis en avant grâce à une icône orange.

![fr-selection-fichiers-lot.gif](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-05346d76.gif)

Sur l’écran Mode global, vous pouvez également modifier unitairement un fichier.

Pour cela, passer la souris sur la vignette de la photo et cliquez sur l’icône représentant un crayon.

![fr-edition-lot-unité.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-01c7eead.png)

La page d’édition de la photo s’ouvre alors dans un nouvel onglet. Vous pouvez maintenant modifier ce que vous souhaiter, enregistrer vos modifications en cliquant sur “Modifier les paramètres”, fermer l’onglet et retourner sur la page Mode global pour continuer vos modifications.

## Gestion par lot : Modifier les fichiers de votre sélection en masse

Une fois que vous avez choisi les photos à modifier, cliquez sur “Choisir une action” : la liste déroulante affiche toutes les modifications que vous pouvez appliquer à votre sélection :

- Supprimer les fichiers
- Associer à un ou plusieurs album(s)
- Déplacer vers un autre album (ou plusieurs)
- Dissocier de l’album en cours
- Ajouter des tags
- Définir l’auteur des photos
- Définir le titre des photos
- Définir la date de création
- Qui peut voir ces photos ? (définir le niveau de confidentialité des photos)
- Synchroniser les méta-données
- Ajouter au panier (si votre panier est vide)
- Retirer du panier (lorsque le filtre choisi est “Panier”)
- Supprimer les tailles multiples des photos
- Générer les tailles multiples des photos
- Vidéos (actions spécifiques aux fichiers vidéos)

![fr-edition-lot-actions.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-d57b7167.png)

### **Exemple : modifier le titre des photos**

Vous avez importé dans Piwigo des fichiers avec un nom généré par l’appareil de prise de vue. Le titre des fichiers par défaut est récupéré depuis le nom du fichier (IMG_4545, IMG_4546…).

Vous souhaitez ajouter un libellé explicite en préfixe du nom actuel.

Une fois les fichiers choisis, sélectionnez l’action “Définir le titre”.

Dans le champ de saisie, saisissez le titre que vous voulez donner à vos fichiers, ici : “cap-saint-vincent”.

![fr-edition-lot-titre.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-d88ce83e.png)

Cliquez sur “Appliquer l’action” : les fichiers ont désormais pour titre “cap-saint-vincent(IMG_XXXX.JPG).

### **Exemple : ajouter un tag à une sélection**

Pour ajouter un tag à une sélection, cliquez sur Choisir une action > Ajouter les tags. Choisir dans la liste un tag existant ou saisissez un texte pour ajouter un nouveau tag.

![fr-edition-lot-tags.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-adc6350f.png)

Cliquez sur Appliquer l’action : le tag a été ajouté à vos photos.

### **Posted Date Changer : Modifier la date d’ajout avec le gestion par lot**

Modifier à posteriori la date d’ajout d’une sélection de photos peut être bien utile, mais par défaut, cette action n’est pas disponible dans Piwigo. Pour l’ajouter, vous devez activer le plugin **Posted Date Changer.**

Une fois ce plugin activé, l’action “Changer la date d’ajout” devient disponible dans la gestion par par lot.

## Gestion par lot : **Mode unitaire**

Le gestionnaire de lot vous permet également de modifier un par un les fichiers de votre sélection.

Pour cela, rendez-vous dans l’onglet Mode unitaire.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-e2b7e596.png)

Cette page affiche tous les fichiers correspondant aux filtres appliqués dans le premier onglet.

!!! Warning "Attention"
    Si vous modifiez les filtres, pensez bien à cliquer sur “Rafraîchir le lot de photos” : cela mettra aussi à jour la sélection affichée dans l’onglet “Mode unitaire”.


Vous pouvez ainsi, pour chaque fichier, modifier son titre, son auteur, sa date de création, son niveau de confidentialité, modifier les tags, le ou les albums associé(s), modifier la description.

N’oubliez pas cliquer sur le bouton Valider en bas de l’écran pour enregistrer vos modifications. 

## Utilisez le panier dans Piwigo

Comme expliqué dans le chapitre précédent, Piwigo vous permet de créer un “Panier” qui contient une sélection de fichiers mis de côté pour plus tard.

Depuis votre galerie, vous pouvez ajouter une photo à votre panier depuis la page de cette photo en cliquant sur l’icône “Ajouter au panier”.

Selon votre thème, l’icône pourra avoir la forme d’un caddie, d’un drapeau, ou encore d’un panier. Sur Modus, le thème par défaut de Piwigo, l’icône a la forme d’un caddie.

![fr-panier-photo.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-b58ec7f7.png)

Vous pouvez également ajouter toutes les photos d’un album à votre panier en cliquant sur l’icône “Ajouter au panier” de la page Album.

![fr-panier-album.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-748879e8.png)

Une fois que vous avez fait votre sélection, vous devez retourner dans l’administration pour visualiser votre panier.

Pour cela cliquez sur le menu Photos > Panier. Ce menu affiche à tout moment le nombre de fichiers dans votre panier.

![fr-panier.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-5004451f.png)

Le menu Panier affiche tout simplement l’écran de gestion par lot, filtré sur le filtre prédéfini “Panier”.

Pour vider le panier, cliquez sur le bouton “Vider le Panier” en dessous du filtre.

![fr-panier-vider.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-c37f1e32.png)
