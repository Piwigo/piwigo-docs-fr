# Gérez les propriétés et métadonnées de vos fichiers

**Cet article présente l’ensemble des possibilités offertes par Piwigo pour décrire, organiser, présenter et indexer vos fichiers avec les propriétés et les métadonnées.**

## Glossaire

Pour commencer, quelques explications!

### **Les métadonnées : c’est quoi ?**

Les métadonnées sont des informations issues du fichier d’origine. Elles sont lues et intégrées par Piwigo au moment de l’import.

Les métadonnées sont surtout importantes pour les photos. Elles sont enregistrées directement par l’appareil au moment de la prise de vue, ou bien par un logiciel de gestion de photo utilisé par le photographe.

Piwigo prend en charge deux types de métadonnées :

- **EXIF** : ces balises sont généralement utilisées pour décrire la manière dont une photo a été prise. Par exemple, les balises peuvent contenir des informations sur le modèle d'appareil photo/smartphone utilisé, l'objectif, la taille de l'ouverture, la longueur focale, la durée d'exposition, la date et l'heure, les coordonnées GPS, etc.
- **IPTC** : l'en-tête IPTC décrit le contenu de l'image. Certains appareils photo vous permettent d'enregistrer votre nom et d'autres informations relatives au droit d'auteur sur une photo numérique, à l'aide de cet en-tête. Parfois, un logiciel d'édition comme Lightroom est utilisé pour ajouter ultérieurement des informations telles que des titres, des sous-titres, des légendes, des descriptions, des mots-clés, etc.

Les métadonnées de base sont les suivantes :

- nom du fichier
- poids du fichier
- dimensions du fichier
- auteur
- date de création

De nombreuses métadonnées supplémentaires peuvent être disponibles, comme la marque de l’appareil photo, le modèle, les caractéristiques de la prise de vue, les mots-clés…

Si vous importez vos fichiers dans Piwigo depuis un logiciel externe comme Lightroom, Digikam, Shotwell ou Aperture, les métadonnées sont importées dans Piwigo depuis ces logiciels.

Par défaut, Piwigo affiche quelques métadonnées de base sur la page de la photo (dimensions, taille du fichier, etc.). Lorsque l'on clique sur l'icône « Afficher les métadonnées », des métadonnées EXIF supplémentaires sont affichées : Marque et modèle de l'appareil photo, date et heure de capture de l'image, et numéro F de l'ouverture. Piwigo n'affiche pas les métadonnées IPTC par défaut.

![Affichage des métadonnées avec le thème Modus](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-9bea2f7b.png)

Affichage des métadonnées avec le thème Modus

![Affichage des métadonnées avec le thème Boostrap Darkroom](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-90e2dfc7.png)

Affichage des métadonnées avec le thème Boostrap Darkroom

### **Les propriétés : c’est quoi ?**

Les propriétés sont des champs internes à Piwigo, qui permettent de décrire et catégoriser vos fichiers. 

Certaines propriétés sont créées par Piwigo, comme la date d’import ; d’autres sont importées depuis les métadonnées, comme la date de création (date de prise de vue) ; d’autres enfin sont choisies par vous.

Certaines propriétés peuvent être ajoutées grâce à des plugins. Le plugin Manage properties permet même de créer des propriétés personnalisées (on en reparle dans cet article).

Dans tous les cas, ces propriétés sont modifiables. Elles peuvent être affichées sur la galerie.

![Affichage des propriétés avec le thème Modus](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-63d42c46.png)

Affichage des propriétés avec le thème Modus

![Affichage des propriétés avec le thème Boostrap Darkroom](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-8c01a21d.png)

Affichage des propriétés avec le thème Boostrap Darkroom

## Gérer les métadonnées de vos photos sur Piwigo

On l’a dit, les métadonnées sont automatiquement intégrées dans Piwigo lorsque vous importez des photos.

Mais il existe quelques options à connaître pour afficher et gérer ces métadonnées.

### Affichage des métadonnées sur la galerie

**Affichage des métadonnées avec Modus**

