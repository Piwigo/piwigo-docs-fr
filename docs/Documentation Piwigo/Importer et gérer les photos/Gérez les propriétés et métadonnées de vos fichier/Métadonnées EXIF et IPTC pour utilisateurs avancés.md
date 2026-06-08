# Métadonnées EXIF et IPTC pour utilisateurs avancés

<aside>
💡

Lisez d’abord le chapitre suivant pour tout comprendre aux métadonnées EXIF et IPTC : [**Gérer les métadonnées dans Piwigo**](../Gérez les propriétés et métadonnées de vos fichier.md)

</aside>

Vous souhaitez personnaliser l’affichage des métadonnées EXIF et IPTC dans Piwigo ?

Comme vous avez pu le lire dans l’article [Gérer les métadonnées dans Piwigo](../Gérez les propriétés et métadonnées de vos fichier.md), vous pouvez personnaliser les métadonnées affichées ou non dans Piwigo en modifiant la configuration à l’aide du plugin [LocalFiles Editor](../../Hébergez votre Piwigo/Modifier la configuration locale avec LocalFiles E.md). Vous pouvez également “mapper” certaines métadonnées avec les propriétés de Piwigo.

Vous trouverez dans cet article des informations utiles pour configurer Piwigo en ce sens.

## Fichier de Configuration Locale

Cliquez ci-dessous pour afficher tous les éléments de la configuration locale qui concernent les métadonnées, avec des explications en français.

- Afficher le fichier
    
    ```jsx
    // +-----------------------------------------------------------------------+
    // |                           LES META-DONNEES                            |
    // +-----------------------------------------------------------------------+
     
    //          CHAPITRE 1er
    //                              LES CHAMPS EXIF
     
    // Le visiteur pourra faire apparaître les méta-données EXIF sur picture.php
    // en cliquant sur l'icône appropriée.
    // show_exif: [false] - [true];
    // Si vous choisissez "false" les champs ne seront pas affichés.
    // Si vous choisissez "true" les champs seront affichés.
    $conf['show_exif'] = true;
    // FIXEME: supprimer l'icône en cas de paramètre à false.
     
    // Piwigo peut stocker les informations EXIF dans la base de données.
    // Cela facilite notamment les recherches. 
    // Pour utiliser les métadonnées EXIF lors de la synchronisation:
    // $conf['use_exif'] = [false] - [true];
    // Si vous choisissez "false", les données ne seront pas enregistrées dans
    // la BDD.
    // Si vous choisissez "true", les données seront enregistrées dans la BDD.
    $conf['use_exif'] = true;
     
    // Si vous décidez d'enregistrer des champs EXIF dans la Base De Données,
    // il faut dire "lesquels". Ce paramétrage est utilisé durant la 
    // synchronisation. Chaque clé du tableau représente une colonne de la
    // table images, chaque valeur correspond à un identifiant EXIF.
    // Seuls les champs listés ci-après sont compatibles. N'en rajoutez pas plus
    // ils ne seront pas inscrits dans la base de données.
    $conf['use_exif_mapping'] = array(
    'date_creation' => 'DateTimeOriginal'
    );
    // Pour rajouter d'autres champs, il faut adapter votre Base De Données. (expérimental)
     
    // Pour n'afficher que les champs EXIF nécessaires, il vous faut définir ici
    // à l'avance quels champs seront à afficher
    // (indépendant de use_exif_mapping).
    // Évidement, les lignes vides n'apparaîtrons pas...
    // Il est possible de choisir des champs parmi des groupes, par exemple
    // ['COMPUTED']['ApertureFNumber']. Pour cela, créer une clé
    // 'COMPUTED;ApertureFNumber'.
    $conf['show_exif_fields'] = array(
    'exif_field_Make'       => 'Make',
    'exif_field_Model'       => 'Model',
    'exif_field_ExposureTime'     => 'ExposureTime',
    'exif_field_FocalLength'     => 'FocalLength', 
    'exif_field_FNumber'       => 'FNumber',
    'exif_field_ExposureBiasValue'     => 'ExposureBiasValue',
    'exif_field_ISOSpeedRatings'     => 'ISOSpeedRatings',
    'exif_field_DateTimeOriginal'     => 'DateTimeOriginal',
    'exif_field_ExposureProgram'     => 'ExposureProgram',
    'exif_field_Make'       => 'Make',
    'exif_field_Model'       => 'Model',
    'exif_field_ExposureTime'     => 'ExposureTime',
    'exif_field_FocalLength'     => 'FocalLength', 
    'exif_field_FNumber'       => 'FNumber',
    'exif_field_ExposureBiasValue'     => 'ExposureBiasValue',
    'exif_field_ISOSpeedRatings'     => 'ISOSpeedRatings',
    'exif_field_DateTimeOriginal'     => 'DateTimeOriginal',
    'exif_field_TakenDate'     => 'TakenDate',
    'exif_field_ExposureProgram'     => 'ExposureProgram',
    'exif_field_ModeArray'       => 'ModeArray',
    'exif_field_SelfTimer'       => 'SelfTimer',
    'exif_field_ImageQuality'     => 'ImageQuality',
    'exif_field_Flash'      => 'Flash',
    'exif_field_Drive'       => 'Drive',
    'exif_field_FocusMode'       => 'FocusMode',
    'exif_field_ImageSize'      => 'ImageSize',
    'exif_field_EasyShootingMode'     => 'EasyShootingMode',
    'exif_field_Contrast'      => 'Contrast',
    'exif_field_Saturation'     => 'Saturation',
    'exif_field_Sharpness'       => 'Sharpness',
    'exif_field_MeteringMode'     => 'MeteringMode',
    'exif_field_ExposureProgram'     => 'ExposureProgram',
    'exif_field_MinFocal'       => 'MinFocal',
    'exif_field_MaxFocal'       => 'MaxFocal',
    'exif_field_FlashActivity'     => 'FlashActivity',
    'exif_field_Stabilization'     => 'Stabilization',
    'exif_field_SpotMeteringMode'     => 'SpotMeteringMode'
    );
     
    // Le titre de l'information affichée sur picture.php sera une clé de
    // langue, comme par exemple $lang['exif_field_Make'] si elle existe.
    // Pour les champs composés, ne prendre en compte que le dernier niveau 
    // Par exemple pour la clé 'COMPUTED;ApertureFNumber' vous avez besoin de
    // $lang['exif_field_ApertureFNumber']
    //
    // Maintenant que vous avez choisi vos informations EXIF à afficher, nous
    // allons voir comment les traduire dans votre langue. J'utilise le plugin
    // LocalFile Editor.
    // Rendez vous dans Administration > Plugins > LocalFile Editor > Langue
    // Choisissez le fichier de langue qui vous convient.
    // Je veux traduire:   'exif_field_Make'
    // Pour cela nous allons écrire la ligne suivante dans le fichier de
    // langue :
    // $lang['exif_field_Make'] = 'Marque';
     
     
    //          CHAPITRE 2e
    //                             LES CHAMPS IPTC
     
     
    // C'est exactement le même raisonnement que pour les champs EXIF.
    // Pour plus d'informations sur la correspondance des champs :
    // http://fr.piwigo.org/doc/doku.php?id=utiliser:utilisation:fonctionnalites:meta
     
    $conf['show_iptc'] = true;
     
    $conf['use_iptc'] = true;
     
    $conf['use_iptc_mapping'] = array(
    'keywords'        => '2#025',
    'author'          => '2#122',
    'name'            => '2#105',
    'comment'         => '2#120'
    );
     
    $conf['show_iptc_mapping'] = array(
    'iptc_Object'                                  => '2#005',
    'iptc_Edit_Status'                             => '2#007',
    'iptc_Urgency'                                 => '2#010',
    'iptc_Category'                                => '2#015',
    'iptc_Supplemental_Category'                   => '2#020',
    'iptc_Fixture_Identifier'                      => '2#022',
    'iptc_Keywords'                                => '2#025',
    'iptc_Release_Date'                            => '2#030',
    'iptc_Release_Time'                            => '2#035',
    'iptc_Special_Instructions'                    => '2#040',
    'iptc_Reference_service'                       => '2#045',
    'iptc_Reference_Date'                          => '2#047',
    'iptc_Reference_Number'                        => '2#050',
    'iptc_Date_Created'                            => '2#055',
    'iptc_Time_Created'                            => '2#060',
    'iptc_Originating_Program'                     => '2#065',
    'iptc_Program_version'                         => '2#070',
    'iptc_Object_cycle'                            => '2#075',
    'iptc_By_line'                                 => '2#080',
    'iptc_By_line_Title'                           => '2#085',
    'iptc_City'                                    => '2#090',
    'iptc_Province_State'                          => '2#095',
    'iptc_Country_Primary_Location_Code'           => '2#100',
    'iptc_Country_Primary_Location_Name'           => '2#101',
    'iptc_Original_Transmission_Reference'         => '2#103',
    'iptc_Headline'                                => '2#105',
    'iptc_Credit'                                  => '2#110',
    'iptc_Source'                                  => '2#115',
    'iptc_Copyright_Notice'                        => '2#116',
    'iptc_Contact'                                 => '2#118',
    'iptc_Caption_Abstract'                        => '2#120',
    'iptc_Writer_Editor'                           => '2#122',
    'iptc_Image_Type'                              => '2#130'
      );
    ```
    

