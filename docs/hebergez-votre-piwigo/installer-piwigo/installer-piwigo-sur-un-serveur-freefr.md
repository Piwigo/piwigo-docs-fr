# Installer Piwigo sur un serveur free.fr

<aside>
⚠️

La solution d’hébergement gratuit “Pages perso” accessible avec un abonnement Internet Free n’est pas adaptée à l’hébergement de Piwigo. Nous ne recommandons pas cette solution d’hébergement. 

</aside>

## Pourquoi vous ne devriez pas installer Piwigo chez Free

Le fournisseur d'accès à internet Free propose une solution d'hébergement web gratuite avec 10 Go de stockage appelée “Pages Perso”. Elle était autrefois accessible à tout le monde, mais depuis février 2024, elle est réservée aux abonnés Free.

Cette solution a le mérite d'être gratuite sauf mais elle est très limitée :

- À l’heure où nous écrivons ces lignes, le serveur PHP des pages perso Free est bloqué sur PHP 5.6, une version obsolète de PHP qui n’est pas compatible avec la dernière version de Piwigo ;
- Pas de possibilité d’installer les librairies ImageMagick et ffmpeg, ce qui pose des problèmes pour la génération des miniatures et empêche d’héberger des vidéos ;
- De nombreuses fonctions PHP sont désactivées.

Ainsi, l’installation de Piwigo sur un hébergement “free.fr” est une procédure complexe et hasardeuse, qui oblige à utiliser une version obsolète de Piwigo ou de modifier le code source du logiciel. Nous ne garantissons pas son fonctionnement.

## Ressources pour installer Piwigo chez Free

Toutefois, si vraiment vous insistez pour héberger Piwigo chez Free, voici quelques ressources qui pourraient vous aider.

- [Tuto d’installation de Piwigo sur hébergement free.fr](https://fr.piwigo.org/doc/doku.php?id=utiliser:apprendre:install:installation:free.fr)
- [\[Forum\] installation version 14.1.0 chez free](https://fr.piwigo.org/forum/viewtopic.php?id=30365) (janvier 2024)
- [Existe t-il un hebergeur gratuit autre que Free ?](https://fr.piwigo.org/forum/viewtopic.php?id=30429) (mars 2024)
