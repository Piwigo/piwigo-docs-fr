# Envoyer des emails de notification aux utilisateurs

Vous pouvez avoir besoin d’envoyer des emails à certains utilisateurs de Piwigo, pour les prévenir que de nouvelles photos ou de nouveaux albums ont été créés.

Pour cela, vous avez principalement deux possibilités.

## Notifications sur un album

Dans l’administration, vous pouvez envoyer un email à des utilisateurs ou des groupes d’utilisateurs au sujet d’un album en particulier.

Cela permet de les informer lorsqu’un nouvel album a été créé, ou lorsque des modifications ont été effectuées.

Pour cela, vous devez vous rendre dans Albums > Gérer, modifier l’album concerné, et vous rendre dans l’onglet “Notification”.

Cet onglet permet de définir les utilisateurs ou groupes d’utilisateurs à notifier, et le contenu du message complémentaire si nécessaire.

![fr-notif-album.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-5996131d.png)

Les personnes concernées recevront un email contenant un lien vers l’album, accompagné de votre message.

![fr-notif-album.email.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-63560b26.png)

<aside>
ℹ️ Attention : avant d’envoyer une notification, pensez à vérifier que les utilisateurs ont bien accès à cet album dans l’onglet Permissions.

</aside>

## Notifications globales

Vous pouvez également mettre en place des emails pour informer les utilisateurs de toutes les nouveautés sur la galerie depuis leur dernière connexion.

<aside>
ℹ️ Attention : seuls les utilisateurs ayant le statut “Webmestre” peuvent accéder à cette fonctionnalité.

</aside>

Pour cela, rendez-vous dans Utilisateurs > Notification.

### Paramétrage des emails

Le premier onglet “Paramètres” permet de définir les paramètres des emails envoyés :

![fr-notif-paramètres.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-e323a31f.png)

- Format HTML : si vous cochez “Oui”, l’email sera mise en page avec des liens, des images et des couleurs. Si vous cochez “Non”, l’email sera envoyé en texte brut.
- Envoyer des emails en tant que : c’est le nom d’expéditeur qui sera affiché dans l’email. Par défaut, c’est le nom de votre galerie Piwigo.
- Ajout d’un contenu détaillé : Si vous cochez “Oui”, l’email contiendra les détails des modifications apportées (nombre de nouvelles photos, d’albums mis à jour, de nouveaux utilisateurs).
- Contenu complémentaire de l’email : permet de définir un message personnalisé qui sera ajouté par défaut aux emails envoyés.
- Inclure l’affichage des dernières photos groupées par date : Si vous cochez “Oui”, l’email contiendra toutes les dernières photos ajoutées, par date d’ajout.

### Définition des utilisateurs à notifier

L’onglet “M’abonner” permet de définir quels utilisateurs recevront des emails de notification.

Pour inscrire ou désinscrire des utilisateurs, déplacez-les vers la colonne de gauche en cliquant sur les flèches orange.

![fr-notif-album.liste.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-e080c127.png)

Lorsqu’un utilisateur est inscrit, il reçoit un email de confirmation. Si il le souhaite, il peut se désinscrire.

![fr-notif-confirmation.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-6af3300a.png)

### Envoyer un email de notification

L’onglet “Envoi” permet de déclencher l’envoi d’un email.

![fr-notif-envoi.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-e218a99c.png)

La section “Sélection des destinataires” affiche les utilisateurs inscrits aux notifications, et qui sont concernés (c’est à dire qu’il y a eu des nouveautés sur Piwigo depuis la dernière notification qu’ils ont reçue). Vous pouvez cocher ou décocher les utilisateurs à qui vous voulez envoyer un email.

La section “Contenu complémentaire” affiche le message par défaut défini dans les paramètres et permet de le personnaliser.

Cliquez sur “Envoi” pour déclencher l’envoi de l’email.

![fr-notif-contenu-email.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-61145fe7.png)

## **Protect Notification : Changer l’expéditeur des emails de notification**

Parfois, il arrive que les emails de notification envoyés par Piwigo arrivent en SPAM. Cela vient du fait qu’ils sont envoyés par l’adresse email de l’administrateur principal (webmestre). Le serveur [piwigo.com](http://piwigo.com) n’ayant pas le droit d’envoyer des emails depuis cette adresse mail, les emails sont considérés comme non sécurisés.

Pour régler ce problème, vous pouvez installer le plugin **Protect Notif**.

Une fois ce plugin activé, tous les emails de notifications envoyés par Piwigo seront expédiés depuis une fausse adresse du type “no-reply@phototheque.piwigo.com”.

En conséquence, les emails de notification seront correctement distribués.

<aside>
ℹ️ Depuis février 2024, Protect Notif est activé par défaut sur tous les nouveaux comptes créés sur piwigo.com.

</aside>

Sommaire de l’article

---

← Précédent

[Les niveaux de confidentialité](/les-utilisateurs/les-niveaux-de-confidentialite)

Suivant →

[Les groupes d’utilisateurs](/les-utilisateurs/les-groupes-dutilisateurs)