Si vous utilisez le thème [Modus](/les-themes/le-theme-modus), une icône en forme d’appareil photo sur la page d’une photo permet d’afficher les métadonnées.

![afficher-metadonnees.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-03424eb2.png)

Si vous cliquez sur cette icône, les métadonnées s’ajoutent aux propriétés dans la section de droite.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-d03835eb.png)

Si vous souhaitez masquer l’icône d’affichage des métadonnées sur votre galerie, rendez-vous dans l’administration : menu Configuration > Options, onglet “Afficher”, section “Page de la photo” : vous pouvez alors cocher ou décocher l’option “Activer l’icône Montrer les métadonnées du fichier”.

Si vous souhaitez que les métadonnées soient toujours affichées sur votre galerie, sans que l’on ait besoin de cliquer sur cette icône, alors installez le plugin **AlwaysShowMetadata.**

**Affichage des métadonnées avec Bootstrap Darkroom**

Si vous utilisez le thème [Bootstrap Darkroom](/les-themes/le-theme-bootstrap-darkroo), les métadonnées, lorsqu’elles sont disponibles, s’affichent par défaut en dessous de la photo, dans la colonne de droite.

Elles peuvent également s’afficher dans un onglet, ou bien dans une barre latérale, selon l’option que vous aurez choisie dans la configuration de votre thème.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-26cc9774.png)

Si vous souhaitez masquer les métadonnées avec le thème Boostrap Darkroom, la seule solution et de masquer également les propriétés, via la configuration du thème, en choisissant l’option “Position des informations de l’image= Désactivé”.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-faf56793.png)

### Synchroniser les métadonnées

Sur la page d'édition d'une photo dans l'administration, un bouton vous permet de synchroniser les métadonnées d'un fichier. Cette action permet d'importer les métadonnées de vos fichiers dans votre base de données Piwigo. Normalement, cela devrait être fait automatiquement lorsque vous avez importé les fichiers dans Piwigo.

Mais cela peut être utile si les photos ont été importées par FTP et que l'étape de synchronisation a été omise.

Cela peut également être utile après un changement de configuration, pour appliquer les nouvelles configurations d'importation des métadonnées.

Si vous utilisez une galerie Piwigo auto-hébergée et que vous utilisez la synchronisation FTP pour importer vos fichiers, vous pouvez également synchroniser les métadonnées par lots via le menu « Synchroniser » de votre panneau d'administration. [En savoir plus sur la synchronisation FTP](/hebergez-votre-piwigo/import-et-synchronisation-de-photos-ftp)

### Read Metadata : Afficher toutes les métadonnées d’un fichier

Si vous souhaitez pouvoir afficher dans l’administration toutes les métadonnées d’un fichier présent sur votre galerie, vous devez installez le plugin **Read Metadata**.

L’écran de Configuration de ce plugin vous permet d’extraire les métadonnées d’un fichier, depuis son identifiant ou en le sélectionnant dans une liste déroulante.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-42bf4334.png)

### Afficher plus de métadonnées EXIF

Comme nous l'avons dit, Piwigo affiche certaines métadonnées EXIF par défaut. Mais vous pouvez afficher plus de champs EXIF si vous le souhaitez.

Si vous êtes un client piwigo.com, vous devez contacter le support.

Si vous gérez une galerie Piwigo auto-hébergée, il vous suffit d'éditer le fichier de configuration à l'aide de [LocalFiles Editor](/hebergez-votre-piwigo/modifier-la-configuration-locale-avec-localfiles-editor).

