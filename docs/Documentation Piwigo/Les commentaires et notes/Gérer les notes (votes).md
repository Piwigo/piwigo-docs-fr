# Gérer les notes (votes)

Avec Piwigo vous pouvez permettre aux visiteurs de votre galerie de noter les photos et autres fichiers en leur attribuant un nombre d’étoiles. Cela permet de mettre en place un système de votes pour organiser des concours photo par exemple.

## Activer ou désactiver les notes

Pour activer ou désactiver les notes, rendez-vous dans l’administration, menu Configuration > Options.

Dans la section Permissions, cochez ou décochez l’option **“Permettre les notations”.**

Si vous cochez cette case, une nouvelle option apparaît : “Notation par les invités”. Cochez cette option si vous acceptez que tous les visiteurs (même anonymes) puissent noter un fichier, et décochez-la si vous souhaitez réserver cette possibilité aux utilisateurs connectés sur votre galerie.

## Afficher les notes sur la galerie

Lorsque les notes sont activées sur votre galerie, deux nouveaux attributs apparaissent à côté d’une photo :

- Score : On affiche ici le score d’une photo (c’est à dire la note moyenne, pondérée par le nombre de notes) ainsi que le nombre de votes.
- Notez cette photo : permet aux visiteurs de noter la photo en cliquant sur le nombre d’étoiles désiré (1 étoile=0, 6 étoiles=5). Un utilisateur peut modifier sa note à tout moment.

![fr-note-photo.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-a464612d.png)

Lorsque les notes sont activées, un onglet “Mieux notées” est ajouté sur votre galerie.

Il permet de visualiser toutes les photos qui ont été notées, triées par score (du plus haut au plus faible).

![fr-mieux-notees.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-f5e1d59b.png)

<aside>
ℹ️ P**ourquoi utiliser un score pondéré plutôt qu’une note moyenne ?**

Si on utilise la note moyenne, une photo avec une seule note de 5/5 sera considérée comme mieux notée qu’une photo avec 500 notes et une moyenne de 4,8/5. Dans une logique de concours, ce n’est pas pertinent.

</aside>

## Gérer les notes dans l’administration

Pour gérer les notes dans l’administration, rendez-vous dans le menu Photos > Notation.

Cet écran contient deux onglets : Photos et Utilisateurs.

### Notes par photo

L’onglet Photos affiche la liste des photos qui ont été notées et pour chacune, toutes les informations liées aux notes (nombre de notes, score, note moyenne, somme des notes, utilisateurs ayant voté, dates de votes…).

Vous pouvez trier cette liste selon divers critères. Vous pouvez également filtrer les notes par type d’utilisateurs (utilisateurs enregistrés ou invités anonymes). Vous pouvez enfin filtrer la liste par album.

Vous pouvez supprimer toutes les notes d’une photo et remettre le score à zéro en cliquant sur la corbeille à droite de chaque ligne.

Pour modifier une photo, cliquez sur sa vignette : vous serez redirigé vers l’écran d’édition de la photo.

![fr-notes-admin.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-318cf195.png)

### Notes par utilisateur

L’onglet utilisateur affiche la liste des utilisateurs ayant noté des photos et pour chacun, toutes les informations liées aux notes (date de la dernière note, nombre de note, note moyenne, distribution des votes par note…).

Vous pouvez filtrer la liste pour n’affiche que les utilisateurs ayant laissé plus d’un certain nombre de notes.

Vous pouvez supprimer toutes les notes laissées par un utilisateur en cliquant sur la corbeille à droite de la ligne.

![fr-notes-utilisateurs.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-5673f22f.png)

## Remettre à zéro toutes les notes

Le plugin Delete Hit/Rate permet de remettre à zéro les notes :

- D’une photo en particulier, directement depuis l’éditeur de photo
- De toutes les photos d’un album, directement depuis l’éditeur d’album

Il permet également de remettre à zéro toutes les notes de la galerie depuis la page Outils > Maintenance.

Sommaire de l’article
