# Two Factor Authentication : activez la double authentification sur Piwigo

Sommaire :

Depuis la version 16 de Piwigo, il est possible d’activer la double authentification (*two-factor authentication* en anglais, ou *2FA*) pour les utilisateurs. Il s’agit d’une méthode d’authentification forte, depuis plus en plus utilisée aujourd’hui. Quand on active la double authentification, les utilisateurs devront passer par deux étapes pour accéder à Piwigo :

- Étape 1 : identification classique (login + mot de passe)
- Étape 2 : vérification de leur identité, via l’envoi d’un email ou l’utilisation d’une application générant un code à usage unique (TOTP)

Pour mettre en place ce système d’authentification à deux facteurs, vous devez installer et activer le plugin **Two Factor Authentication.**

## Configuration du plugin **Two Factor Authentication**

Pour configurer la double authentification, rendez-vous dans la configuration du plugin.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-8d70ca77.png)

Plusieurs options sont disponibles : 

- Nombre maximal de tentatives échouées avant le verrouillage : si un utilisateur essaye plusieurs fois de se connecter sans succès, son profil sera verrouillé. Vous pouvez régler ici le nombre d’essais maximum.
- Durée du verrouillage (en secondes) : durée pendant laquelle le profil sera verrouillé après que le nombre maximum de tentatives échouées soit atteint.

Deux méthodes disponibles pour la double authentification :

- 2FA par application : les utilisateurs devront utiliser une application d’authentification qui génère un code à usage unique (TOTP)
- 2FA par e-mail : les utilisateurs recevront un code à usage unique par email.

Si vous le souhaitez, vous pouvez activer ces deux méthodes : les utilisateurs choisiront celle qui leur convient le mieux.

## Activation de la double authentification par les utilisateurs

Une fois la double authentification activée via le plugin Two Factor Authentication, elle n’est pas activée par défaut pour les utilisateurs de Piwigo.

Chaque utilisateur doit activer lui-même la double authentification.

Pour cela, il faut se rendre sur la galerie Piwigo et sur la page “Profil” qui permet de gérer son compte utilisateur.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-50dd4d70.png)

Cliquer sur la flèche pour afficher les options sous “Authentification à deux facteurs” : vous pouvez alors choisir la méthode d’authentification que vous souhaitez. 

Remarque : si une seule méthode a été activée dans le paramétrage du plugin, seule cette méthode s’affiche ici.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-ab87f354.png)

## Utiliser la double authentification à l’aide d’une application d’authentification

Si vous choisissez cette méthode, vous devez utiliser une application d’authentification, comme 1Password, Authy, Microsoft Authenticator, TOTP, ou toute autre application permettant de générer des codes de connexion à usage unique.

Vous devez d’abord installer l’application de votre choix sur votre téléphone, si ce n’est pas déjà fait. Dans cette documentation, nous montreront comment cela fonctionne avec l’application gratuite TOTP (disponible pour Apple iOS et Android).

Rendez-vous sur votre profil et cochez “Configuration à l’aide d’une application d’authentification”. Les instructions s’affichent alors.

![image - copie.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-f6ac0445.jpg)

Lancer l’application d’authentification sur votre téléphone, et ajoutez votre compte Piwigo en scannant le QR code qui s’affiche à l’écran.

![IMG_4246.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-c4f445ae.jpg)

Une fois le compte ajouté, l’application génère un code à usage unique.

![IMG_4247.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-2418bf3f.jpg)

 Saisissez le code à usage unique dans la zone prévue à cet effet sur votre profil Piwigo.

 

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-1fe1869c.png)

Piwigo affiche alors le message ci-dessous.

![image (1) - copie.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-413aab0c.jpg)

Copiez les codes de récupération et stockez les dans un fichier, une note, un email, ou tout lieu sécurisé dont vous êtes certain de vous souvenir.

