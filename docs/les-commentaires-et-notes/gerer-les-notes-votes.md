# Personnaliser la gestion des commentaires avec des plugins

Dans l’article [Gérer les commentaires](/les-commentaires-et-notes/commentaires-options-avancees), nous présentons les options de base dans Piwigo sur la gestion des commentaires. Mais il existe plusieurs plugins permettant d’aller plus loin : on fait le tour de ces options dans cet article.

## Options de mise en forme des commentaires

### **BBCode Bar :** Ajouter une barre d’outils pour mettre en forme les commentaires

Si vous souhaitez que les utilisateurs puissent mettre en forme leurs commentaires (texte en gras, en italique, listes à puces,…) il suffit d’installer le plugin **BBCode Bar**.

Ce plugin permet d’afficher une barre de mise en forme dans la fenêtre de commentaire. Vous pouvez activer ou pas les options.

![fr-plugin-bbcode.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-65bdc4b6.png)

### Smilies Support : Ajouter des émoticônes dans les commentaires

Si vous souhaitez que les utilisateurs puissent ajouter des émoticônes dans les commentaires, il suffit d’installer le plugin **Smilies Support.**

Ce plugin permet de choisir un jeu d’émoticônes à ajouter à votre galerie. Au moment de saisir son commentaire, l’utilisateur peut choisir un émoticône dans la liste.

![fr-commentaire-smilies.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-929139e0.png)

!!! info
    Remarque : Ces émoticônes sont du même type que ceux que l’on retrouve dans les  forums de discussions. Il ne faut pas les confondre avec les émojis que l’on utilise beaucoup plus de nos jours. Piwigo n’intègre pas de clavier d’émojis.


## **Subscribe to Comments :** S’abonner aux commentaires

Si vous souhaitez qu’un utilisateur (autre qu’un administrateur) puisse être notifié lorsqu’un nouveau commentaire est publié il suffit d’installer le plugin **Subscribe to Comments**.

Une fois ce plugin activé, lors de la saisie d’un commentaire, un utilisateur pourra choisir d’être notifié :

- Lorsqu’un nouveau commentaire sera publié sur cette photo (cela revient à s’abonner aux commentaires de cette photo) ;
- Lorsqu’un nouveau commentaire sera publié sur une photo du même album
- Lorsqu’un nouveau commentaire sera publié sur le site

![fr-commentaire-subscribe.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-79712ff5.png)

Un utilisateur peut tout à fait s’abonner aux commentaires sans lui-même saisir de commentaire : pour cela il suffit de cliquer sur “S’inscrire sans commenter”.

Lorsqu’une personne est abonnée aux commentaires, elle reçoit un mail comme ci-dessous à chaque nouveau commentaire. Depuis cet email, il est possible de cliquer sur l’image pour voir la photo, de se désabonner des commentaires de cette photo, et de gérer tous ses abonnements aux commentaires.

![fr-email-subscribe-comment.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-ab899393.png)

## Éviter le SPAM dans les commentaires

Malheureusement, les zones de saisie de commentaires sont souvent appréciées des robots spammeurs. Il est donc parfois nécessaire de mettre en place des actions préventives pour éviter le SPAM.

Plusieurs plugins permettent de contrôler la saisie des commentaires sur Piwigo.

### **Comments Blacklist :** Bannir certains mots des commentaires

Pour définir une liste de mots interdits dans les commentaires, vous pouvez installer le plugin **Comments Blacklist.**

Ce plugin permet de saisir une liste de mots interdits. Si un commentaire comportant un de ces mots est saisi, sa publication sera soit bloquée, soit soumise à modération (selon votre choix).

Cela permet de bannir des mots fréquemment utilisés dans des commentaires “SPAM”, mais également d’éviter les commentaires grossiers, injurieux ou déplacés.

### **Crypto Captcha :** Ajouter un Captcha sur la zone de commentaire

Pour ajouter un Captcha sur le formulaire de saisie de commentaires, vous pouvez installer le plugin **Crypto Captcha.**

Ce plugin oblige les utilisateurs à saisir un Captcha avant de valider un commentaire. Ce captcha peut également être ajouté sur le formulaire de création d’un nouvel utilisateur, afin d’éviter les créations de “faux comptes”.

Plusieurs options sont disponibles pour paramétrer votre Captcha.

![fr-commentaire-captcha.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-52229e17.png)

### **RV Akismet :** Contrôler les commentaires avec Askimet

Vous pouvez utiliser le service en ligne [Akismet](https://akismet.com/), une référence dans le domaine, pour vérifier que les commentaires saisis sur votre galerie ne sont pas des SPAMS.

Pour cela, il suffit d’installer le plugin **RV Akismet.**

Une fois le plugin activé, vous devez créer un compte Akismet : cela vous donnera accès à une clé API que vous devrez saisir dans la configuration du plugin.

!!! info
    Il est possible de créer un compte gratuit sur Akismet, mais certaines options nécessitent un abonnement payant. Les comptes gratuits sont réservés à un usage personnel non commercial.


Le plugin vous donne le choix entre deux options :

- Rejeter tous les commentaires identifiés par Akismet comme du SPAM
- Modérer les commentaires identifiés par Akismet comme du SPAM (c’est à dire les soumettre à une validation avant publication).

## **Comments on Albums :** Accepter les commentaires sur les pages Albums

Par défaut, Piwigo gère les commentaires sur les pages des photos.

Mais si vous le souhaitez, vous pouvez également activer une zone de commentaires sur les pages Albums.

Pour cela, il suffit d’activer le plugin **Comments on Albums**.

Une fois ce plugin activé, il ajoute une fenêtre de saisie de commentaire sur les pages album de votre galerie.

Les commentaires sur les pages des albums sont soumis aux mêmes règles et aux mêmes paramètres que les commentaires des photos.

![fr-commentaire-album.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-2e74e6c3.png)

Une fois ce plugin activé, un onglet Albums est ajouté :

- sur la page de gestion des commentaires dans l’administration
    
    ![fr-albums-comments-admin.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-749f031d.png)
    
- sur la liste page qui liste les commentaires sur la galerie
    
    ![fr-albums-comment-galerie.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-6bb31cb8.png)
    

Sommaire de l’article

---

← Précédent

[Gérer les commentaires](/les-commentaires-et-notes/commentaires-options-avancees)
