# Prérequis

Piwigo a besoin d'un hébergement web pour fonctionner. Pour une
solution de galerie photo "clef en main" (installation, hébergement,
mises à jour, sauvegardes...), ou si vous souhaitez simplement essayer
Piwigo sans l'installer, [ouvrez un compte d'essai gratuit sur
Piwigo.com](https://fr.piwigo.com/inscription).

### Le minimum requis {#le-minimum-requis .pwg-guides-h3}

-   un serveur web comme Apache ou Nginx
-   MySQL 5.6+ ou MariaDB 10.1+. MySQL 5.0 fonctionne mais n'est plus
    officiellement maintenue.
-   PHP 8.2+. Piwigo peut fonctionner avec PHP 7.4+ mais ces anciennes
    versions ne sont plus officiellement supportées et vous exposent à
    des failles de sécurité. Voir [officially PHP supported
    versions](https://www.php.net/supported-versions.php)
    (en anglais).
-   Une bibliothèque graphique: ImageMagick est recommandé pour ses
    performances et sa qualité d'image mais GD, souvent fourni avec
    PHP, peut également faire l'affaire.
-   un logiciel client FTP sera nécessaire pour télécharger les fichiers
    (netinstall ou package complet): l'équipe Piwigo recommande
    FileZilla comme logiciel client FTP, car il est gratuit comme Piwigo
    et compatible avec Windows, Mac et Linux.
-   Assez d'espace disque pour vos photos: en plus des photos que vous
    téléchargez, Piwigo stockera les "tailles multiples" dans un
    répertoire cache de votre serveur.

### Prérequis optionnels {#prérequis-optionnels .pwg-guides-h3}

-   exiftool est requis pour le plugin Write Metadata et d'autres
    plugins qui manipulent les métadonnées EXIF/IPTC
-   ffmpeg est requis pour le plugin VideoJS lors de la création du
    "poster" (image représentant la vidéo)
