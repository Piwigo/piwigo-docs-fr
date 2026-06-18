# Les tags sur votre galerie

**Comment utiliser les tags sur votre galerie Piwigo? Quelles options d’affichage sont à votre disposition? C’est ici qu’on vous explique tout!**

Pour en savoir plus sur les tags, lisez également ces articles:

[Les tags : présentation](/gerer-les-tags/les-tags-presentation)

[Créer et gérer les tags](/gerer-les-tags/creer-et-gerer-les-tags)

[Tag Recognition : Taguez automatiquement vos photos par IA](/gerer-les-tags/tag-recognition-piwigo)

## Utiliser les tags sur votre galerie

Par défaut, les galeries Piwigo sont installées avec deux points de menus pour vos tags : Tags et Tags liés.

### **Tags liés**

![fr-tags-lies.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-92158f13.png)

Sur la page d’accueil, le menu affiche la liste des principaux tags de votre galerie. Un clic sur un tag permet de voir toutes les photos associées à ce tag.

![fr-liste-tag.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-7d9f4986.png)

Si à ce moment là on clique à nouveau sur le menu “Tags liés”, on n’affiche que les tags associés aux photos affichées: on peut alors cliquer sur un nouveau tag: les deux tags sont combinés pour affiner la recherche.

![fr-liste-tag-filtre-galerie2.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-c8281afc.png)

Pour retirer un tag des filtres de recherche, il suffit de cliquer sur la croix à côté de son libellé.

Lorsque que vous cliquez sur “Tags liés” depuis la page d’un album, on n’affiche que la liste des tags présents dans cet album.

**Ainsi, le menu Tags liés est un outil très pratique pour explorer votre photothèque et affiner une recherche au fil de l’eau.**

### **Tags (nuages de tags)**

Le sous-menu “Tags” sous “Explorer” affiche le nombre de tags présents sur votre galerie et permet d’ouvrir une page qui liste tous vos tags.

![fr-tags-menu.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-0c9ca9f3.png)

La page Tags ouverte affiche les tags sous forme de nuages de mots, la taille de chaque tag étant proportionnelle au nombre de photos sur lesquelles il est présent.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-36106dc5.png)

Un clic sur un tag affiche toutes les photos associées à ce tag.

### **Recherche par tag**

Lorsque vous tapez un mot dans le moteur de recherche de la galerie, si ce mot correspond à un tag, vous voyez s’afficher “1 tag trouvé”. Vous pouvez alors cliquer sur le tag pour afficher les photos associées.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-e87fedfe.png)

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-282d6cc1.png)

Si le plugin **RV Autocomplete** est activé sur votre galerie, la liste des tags s’affiche même en autocomplétion lorsque vous effectuez une recherche.

![fr-recherche-tag-autocomplete.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-fe598683.png)

Vous pouvez enfin combiner les tags avec d’autres critères de recherche en utilisant la recherche par filtre. Les filtres sont accessible dès lors que vous avez entamé une recherche, ou bien en cliquant depuis le menu Explorer > Recherche.

Cliquez sur le filtre “Tag” pour ajouter un ou plusieurs tags à votre recherche.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-79347649.png)

[En savoir plus sur le moteur de recherche](/naviguer-sur-votre-galerie-piwigo/rechercher-une-photo-sur-votre-galerie)

## Personnaliser la gestion des tags avec des plugins

### PWG Stuffs: **Afficher un nuage de tags sur votre page d’accueil**