## Fichier de langue FR

Une fois que votre fichier de configuration local est correctement paramétré, il faut encore compléter votre fichier de langage pour que Piwigo restitue les données en Français.

Pour ce faire, toujours à l'aide de LocalFiles Editor, vous allez éditer le fichier `language/fr_FR/local.lang.php` et le compléter avec ce qui suit :

- Afficher le code
    
    ```jsx
    $lang['exif_field_Make']       = 'Marque';
    $lang['exif_field_Model']      = 'Modèle';
    $lang['exif_field_ExposureTime']     = 'Vitesse';
    $lang['exif_field_FocalLength']     = 'Focale';
    $lang['exif_field_FNumber']       = 'Diaphragme';
    $lang['exif_field_ExposureBiasValue']     = 'Correction Expo.';
    $lang['exif_field_ISOSpeedRatings']     = 'ISO';
    $lang['exif_field_DateTimeOriginal']     = 'Photographié le';
    $lang['exif_field_TakenDate']     = 'Prise de vue le';
    $lang['exif_field_ExposureProgram']     = 'Prog. Expo.';
     
    $lang['exif_field_SelfTimer']       = 'Retardateur';
    $lang['exif_field_ImageQuality']     = 'Qualité';
    $lang['exif_field_Flash']       = 'Flash';
    $lang['exif_field_Drive']       = 'Moteur';
    $lang['exif_field_FocusMode']       = 'Auto focus';
    $lang['exif_field_ImageSize']       = 'Taille';
    $lang['exif_field_EasyShootingMode']     = 'Mode auto.';
    $lang['exif_field_Contrast']       = 'Contraste';
    $lang['exif_field_Saturation']       = 'Saturation';
    $lang['exif_field_Sharpness']       = 'Netteté';
    $lang['exif_field_MeteringMode']     = 'Mesure Expo.';
    $lang['exif_field_ExposureProgram']     = 'Prog. Expo.';
    $lang['exif_field_MinFocal']       = 'Focale Min';
    $lang['exif_field_MaxFocal']       = 'Focale Max';
    $lang['exif_field_FlashActivity']     = 'Flash Opt.';
    $lang['exif_field_Stabilization']     = 'Stabilisation';
    $lang['exif_field_SpotMeteringMode']     = 'Mode de mesure';
     
    $lang['iptc_Object']                                  = 'Nom de l\'objet';
    $lang['iptc_Edit_Status']                             = 'Statut éditorial';
    $lang['iptc_Urgency']                                 = 'Priorité';
    $lang['iptc_Category']                                = 'Catégorie';
    $lang['iptc_Supplemental_Category']                   = 'Catégorie supplémentaire';
    $lang['iptc_Fixture_Identifier']                      = 'Identificateur';
    $lang['iptc_Keywords']                                = 'Mots-clés';
    $lang['iptc_Release_Date']                            = 'Date de disponibilité';
    $lang['iptc_Release_Time']                            = 'Heure de disponibilité';
    $lang['iptc_Special_Instructions']                    = 'Instructions spéciales';
    $lang['iptc_Reference_service']                       = 'Service de référence';
    $lang['iptc_Reference_Date']                          = 'Date de référence';
    $lang['iptc_Reference_Number']                        = 'Numéro de référence';
    $lang['iptc_Date_Created']                            = 'Date de création de l\'objet';
    $lang['iptc_Time_Created']                            = 'Heure de création de l\'objet';
    $lang['iptc_Originating_Program']                     = 'Programme ayant créé l\'objet';
    $lang['iptc_Program_version']                         = 'Version du programme ayant créé l\'objet';
    $lang['iptc_Object_cycle']                            = 'Cycle de l\'objet';
    $lang['iptc_By_line']                                 = 'Créateur de l\'objet';
    $lang['iptc_By_line_Title']                           = 'Titre du créateur';
    $lang['iptc_City']                                    = 'Ville';
    $lang['iptc_Province_State']                          = 'Province-État';
    $lang['iptc_Country_Primary_Location_Code']           = 'Code du pays';
    $lang['iptc_Country_Primary_Location_Name']           = 'Libellé du pays';
    $lang['iptc_Original_Transmission_Reference']         = 'Référence de la transmission';
    $lang['iptc_Headline']                                = 'Titre';
    $lang['iptc_Credit']                                  = 'Crédit';
    $lang['iptc_Source']                                  = 'Source';
    $lang['iptc_Copyright_Notice']                        = 'Copyright';
    $lang['iptc_Contact']                                 = 'Contact';
    $lang['iptc_Caption_Abstract']                        = 'Description';
    $lang['iptc_Writer_Editor']                           = 'Auteur de la Description';
    $lang['iptc_Image_Type']                              = 'Type de l\'image';
    ```
    

