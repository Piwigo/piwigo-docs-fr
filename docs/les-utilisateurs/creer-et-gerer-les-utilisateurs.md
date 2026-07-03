# Créer et gérer les utilisateurs

## Voir et gérer les utilisateurs

Pour créer, modifier, supprimer des utilisateurs dans l’administration de Piwigo, vous devez cliquer dans le menu de gauche Utilisateurs > Gérer.

![liste-users-fr.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-dc08d31f.png)

Le premier onglet liste les utilisateurs créés sur votre Piwigo et permet d’effectuer un certain nombre d’actions.

- Créer un utilisateur
- Rechercher un utilisateur
- Modifier un utilisateur
- Modifier plusieurs utilisateurs en masse
- Modifier l’utilisateur invité (anonyme)

!!! info
    Depuis la version 15 de Piwigo, vous pouvez trier la liste des utilisateurs par nom ou par date de création en cliquant sur l’intitulé de la colonne. 


## Comment créer un nouvel utilisateur dans l’administration?

Pour créer un nouvel utilisateur dans l’administration de Piwigo, dans la liste des utilisateurs, cliquez sur “Ajouter un utilisateur” : une fenêtre s’ouvre.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-9e061dec.png)

Cette fenêtre permet de définir les informations suivantes pour votre utilisateur :

- nom d’utilisateur (identifiant qui permet de se connecter à Piwigo)
- email
- statut ([en savoir plus sur les statuts](les-statuts-utilisateurs))
- niveau de confidentialité ([en savoir plus sur les niveaux de confidentialité](les-niveaux-de-confidentialite))
- groupe(s) ([en savoir plus sur les groupes d’utilisateurs](les-groupes-dutilisateurs))
- autorisation ou pas de télécharger des fichiers sur la galerie

Par défaut, les nouveaux utilisateurs héritent des mêmes préférences que l’utilisateur “Invité” (dont on parle [un peu plus tard](creer-et-gerer-les-utilisateurs) dans cette page).

Une fois que vous avez créé un nouvel utilisateur, vous pouvez le modifier pour personnaliser son profil.

Depuis Piwigo 15, lorsque vous créez un utilisateur depuis l’administration, un lien lui est automatiquement envoyé par email pour qu’il choisisse son mot de passe.

## Comment modifier un utilisateur ?

Pour modifier un utilisateur depuis la liste des utilisateurs, il suffit de cliquer sur l’icône en forme de crayon, à gauche du nom dans la liste des utilisateurs. L’utilisateur sélectionné est mis en évidence grâce à la couleur orange.

![fr-editer-utilisateur.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-1ca839b9.png)

L’écran de modification d’un utilisateur s’ouvre alors.

![modif-user -.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-2bf503b5.png)

Cet écran permet de modifier de nombreux paramètres utilisateurs et de visualiser certaines informations.

Ces infos sont regroupées en 3 parties :

- informations principales à gauche
- onglet propriétés à droite
- onglet préférences à droite

Certains plugins ajoutent de nouveaux onglets à cet écran.

### Modifier l’identifiant et le mot de passe d’un utilisateur

La section de gauche de l’écran permet de modifier l’identifiant et le mot de passe d’un utilisateur.

**Nom d’utilisateur / identifiant**

Le nom d’utilisateur apparaît en haut à gauche de la fenêtre.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-dffce812.png)

Cliquez sur l’icône en forme de crayon pour le modifier ; le nom d’utilisateur devient alors éditable dans une fenêtre.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-b9a92ea4.png)

!!! Warning "Attention"
    Le nom d’utilisateur est également un identifiant qui permet aux utilisateurs de se connecter à Piwigo.  Ne le modifiez pas sans prévenir les utilisateurs.

**Mot de passe**

Cliquez sur “mot de passe” pour ouvrir l’écran ci-dessous.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-9d940eb7.png)

Cette fenêtre permet :

- de copier le lien de réinitialisation du mot de passe pour le transmettre à un utilisateur (si l’envoi par mail du lien ne fonctionne pas)
- de renvoyer le lien d’initialisation du mot de passe par email
- de modifier le mot de passe d’un utilisateur

### Modifier les permissions sur les albums d’un utilisateur

