# Installation Docker

!!! abstract "Prérequis de l'installation docker"
     Ce guide part du principe que vous pouvez vous connecter à votre serveur avec SSH et que vous avez déjà installé Docker. Si ce n'est pas le cas, installez Docker en suivant la [documentation officielle de docker (eng)](https://docs.docker.com/engine/install/)

## Étape 1 - Installation du conteneur docker

Connectez vous à votre serveur et créez un dossier `Piwigo` puis Téléchargez le fichier `compose.yaml` du répertoire [Piwigo/piwigo-docker](https://github.com/Piwigo/piwigo-docker)

!!! tip "Vous pouvez utiliser la commande curl suivante pour le faire depuis votre terminal :"
    ```
    curl -O "https://raw.githubusercontent.com/Piwigo/piwigo-docker/refs/heads/main/compose.yaml"
    ```

Créez un fichier texte appelé `.env`, avec les champs suivants :

=== "Champs requis"

    ```bash
    piwigo_port=8080
    db_user_password=
    timezone=
    ```

=== "Explications des champs"

    ```bash
    piwigo_port= # Le port exposé par docker
    db_user_password= # Mot de passe de la base de donnée
    timezone= # La Timezone du conteneur 
    PIWIGO_UID= # l'ID de l'utilisateur qui possédera le dossier Piwigo
    PIWIGO_GID= # l'ID du groupe qui possédera le dossier Piwigo
    ```
    
=== "Valeurs par défaults"
    ```bash
    piwigo_port=8080
    db_user_password=
    timezone=UTC
    PIWIGO_UID=1000
    PIWIGO_GID=1000
    ```

=== "Exemple de configuration"

    ```bash
    piwigo_port=10004
    db_user_password=Nkhcfnfk5GmpnLGIFoIDJqRFPW22C7PlyEUYVaB1lkte5Dn0wOQs3TI4wom1E4A6
    timezone=Europe/Paris
    PIWIGO_UID=1001
    PIWIGO_GID=1004
    ```

!!! tip "Conseil" 
    Vous pouvez utiliser la commande suivante pour créer un mot de passe fort valide : 
    ```bash
    printf $(tr -dc '[:alnum:]' </dev/urandom | head -c64)"\n" 
    ```
    
Démarrez le conteneur avec la commande suivante : `docker compose up -d`.  
Vous pouvez consulter les logs avec  `docker compose logs`.

## Étape 2 - Configuration du Proxy inverse (reverse proxy)

Il est fortement recommandé d'utiliser Piwigo Docker derrière un proxy inverse comme Nginx.

!!! info
    Vous pouvez héberger Piwigo à la racine de votre site web, sur un sous-domaine et/ou un sous-répertoire. Peu importe votre choix, il est recommandé de ne pas utiliser les numéros de version de Piwigo dans votre URL.


Des exemples de configurations sont disponibles ci-dessous : 

!!! Warning ""

    Gardez en tête que Docker ignore vos règles pare-feu.
    
    Si vous avez modifié le port dans le fichier `.env`, vous aurez également besoin d'adapter le paramètre `proxy_pass` dans les exemples. 

=== "Héberger sur un domaine ou sous domaine"

    ```nginx
    server {
      listen 80;
      server_name my_domain.tld;
      location / {
        proxy_pass http://127.0.0.1:8080/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
      }
    }
    ```

=== "Héberger sur un sous-chemin"

    Si vous voulez héberger votre Piwigo dans un sous-chemin, par exemple: `mon_domaine.fr/gallery`, vous aurez besoin de passer le sous-chemin au conteneur en ajoutant le champ `proxy_set_header X-Forwarded-Prefix /gallery`

    ```nginx
    server {
      listen 80;
      server_name my_domain.tld;
      location /gallery/ {
        proxy_pass http://127.0.0.1:8080/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Prefix /gallery;
      }
    }
    ```

## Étape 3 - Paramétrages

Une fois votre conteneur démarré et votre reverse-proxy configuré, ouvrez un navigateur web et allez sur l'URL de votre Piwigo. Piwigo détectera automatiquement qu'il n'est pas encore configuré et vous redirigera vers la page d'installation.

<figure markdown="span">
    ![](https://ressources.piwigo.com/_datas/c/v/7/cv7jpz6hf8/i/uploads/c/v/7/cv7jpz6hf8//2026/06/29/20260629150900-80ede7d4-me.webp)
    <figcaption>Page d'installation</figcaption>
</figure>

Remplissez la section des paramètres de connexion a la base de données MySQL avec les informations suivantes :

- Adresse du serveur : `piwigo-db:3306`
- Votre identifiant de connexion : `piwigodb_user`
- Mot de passe : Utilisez le mot de passe noté dans le fichier `.env`
- Le nom de la base de données : `piwigodb`
- Le préfixe des tables de Piwigo : `piwigo_` 

Pour la création du compte administrateur de la galerie, sont à renseigner :

- L'identifiant du compte à renseigner selon votre choix
- Le mot de passe associé à cet identifiant, à saisir une seconde fois pour confirmation
- L'adresse e-mail permettant aux visiteurs de rentrer en contact avec vous

Cliquez sur “démarrez l'installation”

## Étape 4 - Après l'installation

Une fois l'installation terminée, vous pouvez vous rendre sur la galerie. Identifiez-vous pour accéder à la partie administration.

<figure markdown="span">
    ![](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8//2026/06/26/20260626155501-7cf8f4d0.webp)
    <figcaption>La galerie est installée</figcaption>
</figure>