## Documentation IPTC

Voici les définitions officielles des codes IPTC (source : [http://www.dublincore.org/](http://www.dublincore.org/)), un tableau bien utile pour les photographes qui souhaitent les utiliser dans un cadre professionnel et de collaboration.

| Set (numéro du champ) | Nom du champ | Description | Traduction et Commentaire |
| --- | --- | --- | --- |
| 5 | Object | Name non répétable, 64 caractères maximum | Nom de l'objet |
| 7 | Edit Status | non répétable, 64 caractères maximum | Statut éditorial |
| 10 | Urgency | non répétable, un seul caractère | Priorité |
| 15 | Category | non répétable, 3 caractères maximum | Catégorie - ce champ est obsolète dans IIMV4 |
| 20 | Supplemental Category | répétable, 32 caractères maximum | Catégorie supplémentaire |
| 22 | Fixture Identifier | non répétable, 32 caractères maximum | Identificateur |
| 25 | Keywords | répétable, 64 caractères maximum | Mots-clés |
| 30 | Release Date | non répétable, 8 caractères, forme AAAAMMJJ | Date de disponibilité |
| 35 | Release Time | non répétable, 11 caractères, forme HHMMSS±HHMM | Heure de disponibilité, suit la norme ISO8601. |
| 40 | Special Instructions | non répétable, 256 caractères maximum | Instructions spéciales |
| 45 | Reference service | répétable, 10 caractères maximum. Optionnel | Service de référence (doit être suivi des champs 47 et 50) |
| 47 | Reference Date | obligatoire si le champ 45 est présent, 8 caractères, forme AAAAMMJJ | Date de référence |
| 50 | Reference Number | obligatoire si le champ 45 est présent, 10 caractères maximum | Numéro de référence |
| 55 | Date Created | non répétable, 8 caractères, forme AAAAMMJJ | Date de création de l'objet |
| 60 | Time Created | non répétable, 11 caractères, forme HHMMSS±HHMM | Heure de création de l'objet, suit la norme ISO8601. |
| 65 | Originating Program | non répétable, 32 caractères maximum | Programme ayant créé l'objet |
| 70 | Program version | non répétable, 10 caractères maximum | Version du programme ayant créé l'objet |
| 75 | Object cycle | non répétable, un seul caractère | Cycle de l'objet 'a' = le matin, 'b' = l'après-midi, 'c' = matin et après-midi |
| 80 | By-line | répétable, 32 caractères maximum | Créateur de l'objet (auteur): nom du rédacteur, du photographe, etc. |
| 85 | By-line Title | répétable, 32 caractères maximum | Titre du créateur ou des créateurs. Ex. “Staff Photographer”, “Envoyé spécial” |
| 90 | City | non répétable, 32 caractères maximum | Ville |
| 95 | Province/State | non répétable, 32 caractères maximum | Province/État |
| 100 | Country/Primary Location Code | non répétable, 3 caractères | Code du pays, suit la norme ISO3166 (codes pays sur 3 caractères) |
| 101 | Country/Primary Location Name | non répétable, 64 caractères maximum | Libellé du pays |
| 103 | Original Transmission Reference | non répétable, 32 caractères maximum | Référence de la transmission (code) |
| 105 | Headline | non répétable, 256 caractères maximum | Titre de la photo |
| 110 | Credit | non répétable, 32 caractères maximum | Crédit (fournisseur de l'objet) |
| 115 | Source | non répétable, 32 caractères maximum | Source (propriétaire intellectuel de l'objet) |
| 116 | Copyright Notice | non répétable, 128 caractères maximum | Copyright |
| 118 | Contact | répétable, 128 caractères maximum | Contact |
| 120 | Caption/Abstract | non répétable, 2000 caractères maximum | Description, Résumé, Commentaire |
| 122 | Writer/Editor | répétable, 32 caractères maximum | Auteur de la Description (du champ 120) |
| 130 | Image Type | non répétable, 2 caractères | Type de l'image (cf. le document IPTC-NAA IIMV4) |

## Champs EXIF supplémentaires

Dans la liste ci-dessous Se trouve un certain nombre d'éléments utilisables pour les utilisateurs expérimentés. 'exif_field_Tag Name' ⇒ 'Tag Name'

- Voir la liste
    
    ```jsx
    'exif_field_InteropIndex'      => 'InteropIndex',
    'exif_field_InteropVersion'      => 'InteropVersion',
    'exif_field_ProcessingSoftware'      => 'ProcessingSoftware',
    'exif_field_SubfileType'      => 'SubfileType',
    'exif_field_OldSubfileType'      => 'OldSubfileType',
    'exif_field_ImageWidth'      => 'ImageWidth',
    'exif_field_ImageHeight'      => 'ImageHeight',
    'exif_field_BitsPerSample'      => 'BitsPerSample',
    'exif_field_Compression'      => 'Compression',
    'exif_field_PhotometricInterpretation'      => 'PhotometricInterpretation',
    'exif_field_Thresholding'      => 'Thresholding',
    'exif_field_CellWidth'      => 'CellWidth',
    'exif_field_CellLength'      => 'CellLength',
    'exif_field_FillOrder'      => 'FillOrder',
    'exif_field_DocumentName'      => 'DocumentName',
    'exif_field_ImageDescription'      => 'ImageDescription',
    'exif_field_Make'      => 'Make',
    'exif_field_Model'      => 'Model',
    'exif_field_StripOffsets'      => 'StripOffsets',
    'exif_field_PreviewImageStart'      => 'PreviewImageStart',
    'exif_field_PreviewImageStart'      => 'PreviewImageStart',
    'exif_field_JpgFromRawStart'      => 'JpgFromRawStart',
    'exif_field_Orientation'      => 'Orientation',
    'exif_field_SamplesPerPixel'      => 'SamplesPerPixel',
    'exif_field_RowsPerStrip'      => 'RowsPerStrip',
    'exif_field_StripByteCounts'      => 'StripByteCounts',
    'exif_field_PreviewImageLength'      => 'PreviewImageLength',
    'exif_field_PreviewImageLength'      => 'PreviewImageLength',
    'exif_field_JpgFromRawLength'      => 'JpgFromRawLength',
    'exif_field_MinSampleValue'      => 'MinSampleValue',
    'exif_field_MaxSampleValue'      => 'MaxSampleValue',
    'exif_field_XResolution'      => 'XResolution',
    'exif_field_YResolution'      => 'YResolution',
    'exif_field_PlanarConfiguration'      => 'PlanarConfiguration',
    'exif_field_PageName'      => 'PageName',
    'exif_field_XPosition'      => 'XPosition',
    'exif_field_YPosition'      => 'YPosition',
    'exif_field_FreeOffsets'      => 'FreeOffsets',
    'exif_field_FreeByteCounts'      => 'FreeByteCounts',
    'exif_field_GrayResponseUnit'      => 'GrayResponseUnit',
    'exif_field_GrayResponseCurve'      => 'GrayResponseCurve',
    'exif_field_T4Options'      => 'T4Options',
    'exif_field_T6Options'      => 'T6Options',
    'exif_field_ResolutionUnit'      => 'ResolutionUnit',
    'exif_field_PageNumber'      => 'PageNumber',
    'exif_field_ColorResponseUnit'      => 'ColorResponseUnit',
    'exif_field_TransferFunction'      => 'TransferFunction',
    'exif_field_Software'      => 'Software',
    'exif_field_ModifyDate'      => 'ModifyDate',
    'exif_field_Artist'      => 'Artist',
    'exif_field_HostComputer'      => 'HostComputer',
    'exif_field_Predictor'      => 'Predictor',
    'exif_field_WhitePoint'      => 'WhitePoint',
    'exif_field_PrimaryChromaticities'      => 'PrimaryChromaticities',
    'exif_field_ColorMap'      => 'ColorMap',
    'exif_field_HalftoneHints'      => 'HalftoneHints',
    'exif_field_TileWidth'      => 'TileWidth',
    'exif_field_TileLength'      => 'TileLength',
    'exif_field_TileOffsets'      => 'TileOffsets',
    'exif_field_TileByteCounts'      => 'TileByteCounts',
    'exif_field_BadFaxLines'      => 'BadFaxLines',
    'exif_field_CleanFaxData'      => 'CleanFaxData',
    'exif_field_ConsecutiveBadFaxLines'      => 'ConsecutiveBadFaxLines',
    'exif_field_SubIFD'      => 'SubIFD',
    'exif_field_InkSet'      => 'InkSet',
    'exif_field_InkNames'      => 'InkNames',
    'exif_field_NumberofInks'      => 'NumberofInks',
    'exif_field_DotRange'      => 'DotRange',
    'exif_field_TargetPrinter'      => 'TargetPrinter',
    'exif_field_ExtraSamples'      => 'ExtraSamples',
    'exif_field_SampleFormat'      => 'SampleFormat',
    'exif_field_SMinSampleValue'      => 'SMinSampleValue',
    'exif_field_SMaxSampleValue'      => 'SMaxSampleValue',
    'exif_field_TransferRange'      => 'TransferRange',
    'exif_field_ClipPath'      => 'ClipPath',
    'exif_field_XClipPathUnits'      => 'XClipPathUnits',
    'exif_field_YClipPathUnits'      => 'YClipPathUnits',
    'exif_field_Indexed'      => 'Indexed',
    'exif_field_JPEGTables'      => 'JPEGTables',
    'exif_field_OPIProxy'      => 'OPIProxy',
    'exif_field_GlobalParametersIFD'      => 'GlobalParametersIFD',
    'exif_field_ProfileType'      => 'ProfileType',
    'exif_field_FaxProfile'      => 'FaxProfile',
    'exif_field_CodingMethods'      => 'CodingMethods',
    'exif_field_VersionYear'      => 'VersionYear',
    'exif_field_ModeNumber'      => 'ModeNumber',
    'exif_field_Decode'      => 'Decode',
    'exif_field_DefaultImageColor'      => 'DefaultImageColor',
    'exif_field_JPEGProc'      => 'JPEGProc',
    'exif_field_ThumbnailOffset'      => 'ThumbnailOffset',
    'exif_field_PreviewImageStart'      => 'PreviewImageStart',
    'exif_field_JpgFromRawStart'      => 'JpgFromRawStart',
    'exif_field_JpgFromRawStart'      => 'JpgFromRawStart',
    'exif_field_OtherImageStart'      => 'OtherImageStart',
    'exif_field_ThumbnailLength'      => 'ThumbnailLength',
    'exif_field_PreviewImageLength'      => 'PreviewImageLength',
    'exif_field_JpgFromRawLength'      => 'JpgFromRawLength',
    'exif_field_JpgFromRawLength'      => 'JpgFromRawLength',
    'exif_field_OtherImageLength'      => 'OtherImageLength',
    'exif_field_JPEGRestartInterval'      => 'JPEGRestartInterval',
    'exif_field_JPEGLosslessPredictors'      => 'JPEGLosslessPredictors',
    'exif_field_JPEGPointTransforms'      => 'JPEGPointTransforms',
    'exif_field_JPEGQTables'      => 'JPEGQTables',
    'exif_field_JPEGDCTables'      => 'JPEGDCTables',
    'exif_field_JPEGACTables'      => 'JPEGACTables',
    'exif_field_YCbCrCoefficients'      => 'YCbCrCoefficients',
    'exif_field_YCbCrSubSampling'      => 'YCbCrSubSampling',
    'exif_field_YCbCrPositioning'      => 'YCbCrPositioning',
    'exif_field_ReferenceBlackWhite'      => 'ReferenceBlackWhite',
    'exif_field_StripRowCounts'      => 'StripRowCounts',
    'exif_field_ApplicationNotes'      => 'ApplicationNotes',
    'exif_field_RelatedImageFileFormat'      => 'RelatedImageFileFormat',
    'exif_field_RelatedImageWidth'      => 'RelatedImageWidth',
    'exif_field_RelatedImageLength'      => 'RelatedImageLength',
    'exif_field_Rating'      => 'Rating',
    'exif_field_RatingPercent'      => 'RatingPercent',
    'exif_field_ImageID'      => 'ImageID',
    'exif_field_WangAnnotation'      => 'WangAnnotation',
    'exif_field_Matteing'      => 'Matteing',
    'exif_field_DataType'      => 'DataType',
    'exif_field_ImageDepth'      => 'ImageDepth',
    'exif_field_TileDepth'      => 'TileDepth',
    'exif_field_Model2'      => 'Model2',
    'exif_field_CFARepeatPatternDim'      => 'CFARepeatPatternDim',
    'exif_field_CFAPattern2'      => 'CFAPattern2',
    'exif_field_BatteryLevel'      => 'BatteryLevel',
    'exif_field_Copyright'      => 'Copyright',
    'exif_field_ExposureTime'      => 'ExposureTime',
    'exif_field_FNumber'      => 'FNumber',
    'exif_field_MDFileTag'      => 'MDFileTag',
    'exif_field_MDScalePixel'      => 'MDScalePixel',
    'exif_field_MDColorTable'      => 'MDColorTable',
    'exif_field_MDLabName'      => 'MDLabName',
    'exif_field_MDSampleInfo'      => 'MDSampleInfo',
    'exif_field_MDPrepDate'      => 'MDPrepDate',
    'exif_field_MDPrepTime'      => 'MDPrepTime',
    'exif_field_MDFileUnits'      => 'MDFileUnits',
    'exif_field_PixelScale'      => 'PixelScale',
    'exif_field_IPTC-NAA'      => 'IPTC-NAA',
    'exif_field_IntergraphPacketData'      => 'IntergraphPacketData',
    'exif_field_IntergraphFlagRegisters'      => 'IntergraphFlagRegisters',
    'exif_field_IntergraphMatrix'      => 'IntergraphMatrix',
    'exif_field_ModelTiePoint'      => 'ModelTiePoint',
    'exif_field_Site'      => 'Site',
    'exif_field_ColorSequence'      => 'ColorSequence',
    'exif_field_IT8Header'      => 'IT8Header',
    'exif_field_RasterPadding'      => 'RasterPadding',
    'exif_field_BitsPerRunLength'      => 'BitsPerRunLength',
    'exif_field_BitsPerExtendedRunLength'      => 'BitsPerExtendedRunLength',
    'exif_field_ColorTable'      => 'ColorTable',
    'exif_field_ImageColorIndicator'      => 'ImageColorIndicator',
    'exif_field_BackgroundColorIndicator'      => 'BackgroundColorIndicator',
    'exif_field_ImageColorValue'      => 'ImageColorValue',
    'exif_field_BackgroundColorValue'      => 'BackgroundColorValue',
    'exif_field_PixelIntensityRange'      => 'PixelIntensityRange',
    'exif_field_TransparencyIndicator'      => 'TransparencyIndicator',
    'exif_field_ColorCharacterization'      => 'ColorCharacterization',
    'exif_field_HCUsage'      => 'HCUsage',
    'exif_field_SEMInfo'      => 'SEMInfo',
    'exif_field_AFCP_IPTC'      => 'AFCP_IPTC',
    'exif_field_ModelTransform'      => 'ModelTransform',
    'exif_field_LeafData'      => 'LeafData',
    'exif_field_PhotoshopSettings'      => 'PhotoshopSettings',
    'exif_field_ExifOffset'      => 'ExifOffset',
    'exif_field_ICC_Profile'      => 'ICC_Profile',
    'exif_field_ImageLayer'      => 'ImageLayer',
    'exif_field_GeoTiffDirectory'      => 'GeoTiffDirectory',
    'exif_field_GeoTiffDoubleParams'      => 'GeoTiffDoubleParams',
    'exif_field_GeoTiffAsciiParams'      => 'GeoTiffAsciiParams',
    'exif_field_ExposureProgram'      => 'ExposureProgram',
    'exif_field_SpectralSensitivity'      => 'SpectralSensitivity',
    'exif_field_GPSInfo'      => 'GPSInfo',
    'exif_field_ISO'      => 'ISO',
    'exif_field_Opto-ElectricConvFactor'      => 'Opto-ElectricConvFactor',
    'exif_field_Interlace'      => 'Interlace',
    'exif_field_TimeZoneOffset'      => 'TimeZoneOffset',
    'exif_field_SelfTimerMode'      => 'SelfTimerMode',
    'exif_field_FaxRecvParams'      => 'FaxRecvParams',
    'exif_field_FaxSubAddress'      => 'FaxSubAddress',
    'exif_field_FaxRecvTime'      => 'FaxRecvTime',
    'exif_field_LeafSubIFD'      => 'LeafSubIFD',
    'exif_field_ExifVersion'      => 'ExifVersion',
    'exif_field_DateTimeOriginal'      => 'DateTimeOriginal',
    'exif_field_CreateDate'      => 'CreateDate',
    'exif_field_ComponentsConfiguration'      => 'ComponentsConfiguration',
    'exif_field_CompressedBitsPerPixel'      => 'CompressedBitsPerPixel',
    'exif_field_ShutterSpeedValue'      => 'ShutterSpeedValue',
    'exif_field_ApertureValue'      => 'ApertureValue',
    'exif_field_BrightnessValue'      => 'BrightnessValue',
    'exif_field_ExposureCompensation'      => 'ExposureCompensation',
    'exif_field_MaxApertureValue'      => 'MaxApertureValue',
    'exif_field_SubjectDistance'      => 'SubjectDistance',
    'exif_field_MeteringMode'      => 'MeteringMode',
    'exif_field_LightSource'      => 'LightSource',
    'exif_field_Flash'      => 'Flash',
    'exif_field_FocalLength'      => 'FocalLength',
    'exif_field_FlashEnergy'      => 'FlashEnergy',
    'exif_field_SpatialFrequencyResponse'      => 'SpatialFrequencyResponse',
    'exif_field_Noise'      => 'Noise',
    'exif_field_FocalPlaneXResolution'      => 'FocalPlaneXResolution',
    'exif_field_FocalPlaneYResolution'      => 'FocalPlaneYResolution',
    'exif_field_FocalPlaneResolutionUnit'      => 'FocalPlaneResolutionUnit',
    'exif_field_ImageNumber'      => 'ImageNumber',
    'exif_field_SecurityClassification'      => 'SecurityClassification',
    'exif_field_ImageHistory'      => 'ImageHistory',
    'exif_field_SubjectLocation'      => 'SubjectLocation',
    'exif_field_ExposureIndex'      => 'ExposureIndex',
    'exif_field_TIFF-EPStandardID'      => 'TIFF-EPStandardID',
    'exif_field_SensingMethod'      => 'SensingMethod',
    'exif_field_StoNits'      => 'StoNits',
    'exif_field_MakerNoteCanon'      => 'MakerNoteCanon',
    'exif_field_MakerNoteCasio'      => 'MakerNoteCasio',
    'exif_field_MakerNoteCasio2'      => 'MakerNoteCasio2',
    'exif_field_MakerNoteFujiFilm'      => 'MakerNoteFujiFilm',
    'exif_field_MakerNoteJVC'      => 'MakerNoteJVC',
    'exif_field_MakerNoteJVCText'      => 'MakerNoteJVCText',
    'exif_field_MakerNoteKodak1a'      => 'MakerNoteKodak1a',
    'exif_field_MakerNoteKodak1b'      => 'MakerNoteKodak1b',
    'exif_field_MakerNoteKodak2'      => 'MakerNoteKodak2',
    'exif_field_MakerNoteKodak3'      => 'MakerNoteKodak3',
    'exif_field_MakerNoteKodak4'      => 'MakerNoteKodak4',
    'exif_field_MakerNoteKodak5'      => 'MakerNoteKodak5',
    'exif_field_MakerNoteKodak6a'      => 'MakerNoteKodak6a',
    'exif_field_MakerNoteKodak6b'      => 'MakerNoteKodak6b',
    'exif_field_MakerNoteKodakUnknown'      => 'MakerNoteKodakUnknown',
    'exif_field_MakerNoteKyocera'      => 'MakerNoteKyocera',
    'exif_field_MakerNoteMinolta'      => 'MakerNoteMinolta',
    'exif_field_MakerNoteMinolta2'      => 'MakerNoteMinolta2',
    'exif_field_MakerNoteMinolta3'      => 'MakerNoteMinolta3',
    'exif_field_MakerNoteMinolta4'      => 'MakerNoteMinolta4',
    'exif_field_MakerNoteNikon'      => 'MakerNoteNikon',
    'exif_field_MakerNoteNikon2'      => 'MakerNoteNikon2',
    'exif_field_MakerNoteNikon3'      => 'MakerNoteNikon3',
    'exif_field_MakerNoteOlympus'      => 'MakerNoteOlympus',
    'exif_field_MakerNoteOlympus2'      => 'MakerNoteOlympus2',
    'exif_field_MakerNoteLeica'      => 'MakerNoteLeica',
    'exif_field_MakerNotePanasonic'      => 'MakerNotePanasonic',
    'exif_field_MakerNotePanasonic2'      => 'MakerNotePanasonic2',
    'exif_field_MakerNotePentax'      => 'MakerNotePentax',
    'exif_field_MakerNoteRicoh'      => 'MakerNoteRicoh',
    'exif_field_MakerNoteRicohText'      => 'MakerNoteRicohText',
    'exif_field_PreviewImage'      => 'PreviewImage',
    'exif_field_MakerNoteSanyo'      => 'MakerNoteSanyo',
    'exif_field_MakerNoteSanyoC4'      => 'MakerNoteSanyoC4',
    'exif_field_MakerNoteSanyoPatch'      => 'MakerNoteSanyoPatch',
    'exif_field_MakerNoteSigma'      => 'MakerNoteSigma',
    'exif_field_MakerNoteSony'      => 'MakerNoteSony',
    'exif_field_MakerNoteSonySRF'      => 'MakerNoteSonySRF',
    'exif_field_MakerNoteSonySR2'      => 'MakerNoteSonySR2',
    'exif_field_MakerNoteUnknown'      => 'MakerNoteUnknown',
    'exif_field_UserComment'      => 'UserComment',
    'exif_field_SubSecTime'      => 'SubSecTime',
    'exif_field_SubSecTimeOriginal'      => 'SubSecTimeOriginal',
    'exif_field_SubSecTimeDigitized'      => 'SubSecTimeDigitized',
    'exif_field_ImageSourceData'      => 'ImageSourceData',
    'exif_field_XPTitle'      => 'XPTitle',
    'exif_field_XPComment'      => 'XPComment',
    'exif_field_XPAuthor'      => 'XPAuthor',
    'exif_field_XPKeywords'      => 'XPKeywords',
    'exif_field_XPSubject'      => 'XPSubject',
    'exif_field_FlashpixVersion'      => 'FlashpixVersion',
    'exif_field_ColorSpace'      => 'ColorSpace',
    'exif_field_ExifImageWidth'      => 'ExifImageWidth',
    'exif_field_ExifImageLength'      => 'ExifImageLength',
    'exif_field_RelatedSoundFile'      => 'RelatedSoundFile',
    'exif_field_InteropOffset'      => 'InteropOffset',
    'exif_field_FlashEnergy'      => 'FlashEnergy',
    'exif_field_SpatialFrequencyResponse'      => 'SpatialFrequencyResponse',
    'exif_field_Noise'      => 'Noise',
    'exif_field_FocalPlaneXResolution'      => 'FocalPlaneXResolution',
    'exif_field_FocalPlaneYResolution'      => 'FocalPlaneYResolution',
    'exif_field_FocalPlaneResolutionUnit'      => 'FocalPlaneResolutionUnit',
    'exif_field_ImageNumber'      => 'ImageNumber',
    'exif_field_SecurityClassification'      => 'SecurityClassification',
    'exif_field_ImageHistory'      => 'ImageHistory',
    'exif_field_SubjectLocation'      => 'SubjectLocation',
    'exif_field_ExposureIndex'      => 'ExposureIndex',
    'exif_field_TIFF-EPStandardID'      => 'TIFF-EPStandardID',
    'exif_field_SensingMethod'      => 'SensingMethod',
    'exif_field_FileSource'      => 'FileSource',
    'exif_field_SceneType'      => 'SceneType',
    'exif_field_CFAPattern'      => 'CFAPattern',
    'exif_field_CustomRendered'      => 'CustomRendered',
    'exif_field_ExposureMode'      => 'ExposureMode',
    'exif_field_WhiteBalance'      => 'WhiteBalance',
    'exif_field_DigitalZoomRatio'      => 'DigitalZoomRatio',
    'exif_field_FocalLengthIn35mmFormat'      => 'FocalLengthIn35mmFormat',
    'exif_field_SceneCaptureType'      => 'SceneCaptureType',
    'exif_field_GainControl'      => 'GainControl',
    'exif_field_Contrast'      => 'Contrast',
    'exif_field_Saturation'      => 'Saturation',
    'exif_field_Sharpness'      => 'Sharpness',
    'exif_field_DeviceSettingDescription'      => 'DeviceSettingDescription',
    'exif_field_SubjectDistanceRange'      => 'SubjectDistanceRange',
    'exif_field_ImageUniqueID'      => 'ImageUniqueID',
    'exif_field_GDALMetadata'      => 'GDALMetadata',
    'exif_field_GDALNoData'      => 'GDALNoData',
    'exif_field_Gamma'      => 'Gamma',
    'exif_field_PixelFormat'      => 'PixelFormat',
    'exif_field_Transfomation'      => 'Transfomation',
    'exif_field_Uncompressed'      => 'Uncompressed',
    'exif_field_ImageType'      => 'ImageType',
    'exif_field_ImageWidth'      => 'ImageWidth',
    'exif_field_ImageHeight'      => 'ImageHeight',
    'exif_field_WidthResolution'      => 'WidthResolution',
    'exif_field_HeightResolution'      => 'HeightResolution',
    'exif_field_ImageOffset'      => 'ImageOffset',
    'exif_field_ImageByteCount'      => 'ImageByteCount',
    'exif_field_AlphaOffset'      => 'AlphaOffset',
    'exif_field_AlphaByteCount'      => 'AlphaByteCount',
    'exif_field_ImageDataDiscard'      => 'ImageDataDiscard',
    'exif_field_AlphaDataDiscard'      => 'AlphaDataDiscard',
    'exif_field_OceScanjobDesc'      => 'OceScanjobDesc',
    'exif_field_OceApplicationSelector'      => 'OceApplicationSelector',
    'exif_field_OceIDNumber'      => 'OceIDNumber',
    'exif_field_OceImageLogic'      => 'OceImageLogic',
    'exif_field_Annotations'      => 'Annotations',
    'exif_field_PrintIM'      => 'PrintIM',
    'exif_field_DNGVersion'      => 'DNGVersion',
    'exif_field_DNGBackwardVersion'      => 'DNGBackwardVersion',
    'exif_field_UniqueCameraModel'      => 'UniqueCameraModel',
    'exif_field_LocalizedCameraModel'      => 'LocalizedCameraModel',
    'exif_field_CFAPlaneColor'      => 'CFAPlaneColor',
    'exif_field_CFALayout'      => 'CFALayout',
    'exif_field_LinearizationTable'      => 'LinearizationTable',
    'exif_field_BlackLevelRepeatDim'      => 'BlackLevelRepeatDim',
    'exif_field_BlackLevel'      => 'BlackLevel',
    'exif_field_BlackLevelDeltaH'      => 'BlackLevelDeltaH',
    'exif_field_BlackLevelDeltaV'      => 'BlackLevelDeltaV',
    'exif_field_WhiteLevel'      => 'WhiteLevel',
    'exif_field_DefaultScale'      => 'DefaultScale',
    'exif_field_DefaultCropOrigin'      => 'DefaultCropOrigin',
    'exif_field_DefaultCropSize'      => 'DefaultCropSize',
    'exif_field_ColorMatrix1'      => 'ColorMatrix1',
    'exif_field_ColorMatrix2'      => 'ColorMatrix2',
    'exif_field_CameraCalibration1'      => 'CameraCalibration1',
    'exif_field_CameraCalibration2'      => 'CameraCalibration2',
    'exif_field_ReductionMatrix1'      => 'ReductionMatrix1',
    'exif_field_ReductionMatrix2'      => 'ReductionMatrix2',
    'exif_field_AnalogBalance'      => 'AnalogBalance',
    'exif_field_AsShotNeutral'      => 'AsShotNeutral',
    'exif_field_AsShotWhiteXY'      => 'AsShotWhiteXY',
    'exif_field_BaselineExposure'      => 'BaselineExposure',
    'exif_field_BaselineNoise'      => 'BaselineNoise',
    'exif_field_BaselineSharpness'      => 'BaselineSharpness',
    'exif_field_BayerGreenSplit'      => 'BayerGreenSplit',
    'exif_field_LinearResponseLimit'      => 'LinearResponseLimit',
    'exif_field_CameraSerialNumber'      => 'CameraSerialNumber',
    'exif_field_DNGLensInfo'      => 'DNGLensInfo',
    'exif_field_ChromaBlurRadius'      => 'ChromaBlurRadius',
    'exif_field_AntiAliasStrength'      => 'AntiAliasStrength',
    'exif_field_ShadowScale'      => 'ShadowScale',
    'exif_field_SR2Private'      => 'SR2Private',
    'exif_field_DNGAdobeData'      => 'DNGAdobeData',
    'exif_field_DNGPentaxData'      => 'DNGPentaxData',
    'exif_field_DNGPrivateData'      => 'DNGPrivateData',
    'exif_field_MakerNoteSafety'      => 'MakerNoteSafety',
    'exif_field_CalibrationIlluminant1'      => 'CalibrationIlluminant1',
    'exif_field_CalibrationIlluminant2'      => 'CalibrationIlluminant2',
    'exif_field_BestQualityScale'      => 'BestQualityScale',
    'exif_field_RawDataUniqueID'      => 'RawDataUniqueID',
    'exif_field_AliasLayerMetadata'      => 'AliasLayerMetadata',
    'exif_field_OriginalRawFileName'      => 'OriginalRawFileName',
    'exif_field_OriginalRawFileData'      => 'OriginalRawFileData',
    'exif_field_ActiveArea'      => 'ActiveArea',
    'exif_field_MaskedAreas'      => 'MaskedAreas',
    'exif_field_AsShotICCProfile'      => 'AsShotICCProfile',
    'exif_field_AsShotPreProfileMatrix'      => 'AsShotPreProfileMatrix',
    'exif_field_CurrentICCProfile'      => 'CurrentICCProfile',
    'exif_field_CurrentPreProfileMatrix'      => 'CurrentPreProfileMatrix',
    'exif_field_OffsetSchema'      => 'OffsetSchema',
    'exif_field_OwnerName'      => 'OwnerName',
    'exif_field_SerialNumber'      => 'SerialNumber',
    'exif_field_Lens'      => 'Lens',
    'exif_field_RawFile'      => 'RawFile',
    'exif_field_Converter'      => 'Converter',
    'exif_field_WhiteBalance'      => 'WhiteBalance',
    'exif_field_Exposure'      => 'Exposure',
    'exif_field_Shadows'      => 'Shadows',
    'exif_field_Brightness'      => 'Brightness',
    'exif_field_Contrast'      => 'Contrast',
    'exif_field_Saturation'      => 'Saturation',
    'exif_field_Sharpness'      => 'Sharpness',
    'exif_field_Smoothness'      => 'Smoothness',
    'exif_field_MoireFilter'      => 'MoireFilter'
    ```