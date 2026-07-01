# Import et synchronisation de photos FTP

!!! info
    À lire aussi : [Importer des photos dans Piwigo](../importer-et-gerer-les-photos/importer-des-photos-dans-piwigo)


## Introduction

Si vous utilisez un Piwigo installé sur votre propre serveur (ou un serveur géré par votre organisation), vous pouvez transférer des répertoires de votre ordinateur vers votre Piwigo en utilisant le protocole FTP.

Cette méthode, historiquement la plus ancienne, est plus longue à mettre en œuvre. Elle est destinée aux utilisateurs avancés,  disposant d’une organisation de travail stable.

Si vous possédez une grosse photothèque, c'est peut-être une méthode d'ajout de photos faite pour vous.

Si vous préférez, il existe d’autres méthodes pour importer vos photos : pour en savoir plus, visitez la section [Importer des photos dans Piwigo](../importer-et-gerer-les-photos/importer-des-photos-dans-piwigo).

!!! Warning "Attention"
    Cette méthode d’import n’est accessible que pour les Piwigo auto-hébergés : elle n’est donc pas disponible pour les clients d’une offre Piwigo Cloud.

## Avantages et inconvénients de cette méthode

| Avantages | Inconvénients |
| --- | --- |
| ✅ Parfait pour les grandes galeries | ⚠️ Nécessite de savoir préparer ses photos avant une publication pour le web |
| ✅ Convient pour le chargement de fichiers autres que photographiques | ⚠️ Aucune flexibilité pour renommer/déplacer vos photos et albums |
| ✅ Liberté dans la création de répertoires sur votre serveur | ⚠️ Utilisation d'un logiciel de transfert FTP |
|  | ⚠️ Obligation de synchroniser Piwigo avec vos fichiers |

## Transférer un premier album

1. Créez un répertoire sur votre ordinateur.
2. Copiez des photos à l'intérieur de ce répertoire.
    
!!! Warning "Attention"
    Le nom des répertoires et des fichiers ne doit contenir que des lettres, des chiffres et les caractères `-`, `_` ou `.`

    **Pas d'espace ou de caractères accentués**.

    
3. Avec un client FTP, copiez le répertoire dans le répertoire  `./galleries/` de votre installation de Piwigo.
4. Connectez-vous à votre galerie Piwigo, rendez-vous dans l’administration, menu Outils > Synchronisation. Cochez les options Répertoires + fichiers, Synchroniser les métadonnées et ne pas cocher “Simuler uniquement”.

Bravo ! Un album a été créé sur votre galerie.

## Comprendre la synchronisation

Copier des fichiers sur votre serveur avec votre logiciel FTP ne suffit pas pour que vos photos soient visibles de tous. Piwigo a besoin de *faire le point* sur les changement intervenus. Vous venez d'ajouter des photos, il faut maintenant dire à votre galerie d'afficher vos photos : c’est à cela que sert la **synchronisation**.

Ainsi, à chaque fois que vous voulez transférer des fichiers dans Piwigo en FTP, vous créerez un sous-répertoire de `./galleries/` et vous y déposerez vos éléments (en taille adaptée au web). 

Vous aurez optionnellement besoin de miniatures à placer dans un sous-répertoire de celui créé à l'instant. 

Puis, à partir de l'administration en ligne, vous devrez ***synchroniser*** la base de données afin de lui faire reconnaître vos nouveaux éléments.

## **Organisation des répertoires et des fichiers**

Les répertoires représentant les albums se trouvent dans le répertoire `./galleries/` de votre installation de Piwigo.

Ci-dessous, voici l'arbre des répertoires d'une très petite galerie.

