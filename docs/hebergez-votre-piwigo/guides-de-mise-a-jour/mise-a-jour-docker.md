

!!! info "Ce guide concerne uniquement les utilisateurs de l'image Docker officielle."
    Si vous utilisez une autre image, comme celle de LinuxServer, référez-vous à leur documentation.
    Si vous voulez migrer vers l'image officielle, [consultez ce guide (ENG)](https://github.com/Piwigo/piwigo-docker/wiki/Migration-Guide-from-the-LinuxServer)

## Étape 1 - Rechercher des mises à jour

Le numéro de version du conteneur sera toujours le même que la version de Piwigo qu'il contient. À partir de la version 16.3.0, il y a une lettre à la fin pour dénoter les mises à jour spécifiques au conteneur.

=== "Pour les conteneurs version 16.3 et supérieure"

    Vous pouvez consulter les mises à jour via l'interface :
    
    <figure markdown="span">
      ![](https://ressources.piwigo.com/i?/uploads/c/v/7/cv7jpz6hf8//2026/06/29/20260629172514-64cac366-la.webp)
      <figcaption>Exemple de liste de mises à jour disponibles</figcaption>
    </figure>
    
=== "Pour les conteneurs version 16.2 et inférieure"

    Consultez la liste des tags sur [dockerhub](https://hub.docker.com/r/piwigo/piwigo/tags) ou sur [GitHub](https://github.com/Piwigo/piwigo-docker/pkgs/container/piwigo)

## Étape 2 - Faire une sauvegarde des données

Pour garantir des mises à jour sans risque, il est recommandé de faire une sauvegarde de sa base de données et de ses fichiers.

Naviguer dans le répertoire de votre fichier `compose.yaml` et arrêter le conteneur avec la commande `docker compose down`

### Sauvegarder sa base de données

Vous pouvez utilisez la commande suivante, en modifiant le nom du conteneur pour correspondre à celui que vous utilisez, pour crée une copie de votre base de donnée :

```bash
docker exec -it piwigo-db-1 mariadb-dump -u piwigodb_user -p "piwigodb" | tee db_dump.sql 
```

### Sauvegarder ses photos et fichiers de configurations

Pour faire une sauvegarde de toutes vos photos et fichier de configurations, il suffit de copier les dossiers suivants : `galleries`, `upload` et `local` présent dans `./piwigo-data/piwigo/`.

!!! Warning "Les dossiers `galleries` et `upload` contiennent vos photos et peuvent donc être volimineux" 

### Sauvegarder les fichiers `compose.yaml` et `.env`"

Renommez le fichier `compose.yaml` et faite une copie de votre fichier `.env` (par exemple rajoutant `.bak` à la fin)

???+ tip "Vous pouvez utilisez les commandes suivantes pour renomé le faire automatiquement avec un horodatage."

    ```bash
    mv compose.yaml "compose.yaml_$(date '+%F-%H-%M-%S').bak" 
    cp .env "env$(date '+%F-%H-%M-%S').bak"
    ```

## Étape 3 - Télécharger le nouveau fichier compose et mettre à jour le fichier `.env`

- Télécharger la version du fichier `compose.yaml` qui correspond a votre tag de mise à jour de [l'étape 1](#etape-1-rechercher-des-mises-a-jour)

!!! tip ""

    Vous pouvez utilisez la commande ci dessous en remplaçant `<NUMÉRO DE VERSION>` par votre tag (ex: `16.4a`)

    ```bash
    PWG_DOCKER_VERSION="<NUMÉRO DE VERSION>"; curl -O "https://raw.githubusercontent.com/Piwigo/piwigo-docker/refs/tags/v$PWG_DOCKER_VERSION/compose.yaml" 
    ```
    
- Consultez la page de mise à jour du fichier d'environement sur [Github (eng)](https://github.com/Piwigo/piwigo-docker/wiki/Environment-file-updates) et suivez chaques modification entre votre version actuelle et le tag que vous avez choisit.

??? example "Exemple de mis à jour de la version 15.6 à la version 16.3c"

    `.env` avant la mise à jour :

    ```
    piwigo_port=8080
    db_user_password=4JKQplDWaePjjwqiuAmcWWrwY3oqxWtxRs2XCEObf1wRdD2boDa6VA804kzQm2kj
    ```
    
    rajout de la ligne timezone pour être conforme avec la version `15.7.0` et l'ID/GID  pour la version `16.3.0c` 

    ```
    piwigo_port=8080
    db_user_password=4JKQplDWaePjjwqiuAmcWWrwY3oqxWtxRs2XCEObf1wRdD2boDa6VA804kzQm2kj
    timezone=Europe/Paris
    PIWIGO_UID=1004
    PIWIGO_GID=1001
    ```

## Étape 4 - Mettre à jour et redémarrer le conteneur

Récupérez la nouvelle image avec la commande `docker compose pull` et redémarrez vos conteneurs avec `docker compose up  -d`.  
Vous pouvez consulter les journaux avec `docker compose logs` pour vous assurez que tout fonctionne.
