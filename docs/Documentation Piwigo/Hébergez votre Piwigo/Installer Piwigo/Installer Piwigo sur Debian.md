# Installer Piwigo sur Debian

## Debian 12

Voici les packages nécessaires pour une installation sur une machine Debian 12.

```jsx
apt-get install php8.2-gd php8.2-curl php8.2-imap php8.2-xml php8.2-mbstring php8.2-zip php8.2-mysql php-bcmath imagemagick libjpeg-progs libimage-exiftool-perl curl ffmpeg mediainfo poppler-utils
```

En complément, voici un tutoriel créé par un membre de la communauté Piwigo.

[**How To Install Piwigo on Debian 12**](https://idroot.us/install-piwigo-debian-12/#google_vignette)

- Anciennes versions
    
    ### **Debian 10 (PHP 7)**
    
    rooter en linux su -
    
    chemin idconfig export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
    
    installation curl apt-get install curl
    
    Ensuite, installez ImageMagick [https://packages.debian.org/buster/imagemagick](https://packages.debian.org/buster/imagemagick)
    
    Enfin installer GD apt-get installer php-gd
    
    ### **Debian 9 (PHP 7)**
    
    Il faudra installer ces paquets :
    
    - php-xml
    - php-mbstring