```
galleries
|-- mariage
|   |-- ceremonie
|   |   |-- entree
|   |   |   |-- arrivee-de-paul.jpg
|   |   |   +-- arrivee-de-virginie.jpg
|   |   +-- sortie
|   |       |-- sortie-enfants-honneur.jpg
|   |       +-- sortie-de-paul-et-virginie.jpg
|   +-- cocktail
|       |-- discours001.jpg
|       |-- discours002.jpg
|       +-- discours003.jpg
+-- voyage-de-noces
|   |-- hotel.png
|   |-- video-decollage-avion.avi
|   +-- pwg_representative
|       +-- video-decollage-avion.jpg
+-- seance-photographe
    |-- img0001.jpg
    |-- img0002.jpg
    +-- pwg_format
        |-- img0001.cr2
        |-- img0001.cmyk.jpg
        |-- img0001.zip
        |-- img0002.cr2
        +-- img0002.cmyk.jpg
```

Quelques explications pour mieux comprendre ce schéma :

- A l'exception de "pwg_representative" et "pwg_format", chaque répertoire dans `./galleries/` génère un album. Le nombre de niveaux (profondeur) n'est pas limité.
- Fondamentalement, une photo est représentée par un fichier. Pour Piwigo, un fichier peut être une photo si son extension figure dans la liste du paramètre de configuration `file_ext` (voir fichier include/config.inc.php). Un fichier peut être une photo si son extension figure dans la liste du paramètre de configuration `picture_ext`.
- Les éléments autres que les photos (sons, fichiers texte, tout ce que vous voulez...) sont représentés par défaut par une icône correspondant à l'extension du nom du fichier. De façon optionnelle, un représentant peut être associé (voir le fichier video-decollage-avion.avi dans l'exemple).
- Formats multiples : vous pouvez proposer une photo dans plusieurs formats. Dans cet exemple, il y a 3 formats supplémentaires pour img0001.jpg. Vous pouvez activer cette fonctionnalité en ajoutant `$conf['enable_formats'] = true;` à votre configuration locale et en définissant une liste de formats, comme `$conf['format_ext'] = array('cmyk.jpg', 'cr2', 'zip');` [En savoir plus sur les formats multiples](../importer-et-gerer-les-photos/les-formats-multiples)

!!! Warning "Attention"
    *Attention* : le nom d'un répertoire ou d'un fichier ne doit être composé que de lettres, de chiffres, de "-", "_" ou ".". Pas d'espace ou de caractères accentués.

!!! info
    *Conseil* : un album peut contenir des photos et des sous-albums à la fois. Néanmoins, il est fortement conseillé pour chaque album de choisir entre contenir des photos **ou bien** des sous-albums.


- Une fois que les fichiers sont correctement placés dans les répertoires, se rendre sur l'écran Administration » Outils » Synchroniser.

## Synchronisation des fichiers

Dès lors que vous choisissez de transférer vos fichiers par FTP, la synchronisation est une étape indispensable dès lors que vous *ajouter/renommez/déplacer/supprimer* le *moindre élément* dans vos photos.

!!! Warning "Attention"
    Cette fonctionnalité est inutile si vous transférer vos fichiers par un autre moyen.


Dans l’administration, rendez-vous dans Outils > Synchronisation.

Vous accéder alors à l’écran ci-dessous.

![fr-synchronisation.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-46e5cbc9.png)

Cette page permet de choisir les paramètres de synchronisation et de lancer une synchronisation.

Voici les options proposées :

### **Synchroniser la structure des fichiers avec la base de données**

C’est ce qui permet de dire à Piwigo : “hé ho, il y a de nouveaux fichiers, il serait temps d'aller les voir et de les prendre en compte”.

3 options sont proposées :

- Rien : dans ce cas, on ne synchronisera rien. C’est ce que vous cocherez si vous souhaitez uniquement synchroniser les métadonnées.
- Répertoire uniquement : Avec cette option, on ne synchronisera que les répertoires. C'est utile si vous n'avez pas besoin de synchroniser l'ensemble de votre galerie.
- Répertoires + fichiers : Avec cette option, non seulement vous synchroniserez les dossiers mais aussi les éléments qui les composent. Si vous cochez cette option, de nouvelles options apparaissent.
    
    ![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-4186aded.png)
    
    Afficher un maximum d’informations vous permettra d’obtenir des statistiques sur les résultats de la synchronisation.
    
    Ajouter les nouvelles photos au panier permettra d’ajouter dans votre panier toutes les photos ajoutées (par exemple, pour les traiter ensuite grâce à la [gestion par lot](../importer-et-gerer-les-photos/gestion-par-lot-modifier-et-gerer-une-selection-de-photos)).
    
    “Qui peut voir ces photos” permet de définir le [niveau de confidentialité](../les-utilisateurs/les-niveaux-de-confidentialite) des photos ajoutées.
    

