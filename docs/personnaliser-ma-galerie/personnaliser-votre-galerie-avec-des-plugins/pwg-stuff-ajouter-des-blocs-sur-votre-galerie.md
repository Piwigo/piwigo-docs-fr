# PWG Stuffs : ajouter des blocs sur votre galerie

Le plugin **PWG Stuffs** offre diverses options pour ajouter des blocs à votre galerie. Ces blocs viennent enrichir les pages existantes. C’est donc un plugin très complet pour customiser votre galerie.

Il est principalement utilisé pour :

- Ajouter un nuage de mots-clés sur la page d’accueil
- Ajouter une zone de connexion sur la page d’accueil

---

## Ajouter une zone de connexion (login) sur la page d’accueil avec PWG Stuffs

Si votre galerie est à 100% privée, vous souhaitez sans doute que les utilisateurs arrivant sur la page d’accueil puissent se connecter directement.

C’est possible avec le plugin **PWG Stuffs**.

Dans la configuration du plugin PWG Stuffs, rendez-vous sur l’onglet “Ajoutez un nouveau bloc”. Choisissez dans la liste “Identification” puis cliquez sur “Ajouter un nouveau bloc”.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-7425d3bc.png)

Vous avez maintenant accès aux options de configuration de votre bloc. Ici, vous pouvez personnaliser le titre de votre bloc de connexion, déterminer si ce titre s’affiche ou pas sur la page d’accueil, et définir sur quelles pages ce bloc s’affiche.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-eb422c39.png)

Validez. Vous arrivez alors sur la page de gestion des blocs.

En face de “Bloc principal” cochez “Masquer sur la page d’accueil”.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-9aeb2885.png)

Et le tour est joué ! Votre page d’accueil affiche désormais un formulaire de connexion.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-91e219bd.png)

Retournons dans la gestion des blocs. Vous pouvez supprimer un bloc ajouté en cliquant sur la croix rouge, et modifier sa configuration en cliquant sur l’icône représentant des outils.

## Ajouter un nuage de tags sur la page d’accueil avec PWG Stuffs

Pour ajouter un nuage de tags (ou mots-clés) sur votre page d’accueil ou sur une autre page de votre galerie, cela passe aussi par le plugin PWG Stuff.

Dans la configuration du plugin PWG Stuffs, rendez-vous sur l’onglet “Ajoutez un nouveau bloc”. Choisissez dans la liste “Tags” puis cliquez sur “Ajouter un nouveau bloc”.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-e22f7dc8.png)

Vous avez maintenant accès aux options de configuration de votre bloc. Ici, vous pouvez personnaliser le titre de votre bloc nuage de tags, déterminer si ce titre s’affiche ou pas sur la page d’accueil, et définir sur quelles pages ce bloc s’affiche.

Vous pouvez également choisir entre 3 options d’affichage :

- Nuage de tags
- Regrouper par lettres
- Utiliser le mode Cumulus (le plugin Cumulus Tag Clouds doit être activé. Ce plugin n’est pas disponibles pour les clients d’une offre piwigo.com)

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-64c10f99.png)

Choisissez l’option “Nuage de tags” et validez.

Et le tour est joué ! Votre page d’accueil affiche désormais un nuage de tags.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-59e53a89.png)

Retournons dans la gestion des blocs, modifions le bloc créé en cliquant sur l’icône en forme d’outils et choisissons maintenant l’option “Regrouper par lettres”.

Les tags sont maintenant regroupés par lettre et par ordre alphabétique.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-d15d8db5.png)

## Autres fonctionnalités

Outre le formulaire de connexion et le nuage de tags, le plugin PWG Stuffs permet d’ajouter d’autres blocs sur votre galerie :

- Bloc personnel : ajouter un contenu texte ou html de votre choix, comme un message d’accueil.
- Citation au hasard : affiche une citation en français prise au hasard sur le site [http://citations.hasarddujour.com](http://citations.hasarddujour.com/)
- Derniers commentaires : affiche les derniers commentaires publiés sur la galerie
- Images au hasard : affiche X images au hasard dans la galerie ou dans l’album en cours
- Images du jour : affiche les images favorites de l’utilisateur au statut “webmaster”
- Images récentes : affiche les images récentes de la galerie ou de l’album en cours (s'il y en a)
- Mieux notées : affiche les X images les mieux notées de la galerie ou de l’album en cours
- Plus vues : affiche les X images les plus vues de la galerie ou de l’album en cours

## Droits d’accès sur les blocs

Il est possible de mettre en place une gestion des droits afin de personnaliser l’affichage des blocs en fonction des utilisateurs connectés.

Pour cela, dans la configuration de PWG Stuffs, rendez vous dans l’onglet Configuration.

Vous pouvez mettre en place une gestion des droits :

- Par [statut (ou type) d’utilisateur](../../les-utilisateurs/les-statuts-utilisateurs)
- Par [niveau de confidentialité](../../les-utilisateurs/les-niveaux-de-confidentialite)
- Par [groupe d’utilisateur](../../les-utilisateurs/les-groupes-dutilisateurs)

Imaginons que l’on ne veuille afficher un bloc qu’aux utilisateurs anonymes (non connectés à la galerie). Dans ce cas on va activer les droits par type d’utilisateur.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-d9d326e8.png)

Dans les paramètres d’un bloc, on va maintenant pouvoir cocher les utilisateurs autorisés à voir ce bloc. Dans notre cas, on va cocher uniquement “Invités”. Ainsi, seuls les utilisateurs non connectés verront ce bloc.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-5dc9df53.png)

## Modules en alternance

Il est possible d’aller assez loin avec ce plugin pour personnaliser le contenu de votre galerie en fonction des utilisateurs.

En effet, pour chaque module, vous pouvez choisir le type de page sur lequel il s'affichera, le type d'utilisateur qui le verra, la ligne où il sera affiché et sa largeur. En jouant sur ces éléments, il est possible de faire s'alterner deux modules sur un même emplacement.

Par exemple :

- Module 1 *EDITO*, (paramètres d'affichage : ligne A, 60%, affiché en page d'accueil uniquement, visible de tous), pourrait contenir une présentation de votre galerie.
- A ses côtés, Module 2 *NEWS*, (paramètres d'affichage : ligne A, 40%, affiché en page d'accueil uniquement, visible uniquement des visiteurs non connectés), pourrait donner envie aux nouveaux visiteurs de créer un compte si c’est possible.
- Module 3 *BIENVENUE*, (paramètres d'affichage : ligne A, 40%, affiché en page d'accueil uniquement, visible uniquement des visiteurs connectés), pourrait contenir leur nom d'utilisateur et un mot de bienvenue.

En arrivant, le visiteur voit en haut à gauche l'*EDITO*, à sa droite les *NEWS*. Quand il se connecte, *NEWS* est remplacé par *BIENVENUE*. Puis, quand il commence sa visite des albums, ces modules disparaissent pour laisser plus de place au contenu de votre galerie.