!!! Warning "Attention"
    Comme indiqué sur votre profil, une fois la double authentification activée, les applications tierces qui se connectent à votre compte Piwigo (applications mobiles Piwigo, plugin Lightroom, Piwigo Remote Sync) ne pourront plus se connecter à votre compte utilisateur. [Lisez le dernier chapitre de cette page pour y remédier.](two-factor-authentication-activez-la-double-authentification-sur-piwigo)

## Utiliser la double authentification par email

!!! Warning "Attention"
    Cette méthode n’est pas la plus sûre. Les emails peuvent tomber dans les SPAMS, ou bien ne pas être envoyé si votre serveur est mal configuré. Si vous activez cette méthode, assurez-vous que les emails envoyés par votre Piwigo arrivent bien à destination.

Une fois la double authentification par email activée dans la configuration du plugin, rendez-vous sur votre profil et cochez “Configuration par email”. Vérifiez que l’adresse e-mail associée à votre compte est la bonne, saisissez-là dans la zone “Confirmez votre email” et cliquez sur “Envoyez l’email” : 

![Capture d’écran 2025-11-17 à 12.23.15.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-8f640639.png)

Consultez votre boîte mail, et une fois reçu, saisissez le code dans la zone dédiée.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-9e94e80d.png)

!!! Warning "Attention"
    Comme indiqué sur votre profil, une fois la double authentification activée, les applications tierces qui se connectent à votre compte Piwigo (applications mobiles Piwigo, plugin Lightroom, Piwigo Remote Sync) ne pourront plus se connecter à votre compte utilisateur. [Lisez le dernier chapitre de cette page pour y remédier.](two-factor-authentication-activez-la-double-authentification-sur-piwigo)

## Connexion aux applications tierces lorsque la 2FA est activée

Lorsque la 2FA est activée, les applications tierces qui se connectent à votre Piwigo ne pourront plus le faire en utilisant simplement votre nom d'utilisateur et votre mot de passe. 

En attendant qu'elles implémentent un mécanisme d'identification par clef ou qu'elles implémentent directement la 2FA, Piwigo a prévu une astuce pour que ces applications puissent continuer à fonctionner sans avoir besoin d'être mises à jour.

**Si un utilisateur active la 2FA sur son profil et souhaite pouvoir continuer à se connecter à l’application mobile Piwigo, à Piwigo Remote Sync, ou au plugin d’export Lightroom, il est indispensable de suivre la procédure suivante.**

### Création d’une clé API dans votre profil

Rendez-vous dans la galerie Piwigo et sur la page “Profil” qui permet de gérer son compte utilisateur.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-50dd4d70.png)

Cliquez sur la flèche pour dérouler la zone “Clés API”.

Créez une nouvelle clé API et nommez la du nom de l'application que vous souhaitez connecter, par exemple "Piwigo mobile iOS". 

Choisissez la durée de validité de cette clé : lorsqu’elle arrivera à expiration, vous devrez en créer une nouvelle et réitérer l’opération.

![Capture d’écran 2025-11-17 à 12.34.23.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-2c0cb19d.png)

Cliquez sur “Générer la clé” : Piwigo affiche alors un code “identifiant” et un code “secret” que **vous devez absolument copier et enregistrer** dans un endroit où vous êtes certain de les retrouver (une note, un document, un email…).

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-af647b3d.png)

### Connexion à une application tierce avec votre clé API

À présent connectez-vous à l’application tierce que vous souhaitez utiliser (comme l’application mobile Piwigo, par exemple).

À la place du nom d'utilisateur, fournissez l'ID (identifiant) de la clef d'API, commençant par "pkid-...", et à la place du mot de passe, fournissez le “secret” de la clef d'API : vous êtes connecté et reconnu comme l'utilisateur associé à la clef d'API.

!!! Warning "Attention"
    La clef API ayant une durée de vie limitée, il faudra veiller à la renouveler régulièrement. Piwigo vous enverra un email lorsqu'une de vos clef d'API expirera.