Dans Piwigo, on peut définir si un album est privé ou public. Si il est privé, alors seuls les utilisateurs autorisés pourront le voir dans la galerie.

Pour en savoir plus sur les permissions sur les albums, [lisez cet article](../organiser-les-albums/permissions-et-visibilite-des-albums).

Depuis la fenêtre de modification d’un utilisateur, cliquez sur “Permissions” pour visualiser et modifier les albums qu’il a le droit de consulter.

![modif-user - permissions.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-3ce45b6e.png)

L’écran s’ouvre alors sur une fenêtre qui liste les albums privés :

- sur la gauche, ceux que l’utilisateur a le droit de consulter
- sur la droite, ceux qu’il n’a pas le droit de consulter.

Pour modifier les albums auquel l’utilisateur a accès, il suffit de les déplacer d’une colonne à l’autre en cliquant sur les flèches.

![fr-permissions-utilisateurs-2.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-9d65449e.png)

!!! info
    Si l’utilisateur est membre d’un groupe, les permissions individuelles supplantent celle du groupe. [En savoir plus sur les groupes d’utilisateurs](les-groupes-dutilisateurs)


### Supprimer un utilisateur

L’écran de modification d’un utilisateur permet de le supprimer en cliquant sur l’icône “corbeille”.

![suppr.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-70acd342.png)

Un écran intermédiaire vous permet de valider votre choix.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-15e571e8.png)

### Modifier l’utilisateur principal de votre Piwigo

L’utilisateur “principal” de Piwigo est par défaut le premier utilisateur :

- celui qui a installé Piwigo, si vous hébergez Piwigo vous-même ;
- celui qui a créé le compte, si vous utilisez un compte sur Piwigo Cloud.

Cet utilisateur a le statut “webmestre”.

Il est représenté par une couronne dans la liste des utilisateurs.

![principal.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-d4e8447e.png)

À partir du moment où un utilisateur a le statut “webmestre”, il peut être choisi comme utilisateur principal, en cliquant sur l’icône “couronne” dans la fenêtre de modification d’utilisateur. Si vous validez, il remplacera l’utilisateur principal actuel (il ne peut y avoir qu’un seul utilisateur principal dans un compte Piwigo).

![principal2.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-573ef303.png)

### Modifier les propriétés d’un utilisateur

L’onglet “propriétés” permet de modifier les propriétés définies lors de la création de l’utilisateur.

![modif-user - prop.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-918efe3f.png)

**Adresse email** 

Vous pouvez modifier l’adresse email d’un utilisateur depuis cette fenêtre. N’oublier pas de cliquer sur “Mettre à jour” pour enregistrer les modifications.

**Statut**

Vous pouvez modifier le statut d’un utilisateur, notamment après sa création, pour le changer en Administrateur, Générique, Webmestre…

Pour en savoir plus sur le rôle et les droits associés à chaque Statut, [lisez cet article](les-statuts-utilisateurs).

Il existe certaines limitations :

- L’administrateur connecté ne peut pas modifier son propre statut
- Si vous voulez changer le statut du premier utilisateur de Piwigo (utilisateur principal), vous devez d’abord définir un nouvel utilisateur principal (voir plus loin).

**Niveau de confidentialité**

Par défaut, les niveaux de confidentialités ne sont pas utilisés dans Piwigo. Vous pouvez donc ignorer ce paramètre, sauf si vous avez un besoin très précis.

[En savoir plus sur les niveaux de confidentialité](les-niveaux-de-confidentialite)

**Groupe**

Vous pouvez associer un utilisateur à un ou plusieurs groupes existant depuis la fenêtre de modification d’un utilisateur.

[En savoir plus sur les groupes d’utilisateurs](les-groupes-dutilisateurs)

**Autoriser le téléchargement**

Cochez cette case si vous autorisez un utilisateur à télécharger l’original d’une photo sur votre galerie.

Si vous décochez cette option, l’utilisateur pourra visualiser les photos sur la galerie, mais l’icône de téléchargement sera masquée.

### Modifier les préférences d’un utilisateur

Les préférences modifient l’apparence de la galerie Piwigo en fonction des utilisateurs.

Depuis l’écran de modification d’un utilisateur dans l’administration, l’onglet “préférences” permet de les modifier.

