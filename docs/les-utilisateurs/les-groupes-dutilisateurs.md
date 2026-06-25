# Les groupes d’utilisateurs

Lorsque vous avez beaucoup d’utilisateurs, gérer les paramètres et permissions de chacun devient vite un casse-tête.

C’est pour cela qu’existent les groupes d’utilisateurs.

Avec les groupes, vous définissez une bonne fois pour toutes les permissions et paramètres d’un certain profil d’utilisateurs. 

Ensuite, chaque fois que vous créez un nouvel utilisateur, il suffit de l’affecter au(x) groupe(s) adéquat(s).

Et lorsque vous créerez un nouvel album privé, vous n’aurez pas besoin de lister l’intégralité des utilisateurs qui y ont accès, mais simplement la liste des groupes.

## Créer un nouveau groupe d’utilisateurs

Pour accéder à la liste des groupes d’utilisateurs, rendez-vous dans l’administration, Menu Utilisateurs > Groupes.

L’écran affiche les groupes d’utilisateurs sous forme de tuiles, permet de les modifier, et de créer des groupes.

![fr-groupes-utilisateurs.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-c71feb78.png)

Pour créer un groupe, cliquez sur “Ajouter un groupe” sur l’écran de gestion des groupes.

Vous devez donner un nom à votre groupe : il est créé.

En passant la souris sur votre groupe, vous avez deux options disponibles :

- Gérer les membres
- Gérer les permissions

## Affecter des utilisateurs à un groupe

Pour ajouter des utilisateurs à un groupe depuis l’écran “Groupes”, passez la souris sur le groupe et cliquez sur “Gérer les membres”.

Une fenêtre s’ouvre, qui vous permet de choisir les utilisateurs à affecter à ce groupe. 

![fr-associer-groupe-user.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-459cda8e.png)

Pour associer un utilisateur, sélectionnez-le dans la liste et cliquez sur l’icône orange. 

Continuez ainsi autant que vous le souhaitez. La liste des utilisateurs associés au groupe s’affiche en bas de la fenêtre. En cas d’erreur, vous pouvez les retirer du groupe.

Vous pouvez également, si vous préférez, passer par la liste des utilisateurs pour les associer à un groupe. Vous pouvez ainsi associer manuellement chaque utilisateur à un ou plusieurs groupes, ou affecter des utilisateurs à des groupes en masse via le mode sélection.

Pour en savoir plus, [lisez l’article sur la gestion des utilisateurs](creer-et-gerer-les-utilisateurs).

## Gérer les permissions d’un groupe

Pour définir à quels albums un groupe a accès depuis l’écran “Groupes”, passez la souris sur le groupe et cliquez sur “Gérer les permissions”.

L’écran qui s’ouvre affiche à gauche, les albums privés auxquels ce groupe a accès, et à droite ceux auxquels il n’a pas accès. Par défaut, lorsque l’on crée un groupe, tous les albums sont interdits.

Pour autoriser des albums aux membres d’un groupe, il suffit de déplacer les albums interdits dans la colonne “Autorisés” grâce aux flèches.

![fr-permissions-groupes.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-f2f4c11f.png)

Pour définir les groupes autorisés pour un album en particulier, vous pouvez également passer par la liste des albums et l’éditeur d’album. L’onglet Permissions, lorsque l’on modifie un album, permet de définir les groupes autorisés à voir l’album.

[En savoir plus sur les permissions sur les albums](../organiser-les-albums/permissions-et-visibilite-des-albums)

![fr-permissions-groupes-album.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-b5b5ba10.png)

## Renommer un groupe

Pour renommer un groupe d’utilisateurs depuis la liste des groupes, cliquez sur l’icône en forme de crayon à côté de son nom, modifiez le nom, et cliquez sur l’icône orange pour valider votre modification.

![fr-renommer-groupe.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-83bc0d96.png)

## Dupliquer un groupe

Pour gagner du temps lors de la création d’un groupe d’utilisateurs, vous pouvez dupliquer un groupe existant. Pour cela, dans la liste des groupes, cliquez sur les 3 points en haut à droite d’un groupe et cliquez sur “Dupliquer”.

![fr-dupliquer-groupe.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-475c6896.png)

Une copie de ce groupe est alors créée : vous n’avez plus qu’à la renommer et à le modifier.

## Supprimer un groupe

Pour supprimer un groupe, dans la liste des groupes, cliquez sur les 3 points en haut à droite d’un groupe et cliquez sur “Supprimer”.

Pour supprimer plusieurs groupes, activez le mode sélection en cliquant sur le bouton “Mode sélection” en haut à droite de l’écran.

Vous pouvez alors cocher la liste des groupes à supprimer, et cliquer sur “Supprimer”.

![fr-supprimer-selection-groupes.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-3a4a47c9.png)

## Choisir un groupe d’utilisateur associé par défaut aux nouveaux utilisateurs

Vous pouvez définir un groupe qui sera automatiquement associé à tous les nouveaux utilisateurs créés.

Pour cela, dans la liste des groupes, cliquez sur les 3 points en haut à droite d’un groupe et cliquez sur “Associer automatiquement aux futurs utilisateurs”.

## Fusionner des groupes d’utilisateurs

Dans la liste des groupes, vous pouvez fusionner plusieurs groupes en un seul.

Pour cela, cliquez sur le bouton “Mode sélection” en haut à droite de l’écran.

Vous pouvez alors cocher la liste des groupes à fusionner.

![fr-fusionner-groupes.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-e7ec84a2.png)

Vous pouvez choisir quel groupe conserver dans la liste déroulante à droite de l’écran : tous les utilisateurs des autres groupes seront ajoutés au groupe cible, et les autres groupes seront supprimés.

Sommaire de l’article

---

← Précédent

[Envoyer des emails de notification aux utilisateurs](envoyer-des-emails-de-notification-aux-utilisateurs)

Suivant →

[Gérer les contributeurs (plugin Community)](gerer-les-contributeurs-plugin-community)
