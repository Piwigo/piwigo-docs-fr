# Rechercher une photo sur votre galerie

Pour effectuer une recherche sur votre galerie Piwigo, vous avez plusieurs possibilités : aussi bien une simple recherche rapide par mot-clé, qu’une recherche multicritères en combinant plusieurs filtres.

On fait le tour dans cet article !

<aside>
🆕 La recherche a été complètement refondue depuis la version 14 de Piwigo. Si vous souhaitez accédez à l’ancienne documentation de la recherche, lisez cet article :

[[Archive] Ancienne version de la recherche Piwigo](Rechercher%20une%20photo%20sur%20votre%20galerie/%5BArchive%5D%20Ancienne%20version%20de%20la%20recherche%20Piwigo%20decdfdc0cf68475bbb76bac0ba54e891.md)

</aside>

## La recherche rapide

### **Utiliser le champ de recherche rapide**

Si cette fonctionnalité est active sur votre galerie (c’est le cas par défaut sur la plupart des thèmes), vous disposez d’un champ de recherche.

![fr-recherche-modus.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-c682d0d2.png)

Sur certains thèmes, la recherche sera accessible en cliquant sur un point de menu (exemple ci-dessous avec la configuration par défaut du thème Bootstrap Darkroom).

![fr-recherche-boostrap.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-1df6df04.png)

Saisissez un mot dans la recherche rapide et appuyez sur la touche Entrée : les résultats affichent les photos qui correspondent à votre recherche.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-65e33e43.png)

Pour filtrer les résultats, Piwigo recherche par défaut le mot que vous avez saisi :

- dans le nom (titre) de la photo dans Piwigo
- dans le nom du fichier
- dans la description du fichier
- dans les tags associés à vos photos
- dans l’identifiant des photos

Par ailleurs, si le mot-clé saisi correspond à un tag ou au nom d’un album de votre galerie, ils apparaîtront également dans les résultats. Cliquez sur le bouton “Tags trouvés” ou “Albums trouvés” voir la liste des tags / albums correspondant à votre recherche.

![fr-tag-result-search.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-428d7775.png)

### Modifier / affiner une recherche rapide

Depuis la version 14 de Piwigo, à chaque fois que vous faites une recherche rapide, une barre de filtres apparaît au dessus des résultats de la recherche. On en reparlera dans le chapitre suivant. Cette barre de filtres vous permet d’affiner votre recherche en appliquant des critères supplémentaires (tag, album, auteur…).

Cette barre de filtres vous permet également de modifier la recherche en cours. Pour cela, il suffit de cliquer sur la zone affichant le mot que vous avez recherché, ce qui va ouvrir une fenêtre.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-46d07e70.png)

Dans cette fenêtre, vous allez pouvoir :

- modifier le contenu de votre recherche
- effectuer une recherche sur plusieurs mots en filtrant sur tous les mots ou bien l’un des mots ;
- modifier où Piwigo effectue sa recherche (par exemple, en désactivant la recherche dans les descriptions des photos).

### RV autocomplete : Activer l’**autocomplétion sur le moteur de recherche rapide**

Vous souhaitez gagner encore plus de temps lorsque vous rechercher un tag ou un album sur votre galerie ?

On vous conseille d’utiliser le plugin **RV autocomplete**.

Une fois ce plugin activé, quand vous saisirez une recherche, les albums et tags correspondant à votre recherche seront automatiquement proposés.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-91670494.png)

## Les filtres de recherche multicritères

### Lancer une recherche multicritères

Depuis la version 14 de Piwigo, l’ancienne recherche avancée a été remplacée par une barre de filtres.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-c7bd8d70.png)

Pour lancer une recherche, vous avez plusieurs possibilités :

- Utiliser le formulaire de recherche rapide (présenté au chapitre précédent) : vous pourrez alors affiner ou réinitialiser votre recherche grâce aux filtres
- Vous rendre dans le menu Explorer > Recherche (thème Modus) ou Découvrir > Recherche (thème Bootstrap Darkroom), pour afficher la page de recherche avec les filtres.
- Depuis la page d’un album ou d’un tag, cliquer sur le bouton ou l’icône “Recherche dans ce lot” (si ce bouton est activé sur votre galerie).

### Choisir les filtres affichés

Par défaut, la barre de filtres affiche 4 filtres :

- recherche par mot (même fonctionnement que la recherche rapide)
- filtrer par Tag
- filtrer par Album
- filtrer par Auteur

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-a6bccb35.png)

Vous pouvez cliquer sur “Choisir les filtres” pour ajouter d’autres critères :

- Date d’ajout (date d’import dans Piwigo)
- Date de création (date de création du fichier)
- Ajouté par (choix de l’utilisateur ayant importé le fichier)
- Type de fichier (extension de fichier : JPG, PNG…)
- Ratio (portrait, carré, paysage…)
- Poids (en octets)
- Hauteur (en pixels)
- Largeur (en pixels)

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-de87e491.png)

Cliquez simplement sur un critère pour l’ajouter ou le retirer de la barre de filtres, et validez. Les critères choisis sont appliqués. Votre choix de filtres visibles est sauvegardé, mais il ne s'applique qu'à votre utilisateur.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-713e07fe.png)

### Utiliser les filtres pour trouver des photos

**Rechercher par mot**

Ce filtre fonctionne comme la recherche rapide. 