![modif-user-pref.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-ebe7e1fb.png)

Chaque utilisateur peut également les modifier lui-même lorsqu’il est connecté à la galerie, en cliquant sur le menu “Personnaliser”.

!!! info
    La modification des préférences par les utilisateurs via la galerie peut être désactivée dans les Options de Piwigo (en décochant l’option “Permettre la personnalisation de l'affichage”). Dans ce cas, le menu “Personnaliser” ne sert qu’à modifier son adresse mail et / ou son mot de passe.


Vous pouvez enfin modifier en masse les préférences d’une liste d’utilisateurs en utilisant le mode Sélection (voir chapitre [Modifier des utilisateurs en masse](creer-et-gerer-les-utilisateurs)).

Pour modifier les préférences appliquées par défaut aux nouveaux utilisateurs, il faut modifier le profil “invité ([voir plus loin](creer-et-gerer-les-utilisateurs)).

Voici quelques précisions sur les préférences.

**Photos par page**

Il s’agit du nombre de photos affichées sur une page dans la galerie (sur la page d’un album par exemple). Par défaut, ce chiffre est fixé à 15, ce qui signifie qu’au delà de 15 photos sur une page, des liens de pagination seront affichés. Vous pouvez augmenter ou diminuer ce nombre.

**Thème**

Dans la majeure partie des cas, les galeries Piwigo n’utilisent qu’un seul thème. Ce paramètre n’a donc pas à être modifié. Il n’est utile que si vous avez installé plusieurs thèmes sur votre galerie, et que vous souhaitez afficher des thèmes différents en fonction des utilisateurs.

[En savoir plus sur les thèmes](../les-themes)

**Langue**

Sur chaque galerie, une langue par défaut est définie, mais on peut en installer plusieurs.

Cet paramètre permet ainsi de choisir, pour un utilisateur donné, quelle langue sera utilisée pour l’interface de Piwigo, parmi les langues activées sur la galerie.

[En savoir plus sur les langues](../personnaliser-ma-galerie/gerer-les-langues-disponibles-sur-votre-galerie)

**Période récente**

Il s’agit de la période d’affichage des photos lorsque l’utilisateur clique sur le menu “Photos récentes” de votre galerie. Cette période, fixée par défaut à 7 jours, peut être modifiée.

**Développer tous les albums**

Par défaut, cette option est désactivée, ce qui fait que le menu Albums sur la galerie ne liste que les albums à la racine (pas les sous-albums).

![fr-menu-albums-pas-developpe.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-b46ba04f.png)

Si vous cochez cette option, le menu affichera l’arborescence complète.

![fr-menu-albums-developpe.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-ab23472c.png)

**Montrer le nombre de commentaires**

Cette option permet d’afficher le nombre de commentaires de chaque photo sous la miniature dans les pages de listes sur la galerie web.

!!! info
     Cette option est compatible avec certains thèmes (Elegant, Boostrap Darkroom) mais pas avec le thème Modus.


![fr-commentaires-galerie.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-11e06380.png)

**Montrer le nombre de visualisations**

Cette option permet d’afficher le nombre de visites de chaque photo sous la miniature dans les pages de listes sur la galerie web.

!!! info
    Cette option est compatible avec certains thèmes (Elegant, Boostrap Darkroom) mais pas avec le thème Modus.


![fr-nombre-visites-galerie.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-6a52c837.png)

## Voir l’historique d’un utilisateur

L’écran de modification d’un utilisateur affiche la date de création et la dernière date de connexion d’un utilisateur. Il permet également d’accéder à l’historique des visites de cet utilisateur en cliquant sur le bouton “Historique des visites”.

![modif-user-history.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-3483d40d.png)

### Historique des visites

Le bouton “Historique des visites” permet d’ouvrir l’historique des visites de cet utilisateur. Cela permet de voir quels albums ont été consultés, quelles photos ont été vues et téléchargées.

[En savoir plus sur l’historique des visites](../administrer-piwigo/consultez-les-statistiques-de-votre-piwigo)

![fr-historique-visite-utilisateur.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-2b05d3ae.png)

### Activité des administrateurs

Pour visualiser l’historique détaillé de toutes les actions d’un utilisateur dans l’administration, vous devez vous rendre dans l’onglet Activité de la page Utilisateurs.

[En savoir plus sur l’historique des activités](../administrer-piwigo/consultez-les-statistiques-de-votre-piwigo)

!!! info
    Si vous êtes client d’une offre Piwigo Cloud, cette fonctionnalité n’est accessible qu’à partir de l’offre Équipe.


![fr-activités.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-22d1787b.png)

## Rechercher un utilisateur

La liste des utilisateurs permet d’effectuer une recherche pour trouver facilement un utilisateur si vous en avez beaucoup.

Un moteur de recherche permet de retrouver un utilisateur par son identifiant. Tapez quelques lettres dans le moteur de recherche : la liste se met à jour automatiquement.

![fr-recherche-user.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-8a4636ae.png)

Vous pouvez également cliquez sur le bouton Filtres pour afficher des critères de recherche.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-56a6d54f.png)

