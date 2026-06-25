# Les niveaux de confidentialité

## Les niveaux de confidentialité : pour quoi faire ?

Pour déterminer quels utilisateurs ont accès à quels contenus dans Piwigo, la solution la plus courante et la plus pratique, c’est d’utiliser les permissions sur les albums.

Pour rappel, un album peut être privé ou public, et les utilisateurs et groupes d’utilisateurs ont accès, ou non, à chaque album privé. [En savoir plus sur la visibilité des albums](../organiser-les-albums/permissions-et-visibilite-des-albums)

Ainsi, lorsqu’un utilisateur est connecté à votre galerie, il visualise uniquement les albums auxquels il a accès.

Mais dans certains cas, vous pouvez avoir besoin de gérer un niveau de droits plus fins, fichier par fichier, au-delà des albums. C’est à cela que servent les “niveaux de confidentialité”.

!!! Warning "Attention"
    Attention ! Il s’agit d’une fonctionnalité avancée de Piwigo, que l’on vous déconseille d’utiliser si vous êtes débutant.


## Les niveaux de confidentialité : comment ça marche ?

Dans Piwigo, chaque fichier peut être associé à un niveau de confidentialité.

Ainsi, lorsque vous éditez une photo, vous pouvez déterminer son niveau de confidentialité grâce au champ “Qui peut voir cette photo ?” (par défaut : Tout le monde).

![fr-niveau-confidentialité.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-0642c124.png)

Lorsque vous déroulez la liste, vous pouvez choisir le niveau de confidentialité affecté à cette photo. 

![fr-niveau-confidentialité2.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-5e1e5222.png)

Lorsque l’on utilise les niveaux de confidentialité, chaque utilisateur devra lui aussi être associé à un niveau de confidentialité :

- Admins (attention : cela n’a rien à voir avec le statut Administrateur)
- Famille
- Amis
- Contacts
- Aucun (par défaut)

Les utilisateurs ayant le niveau le plus haut (Admins) auront accès à tout.

Les utilisateurs “Famille”, eux, n’auront accès qu’aux photos associées aux niveaux de confidentialité “Famille”, “Amis”, “Contacts”.

Les utilisateurs “Amis” n’auront accès qu’aux niveaux “Amis” et “Contacts”.

Les utilisateurs “Contacts” ne verront que les fichiers du niveau “Contacts”.

Et les utilisateurs avec le statut “Aucun” n’auront accès qu’aux fichiers accessibles à “Tout le monde”.

C’est une gestion de droits “en cascade”, un peu complexe à appréhender et relativement “figée”, c’est pourquoi on a tendance à la déconseiller aux utilisateurs débutants.

!!! info
    Si les libellés Admin, Famille, Amis et Contacts ne vous conviennent pas, sachez qu’il est possible de les personnaliser en contactant le support si vous avez un compte sur piwigo.com. En revanche, il n’est pas possible d’ajouter un niveau de confidentialité supplémentaire.


Sommaire de l’article

---

← Précédent

[Créer et gérer les utilisateurs](creer-et-gerer-les-utilisateurs)

Suivant →

[Envoyer des emails de notification aux utilisateurs](envoyer-des-emails-de-notification-aux-utilisateurs)