Vous souhaitez afficher un nuage de tags sur la page d’accueil de votre galerie, comme sur [cet exemple](https://demo3.piwigo.com/)?

C’est possible en activant le plugin **PWG Stuffs**.

[En savoir plus](/personnaliser-ma-galerie/personnaliser-votre-galerie-avec-des-plugins/pwg-stuff-ajouter-des-blocs-sur-votre-galerie) 

### Menu Tags: Lister tous les tags dans le menu

Comme expliqué un peu plus haut sur cette page, par défaut sur votre galerie le menu Tags liés affiche dynamiquement les Tags liés au contenu que vous êtes en train de regarder.

Ainsi, si vous êtes sur la page d’un album dont les photos ne sont associées à aucun Tag, le menu Tags liés n’apparaît pas.

Si vous souhaitez afficher un menu Tags listant tous les tags disponibles sur votre galerie lorsque vous êtes sur une page avec aucun tags liés, vous pouvez activer le plugin **Menu Tags**.

En conséquence, au lieu d’afficher un menu “Tags liés” sur la page d’accueil, le menu affichera un menu “Tags” qui affiche tous les tags de votre galerie, avec une taille proportionnelle à leur taux d’utilisation.

### Birthdate: Afficher l’âge d’un élément d’une photo

Le plugin Birthdate permet d’associer une date de naissance à un tag, pour afficher l’âge d’un élément d’une photo au moment de la prise de vue.

Cette fonctionnalité est souvent utilisé pour des photos de personnes, notamment d’enfants. Imaginons que j’ai une série de photo d’un enfant appelé Jean. J’associe chaque photo à un tag “Jean”. Avec le plugin Birthdate, j’associe le tag “Jean” à sa date de naissance.

Ainsi, sur la galerie, à côté de chaque photo de Jean, on affichera l’âge qu’il avait le jour de la prise de vue (à l’heure près!).

Cette fonctionnalité peut également être utile pour d’autres cas de figures:

- Suivre la croissance d’une plante à partir de sa date de plantation
- Suivre l’évolution d’un bâtiment à partir de sa date de construction
- …

### Tag Groups: Créer des groupes de tags

Par défaut, les tags sont tous au même niveau, contrairement aux albums: ils ne fonctionnent pas en arborescence.

Toutefois, il est possible de créer une arborescence de tags à un niveau grâce au plugin **Tag Groups**.

<aside>
⚠️ Si vous êtes client d’une offre piwigo.com, ce plugin n’est accessible qu’à partir de l’offre Entreprise.

</aside>

?

Au lieu d’être affichés sous la forme d’un nuage de tags sur la page Tags de votre galerie, ils pourront être regroupés par groupe.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-87aed4ac.png)

Ce plugin permet également la mise en place de filtres par groupes de tags sur votre galerie.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-8b84279a.png)

**Comment créer un groupe de tags?**

Pour créer un groupe de tag “couleur” il suffit de créer un tag “couleur:bleu”, un tag “couleur:rouge”, etc.

De la même manière vous pouvez créer un groupe “ville” en créant un tag “ville:paris”, “ville:londres”, etc.

**Comment afficher les tags par groupe?**

L’affichage des tags par groupe remplace l’affichage d’un nuage de tags sur la page Tags de votre galerie.

Pour afficher les tags par groupe, sur la page Tags, cliquez sur le bouton en haut à droite “Montrer les tags par groupe”.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-6eb44453.png)

Si vous souhaitez que par défaut la page Tag affiche les tags par groupes, c’est possible.

Si vous êtes client d’une offre d’abonnement sur piwigo.com, vous devez contacter le support pour activer cette option.

Si vous hébergez vous-même votre Piwigo, vous pouvez l’activer en modifiant la configuration locale avec LocalFiles Editor, à l’aide du paramètre de configuration ci-dessous.

```php
$conf['tags_default_display_mode'] = 'groups';
```

**Comment activer les filtres multicritères par groupe de tag?**

Si vous êtes client d’une offre d’abonnement sur piwigo.com, vous devez contacter le support pour activer cette option.

Si vous hébergez vous-même votre Piwigo, vous pouvez l’activer en modifiant la configuration locale avec LocalFiles Editor, à l’aide des paramètres de configuration ci-dessous.

```php
$conf['tag_groups_index_filters'] = true;
$conf['tag_groups_dynamic_filters'] = true;
```

Pour en savoir plus sur les groupes de tags vous pouvez:

- [Lire cet article de blog](https://fr.piwigo.com/blog/2020/06/05/moteur-de-recherche-multicriteres-phototheque-piwigo/)
- [Voir cette démo d’exemple](https://hannah.piwigo.com/)

### Colorer les tags avec Colored Tags

Il est possible d’affecter une couleur aux tags en activant le plugin Colored Tags.

Une fois ce plugin activé, dans la configuration du plugin vous pouvez définir une liste de couleurs, via un code hexadécimal ou en choisissant dans le cercle chromatique.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-82a21470.png)

Pour modifier la couleur associée à un tag, vous devez vous rendre dans l’administration, Menu Photos> Tags, et passer en mode sélection. Vous pourrez alors affecter une couleur à un ou plusieurs tags.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-36c753c5.png)

Les couleurs des tags sont visibles sur votre galerie, dans le menu Tags Liés et dans la page Tags.

![fr-colored-tags-liés.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-5fdb42a4.png)

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-b2ee89ad.png)

### Tag To Keyword: Renommer “tag” en “mot-clé”

Certains utilisateurs n’apprécient pas le terme “tag” et lui préfèrent “mot-clé”.

C’est pourquoi il existe un plugin “Tag To Keyword” qui, une fois activé, remplace le mot “tag” par “mot-clé”.

Sommaire de l’article

---

← Précédent

[La page Photo sur votre galerie](/naviguer-sur-votre-galerie-piwigo/la-page-photo-sur-votre-galerie)

Suivant →

[Rechercher une photo sur votre galerie](/naviguer-sur-votre-galerie-piwigo/rechercher-une-photo-sur-votre-galerie)