Vous pouvez filtrer la liste des utilisateurs par :

- Statut (Webmaster, Administrateur, Visiteur…)
- Niveau de confidentialité
- Groupe
- Date d’enregistrement (création de l’utilisateur)

## Modifier des utilisateurs en masse

Vous avez besoin d’appliquer des modifications à une sélection d’utilisateurs ?

Pour cela, il suffit de cliquer sur le bouton “Mode sélection” depuis la liste des utilisateurs, à droite de l’écran.

![fr-selection-utilisateurs1.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-3efe3591.png)

Une fois le mode sélection activé, vous pouvez cocher les utilisateurs à modifier : ils apparaissent les uns après les autres dans une liste à droite de l’écran. En cas d’erreur, vous pouvez retirer un utilisateur de la liste sélectionnée en cliquant sur la croix à côté de son nom.

En haut de l’écran, les boutons Toute la page / Tout le lot / Rien / Inverser vous permettent d’aller plus vite dans la sélection si vous avez de nombreux utilisateurs à gérer.

- Cliquer sur “Toute la page” ajoute tous les utilisateurs visibles à l’écran à votre liste de sélection
- Cliquer sur “Tout le lot” ajoute tous les utilisateurs de votre Piwigo à votre liste de sélection
- Cliquer sur “Rien” vide votre liste de sélection
- Cliquer sur “Inverser” ajoute à la sélection tous les utilisateurs, sauf ceux actuellement sélectionnés.

![fr-selection-utilisateurs.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-afa61c3d.png)

Une fois votre sélection d’utilisateur terminée, cliquez sur l’action de votre choix :

- Supprimer les utilisateurs
- Associer à un groupe / dissocier d’un groupe
- Autoriser le téléchargement
- Modifier le niveau de confidentialité
- Modifier les préférences (nombre de miniatures par page, thème, langue, période récente, développer tous les albums, montrer le nombre de visualisations)

## Modifier les paramètres “invité”

La page de gestion des utilisateurs permet de modifier l’utilisateur “invité”.

L’utilisateur “invité” correspond au profil des visiteurs anonymes de la galerie, qui la consultent sans être connectés sur Piwigo. Mais ce n’est pas tout : les paramètres de cet utilisateur sont également les paramètres par défaut de tous les nouveaux utilisateurs.

Pour modifier ce profil invité, cliquez sur “Editer l’utilisateur invité”.

![fr-user-invite.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-8b8fb7ff.png)

Cela ouvre une fenêtre semblable à la fenêtre de modification d’un utilisateur.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-5e8b1b22.png)

## Autoriser ou interdire aux visiteurs de la galerie de créer un compte

En fonction de l’usage de votre galerie Piwigo, vous pouvez accepter ou refuser que les visiteurs créent un compte eux-même.

Par exemple :

- Les entreprises et organisations qui gèrent une photothèque privée avec Piwigo ne veulent pas qu’une personne externe à l’entreprise puisse créer un compte : les utilisateurs sont toujours créés par un administrateur.
- Certaines organisations (par exemple, des offices de tourisme) permettent aux personnes habilitées (journalistes, partenaires, écoles…) de créer un compte sur leur photothèque pour accéder à des visuels libres de droit, mais elles souhaitent que la création de ces comptes soit validée par un administrateur.
- D’autres gestionnaires de photothèque mettent une partie de leur contenus à disposition du grand public, mais souhaitent que les utilisateurs créent un compte avant d’accéder à la galerie, pour mieux connaître l’usage de leurs contenus et pour collecter les coordonnées des personnes intéressées.

