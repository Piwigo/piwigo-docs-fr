# Installer Piwigo en local

Il est possible d’installer Piwigo en local sur votre ordinateur, même si ce n’est pas très utile à moins que vous ne soyez développeur.

## Installer un serveur local

Tout d’abord, vous devez installer sur votre ordinateur un serveur web.

***Sous Windows :***

- [EasyPHP](http://www.easyphp.org/)
- [wampserver](http://www.wampserver.com/)

***Sous Linux*** : 

Vous devrez installer un serveur LAMP sur votre machine.

- [pour Ubuntu](http://doc.ubuntu-fr.org/lamp)
- [pour Archlinux](https://www.linuxtricks.fr/wiki/arch-installer-un-serveur-lamp)
- [pour Debian](https://wiki.debian.org/LaMp)

## Installer Piwigo

Vous devez ensuite suivre la [procédure manuelle](../guides-installation/installation-manuelle.md) d’installation de Piwigo, et copier les fichiers d’installation dans votre répertoire web `www`.

## Configuration de votre base de données

Lors de l’installation de Piwigo, vous devez saisir les identifiants d’accès à votre base de données qui sont stockés dans le fichier `database.inc.php`.

Les paramètres à saisir pour bien configurer la connexion au serveur local dépendent de la méthode utilisée. Pour EasyPHP, en fonction de votre version, le mot de passe peut être: 'mysql' ou 'rien_du_tout'

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-06cfb1c9.png)

Le contenu de votre fichier `./piwigo/local/config/database.inc.php` ressemblera à ça :

```php
<?php
$conf['dblayer'] = 'mysql';
$conf['db_base'] = 'piwigo';
$conf['db_user'] = 'user';
$conf['db_password'] = 'xxxxxx';
$conf['db_host'] = 'localhost';
 
$prefixeTable = 'piwigo_';
 
define('PHPWG_INSTALLED', true);
define('PWG_CHARSET', 'utf-8');
define('DB_CHARSET', 'utf8');
define('DB_COLLATE', '');
 
?>
```

## Gestion des EXIF

La gestion des EXIF n'est pas activée par défaut par EasyPHP. Pour l'activer suivez les étapes suivantes :

- Fermez complètement EasyPHP
- Dans `..\EasyPHP\apache\php.ini` recherchez `;extension=php_exif.dll` et supprimer la ligne.
- Recherchez `extension=php_mbstring.dll` et ajoutez sous cette ligne une nouvelle ligne avec `extension=php_exif.dll`
- Sauvegardez.
- Redémarrez EasyPHP.

Avec linux il faut compiler php avec l'option `—enable-EXIF`

## Ressources utiles

Voici quelques liens pour vous aider en cas de problème.

- [\[Forum\] Piwigo et easyphp](https://fr.piwigo.org/forum/viewtopic.php?pid=182719)
- [\[Forum\] Réinstaller ma galerie en local sous Windows EasyPHP](https://fr.piwigo.org/forum/viewtopic.php?id=30486)
- [\[Vidéo\] Installer Piwigo en local sur Unbutu (EN)](https://www.youtube.com/watch?v=EGC6BBlQ_FQ)
