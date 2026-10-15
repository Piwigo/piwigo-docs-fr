---
title: Déplacez Piwigo vers un autre serveur
description: "Si vous souhaitez transférer votre gallerie Piwigo vers un nouvel hébergeur, passer de Piwigo Cloud à votre propre environnement ou déplacer votre galerie vers un sous-répertoire ? Vous êtes au bon endroit !"
---

# Déplacez Piwigo vers un autre serveur / emplacement

Si vous souhaitez transférer votre galerie Piwigo vers un autre hébergeur, passer de Piwigo Cloud à votre propre environnement ou déplacer votre galerie vers un sous-répertoire ? Vous êtes au bon endroit !

## Déplacez Piwigo vers un autre serveur

Pour déplacez votre galerie Piwigo vers un autre serveur, il faut suivre les étapes suivantes dans l'ordre indiqué.

### Étape 1 : Faire une sauvegarde de votre base de données (DB)

  La plupart du temps, vous utiliserez le gestionnaire de bases de données **phpMyAdmin**.

### Étape 2 : Sauvegardez tous vos fichiers via FTP

En utilisant un logiciel FTP, sélectionnez le répertoire dans lequel vous avez installé votre galerie. Par défaut le répertoire est `./piwigo`

### Étape 3 : Importer votre DB sur votre nouvel hébergeur

Pour importer votre DB il faut effectuer l'opération inverse de celle décrite au point [n°1](#etape-1-faire-une-sauvegarde-de-votre-base-de-donnees-db) c'est-à-dire à "importer" la sauvegarde précédemment créée dans le gestionnaire phpMyAdmin.  
Si votre sauvegarde est trop volumineuse, vous devrez supprimer l'historique de votre galerie sur votre hébergeur initial et refaire une sauvegarde de la DB. Si cela ne suffit pas, il se peut que certains plugins occupent beaucoup d'espace, désinstallez-les et effectuez une nouvelle sauvegarde.

### Étape 4 : Déplacez tout vos fichier vers votre nouvel hébergeur via FTP

C'est l'inverse du point [n°2](#etape-2-sauvegardez-tous-vos-fichiers-via-ftp), 

This is the reverse of point #2, il faut "envoyer" vos fichiers vers le nouveau dossier d'installation.

### Étape 4 : Édité le fichier `./local/config/database.inc.php`

Voici un example avec des commentaires explicatifs :

```php
<?php
$conf['dblayer'] = 'mysql'; // Type de la base de donnée
$conf['db_base'] = 'piwigo'; // Nom de la base de donnée
$conf['db_user'] = 'gotcha'; // Identifiant de l'utilisateur de la base de donnée
$conf['db_password'] = 'xxxxxx'; // Mot de passe de l'utilisateur de la base de donnée
$conf['db_host'] = 'localhost'; // Addresse de la base de donnée
$prefixeTable = 'piwigo_'; // Préfix des tables de piwigo
 
define('PHPWG_INSTALLED', true);
define('PWG_CHARSET', 'utf-8');
define('DB_CHARSET', 'utf8');
define('DB_COLLATE', '');
 
?>
```

## Passer de Piwigo Cloud à votre propre environnement

Si vous avez déjà une galerie hébergée sur Piwigo cloud et vous souhaitez la déplacer vers votre propre environnement, vous pouvez suivre ce guide.

- Sur votre compte Piwigo cloud, allez sur la page \[Administration > Mon compte > Gérer > onglet Mes données\] et demandez de récupérer vos données. Elles vous seront envoyées sous la forme d'une liste de fichiers zip de 500 MB. Vous pouvez également demander un accès FTP si vous contactez le support client Piwigo cloud.
- Décompressez le contenu des fichiers ZIP. Dans le premier fichier ZIP, vous trouverez la sauvegarde de la base de données SQL ainsi que le répertoire `local`. Tous les fichiers ZIP, y compris le premier, contiennent le répertoire `upload`.
- Modifiez le fichier `local/config/database.inc.php` afin qu’il corresponde aux identifiants de votre base de données sur votre nouveau serveur d’hébergement. Veuillez noter que les tables n’ont pas de préfixe sur Piwigo Cloud; modifiez donc `$prefixeTable = '';`
- Transférez les répertoires `local` et `upload` sur votre nouvel hébergeur
- Importez votre sauvegarde de base de données
- Vous êtes prêt à commencer; vous devrez certainement installer/activer quelques plugins que vous utilisiez sur Piwigo Cloud, mais votre galerie Piwigo vous le signalera.

## Déplacer votre galerie vers un sous-répertoire

### Je ne souhaite pas déplacer mes photos

!!! info "Info :"
    Dans les étapes ci-dessous nous utiliseront la convention selon laquelle le point {.} correspond à `http://www.exemple.com`
    Pour la base de données (BD), nous supposerons que le préfixe de vos tables est `piwigo_`.

- Étape 1: Activez le mode maintenace dans l'administration (\[Administration > Outils > Maintenance\])
- Étape 2: Rendez-vous maintenant à l'adresse `./my_gallery/index.php` pour vérifier que le site est en maintenance.
- Étape 3: Copiez tous les répertoires et fichiers Piwigo depuis la racine vers le répertoire `./my_gallery/`, à l'exception de `./galleries/` et de `./uploads/`.
- Étape 4: Passons maintenant à la première modification de votre base de données (BD) ⇒ Dans votre BD, à l'aide de phpMyAdmin, dans l'onglet "SQL", saisissez le code suivant :

```sql
UPDATE `piwigo_sites` SET `galleries_url` = '../galleries/' WHERE `id` =1 AND  `galleries_url` = './galleries/';
UPDATE `piwigo_sites` SET `galleries_url` = '../uploads/' WHERE `id` =2 AND  `galleries_url` = './uploads/';
```

- Étape 5: Connectez vous à `./my_gallery`/identification.php` et vérifiez que le répertoire `./galleries/` fonctionne correctement pour la gestion des albums. Pour cela : rendez-vous dans Administration > Outils > Synchroniser, puis dans l'onglet "Gestionnaire du site"; vous devriez y voir `./galleries/`. Si ce n'est pas le cas, recommencez.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-30c509c5.png)

- Étape 6: Vous devez maintenant renommer (à la racine) le fichier `./index.php` en `./index.old.php`.
- Étape 7: La galerie peut désormais être déverrouillée (\[Administration > Outils > Maintenance\])
- Étape 8: Nous allons placer le nouveau fichier `index.php` à la racine du site :
    1. Renommez l'ancien fichier `index.php` en `index.php.old`
    2. Votre nouveau fichier `index.php` servira de page d'accueil lorsque vous accéderez à `http://www.exemple.com`.
- Étape 9: Ensuite, pour finaliser le processus, il est nécessaire de mettre à jour les informations concernant les chemins d’accès (entre autres) : Administration > Outils > Maintenance, puis sélectionnez :
    1. Mettre à jour les informations des albums
    2. Mettre à jour les informations des photos
    3. Purger les modèles compilés
- Étape 9: Dernière vérification : assurez-vous que les images sont bien disponibles sur le site.

Dans quelques jours (le temps de vérifier que tout s'est bien passé), vous pourrez supprimer tous vos anciens dossiers et fichiers situés à la racine, à l'exception des éléments suivants : `./galleries/` `./uploads/` `./my_gallery/` `./index.php`

### Je veux tout déplacer sur le même serveur (en incluant les photos)

C'est extrèmement simple ! Déplacez les dossiers et c'est bon !
