# Installer Piwigo sur un disque dur réseau

<aside>
⚠️

Cette doc a été proposé sur le forum communautaire en 2010. Si elle n’est plus à jour, merci de nous en faire part.

</aside>

Ci-dessous une recette pour expliquer comment utiliser un disque dur en réseau avec Piwigo.

- OS Linux Fedora 11, avec Apache, MySQL,  et PhpMyAdmin
- Piwigo dans sa dernière version
- Disque dur réseau additionnel (DDR), connecté par Ethernet, proposant entre autres le protocole SMB (CIFS/Samba) (disque d2 Network dans mon cas)
- Toutes les opérations sont à effectuer sous root
- La paire machin/truc désigne le couple administrateur/password du DDR.

a) Installer samba-client sur le serveur de Piwigo (PWG) par :

```php
yum install samba-client 
```

b) Créer (par ex.) un dossier sur PWG par :

```php
mkdir /mnt/CIFS
```

c) Monter le DDR (adresse IP: 192.168.0.zz) par :

```php
/sbin/mount.cifs //192.168.0.zz/share /mnt/CIFS -o user=machin,password=truc,uid=apache,gid=apache,file_mod=0777,dir_mod=0777 
```

(s'il faut démonter le DDR, utiliser : `umount.cifs /mnt/CIFS`)

d) Supposons que la branche de l'install Piwigo que l'on souhaite installer sur le DDR soit le dossier upload

e) Créer (par ex.) un dossier déporté sur le DDR par :

```php
mkdir -p /mnt/CIFS/vous/Storage/Piwigo/upload
```

Le dossier ainsi créé devrait avoir cette tête-là :

```php
ls -ld /mnt/CIFS/vous/Storage/Piwigo/upload
```

drwxrwxrwx. 1 apache apache 0 sept. 18 00:43 /mnt/CIFS/vous/Storage/Piwigo/upload

f) Se déplacer à la racine de l'install Piwigo par :

```php
cd /var/www/html/pwg01 
```

g) renommer temporairement le dossier upload :

```php
mv upload SAVE-upload 
```

h) Créer un lien symbolique sur PWG par :

```php
ln -s /mnt/CIFS/vous/Storage/Piwigo/upload 
```

i) Faire une sauvegarde de sécurité pour l'arborescence upload par :

```php
tar czf tar-upload.tgz SAVE-upload 
```

j) Déplacer l'arborescence upload vers le DDR par :

```php
mv SAVE-upload/* /mnt/CIFS/vous/Storage/Piwigo/upload/ 
```

k) Configurer SElinux par :

```php
setenforce 0 //(pour passer SELinux en mode 'permissif')
setsebool -P httpd_use_cifs on //(peut-être redondant avec le précédent)
//Ajouter cette ligne à la place de 'SELINUX=enforcing' dans /etc/selinux/config
SELINUX=permissive
sestatus //(pour vérifier)
SELinux status: enabled
SELinuxfs mount: /selinux
Current mode: permissive
Mode from config file: permissive
Policy version: 24
Policy from config file: targeted
semanage boolean -l | grep httpd_use_cifs //(pour vérifier)
httpd_use_cifs → ouvert Allow httpd to access cifs file systems
```

l) Configurer Apache en adaptant/ajoutant/vérifiant les directives suivantes dans /etc/httpd/conf/httpd.conf

```php
<Directory ”/var/www/html/”>
         Options  Indexes  FollowSymLinks\\
         AllowOverride Options\\
         Order allow,deny\\
         Allow from all\\
</Directory>
php_admin_value safe_mode off
EnableSendfile Off
EnableMMAP Off
```

Remarque : la configuration d'open_basedir n'est pas nécessaire.

m) Redémarrer Apache par :

```php
service httpd restart 
```

Et cela devrait être bon ! Certains trucs devraient paraître superflus aux puristes, mais j'ai préféré fournir tous mes tuyaux, en mettant ceinture ET bretelles. Vous devriez pouvoir regarder vos photos, et faire au moins des mises à jour avec pLoader.

*Source* : [http://fr.piwigo.org/forum/viewtopic.php?pid=152129#p152129](http://fr.piwigo.org/forum/viewtopic.php?pid=152129#p152129)