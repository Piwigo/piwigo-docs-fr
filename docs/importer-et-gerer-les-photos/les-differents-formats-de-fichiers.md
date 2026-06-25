# Les différents formats de fichiers

**Quels sont les formats de fichiers compatibles avec Piwigo ? On vous explique tout !**

## Clients piwigo.com et auto-hébergement : les différences

Pour commencer, les choses sont légèrement différentes selon que vous ayez un compte sur [piwigo.com](http://piwigo.com) ou que vous hébergiez vous-même votre Piwigo.

- J’héberge moi-même mon Piwigo
    
    Si vous hébergez vous-même votre Piwigo, par défaut vous ne pourrez importer que des fichiers de type jpg, jpeg, png, et gif. Mais ce paramétrage est facile à changer en modifiant la configuration locale avec LocalFiles Editor ([en savoir plus](../hebergez-votre-piwigo/modifier-la-configuration-locale-avec-localfiles-editor)).
    
    De plus, si vous hébergez vous-même votre Piwigo, vous devez installer et activer le plugin VideoJS pour pouvoir importer sur votre galerie des fichiers multimédia (video et audio).
    
- J’ai un compte Piwigo hébergé sur piwigo.com
    
    Si vous avez créé un compte sur piwigo.com, la gestion des fichiers images, video et audio est activée par défaut.
    
    Mais pour pouvoir accepter les formats de fichier “Premium” (PDF, PSD, AI…), vous devrez opter pour un abonnement Équipe, Entreprise, ou VIP.
    

## **Fichiers images**

Piwigo vous permet d'importer des fichiers images, qui sont lisibles dans un navigateur web. Les extensions de fichiers images supportés par Piwigo sont les suivants :

- .jpg
- .jpeg
- .png
- .gif
- .webp
- .heic

Tous ces formats sont reconnus par Piwigo, qui générera une vignette pour les images visibles dans l'administration de Piwigo ainsi que dans votre galerie.

### Précisions sur le format .gif

Piwigo permet également d'importer des GIF animés (extension de fichier .gif). Si le fichier d’origine est plus grand que la taille des miniatures sur votre galerie (par défaut, 144x144) la galerie affichera uniquement une prévisualisation du fichier GIF, créée à partir de la première image composant l'animation. Il faudra afficher l’original pour “jouer” l’animation.

### Précisions sur le format .webp

Depuis la version 14 de Piwigo, vous pouvez également importer des fichiers image au format webp.

Si vous hébergez vous-même votre Piwigo, vous pouvez l’ajouter via le plugin [LocalFiles Editor](../hebergez-votre-piwigo/modifier-la-configuration-locale-avec-localfiles-editor), en ajoutant `webp` au niveau du paramètre `$conf['picture_ext']` comme dans l’exemple ci-dessous.

```php
$conf['picture_ext'] = array('jpg','jpeg','png','gif','webp');
```

!!! info
    WebP est le type le plus "supporté par les navigateurs web" pour remplacer le JPEG. WebP est supporté à l'import aussi bien qu'à l'affichage, et Piwigo va générer un fichier webp pour chaque taille affichée dans votre galerie. WebP peut remplacer le JPEG avec une meilleure qualité pour un poids équivalent, remplacer les GIF animés pour une fraction du poids et même remplacer les PNG avec une compression non destructive et de la transparence.


!!! Warning "Attention"
    Pour supporter les WebP animés, vous devrez peut-être mettre à jour le système d’exploitation de votre serveur si vous utilisez un Piwigo auto-hébergé.


### Cas particulier du format HEIC

HEIC est un format d’image supporté dans Piwigo depuis la version 14. C’est le format de fichier généré par défaut sur iOS, et sur certains téléphones Android.

Les fichiers HEIC ne sont pas affichables dans un navigateur web : Piwigo génère donc une prévisualisation du fichier. 

Pour activer le support du format HEIC si vous hébergez vous-même votre Piwigo, vous devez l’ajouter via le plugin [LocalFiles Editor](../hebergez-votre-piwigo/modifier-la-configuration-locale-avec-localfiles-editor).

Si ce n’est pas déjà le cas, vous devez d’abord activer le paramètre `upload_form_all_types` comme ci-dessous.

```php
$conf['upload_form_all_types'] = true;
```

Ensuite, vous devez ajouter `heic` au niveau du paramètre `$conf['file']` comme dans l’exemple ci-dessous.

```php
$conf['file_ext'] = array_merge(
  $conf['picture_ext'],
  array('jpg','jpeg','png','gif','heic')
  );
```

!!! Warning "Attention"
    Pour supporter les fichiers HEIC, vous devrez peut-être mettre à jour le système d’exploitation de votre serveur si vous utilisez un Piwigo auto-hébergé.

## **Fichiers vidéo et audio**

Piwigo permet d'importer des fichiers audiovisuels avec les extensions suivantes :

- .mp4
- .m4v
- .webm
- .webmv
- .ogg
- .ogv
- .mp3

!!! info
    Si vous hébergez vous-même votre Piwigo, vous devez installer et activer le plugin VideoJS pour accepter ce type de fichier. Si vous êtes client d’une offre piwigo.com, ce plugin est activé par défaut.


Lorsque vous importez un fichier vidéo dans Piwigo, une vignette de prévisualisation est créée à partir de la première image de votre vidéo. La vidéo est lisible depuis votre galerie, grâce au lecteur vidéo intégré à Piwigo. Vous pouvez lire la vidéo grâce au gros bouton de lecture.

![](https://s3.amazonaws.com/helpscout.net/docs/assets/61e7cec9c1b8c85d97faea30/images/62d9457979bb3605c3949821/file-JX0mTPdLyh.png)

Lorsque vous importez un fichier audio dans Piwigo, il sera représenté sur votre galerie par l'icône ci-dessous. Le fichier audio peut être écouté depuis votre galerie, grâce au lecteur intégré à Piwigo.

![](https://s3.amazonaws.com/helpscout.net/docs/assets/61e7cec9c1b8c85d97faea30/images/62d6e0c3c74a080359c8b31a/file-aSH00yRAHB.png)

Pour activer le support des vidéos, si vous hébergez vous-même votre Piwigo, vous devez d’abord activer le paramètre `upload_form_all_types` comme ci-dessous (si ce n’est pas déjà fait) via le plugin [LocalFiles Editor](../hebergez-votre-piwigo/modifier-la-configuration-locale-avec-localfiles-editor).

```php
$conf['upload_form_all_types'] = true;
```

Vous devez ensuite ajouter les extensions souhaitées au niveau du paramètre `$conf['file_ext']` comme dans l’exemple ci-dessous.

```php
$conf['file_ext'] = array_merge(
  $conf['picture_ext'],
  array('mp4','webmv','m4v','webm')
  );
```

!!! Warning "Attention"
    Si vous utilisez une galerie auto-hébergée et que vous rencontrez des problèmes avec le téléchargement de vidéos ou la génération de vignettes, [consultez cet article](../hebergez-votre-piwigo/problemes-generation-vignettes-miniatures).

### **🎦 Cas particulier des vidéos MOV**

Si vous enregistrez des vidéos depuis un iPhone, un iPad ou depuis le logiciel Quicktime pour Apple, les fichiers générés ont une extension .mov. Ce format de fichier n'est pas compatible avec Piwigo, car il ne s’affiche pas correctement dans les navigateurs web.

Mais il existe plusieurs moyens de les transférer quand même sur Piwigo.

**Depuis l’application mobile Piwigo pour iOS**

Depuis [l'application mobile Piwigo pour iOS,](../les-applications-mobiles/lapplication-mobile-piwigo-pour-ios) vous allez pouvoir envoyer des vidéos MOV vers Piwigo. Les vidéos seront converties pendant le transfert en fichier .mp4. Elles seront donc lisibles depuis votre galerie, comme n'importe quelle autre vidéo.

**Depuis l’administration Piwigo (vous hébergez Piwigo vous-même)**

Si vous avez besoin de transférer des vidéos MOV depuis l'administration de Piwigo, c’est possible, mais par défaut, les vidéos ne sont pas visibles via le lecteur vidéo de votre galerie : il faudra les télécharger pour les visionner.

Pour que votre Piwigo accepte d’importer des fichiers .mov, vous devez modifier le paramètre `$conf['file_ext']`  et ajouter le format mov comme dans l’exemple ci-dessous avec [LocalFiles Editor](../hebergez-votre-piwigo/modifier-la-configuration-locale-avec-localfiles-editor).

```php
$conf['file_ext'] = array_merge(
  $conf['picture_ext'],
  array('mp4','webmv','m4v','webm','mov')
  );
```

Vous pouvez aussi faire le choix de convertir vos fichiers .mov au format MP4 avant de les importer dans Piwigo, ce qui a deux avantages : 

- Les vidéos seront lisibles depuis votre galerie Piwigo ;
- Leur poids sera fortement réduit.

Pour savoir comment convertir un fichier, lire le chapitre suivant.

**Depuis l’administration Piwigo (clients piwigo.com uniquement)**

Si vous êtes client d’une offre d’abonnement piwigo.com, vous pouvez demander au support la mise en place de la conversion automatique des fichiers .mov vers .mp4. 

Si nous activons cette option, les fichiers .mov importés dans Piwigo depuis l’administration seront automatiquement convertis en .mp4. Au moment du téléchargement, l’utilisateur choisira si il souhaite télécharger la version .mov ou la version .mp4.

!!! Warning "Attention"
    Attention ! Si vous choisissez d’activer cette option, cela utilise une place plus importante sur votre espace de stockage, car chaque vidéo est stockée en deux versions, et car les fichiers .mov sont très volumineux.

Vous pouvez aussi faire le choix de convertir vos fichiers .mov au format MP4 avant de les importer dans Piwigo, ce qui a deux avantages : 

- Les vidéos seront lisibles depuis votre galerie Piwigo ;
- Leur poids sera fortement réduit.

Pour savoir comment convertir un fichier, lire le chapitre suivant.

### **🎦 Convertir vos fichiers vidéo**

Si vous souhaitez importer un fichier vidéo non supporté par Piwigo (par exemple, un fichier AVI), il vous suffit de convertir vos fichiers vidéo vers le format MP4 : vous pouvez le faire avec de nombreux logiciels de montage vidéo, ou encore avec des outils gratuits en ligne [comme celui-ci](https://video.online-convert.com/fr/convertir-en-mp4).

!!! info
    Nous conseillons le format de fichier MP4 avec un codec vidéo H.264 et audio AAC. Cela permet de conserver un haut degré de qualité même quand la vidéo est compressée. Les fichiers MP4 encodés de cette façon pèsent moins lourds : ainsi, ils consomment moins d'espace de stockage, et économisent de la bande passante. Enfin, cela garantit la compatibilité avec les lecteurs vidéo.


### ⚙️ Configuration du plugin VideoJS

On l’a vu, c’est le plugin VideoJS qui permet de gérer les fichiers vidéo dans Piwigo. Ce plugin utilise le lecteur vidéo open source VideoJS.

La configuration du plugin VideoJS vous donne accès à un certain nombre d’options.

- Afficher le nombre de vidéos dans votre galerie
- Choisir le comportement du lecteur vidéo (préchargement ou pas de la vidéo, lecture automatique, lecture en boucle, affichage ou non des boutons de lecture/pause, volume, langue du lecteur).
- Personnaliser le style du lecteur vidéo en choisissant parmi les styles disponibles ou en ajoutant du code CSS personnalisé
- Définir la hauteur maximum de la vidéo
- etc.

Vous trouverez une documentation détaillée du plugin VidéoJS [sur sa page GitHub](https://github.com/Piwigo/piwigo-videojs/wiki).

## ⭐️ Autres formats de fichiers

Ces formats de fichier sont réservé aux clients d’une offre Équipe, Entreprise ou VIP sur piwigo.com, et aux utilisateurs qui hébergent eux-même leur Piwigo.

- Fichiers PDF
- Fichiers SVG
- Fichiers EPS
- Fichiers TIF et TIFF
- Fichier PSD (générés par Adobe Photoshop)
- Fichiers AI (générés par Adobe Illustrator)

Pour ce type de fichiers, Piwigo génère une prévisualisation qui les rend consultables dans l'administration et dans votre galerie.

Pour activer le support de ces fichiers, si vous hébergez vous-même votre Piwigo, vous devez d’abord activer le paramètre `upload_form_all_types` comme ci-dessous (si ce n’est pas déjà fait) via le plugin [LocalFiles Editor](../hebergez-votre-piwigo/modifier-la-configuration-locale-avec-localfiles-editor). 

```php
$conf['upload_form_all_types'] = true;
```

Vous devez ensuite ajouter les extensions souhaitées au niveau du paramètre `$conf['file_ext']` comme dans l’exemple ci-dessous.

```php
$conf['file_ext'] = array_merge(
  $conf['picture_ext'],
  array('pdf','ai','psd','eps')
  );
```

!!! Warning "Attention"
    Si vous utilisez une galerie auto-hébergée et que vous rencontrez des problèmes avec la génération de vignettes pour les fichiers PDF, ou la visualisation des fichiers AI, PSD, HEIC, TIF ou TIFF, [consultez cet article](../hebergez-votre-piwigo/problemes-generation-vignettes-miniatures).


### **Cas particulier des fichiers PDF dans Piwigo**

Pour les fichiers PDF, Piwigo génère un aperçu en extrayant la première page et en la convertissant en image. Cette image est affichée dans l'album.

Depuis Piwigo 15, sur la page du fichier, Piwigo embarque un lecteur PDF qui permet de lire le fichier.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-a0043554.png)

Vous pouvez également cliquer sur l’icône « Télécharger ce fichier » : vous téléchargerez le document sur votre ordinateur.

## **📄 Autres formats de documents**

Si vous avez besoin d'importer d'autres formats de fichiers dans un compte hébergé sur piwigo.com (Excel, Word, Open Office...), vous pouvez en faire la demande en contactant le support si vous êtes un client piwigo.com, ou en modifiant votre fichier de configuration si vous hébergez vous-même votre Piwigo.

Ces fichiers ne seront pas lisibles directement sur Piwigo, mais ils pourront être téléchargés pour être ouverts ensuite dans le logiciel qui convient.

Piwigo n’étant pas capable de créer une prévisualisation du document, il affichera une icône générique à la place.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-a13f0242.png)

Vous pouvez aussi, grâce au plugin **Photo Update**, ajouter votre propre prévisualisation.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-9ae534a3.png)

## Formats multiples : proposez plusieurs formats pour une même image

Si vous souhaitez pouvoir proposer différents formats de fichiers pour une même image sur votre galerie (par exemple, un format JPG, un format PNG et un format PSD), c’est possible ! Pour cela, vous devez activer l’option Formats Multiples.

[En savoir plus sur les formats multiples](les-formats-multiples)

!!! info
    Si vous êtes client d’une offre piwigo.com, cette fonctionnalité n’est accessible qu’à partir de l’offre Entreprise.


## Embedded Videos: **Embarquez sur votre galerie des fichiers hébergés sur d'autres plateformes (Youtube...)**

Vous souhaitez afficher sur votre galerie des contenus déjà hébergés ailleurs, comme par exemple, des vidéos issues de votre chaîne Youtube ?

C'est possible grâce au plugin **Embedded Videos**.

Avec ce plugin, vous pourrez afficher dans les albums de votre choix des vidéos issues des plateformes externes comme Youtube, Vimeo ou Dailymotion.

Une fois le plugin activé, pour ajouter une vidéo externe à votre galerie, rendez vous dans la configuration du plugin.

Vous pouvez alors choisir dans quel album ajouter une vidéo.

Par défaut, la page permet d’ajouter une vidéo depuis les plateformes d’hébergement Youtube, Dailymotion, Vimeo, Wat et Wideo, en donnant simplement l’URL de la vidéo.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-405669c9.png)

Vous pouvez choisir l’album dans lequel vous souhaitez que la vidéo soit visible, ainsi que d’autres paramètres (taille de la vidéo, récupérer la description et les tags, etc).

L’onglet “Ajouter un code d’intégration” vous permet d’ajouter directement un code “embedded” depuis une autre plateforme. Il ne doit pas être utilisé pour les plateformes Youtube, Dailymotion, Vimeo, Wat et Wideo.

L’onglet Configuration du plugin permet de définir certains paramètres globaux du plugin:

- taille par défaut des vidéos
- démarrage automatique ou non
- récupération automatique de la description et des tags de la vidéo
- paramètres du lecteur (pour Vimeo et Dailymotion)

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-595432d2.png)

### Problème connu avec le plugin Embedded Videos

Si vous hébergez vous-même votre Piwigo et que vous avez un message d’erreur en utilisant ce plugin, ajoutez le code suivant dans votre fichier de configuration via le plugin LocalFiles Editor.

```php
$conf['show_php_errors'] = E_ALL ^ E_DEPRECATED ^ E_WARNING;
```

## Panorama : Gérer les images panoramiques

Les panoramas sont des photos classiques mais dont la largeur est particulièrement importante par rapport à la hauteur. Ce sont souvent des photos prises avec un appareil en mode “panoramique”.

Ces photos sont gérées sans problème par Piwigo, mais leur format particulier n’est pas spécialement mis en valeur.

![Une photo panoramique](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-eefe015e.png)

Une photo panoramique

Si vous souhaitez offrir aux visiteurs de la galerie la possibilité de naviguer au sein d’une photo panoramique, vous pouvez utiliser le plugin **Panoramas**.

Une fois ce plugin activé, il applique aux photos que vous aurez choisies un mode de visualisation différent, comme vous pouvez le voir ci-dessous.

![panorama.gif](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-72f8f3da.gif)

Les paramètres de configuration du plugin vous donnent de nombreuses possibilités de personnalisation.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-fe138684.png)

Pour définir quelles photos doivent être présentées en mode Panorama (180 ou 360°), Piwigo s’appuie sur leur nom.

Par défaut, les photos doivent intégrer _180 ou _360 dans leur nom pour être affichées en mode Panorama, mais c’est  paramétrable.