- Cliquez ici pour voir comment ajouter de nouveaux champs EXIF à votre galerie Piwigo
    
    Par défaut, voici les champs EXIF affichés.
    
    ```php
    $conf['show_exif_fields'] = array(
      'Make',
      'Model',
      'DateTimeOriginal',
      'COMPUTED;ApertureFNumber'
      );
    ```
    
    Pour afficher plus de champs EXIF, tout ce que vous avez à faire est d'ajouter leurs clés dans votre fichier de configuration avec LocalFiles Editor. En insérant l'exemple de code ci-dessous dans votre plugin de configuration, vous ajouterez quelques données supplémentaires pour les appareils photo :
    
    ```php
    $conf['show_exif_fields'] = array(
      'DateTimeOriginal',
      'Make',
      'Model',
      'ExposureProgram',
      'FocalLengthIn35mmFilm',
      'FNumber',
      'ExposureTime',
      'ISOSpeedRatings',
      'Flash',
      'WhiteBalance',
      'UserComment'
      );
    ```
    
    Pour voir toutes les métadonnées EXIF disponibles, utilisez le plugin Read Metadata présenté dans le chapitre précédent.
    
    Si vous ne souhaitez pas afficher les métadonnées EXIF dans votre galerie, ajoutez le code suivant à votre fichier de configuration :
    
    ```php
    $conf['show_exif'] = false;
    ```
    

### Afficher les métadonnées IPTC

Comme nous l'avons dit, Piwigo n'affiche pas les métadonnées IPTC par défaut. Mais c'est possible !

Si vous êtes un client piwigo.com, vous devez contacter le support.

Si vous gérez une galerie Piwigo auto-hébergée, il vous suffit d'éditer les fichiers de configuration en utilisant [LocalFiles Editor.](/hebergez-votre-piwigo/modifier-la-configuration-locale-avec-localfiles-editor)

- Cliquez ici pour voir comment afficher les champs IPTC dans votre galerie Piwigo
    
    Ajoutez ce paramètre à votre fichier de configuration à l'aide de LocalFiles Editor.
    
    ```php
    $conf['show_iptc'] = true;
    ```
    
    Vous devez ensuite choisir les champs à afficher. Voici un exemple :
    
    ```php
    $conf['show_iptc_mapping'] = array(
      'iptc_creator'         => '2#080',
      'iptc_title'           => '2#005',
      'iptc_headline'        => '2#105',
      'iptc_description'     => '2#120',
      'iptc_keywords'        => '2#025',
      );
    ```
    
    Pour voir toutes les métadonnées IPTC disponibles, il suffit d'utiliser le plugin Read Metadata présenté plus haut dans cette page.
    

### Mapping des métadonnées et des propriétés

Par défaut, les métadonnées EXIF et IPTC peuvent être affichées sur la page de la photo, elles ne peuvent pas faire l'objet d'une recherche.

Si vous le souhaitez, vous pouvez associer certaines métadonnées à des propriétés Piwigo, afin qu'elles puissent être utilisées pour rechercher et trier les photos dans votre galerie. Par exemple, le champ EXIF « Modèle » peut être ajouté dans les tags, si vous souhaitez filtrer les photos par modèle d'appareil photo.

Si vous êtes un client piwigo.com, vous devez contacter le support pour le faire.

Si vous gérez une galerie Piwigo auto-hébergée, il vous suffit d'éditer le fichier de configuration en utilisant LocalFiles Editor.

- Cliquez ici pour voir comment associer les métadonnées EXIF aux propriétés.
    
    Par défaut, la métadonnée EXIF « DateTimeOriginal » est importée comme date de création dans Piwigo grâce au paramètre de configuration suivant.
    
    ```php
     $conf['use_exif_mapping'] = array('date_creation' => 'DateTimeOriginal' ); 
    ```
    
    Vous pouvez ajouter d'autres options de mapping en ajoutant de nouvelles lignes à ce paramètre.
    
    Cet exemple importe des commentaires dans la propriété description :
    
    ```php
    $conf['use_exif_mapping'] = array(
      'date_creation'        => 'DateTimeOriginal',
      'comment'              => 'UserComment',
      );
    ```
    
    Cet exemple importe les modèles d'appareils photo en tant que tags :
    
    ```php
    $conf['use_exif_mapping'] = array(
      'date_creation'        => 'DateTimeOriginal',
      'tags'                 => 'Model',
      );
    ```
    
