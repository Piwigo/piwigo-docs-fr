# Gérer les commentaires

Avec Piwigo, vous pouvez permettre aux visiteurs de votre galerie d’ajouter des commentaires sur les contenus de votre photothèque.

## Activer ou désactiver les commentaires sur votre galerie

Pour activer ou désactiver les commentaires sur votre galerie, rendez-vous dans l’administration, menu Configuration > Options, puis dans l’onglet Commentaires.

Pour activer les commentaires, cochez l’option “Activer les commentaires” et enregistrez les paramètres. Mais prenez le temps d’abord de consulter les options disponibles (voir chapitre suivant) !

## Options de gestion des commentaires

Une fois l’option cochée “Activer les commentaires”, plusieurs sous-options apparaissent : parcourez-les attentivement !

![fr-options-commentaires.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-e01476a8.png)

Quelques précisions sur certaines de ces options :

- **Commentaires pour tous :** si vous cochez cette case, même les visiteurs anonymes (non enregistrés sur votre galerie) peuvent laisser un commentaire ;
- **Validation :** si vous cochez cette case, les commentaires ne seront pas immédiatement publiés ; ils devront être validés par un administrateur avant de devenir visibles sur votre galerie.
- **Notification des administrateurs :** si vous cochez l’option “Validation”, on vous conseille d’activer la notification des administrateurs quand un commentaire est **en attente de validation**. Vous pouvez aussi ne pas demander aux administrateurs de valider les commentaires, mais simplement les informer quand un commentaire est publié, en cochant l’option “Notifier les administrateurs lorsqu’un commentaire est **ajouté”**.

### **Quelques conseils pour éviter le spam dans les commentaires :**

Par défaut, un contrôle est mis en place pour éviter les abus : si un utilisateur essaye de poster plusieurs commentaires sur une même photo depuis la même adresse IP dans un intervalle très court, le système bloque l’envoi du deuxième commentaire.

Mais cela ne règle pas tous les problèmes. 

Si votre galerie est publique et que vous acceptez les commentaires de la part des visiteurs anonymes, vous courez un risque : que vos commentaires soient pollués par des robots spammeurs. 

Pour éviter cela, nous vous conseillons de respecter quelques bonnes pratiques :

- Ne cochez pas l’option “Autoriser les utilisateurs à donner un lien vers leur site web” : lorsque tout le monde peut laisser un commentaire sur un site, cette option est très appréciée des spammeurs ;
- Obligez les utilisateurs à donner des informations pour laisser un commentaire (adresse email, nom d’utilisateur)
- Si nécessaire, ajoutez un contrôle antispam sur les commentaires (pour en savoir plus, visitez la page [Commentaires : options avancées](/les-commentaires-et-notes/gerer-les-notes-votes))

## Affichage des commentaires sur la galerie

Sur votre galerie, les commentaires sont affichés sur la page d’une photo, en bas de la photo (dans la plupart des thèmes).

Si les commentaires sont réservés aux utilisateurs enregistrés, les visiteurs anonymes pourront voir le nombre de commentaires et lire les commentaires publiés, mais ils ne verront pas s’afficher le formulaire de publication d’un commentaire.

### Affichage des commentaires avec le thème Modus

Sur les galeries utilisant le thème Modus, sous chaque photo on affiche à gauche le formulaire de saisie d’un nouveau commentaire, et à droite la liste des commentaires déjà publiés.

![fr-commentaire-modus.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-92daec06.png)

### Affichage des commentaires avec le thème Bootstrap Darkroom

Sur les galeries utilisant le thème Bootstrap Darkroom, sous chaque photo on affiche à droite les commentaires publiés. 

![fr-commentaire-bd.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-cd835f3b.png)

Le bouton “Ajouter un commentaire” permet d’ouvrir un onglet de saisie d’un nouveau commentaire.

![fr-commentaire-bd-2.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-56fc5fa2.png)

### Page des commentaires sur votre galerie

Sur votre galerie, vous pouvez voir tous les commentaires grâce à la page sous le menu Explorer > Commentaires.

Cette page affiche tous les commentaires publiés sur votre galerie avec la photo associée, la date, etc.

Vous pouvez choisir de trier les commentaires par photo ou par date, et utiliser le moteur de recherche pour filtrer les commentaires (par album, par auteur, en recherchant un mot en particulier…).

![fr-commentaires-galerie2.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-238257e9.png)

!!! info
    Remarque : Depuis cette page, les administrateurs ont la possibilité de valider, éditer et supprimer les commentaires.


## Gérer, modifier, supprimer les commentaires

### Valider les commentaires en attente suite à un email

Lorsqu’un nouveau commentaire est en attente de validation et que les administrateurs sont notifiés (voir le chapitre “Options de gestion des commentaires”), ils reçoivent un mail comme ci-dessous avec une mention “Ce commentaire doit être validé”.

![fr-email-admin-commentaire2.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-b74d2e24.png)

Le lien “Gérer ce commentaire” permet d’accéder directement au commentaire sur la galerie, et donne accès aux 3 options disponibles : Valider, Supprimer (revient à rejeter le commentaire), Editer (modifier).

![fr-email-lien-commentaire.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-923f602a.png)

### Valider les commentaires en attente dans l’administration

Depuis l’administration de Piwigo, vous pouvez gérer les commentaires depuis le menu Outils > Commentaires.

Depuis cet écran, vous pouvez voir tous les commentaires publiés sur votre galerie en cliquant sur “Tout”.  Si vous avez activé l’option “Validation des commentaires”, vous repérer les commentaires en attente de validation grâce au libellé “En attente” en rouge.

![fr-commentaires-admin.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-c7bdcbca.png)

Pour voir uniquement les commentaires en attente de validation, cliquez sur le bouton “En attente”.

Pour valider ou rejeter un commentaire, il suffit de le cocher et de cliquer sur “Valider” ou “Rejeter”.

![fr-commentaire-rejeté.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-fa8c07fb.png)

Une fois rejeté, un commentaire n’est plus visible dans la liste.

Remarque : Lorsqu’un commentaire est en attente de validation, un bandeau s’affiche sur le tableau de bord des administrateurs. Un bouton permet d’accéder directement à la page de gestion des commentaires en attente.

![fr-tableaubord-comment.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-9d10930e.png)

### Modifier ou supprimer un commentaire

Les administrateurs peuvent supprimer ou modifier les commentaires des utilisateurs depuis la galerie.

Lorsqu’un administrateur visualise les commentaires d’une photo sur la galerie, il a accès à deux actions pour chaque commentaire : “Editer” (modifier) et “Supprimer”. Si le commentaire est en attente de validation, l’action “Valider” est également disponible.

![fr-editer-supprimer-commentaires.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-90547659.png)

!!! info
    Si vous avez coché les options qui autorisent les utilisateurs à supprimer / modifier leurs propres commentaires, ils auront accès également à ces actions sur leurs commentaires (sauf les visiteurs anonymes, non enregistrés).


Ces actions sont bien entendu disponibles également depuis la page des commentaires sur la galerie.

Lorsque les administrateurs sont notifiés par email à chaque ajout de commentaire (sans validation), ils reçoivent un email qui contient un lien pour lire et éventuellement, modifier ou supprimer le commentaire.

Sommaire de l’article

---

Suivant →

[Personnaliser la gestion des commentaires avec des plugins](/les-commentaires-et-notes/gerer-les-notes-votes)
