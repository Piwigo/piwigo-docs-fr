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

### Étape 5 : Édité le fichier `./local/config/database.inc.php`

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

Si vous souhaitez déplacer votre galerie vers un sous-répertoire (par exemple déplacer votre galerie de `https://example.com/photos` vers `https://example.com/media`) il vous suffit de déplacer les dossiers et d'aller dans \[Administration > Outils > Maintenance\], puis sélectionnez :

1.  Mettre à jour les informations des albums
2.  Mettre à jour les informations des photos
3.  Purger les modèles compilés