- Cliquez ici pour savoir comment associer les métadonnées IPTC aux propriétés.
    
    Exemple de mapping qui importe les métadonnées IPTC (souvent ajoutées avec Adobe Lightroom) dans les champs Piwigo correspondants :
    
    ```php
    $conf['use_iptc_mapping'] = array(
      'author'          => '2#080',
      'name'            => '2#005',
      'comment'         => '2#120',
      'keywords'        => '2#025',
      );
    ```
    

### Liste intégrale des métadonnées EXIF et IPTC

Vous souhaitez connaître l’intégralité des métadonnées EXIF et IPTC, et paramétrer Piwigo de façon avancée pour les afficher ? Lisez l’article ci-dessous.

[Métadonnées EXIF et IPTC pour utilisateurs avancés](/importer-et-gerer-les-photos/gerez-les-proprietes-et-metadonnees-de-vos-fichiers/mtadonnes-exif-et-iptc-pour-utilisateurs-avancs)

### Write Metadata : Remplacer les métadonnées par les propriétés

Si vous souhaitez remplacer certaines métadonnées IPTC des fichiers importés sur votre galerie par les informations inscrites dans les propriétés Piwigo (titre, description, auteur, tags), vous devez installez le plugin **Write Metadata.**

!!! info
    Si vous êtes client d’une offre piwigo.com, ce plugin n’est accessible qu’à partir de l’offre Équipe.


### Exif View : Traduire les valeurs EXIF de vos photos

Si vous souhaitez pouvoir traduire les valeurs EXIF dans la langue de la galerie, vous devez installer le plugin **Exif View**.

### IPTC from Mac : Régler des problèmes de caractères spéciaux dans vos métadonnées

Si vous voyez des caractères étranges dans les métadonnées IPTC de vos photos, vous pouvez installer le plugin IPTC from Mac, qui convertit Ies données IPTC écrites en MacRoman vers un encodage UTF-8.

## Gérer les propriétés sur Piwigo

### Modifier les propriétés d’un fichier

Contrairement aux métadonnées, c’est à vous de définir dans Piwigo les propriétés de vos fichiers. Vous pouvez les modifier lorsque vous modifiez une photo dans l’administration.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-14089b76.png)

!!! info
    Pour en savoir plus sur l’édition de photo, lisez les articles suivants :
    
    * [Modifier ou supprimer une photo](/importer-et-gerer-les-photos/modifier-ou-supprimer-une-photo)
    * [Gestion par lot : Modifier et gérer une sélection de photos](/importer-et-gerer-les-photos/gestion-par-lot-modifier-et-gerer-une-selection-de-photos)


Par défaut, voici les propriétés et informations proposées par Piwigo pour qualifier un fichier.

### **Titre**

C’est le nom de la photo qui sera affiché sur la galerie. Selon votre thème et les paramétrages choisis, le titre pourra être affiché à plusieurs endroits sur votre galerie.

Par défaut, le nom est créé à partir du nom du fichier, mais vous pouvez le modifier.

Le nom d’une photo permet de la retrouver facilement grâce au moteur de recherche : c’est donc un paramètre important.

### **Auteur**

Cette propriété permet de citer l’auteur, par exemple le photographe à l’origine de la photo. C’est un champ libre de type texte qui pourra être affiché sur la galerie.

### **Date de création**

Par défaut, la date de création est importé à partir des *métadonnées* du fichier. 

Pour une photo, ce sera généralement la date de prise de vue ; pour un autre type de fichier, ce sera la date de création du fichier.

Lorsque vous éditez une photo, vous pouvez cliquer sur “Vider” pour laisser cette propriété vide, ou bien modifier la date si la date affichée par défaut ne vous convient pas.

### **Albums associés**

Les albums associés ne sont pas une propriété à proprement parler même si ils apparaissent dans la liste des propriétés d’une photo.

Il s’agit de l’album ou des albums dans lesquels cette photo est présente.

Pour rappel, dans Piwigo, un fichier peut être présent dans plusieurs albums.

Lorsque vous éditez une photo, pour retirer la photo d’un album, cliquez sur la croix au niveau du nom de l’album.

Pour ajouter la photo à un autre album, cliquez sur le bouton “Ajouter”.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-c21f4867.png)

