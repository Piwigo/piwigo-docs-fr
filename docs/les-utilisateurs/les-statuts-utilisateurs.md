# Les statuts utilisateurs

Pour bien comprendre la gestion des utilisateurs dans Piwigo, la première chose à connaître, c’est le fonctionnement des différents **Statuts**.

Dans Piwigo, il existe 5 statuts, qui donnent des droits différents. Un utilisateur a obligatoirement l’un de ces 5 statuts.

En voici la liste.

## 1- Administrateur

Un administrateur a accès à toutes les données présentes dans Piwigo, et surtout, il a accès à l’espace d’administration :

- ajout, modification et suppression d’albums,
- ajout, modification et suppression de photos,
- ajout, modification et suppression d’utilisateurs,
- gestion des tags,
- visualisation des statistiques et de l’historique des actions dans la galerie,
- gestion des commentaires.

En revanche, il n’a pas accès au paramétrage du thème de la galerie, ni à l’ajout de plugins.

Dans la plupart des organisations, les administrateurs sont les gestionnaires de la photothèque : documentaliste, responsable communication, iconographe…

!!! info
    Un administrateur a accès à tous les albums et toutes les photos dans l’administation. En revanche, une fois connecté sur la galerie web, les permissions s’appliquent : il ne voit que les albums publics ou les albums privé auxquels il a accès.


## 2- **Visiteur**

Un visiteur peut se connecter à votre galerie Piwigo, mais pas à l’administration. Par défaut, quand vous créez un utilisateur, ou quand un utilisateur s’enregistre lui-même, il a le statut de visiteur.

Un visiteur peut visualiser et télécharger les fichiers de votre photothèque auxquels il a droit, mais il ne peut pas ajouter de photo à Piwigo (sauf avec le plugin [Community](gerer-les-contributeurs-plugin-community)).

Au sein d’une organisation, dans la majorité des cas, la plupart des utilisateurs sont des visiteurs : ce sont les personnes qui se connectent à la photothèque pour rechercher et télécharger les fichiers dont elles ont besoin.

## 3- **Webmestre**

Un webmestre a les mêmes droits que l’administrateur, mais également d’autres droits : activer ou désactiver des plugins, modifier le thème, accéder aux options de configuration de la galerie…

Par défaut, le premier utilisateur créé lors de la création d’un compte Piwigo ou de l’installation d’un Piwigo (utilisateur principal) a le statut de webmestre (ou webmaster).

## 4- Générique

Ce statut peut être utile lorsque plusieurs personnes partagent le même compte utilisateur. 

Les profils génériques ont accès à votre galerie mais pas à l’administration, comme les visiteurs, mais avec quelques spécificités (pas de possibilité de modifier le mot de passe ou la langue d’affichage, par exemple).

## 5- Invité (désactivé)

Les utilisateurs ayant ce statut ne peuvent pas se connecter à Piwigo. 

Ce statut est utile pour désactiver le compte d’un utilisateur sans supprimer son historique.

!!! Warning "Attention"
    Attention ! À ne pas confondre avec le “compte invité” ou “guest”, qui est le nom générique donné au profil des visiteurs anonyme (non connectés à la galerie) : voir ci-dessous


## Cas particulier : l’utilisateur “Guest”

L’utilisateur Guest (ou invité) est un utilisateur “fantôme” dans Piwigo. Il correspond aux visiteurs non connectés qui visitent votre galerie.

Dans l’administration, vous pouvez déterminer les permissions et paramètres appliqués à ces utilisateurs. Ils seront appliqués par défaut à tous les nouveaux utilisateurs créés par la suite : ce sont donc les paramètres “de base” de Piwigo.

Pour savoir comment modifier le compte “Guest”, [lisez cet article](creer-et-gerer-les-utilisateurs).

## Le statut de contributeur (plugin Community)

Dans nos [offres tarifaires](https://fr.piwigo.org/tarifs), nous mentionnons le statut de “Contributeur”.

Ce statut n’est pas un type d’utilisateur à proprement parler : il qualifie les utilisateurs non administrateurs autorisés à importer des fichiers dans Piwigo lorsque le plugin Community est activé. 

Pour en savoir plus, lisez cet article : [Gérer les contributeurs (plugin Community)](gerer-les-contributeurs-plugin-community)
