# Installation Manuelle

!!! abstract "Prérequis de l'installation manuelle"
    Ce guide couvre uniquement l'installation de piwigo, pour consulter les dépendences nécéssaire consulter le guide sur les [prérequis](prerequis.md)

## Étape 1 - Téléchargement de l'archive

Commencez par [télécharger le logiciel](https://fr.piwigo.org/obtenir-piwigo), qui se présente sous la forme d'une archive au format Zip, et décompressez le.

## Étape 2 - Dépôt des fichiers sur l'espace web

Transfer the archive content to your web server with any FTP client.

!!! info
    L'équipe Piwigo recommande FileZilla comme client FTP car, tout comme Piwigo, il est gratuit et compatible avec Windows et Linux.

Exécutez le client FTP, et connectez-vous au serveur. Avec FileZilla, effectuez une connexion rapide :

- Adresse du serveur 
- Identifiant de connexion
- Mot de passe

Cliquez sur connexion rapide. Vous êtes maintenant connecté sur votre espace web.

![](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8//2026/06/26/20260626155500-5ba173ff.webp)

1.  Créez un répertoire “photos” sur votre espace web.
2.  Rendez-vous dans le répertoire ou vous avez désarchivé les fichiers de `piwigo-2.0.x`.
3.  Sélectionner Tout les fichiers et transférez les sur votre serveur dans le répertoire `photos`.

## Étape 3 - Paramétrages

!!! info
    Vous pouvez aussi installer Piwigo à la racine de site Web, le répertoire `photos` n'est pas obligatoire. Indépendamment du nom de répertoire que vous choisissez, il est déconseillé de mettre le numéro de version de la galerie dans le nom du répertoire.

Lorsque tous les fichiers sont déposés, rendez-vous à l'adresse de votre espace web là ou vous avez déposé les fichiers, par example `http://example.com/photos` Piwigo détectera que rien n'est encore installé et vous redirigera vers la page d'installation.

<figure markdown="span">
    ![](https://ressources.piwigo.com/_datas/c/v/7/cv7jpz6hf8/i/uploads/c/v/7/cv7jpz6hf8//2026/06/26/20260626155501-48828109-me.webp)
    <figcaption>Page d'installation</figcaption>
</figure>

Vous devez maintenant renseigner les informations concernant le serveur MySQL et celles du compte qui vous servira à administrer la galerie.

Remplissez les paramètres de connexion à la base de données MySQL, tels que fournis par votre fournisseur d'hébergement Web :

- Adresse du serveur 
- Votre identifiant de connexion (Attention, il se peut que votre hébergeur vous fournisse des identifiants de connexion différents pour la connexion à votre site web et celle du serveur MySQL).
- Mot de passe
- Le nom de la base de données
- Le préfixe des tables de Piwigo 

!!! note ""
    Généralement les hébergeurs fournissent une base de donnée par utilisateur, mais il est possible de créer plusieurs tables dans une base. Afin de ne pas générer de conflits avec d'autres logiciels, ou si vous souhaitez installer plusieurs galeries sur le même site, les noms des tables sont préfixés, par défaut, avec `piwigo_`. Vous pouvez modifier ce préfixe selon vos besoin, seuls les caractères alphanumériques sont autorisés (et pas d'espaces).

Pour la création du compte administrateur de la galerie, sont à renseigner :

- L'identifiant du compte à renseigner selon votre choix
- Le mot de passe associé à cet identifiant, à saisir une seconde fois pour confirmation
- L'adresse e-mail permettant aux visiteurs de rentrer en contact avec vous

Cliquez sur “démarrez l'installation”.
Si tout se déroule correctement ou s'il y a un problème, vous serez informé

<figure markdown="span">
    ![](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8//2026/06/26/20260626155501-7b2c5f28.webp)
    <figcaption>L'installation s'est correctement déroulée</figcaption>
</figure>

## Étape 4 - Après l'installation

Une fois l'installation terminée, vous pouvez vous rendre sur la galerie. Identifiez-vous pour accéder à la partie administration.

<figure markdown="span">
    ![](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8//2026/06/26/20260626155501-7cf8f4d0.webp)
    <figcaption>La galerie est installée</figcaption>
</figure>

---

!!! abstract "Articles complémentaires"
    - **[Installer Piwigo sur un disque dur réseau](../installer-piwigo/installer-piwigo-sur-un-disque-dur-reseau)**
    - **[Installer Piwigo sur un serveur free.fr](../installer-piwigo/installer-piwigo-sur-un-serveur-freefr)**
    - **[Installer Piwigo en local](../installer-piwigo/installer-piwigo-en-local)**
    - **[Installer Piwigo sur Debian](../installer-piwigo/installer-piwigo-sur-debian)**
    - **[Installer Piwigo sur un NAS](../installer-piwigo/installer-piwigo-sur-un-nas)**