Une fenêtre s’ouvre qui liste les albums existants. Elle liste les albums existants et permet de rechercher l’album de votre choix. Cliquez sur + pour ajouter la photo à l’album choisi. Vous pouvez également créer un nouvel album en cliquant sur “Mode création”.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-7b9083b0.png)

Une fois la sélection d’album effectuée, vous revenez sur la page d’édition de la photo. N’oubliez pas de cliquer sur le bouton “Enregistrer les paramètres” pour sauvegarder vos modifications !

Pour en savoir plus sur les albums, [lisez cette série d’articles](/organiser-les-albums).

### **Représentation des albums (vignette d’un album)**

Lorsque vous éditez une photo, cette propriété affiche la liste des albums pour lesquels la photo en cours a été choisie comme vignette principale.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-c562a159.png)

Si une photo est choisie pour représenter un album, c’est elle qui s’affichera sur votre galerie dans la liste des albums. 

Par défaut, la photo choisie par Piwigo pour représenter un album dans la liste est la première photo importée dans l’album, mais vous pouvez très bien le modifier si vous le souhaitez.

A noter qu’une photo n’a pas besoin d’être associée à un album pour le représenter.

Pour en savoir plus sur les albums, [lisez cette série d’articles](/organiser-les-albums).

### **Tags**

Pour organiser et décrire vos photos, vous pouvez les associer à des tags (que l’on peut aussi appeler mots-clés, ou étiquettes).

Les tags s’affichent sur la page d’une photo sur votre galerie au même niveau que les propriétés, et sont utilisables pour rechercher une photo répondant à un ou plusieurs critères.

Lorsque vous éditez une photo dans l’administration, le champs Tags fonctionne de la même façon que le champ Album, à une différence près : si vous saisissez le nom d’un tag qui n’existe pas encore, vous pouvez le créer directement en appuyant sur la touche Entrée.

![fr-edition-photo-tags.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-38db2556.png)

Pour en savoir plus sur les tags, [lisez cette série d’articles](/gerer-les-tags)

### **Description**

La propriété Description permet d’afficher un texte de présentation de votre photo sur votre galerie.

En général, la description s’affiche en dessous de votre photo sur votre galerie.

Par défaut, la description s’affiche également en infobulle lorsque vous passez la souris sur la photo.

![fr-description-photo-galerie.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-eefabe72.png)

Si vous utilisez le thème [Bootstrap Darkroom](/les-themes/le-theme-bootstrap-darkroo), vous pouvez choisir d’afficher la description des photos à la place de leur titre sur la page d’un album.

Pour mettre en forme le texte de votre description (mettre un texte en gras, ajouter un lien….), vous avez deux possibilités.

- Si vous connaissez le langage HTML, vous pouvez insérer des balises HTML dans vos descriptions.
- Vous pouvez également installer le plugin **FCKEditor**, qui ajoute un éditeur HTML visuel au champ Description de l’éditeur de photo.

![fr-description-fckeditor.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-9f459681.png)

Pour en savoir plus sur FCKEditor, [lisez cet article](/administrer-piwigo/plugins-pour-les-administrateurs).

Pour pouvoir traduire les descriptions en plusieurs langues, utilisez le plugin **Extended Description**.

Pour en savoir plus sur la traduction des contenus avec Extended Description, [lisez cet article](/personnaliser-ma-galerie/gerer-les-langues-disponibles-sur-votre-galerie).

### **Qui peut voir cette photo (niveau de confidentialité)**

Cette propriété permet de définir le Niveau de confidentialité d’un fichier.

Par défaut, le niveau de confidentialité est fixé sur “Tout le monde” : si l’album est privé, la photo sera affichée pour tous les utilisateurs identifiés et habilités à voir l’album.

![fr-edition-photo-condidentialité.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-8ab37948.png)

Mais vous pouvez définir un niveau de confidentialité plus fin en choisissant une autre option dans la liste déroulante. 

![fr-edition-photo-condidentialité2.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-85a849c3.png)

