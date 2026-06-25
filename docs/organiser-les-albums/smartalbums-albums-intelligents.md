# SmartAlbums (albums intelligents)

Il est possible de créer des albums “intelligents”, alimentés automatiquement par des photos qui répondent à certains critères.

Pour cela, vous devez installer le plugin **SmartAlbums**.

!!! info
    Si vous êtes client d’une offre piwigo.com, ce plugin n’est accessible qu’à partir de l’offre Entreprise.


Une fois le plugin activé, rendez vous dans sa page de configuration.

## Créer un Smart Album

Le premier onglet liste les Smart Albums et permet d’en créer un nouveau. Un SmartAlbum peut être ajouté à la racine de votre galerie ou à l’intérieur d’un album parent.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-25dfbcbf.png)

Une fois le SmartAlbum créé, vous pouvez déterminer les critères qui définissent son contenu.

Pour cela, choisissez un filtre parmi les critères proposés : tags, date, album, nom, dimensions, auteur, nombre de vues, etc.

Par exemple, nous allons créer un album alimenté par toutes les photos ayant le tag associé “chien”. Un clic sur le bouton “Compter” permet de connaître le nombre de photos concernées.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-5a74e365.png)

Vous pouvez combiner plusieurs filtres et choisir :

- Si les photos doivent respecter tous les filtres pour rejoindre le SmartAlbum,
- Ou si elle doivent respecter au moins un filtre.

Une fois vos filtres définis, cliquez sur “Save” pour enregistrer votre SmartAlbum.

## Gérer les Smart Albums

Les albums créés ainsi sont visibles dans la liste des albums comme n’importe quel autre album. Vous pouvez modifier les filtres en modifiant l’album et en vous rendant dans l’onglet “SmartAlbum”.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-b9447f46.png)

Retournons dans la configuration du plugin SmartAlbums.

Les SmartAlbums créés sont visibles dans la liste.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-00a9b910.png)

Vous pouvez à tout moment regénérer les photos des SmartAlbums, soit de manière globale, soit album par album. Regénérer les photos permet de mettre à jour le contenu d’un SmartAlbum.

## Configuration des Smart Albums

L’onglet Configuration permet de définir certains paramètres.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-ae72fafe.png)

- **Fréquence de mise à jour des SmartAlbums** : les SmartAlbums ne sont pas mis à jour en temps réel. Si vous venez d’importer de nouvelles photos, elles ne viendront pas immédiatement alimenter un SmartAlbum, sauf si vous “forcez” la mise à jour en utilisant la fonctionnalité de regénération des SmartAlbums. Par défaut, les SmartAlbums sont mis à jour tous les 3 jours mais vous pouvez personnaliser ce paramètre.
- **Mettre à jour les albums après la mise en ligne d’un fichier :** si vous souhaitez que les SmartAlbums soient regénérés automatiquement après chaque nouvel import, cochez cette option, mais attention : cela peut ralentir votre galerie, notamment si vous avez beaucoup de contenu.
- **Exclure les SmartAlbums de la gestion des droits d’accès :** dans ce cas, les SmartAlbums sont considérés comme privés pour tout le monde, et un utilisateur ne peut voir leur contenu que si il est disponible dans un autre album auquel il a accès.
