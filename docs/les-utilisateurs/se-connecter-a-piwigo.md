# Se connecter à Piwigo

## Comment se connecter à Piwigo ?

Pour vous connecter à votre compte Piwigo, vous devez donc vous rendre sur l’URL (l’adresse web) de votre galerie. 

Si vous utilisez Modus, le thème par défaut installé avec Piwigo, un lien “Connexion” est disponible en haut à droite de votre écran. Ce lien ouvre la fenêtre qui permet de se connecter à Piwigo.

![fr-piwigo-connexion.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-569c3cd5.png)

Si vous utilisez le thème Bootstrap Darkroom, le bouton de connexion ouvre une fenêtre modale de connexion mais n’ouvre pas une nouvelle page.

![fr-piwigo-connexion-boostrap.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-ea1e7b96.png)

!!! Warning "Attention"
    Il est possible, selon le thème et la personnalisation de votre galerie, que l’écran de connexion soit différent de ce qui est affiché dans les images précédentes.


L'URL de votre page de connexion Piwigo est `mygallery.com`/identification.php, `mygallery.com` représentant l'URL racine de votre galerie. 

Si votre galerie est hébergée sur [Piwigo Cloud](http://piwigo.org) et que vous n’avez pas personnalisé le nom de domaine de votre galerie, votre URL de connexion ressemble à `mygallery`.piwigo.com/identification.php, `mygallery` représentant le nom d'utilisateur que vous avez choisi lors de la création de votre compte.

Pour vous connecter à Piwigo, vous pouvez utiliser votre identifiant OU votre adresse email dans le champ “Nom d’utilisateur”.

Vous devez également saisir votre mot de passe.

Une fois connecté, vous êtes redirigé sur votre galerie.

## Comment afficher un formulaire de connexion sur la page d’accueil ?

Si vous souhaitez que la page d’accueil affiche directement un formulaire de connexion, c’est possible avec le plugin **PWG Stuffs**.

[En savoir plus](../personnaliser-ma-galerie/personnaliser-votre-galerie-avec-des-plugins/pwg-stuff-ajouter-des-blocs-sur-votre-galerie)

## Comment se connecter à l’administration de Piwigo ?

Si vous êtes connecté à votre Piwigo en tant qu’administrateur, il vous suffit de cliquer sur le menu Admin depuis votre galerie web pour basculer sur l’administration.

Par défaut, si vous utilisez le thème Modus, le menu Admin est situé en haut à droite de votre écran.

![fr-connexion-admin-modus.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-5238056d.png)

Si vous utilisez le thème Bootstrap Darkroom, le menu d’accès à l’administration est accessible en cliquant sur votre nom d’utilisateur en haut à droite.

![fr-connexion-admin-boostrap.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-daf8dced.png)

## Comment récupérer mon mot de passe ?

Si vous avez perdu votre mot de passe, il est impossible de le récupérer, que vous soyez client d’une offre Piwigo Cloud, ou utilisateur d’un piwigo auto-hébergé. Vous devez donc réinitialiser votre mot de passe.

Pour réinitialiser votre mot de passe, vous devez vous rendre sur la fenêtre de connexion à Piwigo et cliquer sur “Mot de passe oublié”.

En entrant votre nom d’utilisateur ou votre adresse email, vous recevez par email un lien pour réinitialiser votre mot de passe.

Vous pouvez également demander à un administrateur de vous envoyer un email avec un lien de réinitialisation de votre mot de passe, ou de définir un nouveau  mot de passe pour vous et de vous le communiquer.

## Comment récupérer mon identifiant ou mon adresse email ?

Vous avez oublié votre identifiant et / ou l’adresse email avec laquelle vous vous connectez à Piwigo ?

Pas de panique : il y a plusieurs possibilités pour récupérer votre compte.

### Demander à un administrateur

Si vous travaillez en équipe, contactez l’administrateur principal de votre Piwigo : il pourra retrouver votre compte et générer un nouveau mot de passe.

Vous pouvez également rechercher dans votre boîte mail l’email qui vous a été envoyé à la création de votre compte.

### Retrouver les identifiants reçus par email à la création du compte

Si vous êtes le seul utilisateur de votre Piwigo, ou si vous êtes l’administrateur principal (le webmestre), vous avez normalement reçu vos identifiants par email.

- Si votre Piwigo est hébergé sur [Piwigo Cloud](http://piwigo.org) : vous avez reçu un email au moment de la création de votre compte Piwigo.
- Si vous hébergez vous-même votre Piwigo : lorsque vous avez installé Piwigo la première fois, si vous êtes passé par le formulaire d’installation, vous avez peut-être coché la case “recevoir mes identifiants par email”.

### Vous ne réussissez vraiment pas à vous connecter à Piwigo ?

Si vous avez un compte sur Piwigo Cloud, contactez le support : nous trouverons un moyen de le récupérer.

Si vous hébergez vous-même votre Piwigo, nous ne pouvons malheureusement pas vous aider. Si vous avez accès à la base de données de Piwigo, vous pouvez en revanche retrouver votre identifiant dans la table Users.

## Comment créer un nouveau compte sur une galerie Piwigo ?

Pour créer un nouvel utilisateur sur Piwigo, il a deux possibilités.

### Cas n°1 : c’est un administrateur qui crée les comptes utilisateurs

Parfois, l’option “Permettre l'enregistrement des utilisateurs” a été désactivée (cette option est disponible dans le menu Configuration > Options, onglet général, Section Permissions).

Dans ce cas, il est impossible pour un visiteur de la galerie de créer son compte en autonomie : seul un administrateur peut créer de nouveaux utilisateurs. 

Pour savoir comment créer un utilisateur dans l’administration, [lisez cet article](creer-et-gerer-les-utilisateurs).

### Cas n°2 : les visiteurs de la galerie peuvent créer leur compte

Si l’option  “Permettre l'enregistrement des utilisateurs” a été activée, alors n’importe quel visiteur de la galerie pourra créer son compte.

!!! info
    Pour en savoir plus sur la possibilité pour les utilisateurs de créer leur propre compte sur Piwigo, [lisez cet article](creer-et-gerer-les-utilisateurs).


Pour créer un nouveau compte sur une galerie Piwigo, vous devez cliquer sur Connexion.

Un bouton “S’enregistrer” permet de créer un nouveau compte.

Pour créer un nouveau compte, il faut donner un identifiant, un email et un mot de passe.

!!! info
    Si vous souhaitez ajouter des champs personnalisés au formulaire de création de compte, vous devez activer le plugin User Custom Fields. [En savoir plus](creer-et-gerer-les-utilisateurs)


!!! info
    Si vous souhaitez éviter la création de faux utilisateurs par des robots, vous pouvez contrôler la création de compte grâce à la saisie d’un Captcha. Pour cela, il faut activer le plugin **Crypto Captcha**. [En savoir plus](creer-et-gerer-les-utilisateurs)


Les comptes utilisateurs créés par via la galerie en autonomie ne sont pas administrateurs mais seulement Visiteurs. Pour en savoir plus sur les statuts utilisateurs, [lisez cet article](les-statuts-utilisateurs).

## Comment activer la double authentification (2FA) sur Piwigo ?

Depuis la version 16 de Piwigo, il est possible d’activer la double authentification (authentification à deux facteurs (*two-factor authentication* en anglais, ou *2FA*) pour les utilisateurs. Il s’agit d’une méthode d’authentification forte, depuis plus en plus utilisée aujourd’hui. Quand on active la double authentification, les utilisateurs devront passer par deux étapes pour accéder à Piwigo :

- Étape 1 : identification classique (login + mot de passe)
- Étape 2 : vérification de leur identité, via l’envoi d’un email ou l’utilisation d’une application générant un code à usage unique (TOTP)

Pour mettre en place ce système d’authentification à deux facteurs, vous devez installer et activer le plugin **Two Factor Authentication.**

Cliquez ci-dessous pour lire la documentation de ce plugin :

[**Two Factor Authentication : activez la double authentification sur Piwigo**](se-connecter-a-piwigo/two-factor-authentication-activez-la-double-authentification-sur-piwigo)

## Comment activer le single sign on (SSO) sur Piwigo ?

Si vous travaillez au sein d’une organisation, il est possible que vous utilisiez déjà un système de gestion des utilisateurs et des mots de passe. Vous souhaitez donc que les utilisateurs puissent se connecter à Piwigo automatiquement.

C’est possible de deux façons : avec le plugin **LDAP Login** et avec le plugin **Microsoft 365 connect.**

### LDAP Login : utiliser un annuaire LDAP

Ce plugin permet de connecter Piwigo à un annuaire LDAP.

!!! Warning "Attention"
    Si vous êtes client d’une offre Piwigo Cloud, ce plugin n’est accessible qu’aux clients d’une offre VIP.


### Microsoft 365 connect : connecter Piwigo à un Azure Active Directory

Ce plugin permet de connecter Piwigo à un Active Directory Azure.

!!! Warning "Attention"
    Si vous êtes client d’une offre Piwigo Cloud, ce plugin n’est accessible qu’aux clients d’une offre VIP.


Les utilisateurs peuvent ainsi utiliser leur compte Microsoft 365 pour se connecter à Piwigo.

- L'adresse email de l'utilisateur Piwigo doit correspondre à l'adresse email du compte Microsoft 365.
- Vous devez d'abord déclarer votre Piwigo App dans le portail Azure (explications sur la page de configuration du plugin).

## Password Policy : Définir des règles de sécurité des mots de passe

Le plugin **Password Policy** permet de mettre en place des règles de sécurité sur les mots de passe : score de complexité, politique de renouvellement, gestion des tentatives de connexion échouées…

!!! Warning "Attention"
    Si vous êtes client d’une offre Piwigo Cloud, ce plugin n’est accessible qu’aux clients d’une offre VIP.


Une fois le plugin Password Policy activé sur votre Piwigo, rendez vous dans sa configuration.

L’onglet **Configuration du plugin** permet de définir les règles de sécurité.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-baff783d.png)

Sur cette page vous pouvez donc :

- Activer le renforcement de la sécurité des mots de passe
- Définir le score minimum à atteindre pour qu’un mot de passe soit accepté

Un score inférieur à 100 est considéré comme faible. Un score compris entre 100 et 500 est dans la moyenne. Un score supérieur à 500 est excellent. Le score dépend de différents paramètres (longueur, type de caractères utilisés).

- Tester un mot de passe et obtenir son score.
    
!!! info
    Par exemple, le mot de passe `piwigo12` obtient un score faible (48) alors que le mot de passe `Xhj89^h5M%` obtient un score moyen (286).
    
- Définir si la règle de renforcement des mots de passe est activée pour les administrateurs ou non
- Activer la règle de renouvellement des mots de passe (dans ce cas, l’administrateur pourra obliger des utilisateurs à renouveler leur mot de passe).
- Activer la gestion des tentatives de connexion échouées : au bout d’un nombre de tentatives paramétrable, l’accès à la galerie sera verrouillé. Le message affiché est personnalisable.
    
    ![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-68a6da1c.png)
    

L’onglet Gestion permet de gérer les demandes de renouvellement de mot de passe et de déverrouiller les comptes verrouillés.

![password.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-b567532a.png)