!!! Warning "Attention"
    Attention : cette fonctionnalité ne doit pas être confondue avec les permissions par album ! C’est une fonctionnalité avancée de Piwigo qui peut être un peu complexe à appréhender.


Pour en savoir plus sur les niveaux de confidentialité, [lisez cet article](/les-utilisateurs/les-niveaux-de-confidentialite).

### Affichage des propriétés sur votre galerie

**Affichage des propriétés avec le thème Modus**

Si vous utilisez le thème [Modus](/les-themes/le-theme-modus), les propriétés s’affichent sur la section à droite de la photo. 

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-bd1fe79a.png)

**Affichage des propriétés avec le thème Bootstrap Darkroom**

Si vous utilisez le thème [Bootstrap Darkroom](/les-themes/le-theme-bootstrap-darkroo), les propriétés s’affichent par défaut en dessous de la photo, dans la colonne de droite.

Elles peuvent également s’afficher dans un onglet, ou bien dans une barre latérale, selon l’option que vous aurez choisie dans la configuration de votre thème.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-26cc9774.png)

Si vous souhaitez masquer les propriétés avec le thème Bootstrap Darkroom, vous pouvez le faire via la configuration du thème, en choisissant l’option “Position des informations de l’image= Désactivé”.

**Afficher / masquer les propriétés sur la galerie**

Si vous souhaitez choisir les propriétés qui seront affichées ou non sur votre galerie à côté de chaque fichier, rendez-vous dans l’administration : menu Configuration > Options, onglet “Afficher”, section “Propriétés de la photo”.

![fr-proprietes-galerie.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-24efbb1d.png)

Pour accéder à davantage d’options d’affichage des propriétés, vous pouvez utiliser le plugin **Manage Properties Photos** (voir chapitre suivant).

## Personnaliser les propriétés avec des plugins

### Manage Properties : Personnaliser les propriétés

Vous souhaitez ajouter des propriétés personnalisées sur votre galerie, ou encore modifier l’ordre d’affichage des propriétés existantes ? 

Pour cela, vous devez installer le plugin **Manage Properties Photos**.

!!! info
    Si vous êtes client d’une offre piwigo.com, ce plugin n’est accessible qu’à partir de l’offre Entreprise.

Une fois Manage Properties Photos activé sur votre galerie, rendez-vous dans la configuration du plugin.

L’onglet Propriétés liste les propriétés existantes et permet d’en créer une nouvelle.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-15442db0.png)

Cet onglet permet de masquer des propriétés existantes : il suffit de passer la souris sur une propriété pour afficher l’option “Masquer”.

Il est également possible modifier l’ordre d’affichage des propriétés sur la page Photo de votre galerie, par glissé-déposé.

**Créer une nouvelle propriété personnalisée**

Pour créer une propriété personnalisée, cliquez sur “Créer une nouvelle propriété à la photo”.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-53a18a55.png)

Le champ Libellé permet de choisir le nom de la nouvelle propriété.

Vous devez également choisir le type de propriété. Plusieurs types sont proposés :

**Text**

Choisissez le type text si la valeur de votre propriété est un texte libre (exemple : un nom, une ville…).

**Select**

Choisissez le type select si la valeur de votre propriété est une liste de choix contraints.

Le bouton Ajouter un champ permet d’ajouter les choix possibles pour votre propriété. Dans l’exemple ci-dessous, on a créé une propriété Établissement avec 4 valeurs possibles.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-b6270350.png)

Dans l’édition d’une photo, les administrateurs peuvent choisir la valeur de cette propriété grâce à une liste déroulante.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-827d8692.png)

**Radio**

Le type Radio a le même fonctionnement que le type Select. Il permet également de choisir la valeur de la propriété à partir d’une liste prédéfinie, mais la saisie est présentée à l’aide d’un bouton radio plutôt qu’une liste déroulante.

Dans l’exemple ci-dessous, on a créé une propriété “Droit à l’image” avec deux options : oui et non.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-e3b3be78.png)

**Date**

