# Gérer les langues disponibles sur votre galerie

L’interface de Piwigo est disponible dans plus de 70 langues.

Vous pouvez donc créer une photothèque multilingue avec Piwigo et proposer aux visiteurs de naviguer dans votre photothèque dans la langue de leur choix.

Dans cette article nous vous expliquons comment.

## Gérer les langues disponibles dans Piwigo

Pour modifier les langues disponibles dans votre Piwigo, rendez-vous dans l’administration, menu Configuration > Langues.

L’écran affiche les langues activées sur votre Piwigo, permet d’activer de nouvelles langues et de choisir la langue disponible par défaut.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-6163e782.png)

Si vous avez créé votre compte depuis le site [Piwigo Cloud](fr.piwigo.org), la configuration est la suivante :

- Les langues activées sont le français et l’anglais
- La langue par défaut est le français.

Pour désactiver l’anglais, il suffit de cliquer sur “Désactiver”.

Pour activer une autre langue, il suffit de choisir une langue dans la liste et de cliquer sur “Activer”.

Pour changer de langue par défaut, il suffit de cliquer sur “Par défaut” au niveau de la langue choisie.

Rendez vous ensuite sur votre galerie.

En cliquant sur “Personnaliser”, vous pouvez modifier la langue visible : ce choix ne s’appliquera qu’à vous seul (c’est une préférence enregistrée pour chaque utilisateur).

[En savoir plus sur les préférences](../les-utilisateurs/creer-et-gerer-les-utilisateurs)

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-1da9433e.png)

Le changement de langue est appliqué immédiatement : il s’applique sur tous les textes de votre galerie (menus, boutons d’actions…), mais attention : les contenus dynamiques issus de la base de données (noms des albums, des photos, descriptions…) ne sont pas traduits.

![Une galerie Piwigo en espagnol.](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-f241a9d8.png)

Une galerie Piwigo en espagnol.

## Changer de langue sur votre galerie

Si vous souhaitez rendre le changement de langue facile et rapide sur votre galerie, c’est possible avec le plugin **Language Switch**.

Une fois ce plugin activé, un drapeau apparaît sur votre galerie correspondant à la langue en cours.

Si vous cliquez sur ce drapeau, vous pouvez changer de langue en un clic en choisissant un autre drapeau.

![Changement de langue avec Language Switch et le thème Modus](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-e1cfbd10.png)

Changement de langue avec Language Switch et le thème Modus

![Changement de langue avec Language Switch et le thème Bootstrap Darkroom](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-285c352e.png)

Changement de langue avec Language Switch et le thème Bootstrap Darkroom

## Exif View : Traduire les noms des métadonnées Exif

Si vous souhaitez traduire les valeurs de métadonnées Exif dans la langue de la galerie, vous devez installer le plugin **Exif View**.

## Extended Descriptions : Traduire les noms et descriptions des photos et albums

Si vous souhaitez traduire les noms et descriptions des photos ou des albums, vous devez installer le plugin **Extended Descriptions**.

Ce plugin ajoute de nombreuses fonctionnalités à Piwigo, dont la possibilité d’afficher un titre et une description différente pour une photo ou un album, suivant la langue de l’utilisateur.

Le fonctionnement de ce plugin est documenté dans la page “Configuration” du plugin.

Pour chaque champ que l’on souhaite traduire, on doit, dans l’administration de Piwigo, encadré chaque valeur par deux balises permettant de spécifier la langue, comme dans l’exemple ci-dessous.

```html
[lang=en]Default description[/lang]
[lang=fr]Description en français[/lang]
[lang=de]Deutsche Beschreibung[/lang]
```

Il est possible de spécifier la langue par défaut en utilisant la balise default comme dans l’exemple ci-dessous.

La description (ou le nom) par défaut sera utilisée si la description dans la langue de l'utilisateur n'est pas définie.

Si \[lang=default\] n'existe pas, tout ce qui est situé en dehors des balises de langues sera considéré comme description par défaut.

```html
[lang=default]Default description[/lang]
[lang=fr]Description en français[/lang]

// OR

Default description
[lang=fr]Description en français[/lang]
```

La balise all permet de définir un texte qui sera toujours affiché, quelle que soit la langue de l’utilisateur.

Tout ce qui est situé entre les balises \[lang=all\] et \[/lang\] sera inclus, quelle que soit la langue de l'utilisateur.

Ceci est particulièrement pratique pour inclure du code HTML ou Javascript dans une description.

```html
[lang=all]<p>[/lang]
  [lang=default]Default description[/lang]
  [lang=fr]Description en français[/lang]
  [lang=de]Deutsche Beschreibung[/lang]
[lang=all]</p>[/lang]
```

Notez que le plugin Extended Descriptions vous donne accès à d’autres fonctionnalités pour personnaliser votre galerie.

[En savoir plus](personnaliser-votre-galerie-avec-des-plugins)
