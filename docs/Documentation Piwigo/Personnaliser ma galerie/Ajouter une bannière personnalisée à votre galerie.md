# Ajouter une bannière personnalisée à votre galerie

**De nombreux utilisateurs souhaitent ajouter une bannière personnalisée à leur galerie, sous la forme d’une image, d’un texte, ou d’un mélange des deux.**

Il existe deux principaux moyens pour le faire que nous listons dans cet article :

## Utiliser la zone “bannière des pages”

Par défaut, vous pouvez paramétrer une bannière sur votre galerie via le menu Configuration > Options, dans la zone Bannière des pages.

![fr-config-param-base.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-fb7e504f.png)

Dans cette zone, vous pouvez saisir du contenu texte brut mais également du code HTML. Vous pouvez éditer visuellement le code HTML si vous avez activé le plugin FCK Editor.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-e5fb14e8.png)

Vos pouvez facilement insérer une image, qui peut être présente sur votre Piwigo, sur votre serveur ou sur un autre site Internet. Il vous suffit de récupérer l’URL de cette image et d’ajouter le code HTML ci-dessous dans la zone “Bannière de page”, en remplacer l’URL par celle de votre image.

```html
<img src="https://piwigo.monsite.com/uploads/monimage.png">
```

Les bannières paramétrées dans la zone “Bannière de page” s’affichent de façon légèrement différente selon le thème de votre galerie. 

Voyons le résultat pour chaque thème.

### Afficher une bannière de page avec Modus

Si vous utilisez le thème Modus, la bannière s’affiche en haut de toutes les pages comme dans l’exemple ci-dessous. 

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-c86dde5c.png)

Si la bannière ne s’affiche pas, rendez-vous dans le menu Configuration > Thèmes, puis dans la configuration du thème Modus. Veillez à ce que l’option “Afficher la bannière des pages” soit cochée.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-15353bf8.png)

### Afficher une bannière de page avec Boostrap Darkroom

Par défaut, les bannières de page ne s’affichent pas avec le thème Boostrap Darkroom. Pour les afficher, vous devez vous rendre dans le menu Configuration > Thèmes, puis dans la configuration du thème Boostrap Darkroom.

La zone “En-tête de page” vous permet de choisir entre trois options d’affichage pour votre bannière.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-045c5ef9.png)

- Désactivé : pas de bannière
- Jumbotron :  Le contenu défini dans la zone “Bannière de page” apparaît en haut de toutes les pages.

![fr-banniere-bootstrap-jumbotron.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-d4b01e09.png)

- Image à la une : Cette option vous permet d’utiliser une image présente sur votre Piwigo en arrière plan comme bannière. Vous pouvez si vous le souhaitez afficher cette image en pleine hauteur. Le contenu défini dans la zone “Bannière de page” apparaît au centre en surimpression.
    
    ![fr-banniere-bootstrap-alaune.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-8973fa12.png)
    

### Afficher une bannière de page avec les autres thèmes

La plupart des thèmes supportent la bannière définie dans la zone “Bannière de page”.

Voici quelques exemples de rendu.

- Affichage de la bannière avec le thème Elegant
    
    ![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-f6426a4e.png)
    
- Affichage de la bannière avec le thème Simple White
    
    ![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-e40fe046.png)
    
- Affichage de la bannière avec le thème Clear
    
    ![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-97ca3d1c.png)
    

## Utiliser le plugin Header Manager

Si vous cherchez un moyen plus complet de créer votre bannière, vous pouvez installer le plugin Header Manager.

Dans la configuration du plugin, l’onglet “Ajouter une bannière” permet de télécharger une image qui servira de bannière sur votre site, ou de saisir l’ID de l’image si elle est présente sur votre galerie.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-f8c3d388.png)

Une fois la photo choisie, vous pouvez la retailler facilement pour qu’elle ait la hauteur et la largeur souhaitée.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-0d251b2c.png)

L’onglet Configuration permet de personnaliser votre bannière :

- Afficher seulement une image
- Afficher le titre de votre galerie au dessus de l’image (en transparence)
- Afficher l’image et le texte de votre choix

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-93b64fab.png)

Le plugin Header Manager permet d’avoir plusieurs images différentes pour votre bannière et d’en changer de façon aléatoire.

Vous pouvez même mettre en place des bannières spécifiques par album.

En effet, dans la page d’édition d’un album, le plugin ajoute un onglet “Bannière” permettant, pour un album donné, de choisir quelle bannière afficher parmi les bannières existantes.

---

← Précédent

[Personnaliser le CSS de votre galerie](Personnaliser le CSS de votre galerie.md)