Le type date est à utiliser pour les propriétés de type date. Il permet de définir la valeur de la propriété à partir d’un outil calendrier.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-6af0967e.png)

**Types EXIF et IPTC**

Les propriétés de type EXIF et IPTC permettent de créer une propriété personnalisée, qui reprendra la valeur d’une métadonnée EXIF ou IPTC.

Pour utiliser ce type de propriété, vous devez d’abord aller dans l’onglet Configuration du plugin. Vous devez choisir une photo de référence dans votre galerie qui possède bien des métadonnées EXIF ou IPTC, en saisissant son identifiant numérique.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-7f4862e3.png)

Cela permettra au plugin de charger la liste des EXIF et IPTC disponibles sur votre galerie.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-15ac79f4.png)

Par exemple, vous pouvez créer une propriété Hauteur qui reprendra automatiquement la valeur de la métadonnée EXIF “Height” enregistrée dans votre photo ; la hauteur sera affichée sur la page photo de votre galerie en pixel.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-24a97117.png)

**Voir les propriétés personnalisées**

Une fois que vous avez créé une propriété personnalisée, vous pouvez définir sa valeur pour chaque photo dans l’onglet “Propriétés supplémentaires” de l’éditeur de photo.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-90cf5a66.png)

Les propriétés personnalisées sont également accessibles depuis le gestionnaire de lot, lorsque vous sélectionnez un lot de photos et choisissez l’action “Changer les propriétés des photos”.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-d10dd311.png)

Sur la galerie, si vous avez choisi d’afficher les propriétés personnalisées, elle s’afficheront parmi les autres propriétés. N’oubliez pas que le premier onglet de la configuration du plugin Custom Properties permet de modifier l’ordre d’affichage des propriétés et de masquer celles de votre choix.

![propriete-perso.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-28471200.png)

**Options de Manage Properties**

L’onglet Configuration de Manage Properties offre plusieurs possibilités que nous listons ci-dessous.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-e8f7f3ba.png)

- **Ajouter un champ pour supprimer automatiquement les photos à une date**

Cliquez sur cette option pour créer un champ de type “Date”, qui permet, pour chaque photo, de choisir une date à laquelle elle sera automatiquement supprimée.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-1238d221.png)

- **Déplacer la description dans la table des propriétés**

Cliquez sur cette option pour que la description de la photo s’affiche parmi les propriétés de votre galerie. Vous retrouvez le champ Description dans la liste des propriétés de la configuration du plugin, et pourrez ainsi choisir son ordre d’affichage.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-c308e452.png)

- **Montrer l’ID de l’image**

Cliquez sur cette option pour afficher l’identifiant numérique de chaque fichier parmi les propriétés sur la galerie. Cette fonctionnalité est également disponible avec le plugin **Show Photo Identifier**.

- **Maximum de champs pour les balises "select" et les boutons "radio”**

Définissez ici le nombre de valeurs maximales possibles pour les propriétés de type “liste déroulante” et “bouton radio”.

- **La photo de référence pour les exifs et IPTC**

Voir chapitre précédent.

### Properties Mass Update : Mettre à jour les propriétés en masse depuis un fichier .csv

Vous souhaitez mettre à jour les propriétés d’un lot de photos depuis un tableau existant (par exemple, un fichier Excel) ? 

Pour cela, vous devez installer le plugin **Properties Mass Update**.

!!! info
    Si vous êtes client d’une offre piwigo.com, ce plugin n’est accessible qu’à partir de l’offre Entreprise.


### Show Photo Identifier : Afficher l’identifiant de la photo parmi les propriétés

Le plugin **Show Photo Identifier** permet d’afficher l’identifiant numérique d’une photo sur la page de la photo, parmi ses métadonnées et propriétés.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-3db4f695.png)

### Download Counter : Afficher le nombre de téléchargements parmi les propriétés

Le plugin **Download Counter** permet de comptabiliser le nombre de téléchargements d’une photo et de l’afficher sur la page de la photo, parmi les métadonnées et propriétés de la photo.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-800d45b4.png)

### **Expiry Date :** Ajouter une date d’expiration à un fichier

