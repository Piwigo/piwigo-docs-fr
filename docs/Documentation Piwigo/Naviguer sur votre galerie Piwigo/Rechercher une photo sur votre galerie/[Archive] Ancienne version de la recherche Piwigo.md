# \[Archive\] Ancienne version de la recherche Piwigo

Cette page présente les fonctionnalités de recherche sur une galerie Piwigo jusqu’à la version 13. 

Si vous cherchez la dernière version de la documentation sur la recherche (depuis Piwigo 14), lisez plutôt l’article suivant :

[Rechercher une photo sur votre galerie](../Rechercher une photo sur votre galerie.md)

## La recherche rapide

### **Utiliser le champ de recherche rapide**

Si cette fonctionnalité est active sur votre galerie (c’est le cas par défaut sur la plupart des thèmes), vous disposez d’un champ de recherche.

![fr-recherche-modus.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-c682d0d2.png)

Sur certains thèmes, la recherche sera accessible en cliquant sur un point de menu (exemple ci-dessous avec la configuration par défaut du thème Bootstrap Darkroom).

![fr-recherche-boostrap.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-1df6df04.png)

Saisissez un mot dans la recherche rapide et appuyez sur la touche Entrée : les résultats affichent les photos qui correspondent à votre recherche.

![fr-resultat-recherche.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-d5ab3f0f.png)

Pour filtrer les résultats, Piwigo recherche le mot que vous avez saisi :

- dans le nom (titre) de la photo dans Piwigo
- dans le nom du fichier
- dans la description du fichier
- dans les tags associés à vos photos
- dans l’identifiant des photos

Par ailleurs, si le mot-clé saisi correspond à un tag ou au nom d’un album de votre galerie, ils apparaîtront également dans les résultats.

![fr-recherche-tag-album.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-df1bf3f0.png)

### U**tiliser la recherche rapide comme un pro**

Tout comme dans les moteurs de recherche sur Internet, vous pouvez utiliser des opérateurs pour affiner votre recherche.

| --- | --- |

| tag:tags: | Recherche seulement dans les tags, sans tenir compte des titres ou des descriptions de photos.tag:alain, tag:(alain OR david) |
| photo:photos: | Recherche seulement les photos ayant les mots clés dans leur titre ou leur description.photo:Jacques |
| file: | Recherche dans les noms de fichier.file:DSC_ |
| author: | Recherche par auteur.author:Alain |
| created:taken: shot: | Recherche les photos par date de prise.taken:2003 photos prises en 2003taken:20035,taken:2003-5,taken:2003-05 photos prises à partir de mai 2003taken:2003..2008 photos de 2003 à 2008taken:>2008,taken:2008*,taken:2008.. photos prises à partir du 1er janvier 2008 |
| posted: | Recherche les photos par date d'ajout. |
| width:height: | Recherche les photos ayant une certaine largeur ou hauteur en pixels. |
| size: | Recherche les photos par taille en pixels.size:5m retourne les photos de 5 millions de pixelssize:>12m retourne les photos de 12 millions de pixels ou plus |
| ratio: | Recherche les photos ayant un certain rapport largeur/hauteur.ratio:3/4 OR ratio:4/3 trouve les photos d'un compact en mode portrait ou paysage ratio:>16/9 trouve les panoramas |
| hits: |  |
| score:rating: | Astuce : score:* retournera toutes les photos ayant au moins une note. score: retournera les photos sans note. |
| filesize: | Recherche les photos par taille de fichier.filesize:1m..10m retourne les fichiers dont la taille est comprise entre 1 et 10 Mo. |
| id: | Recherche les photos en utilisant leur identifiant numérique Piwigoid:123..126 trouve les photos 123 à 126 (le nombre de photos peut varier de 0 à 4 car certaines ont pu être effacées). |

### RV autocomplete : Activer l’**autocomplétion sur le moteur de recherche**

Vous souhaitez gagner encore plus de temps lorsque vous rechercher un tag ou un album sur votre galerie ?

On vous conseille d’utiliser le plugin **RV autocomplete**.

Une fois ce plugin activé, quand vous saisirez une recherche, les albums et tags correspondant à votre recherche seront automatiquement proposés.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-91670494.png)

## L**a recherche avancée**

Sur votre galerie Piwigo, vous disposez également d’un formulaire de recherche avancée.

Avec le thème par défaut Modus, ce formulaire est accessible en cliquant sur Explorer > Recherche.

Avec le thème Boostrap Darkroom, ce formulaire est accessible en cliquant sur Découvrir > Recherche.

<aside>
ℹ️ Selon le paramétrage de votre galerie, il peut être accessible via un autre moyen.

</aside>

![fr-piwigo-recherche-avancee.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-0c5c4d16.png)

Avec ce formulaire, vous pouvez saisir un mot dans la première barre de recherche, et choisir les options de votre recherche :

- rechercher tous les mots ou seulement un seul des mots saisis
- appliquer la recherche sur le titre de la photo, la description…
- filtrer par date de création ou date d’ajout
- …

<aside>
ℹ️ Attention : les opérateurs de recherche avancés ne fonctionnent pas sur ce formulaire.

</aside>

## Effectuer une recherche à l’aide des tags

Si vos photos sont correctement indexées à l’aide de tags, alors la recherche par tag peut s’avérer très puissante pour trouver une photo.

Pour en savoir plus, lisez cet article : [Utilisez les tags sur votre galerie](../Les tags sur votre galerie.md)

Sommaire de l’article