### **Synchroniser les informations des photos de la base de données à partir des méta-données des fichiers**

Cette section vous propose une option et deux sous-options :

- Synchroniser les métadonnées (filesize, width, height) : permet de choisir si on synchronise ou non les métadonnées des fichiers.
    - Même les photos déjà synchronisées : si vous cocher cette option, vous allez mettre à jour même les éléments qui sont déjà présents sur votre galerie. Utile lorsque vous avez modifié les métadonnées de vos photos.
    - Écraser les données existantes avec des données vides : si vous cochez cette option, vous allez remplacer les anciennes informations par des nouvelles, même si elles sont vides.

### **Simulation**

Piwigo permet de ne pas effectuer de changement tout de suite afin que vous puissiez vérifier le bon déroulement de la synchronisation.

Comme son nom l'indique, cette fonction va donc simuler le résultat de la synchronisation.

!!! Warning "Attention"
    Si vous souhaitez vraiment synchroniser vos fichiers, vérifiez que cette case n’est pas cochée !


### **Traiter uniquement un album**

Dans cette zone, il vous est possible de naviguer dans vos albums et vous sous-albums afin d'aider Piwigo à trouver les éléments à synchroniser. Il est inutile (voir parfois même dangereux) de synchroniser toute une galerie lorsque l'on connaît le bon répertoire à synchroniser.

Une petite option nommée ”*Rechercher dans les sous-albums*” est là pour vous permettre de ne pas avoir besoin d'affiner trop trop votre recherche du dossier à synchroniser. L'expérience vous dira comment l'utiliser à bon escient.

## Erreurs fréquentes

En cas de problèmes, Piwigo vous informera des erreurs qu'il rencontrera.

Voyons ensemble ces erreurs.

- **PWG-UPDATE-1**: Le nom des répertoires et des fichiers ne doit être constitué *que* de lettres, de chiffres, de ”-”, “_” et ”.” Donc pas de caractères *exotiques* et accentués.
- **PWG-ERROR-NO-FS**: Le fichier ou répertoire ne peut pas être accessible (soit il n'existe pas, soit l'accès est refusé).
- **PWG-ERROR-VERSION**: La version de `create_listing_file.php` sur le site distant et Piwigo doit être la même.
- **PWG-ERROR-NOLISTING**: le fichier listing.xml est introuvable sur le site distant. Ce fichier est généré en choisissant la commande “générer le listing” dans le gestionnaire de sites.

## **Informations complémentaires**

- **pwg_representative** : (Usage facultatif) pour les éléments non image. Exemple: un fichier zip : comme le fichier zip n'est pas une image, c'est l'image jpg du même nom qui sera affichée dans la galerie, le zip sera téléchargeable via l’icône de téléchargement.

## **Conseils**

- Ne pas décocher *Rechercher dans les sous-albums*.
- Garder des noms simples, il y a des restrictions (dues au web, cf. ci-dessous).
- Règles de typographie, Noms des répertoires et images, c'est à dire :
    - pas d'espace et pas d'accents
    - donc uniquement des lettres, des chiffres, des -, des _, ou encore des ….
- Préparer vos éléments avant de les placer sur le serveur.

## Synchronisation unitaire

Il est possible, depuis l’administration de Piwigo, de re-synchroniser les métadonnées d’une photo en cliquant sur l’icône “synchroniser les métadonnées” depuis l’écran d’édition d’une photo.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-7f6b4084.png)