Il peut être nécessaire d’ajouter une date d’expiration à un fichier, pour gérer la date de validité d’une licence, ou encore la validité des droits à l’image associés à une photo.

Pour cela, vous devez installer le plugin **Expiry Date**.

!!! info
    Si vous êtes client d’une offre piwigo.com, ce plugin n’est accessible qu’à partir de l’offre Entreprise.


Une fois le plugin activé, un nouveau champ “Date d’expiration” apparaît sur chaque photo, ainsi que dans le gestionnaire de lot.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-146790b5.png)

La date d’expiration s’affiche à côté des autres propriétés de votre galerie.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-79d6194e.png)

Si vous souhaitez masquer la date d’expiration sur la galerie, vous devez utiliser le plugin **Manage Properties Photo** (voir plus haut sur cette page).

Mais que se passe-t-il lorsque la date d’expiration arrive ?

Pour le définir, rendez vous dans la configuration du plugin Expiry Date.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-2b45667c.png)

Vous avez plusieurs possibilités :

- **Choisir ce que Piwigo doit faire lorsque les photos arrivent à expiration**

Le plugin Expiry Date permet de choisir ce qui se passe lorsque la date d’expiration arrive : ne rien faire, supprimer automatiquement les photos, archiver automatiquement les photos.

Archiver les photos permet de les déplacer automatiquement vers l’album de votre choix, que vous aurez créé au préalable. Cela permet de rendre les photos expirées inaccessibles, sans pour autant les supprimer de votre galerie.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-4ab02106.png)

- **Notifier les utilisateurs ayant téléchargé la photo**

Cochez cette option pour envoyer un email prévenant les utilisateurs ayant téléchargé une photo lorsqu’elle est arrivée à expiration.

Si vous cochez cette option, d’autres choix apparaissent.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-9cd690db.png)

Vous pouvez ainsi envoyer un mail avant la date d’expiration ou uniquement à la date précise, et ajouter un message personnalisé dans l’email envoyé.

- **Notifier les administrateurs lorsqu’une photo est expirée**

Vous pouvez envoyer un email aux administrateurs dès lors que la date d’expiration d’une photo est arrivée?

Comme pour les notifications aux utilisateurs, vous pouvez envoyer un mail avant la date d’expiration ou uniquement à la date précise, et ajouter un message personnalisé dans l’email envoyé.

### Copyrights : Gérer les copyrights d’un fichier

Vous pouvez avoir besoin d’associer un droit d’auteur, ou copyright à une image ou une vidéo, afin de préciser sur votre galerie les droits relatif à ce fichier (exploitation, commercialisation…).

Pour cela, vous devez installer le plugin **Copyrights**.

Une fois le plugin Copyright activé, une nouvelle propriété “Droit d’auteur” apparaît lorsque vous éditez une photo dans l’administration.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-cc901053.png)

Si une valeur est choisie parmi la liste des copyrights disponibles, elle s’affiche sur votre galerie avec les autres propriétés.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-b486b74b.png)

Par défaut, le plugin est installé avec une liste de droits d’auteurs prédéfinis mais vous pouvez les supprimer, les modifier, ou en créer de nouveau dans la configuration du plugin Copyrights.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-89fac6c7.png)

La description d’un copyright s’affiche lorsque l’on passe la souris dessus sur la galerie, et le lien s’ouvre dans un nouvel onglet lorsque l’on clique sur le copyright.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-dcbd73ae.png)

### Edit Filename : Modifier le nom d’un fichier

Par défaut dans l’éditeur de photo, vous pouvez modifier dans Piwigo le titre du média tel qu’il est affiché sur votre galerie, mais pas le nom du fichier source.

Si vous avez besoin de le faire, vous devez installer le plugin **Edit Filename**.

Une fois ce plugin activé, le nom du fichier source est modifiable dans la page d’édition d’une photo.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-d41f0cb7.png)

Sommaire de l’article

---

← Précédent

Suivant →

[Les formats multiples](/importer-et-gerer-les-photos/les-formats-multiples)
