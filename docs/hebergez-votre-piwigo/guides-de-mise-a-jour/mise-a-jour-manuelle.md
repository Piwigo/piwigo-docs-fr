# Mise à jour manuelle

Cette procédure de mise à jour est valable pour toutes les versions supérieures ou égales à 1.4. Pour une version plus ancienne, demandez de l'aide sur le forum.

!!! warning "Consultez les prérequis"
    Avant toutes choses, lisez s'il vous plait la page des Prérequis. Attention particulièrement à votre version de **PHP** / **MySQL**. Si la configuration n'est pas suffisante, n'allez pas plus loin dans le processus de mise à jour, il échouerait.

## Étape 1 - Préparation de l'archive

- [Téléchargez la dernière version de l'archive Piwigo](https://fr.piwigo.org/obtenir-piwigo)
- Sur votre ordinateur, extrayez le répertoire `piwigo`
- Supprimez le répertoire par défaut `piwigo/local`

## Étape 2 - Préparation de la base de données (Recommandé)

Sauvegardez vos tables actuelles

Si vous utilisez une version de la branche 1.7 de PhpWebGallery, vous pouvez utiliser le plugin DB Backup. Les utilisateurs des versions précédentes ou suivant devront sauvegarder leurs tables par exemple via phpMyAdmin

<figure markdown="span">
    ![](https://ressources.piwigo.com/_datas/c/v/7/cv7jpz6hf8/i/uploads/c/v/7/cv7jpz6hf8//2026/06/29/20260629172445-b7bbee28-me.webp)
    <figcaption>Options recommandées pour PhpMyAdmin</figcaption>
</figure>

## Étape 3 - Préparation des fichiers sur le serveur

!!! info "Si vous êtes déjà en Piwigo 2.1 ou plus récent, sautez à l'étape suivante."

Sauvegardez uniquement vos fichiers personnalisés ou tous les fichiers

- Téléchargez l'extension outil `Prepare 2.1 Upgrade`
- Extrayez le fichier `prep21up.php` et transférez le à la racine de votre installation Piwigo
- Ouvrez `prep21up.php` depuis votre navigateur web `http://exemple.com/photos/prep21up.php` et vous recevrez une archive `upgrade21.zip`
Sur votre ordniateur, extrayez le répertoire `local` depuis l'archive `upgrade21.zip` et placez le dans le répertoire `piwigo` (créé à [l'étape numéro 1](#etape-1-preparation-de-larchive)).

## Étape 4 - Préparation de la galerie

**Verrouillez votre galerie**

Avec Piwigo 2.3 ou une version antérieure:Configuration > Générale > Verrouiller la galerie. Après Piwigo 2.4 : Outils > Maintenance

Pour tous les utilisateurs sauf les administrateurs, lors d'un accès les anciennes versions devraient afficher quelque chose comme : “La galerie est verrouillée pour cause de maintenance. Revenir plus tard.”.

<figure markdown="span">
    ![](https://ressources.piwigo.com/_datas/c/v/7/cv7jpz6hf8/i/uploads/c/v/7/cv7jpz6hf8//2026/06/29/20260629172446-132e2d1c-me.webp)
    <figcaption>Verrouillez la galerie.</figcaption>
</figure>

## Étape 5 - Nettoyage

Supprimez tous les fichiers de votre installation actuelle 

!!! Danger "SAUF les répertoires suivants, qui ne doivent PAS être supprimés :"
    - Galleries
    - Upload
    - Plugins
    - Themes
    - Template-extension
    - Local
    - _data

## Étape 6 - Transfert FTP

Utilisez votre logiciel FTP habituel pour transférer la nouvelle version de Piwigo, c'est à dire le contenu du répertoire `piwigo` (extrait pendant [l'étape 1](#etape-1-preparation-de-larchive) et complété pendant [l'étape 3](#etape-3-preparation-des-fichiers-sur-le-serveur)), dans votre installation précédente de Piwigo

## Étape 7 - Mise à jour de la base de données

**Lancez la mise à jour.**

Dans votre navigateur Web, ouvrez le script `upgrade.php` et suivez le guide, `http://example.com/photos/upgrade.php`

<figure markdown="span">
    ![](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8//2026/06/29/20260629172446-2bb8d9d9.webp)
    <figcaption>Page de démarrage de la mise à jour.</figcaption>
</figure>

Pour éviter la mise à jour par un visiteur, vous serez invité à vous identifier.

---

Votre version précédente sera détectée et vous obtiendrez un résumé des opérations de mise à jour effectuées :

<figure markdown="span">
    ![](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8//2026/06/29/20260629172446-82c85f1c.webp)
    <figcaption>Page récapitulative de la mise à jour.</figcaption>
</figure>

Les plugins actifs avant la mise à jour seront désactivés, car ils pourraient ne pas fonctionner avec la nouvelle version et nécessiter leur propre mise à niveau spécifique.

## Étape 8 - Vérifiez le résultat de la mise à jour

Vos premiers tests pourraient prendre du temps pour vous rendre compte de tous les changements.

Comme vous le constaterez, certains de vos anciens plugins ont été intégrés au noyau (comme Plugins Manager), d'autres sont inclus avec la distribution (comme LocalFiles Editor) mais dites vous bien qu'à chaque fois qu'un plugin est désactivé, il y a une bonne raison.

D'abord, essayez de trouver une mise à jour de vos plugins, l'onglet Vérifier les mises à jour pourra vous aider.

Thèmes et templates, gardez une page d'administration ouverte dans votre navigateur pour être capable de revenir en arrière sur n'importe lequel de vos tests.

N'oubliez pas que vos membres ou visiteurs peuvent avoir un thème dans leur profil qui n'est pas compatible avec la nouvelle version. Vous devez remettre un thème compatible pour chacun d'eux dans la page utilisateurs (administration).

## Étape 9 - Déverrouillez votre galerie

Vous commencez à être à l'aise avec notre dernière version, n'oubliez pas de l'ouvrir au public 

## Étape 10 - Nettoyage après mise à jour

**Rien**

Rien ne doit être effacé après une mise à jour. Le fichier upgrade.php lui-même ne sera pas supprimé.Rappelez-vous que le message “Aucune mise à jour exigée” et le processus de connexion protègent votre galerie.