Ainsi, Piwigo vous permet de définir les règles de votre photothèque en termes de création de compte par les visiteurs.

Pour cela, rendez-vous dans l’administration, Menu Configuration > Options, section Permissions.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-389f4f1b.png)

Une option est proposée : **Permettre l’enregistrement des utilisateurs.**

Cocher cette option affichera sur votre galerie un lien “S’enregistrer”, permettant à un visiteur de remplir un formulaire pour créer un compte sur votre galerie. 

L’option associée, “Notifier les administrateurs lors de l’inscription d’un utilisateur”, fait qu’à chaque fois qu’une personne créera un compte sur votre galerie, les administrateurs recevront un email. Ils pourront ainsi vérifier que la personne est bien habilitée à s’enregistrer, et pourront lui accorder les permissions souhaitées, l’ajouter à un groupe, etc.

Vous pouvez choisir de notifier tous les administrateurs lors de la création d’un nouveau compte, ou seulement les membres d’un groupe.

## User Mass Register : créer des utilisateurs en masse

Si vous souhaitez créer plusieurs utilisateurs en une seule fois, vous devez activer le plugin **User Mass Register**.

Ce plugin permet de créer des utilisateurs en masse à partir d’une liste d’adresses email. Les utilisateurs sont créés par défaut avec le statut Visiteur. 

Vous pouvez ensuite modifier ces utilisateurs en masse grâce au mode sélection (voir chapitre : [Modifier des utilisateurs en masse](creer-et-gerer-les-utilisateurs))**.**

!!! info
    Si vous êtes client d’une offre Piwigo Cloud, ce plugin n’est accessible qu’à partir de l’offre Entreprise.


## Add User Note : Ajouter un commentaire à un utilisateur

Pour ajouter une note ou un commentaire à un utilisateur, vous pouvez activer le plugin **Add User Note**.

!!! info
    Si vous êtes client d’une offre Piwigo Cloud, ce plugin n’est accessible qu’à partir de l’offre Équipe.


Ce plugin ajoute un onglet “Remarque” dans la fenêtre d’édition d’un utilisateur.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-b4723ae0.png)

Quand une note a été saisie sur un utilisateur, une icône apparaît à côté de son nom dans la liste.

En passant la souris sur cette icône, vous pourrez lire la note.

![fr-user-note-2.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-1ac4fc6e.png)

## User Custom Fields : Ajouter des champs personnalisés aux utilisateurs

Il est possible de créer des champs personnalisés associés aux utilisateurs.

!!! info
    Si vous êtes client d’une offre Piwigo Cloud, ce plugin n’est accessible qu’à partir de l’offre Équipe.


Pour cela, vous devez activer le plugin User Custom Fields. 

L’intérêt de ce plugin, c’est qu’il permet de demander des informations supplémentaires aux personnes qui s’enregistrent sur votre galerie (lorsque vous avez activé cette possibilité). Les champs supplémentaires peuvent être obligatoires ou pas.

Dans l’exemple ci-dessous, nous avons ajouté le champ “Ville” dans le formulaire d’inscription sur la galerie.

![fr-user-custom-field-galerie.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-72711215.png)

Lorsque que ce plugin est activé, un onglet “Champs personnalisés” apparaît sur la fenêtre d’édition d’un utilisateur.

Cliquer sur cet onglet permet de visualiser le contenu des champs personnalisés. 

## Crypto Captcha : Empêcher la création de faux utilisateurs

Pour éviter que des robots ne créent de faux utilisateurs sur votre galerie, vous pouvez installer le plugin **Crypto Captcha**.

Ce plugin oblige les utilisateurs à saisir un Captcha avant de créer un compte. Ce Captcha peut également être ajouté sur le formulaire de publication de commentaire.

Plusieurs options sont disponibles pour paramétrer votre Captcha.

![fr-captcha-creation-utilisateur.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-b8c55def.png)