Vous pouvez saisir un ou plusieurs mots, décider si on veut afficher les résultats qui contiennent tous les mots ou seulement l’un d’entre eux, et choisir où rechercher le mot saisi (dans le titre de la photo, le nom de fichier, la description…).

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-ab12b387.png)

Un clic sur “Supprimer” désactive le filtre ; un clic sur “Vider” réinitialise le filtre.

**Rechercher par tag**

Le filtre “tag” permet d’afficher les photos associées à un ou plusieurs tags.

Vous pouvez choisir si la recherche doit renvoyer les photos associées à tous les tags choisis ou au moins l’un d’entre eux. 

En cliquant dans le champ de recherche, vous affichez une liste déroulante de tous les tags, dans laquelle vous pouvez rechercher le tag voulu en tapant les premières lettres.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-dd8959c8.png)

Un clic sur “Supprimer” désactive le filtre ; un clic sur “Vider” réinitialise le filtre.

**Rechercher par date d’ajout et date de création de la photo**

Le filtre “date d’ajout” permet de filtrer les photos en fonction de leur date d’import dans Piwigo, et le filtre “date de création” par date de création du fichier.

Plusieurs plages sont proposées : 7 derniers jours, 30 derniers jours, 3 derniers mois… On affiche également le nombre de photos correspondant à chaque plage de dates. Les filtres non pertinents sont grisés.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-0696b257.png)

Vous pouvez également cliquer sur “Dates personnalisées” pour filtrer sur une ou plusieurs plages de date de votre choix. Ces plages peuvent correspondre à une année, un mois, un jour… ou une combinaison de tout cela.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-6788fd4b.png)

Un clic sur “Supprimer” désactive le filtre ; un clic sur “Vider” réinitialise le filtre.

**Rechercher par album**

Le filtre par album permet de rechercher des photos au sein d’un ou plusieurs albums, en incluant ou pas les sous-albums.

![album-filtre.gif](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-d809899b.gif)

Un clic sur “Supprimer” désactive le filtre ; un clic sur “Vider” réinitialise le filtre.

**Rechercher par auteur**

Le filtre par auteur permet de rechercher une photo par auteur, en recherchant dans la liste déroulante des auteurs existants.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-d45f7996.png)

Un clic sur “Supprimer” désactive le filtre ; un clic sur “Vider” réinitialise le filtre.

**Rechercher par “ajouté par” (utilisateur ayant importé le fichier)**

Le filtre “Ajouté par” permet de lister les utilisateurs ayant importé des fichiers dans votre Piwigo et de filtrer les résultats de la recherche. On affiche le nombre de photos pour chaque utilisateur.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-c816fca4.png)

Un clic sur “Supprimer” désactive le filtre ; un clic sur “Vider” réinitialise le filtre.

**Rechercher par type de fichier (format)**

Le filtre “Type de fichier” permet de filtrer les résultats par format (ou extension de fichier).

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-a54b50ad.png)

**Rechercher par ratio**

Le filtre “Ratio” permet de filtrer les fichiers par ratio hauteur/largeur. Plusieurs ratios sont détectés par Piwigo : portrait, carré, paysage, panorama.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-55552d24.png)

**Rechercher par poids**

Le filtre “Poids” permet de filtrer les fichiers en fonction d’un poids minimum et / ou maximum. Cliquez sur l’échelle pour déplacer le curseur.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-cf9505a6.png)

**Rechercher par hauteur / largeur**

Les filtres par hauteur / largeur permettent de filtrer les fichiers en fonction d’une hauteur / largeur minimum et / ou maximum, en pixels. Cliquez sur l’échelle pour déplacer le curseur.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-1b577ce3.png)

### Combiner plusieurs filtres

La puissance de ce moteur de recherche vient de sa capacité à combiner plusieurs filtres et de voir les résultats mis à jour instantanément. 

À tout moment vous pouvez ajouter ou retirer un filtre, modifier les critères et affiner votre recherche, comme on le voit dans l’animation ci-dessous.

![filtres.gif](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-5949c04a.gif)

### Rechercher une photo dans un lot (album ou tag)

Sur la page d’un album ou d’un tag, il est possible d’afficher un bouton ou une icône permettant de lancer une recherche au sein de ce lot de photos.

Le bouton “Rechercher dans ce lot” :

![bouton-lot.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-6e730b84.png)

L’icône “Rechercher dans ce lot” dans la barre d’outils de la page Album.

![icone-lot.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-9d25876d.png)

Un clic sur ce bouton ou cette icône lance une recherche au sein de l’album / du tag.

Pour activer ou désactiver l’affichage de ce bouton et de cette icône sur votre galerie, rendez-vous dans l’administration, menu Configuration > Options, onglet “Afficher”.

![configuration-lot.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-379eeb52.png)

## Effectuer une recherche à l’aide des tags liés

Si vos photos sont correctement indexées à l’aide de tags, alors la recherche par tag peut s’avérer très puissante pour trouver une photo. Vous pouvez rechercher une photo par tag en utilisant le moteur de recherche, mais également en navigant par tags avec la fonctionnalité “Tags liés” ou un nuage de tags.

Pour en savoir plus, lisez cet article : [Utilisez les tags sur votre galerie](Les tags sur votre galerie.md)

Sommaire de l’article

---

← Précédent

[Les tags sur votre galerie](Les tags sur votre galerie.md)

Suivant →

[Gérer ses favoris](Gérer ses favoris.md)