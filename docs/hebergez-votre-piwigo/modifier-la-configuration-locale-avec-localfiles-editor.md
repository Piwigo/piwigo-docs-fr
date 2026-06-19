# Modifier la configuration locale avec LocalFiles Editor

## Introduction

La configuration locale consiste à modifier certains paramètres de votre galerie Piwigo, qui ne sont pas modifiables via une interface visuelle dans l’administration.

Ces paramètres sont stockés dans un fichier de configuration : `config_default.inc.php`

Ce fichier ne doit **JAMAIS** être modifié : en revanche, vous pouvez le *surcharger en utilisant le plugin* **LocalFiles Editor**.

!!! info
    On vous déconseille très fortement de modifier les fichiers de Piwigo directement via FTP. Utiliser le plugin **LocalFiles Editor** a de nombreux avantages comme vous allez le voir.

## Activer le plugin LocalFiles Editor

La première étape pour modifier la configuration locale est donc d’activer le plugin LocalFiles Editor.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-a37ca8d0.png)

Une fois le plugin activé, cliquez sur “Configuration”.

Vous avez alors accès à l’écran ci-dessous : 

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-67285369.png)

## C**onfiguration par défaut**

Depuis cet écran, vous avez accès au fichier de configuration par défaut qui liste toutes les options de configuration disponibles dans ce fichier : pour cela cliquez sur le lien *Afficher le fichier "config_default.inc.php"* en haut à droite de l’écran.

Chaque ligne commençant par `$conf` représente une option.

Les options sont regroupées en sections cohérentes (urls, tags, related albums…).

Au dessus de chaque options, une section en commentaires (commençant par `//` ) explique le rôle de l’option.

Prenons un exemple avec l’option `'enable_formats'`: cette option permet d’activer ou pas la gestion des formats multiples sur votre galerie. Par défaut, elle est désactivée  (`false`).

```php
// enable_formats: should Piwigo search for multiple formats?
$conf['enable_formats'] = false;
```

## Modifier la configuration locale

Comme on l’a dit, il ne faut pas modifier le fichier de configuration livré avec votre Piwigo.

LocalFiles Editor va vous permettre de surcharger les paramètres de ce fichier, c’est à dire de spécifier quels paramètres doivent être modifiés par rapport au fichier de base.

Reprenons l’exemple précédent : imaginons que vous souhaitez activer la gestion des [formats multiples](/importer-et-gerer-les-photos/les-formats-multiples).

Vous n’avez qu’à copier la section correspondant au paramètre `'enable_formats'` et à la coller dans l’onglet Configuration Locale de LocalFiles Editor. Vous pouvez maintenant remplacer la valeur `false` par `true` comme dans l'exemple ci-dessous.

!!! Warning "Attention"
    Attention ! Le fichier doit toujours commencer par `<?php` et finir par `?>`


![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-eda5b202.png)

Enregistrez le fichier : le paramètre est mis à jour et la gestion des formats multiples est activée.

!!! info
On vous conseille de copier également l’explication en commentaires au dessus de la ligne contenant le paramètre de configuration. Ainsi, vous vous souviendrez plus facilement du rôle de chaque paramètre.


## Traduction en français du fichier "config_default.inc.php"

Pour vous aider à comprendre le rôle de chaque paramètre, nous avons traduit les commentaires du fichier de configuration par défaut.

Sommaire de l’article

- Cliquez sur la flèche pour voir le fichier traduit en français
    
    ```php
    // +-----------------------------------------------------------------------+
    // | Divers                                                                |
    // +-----------------------------------------------------------------------+
    // order_by : comment changer l'ordre d'affichage des images dans une	 
    // catégorie ?
    //
    // Il y a plusieurs champs qui peuvent servir à ordonner l'affichage :
    //
    //  - date_available : date d'ajout dans la galerie
    //  - file : le nom du fichier
    //  - id : l'identifiant unique de l'image
    //  - date_creation : la date de création
    //  - rank : position manuel des photos
    //
    //  ATTENTION: avec date_creation si votre APN ne renseigne pas l'heure
    //  Piwigo classera vos photo différemment en l'absence de ce
    // renseignement. 
    // 
    // Une fois que vous avez choisi quels champs utiliser, vous devez choisir
    // l'ordre croissant ou décroissant sur chaque champ. Exemples :
    //
    // 1. $conf['order_by'] = " order by date_available desc, file asc";
    //    va ordonner selon la date d'ajout par ordre croissant, puis sur le
    // nom du fichier par ordre croissant
    //
    // 2. $conf['order_by'] = " order by file asc";
    //    va ordonner selon le nom du fichier par ordre croissant
    $conf['order_by'] = ' ORDER BY date_available DESC, file ASC, id ASC';
    //
    // 3. $conf['order_by_inside_category'] = $conf['order_by'];
    //    Cette ligne "obligatoire" pour appliquer vos paramètres aux
    //    sous albums.
    $conf['order_by_inside_category'] = $conf['order_by'];
    // file_ext : extensions des fichiers autorisés, sensible à la casse
    $conf['file_ext'] = array('jpg','JPG','jpeg','JPEG',
                              'png','PNG','gif','GIF','mpg','zip',
                              'avi','mp3','ogg');
     
    // picture_ext : extensions pour les fichiers de type image, doit être un
    // sous ensemble de $conf['file_ext']
    $conf['picture_ext'] = array('jpg','JPG','jpeg','JPEG',
                                 'png','PNG','gif','GIF');
     
    // top_number : nombre d'éléments à afficher pour les catégories spéciales
    // "les plus visitées", "les mieux notées".
    $conf['top_number'] = 15;
     
    // anti-flood_time : nombre de secondes entre 2 commentaires,
    // 0 pour désactiver
    $conf['anti-flood_time'] = 60;
     
    // comment_spam_reject : les commentaires considérés comme des spam
    // ne sont pas enregistrés (false permet de les enregistrer malgré tout
    // mais ils nécessiteront
    // une validation de l'administrateur)
    $conf['comment_spam_reject'] = true;
     
    // comment_spam_max_links :
    // nombre maximum de liens dans les commentaires avant de les considérer
    // comme des spams ( 0 : alors 1 lien, c'est déjà considéré comme du spam).
    $conf['comment_spam_max_links'] = 3;
     
    // calendar_datefield : champs date de la table "images" utilisé pour le
    // calendrier.
    $conf['calendar_datefield'] = 'date_creation';
    // calendar_show_any : Le calendrier dispose d'une option 'tout' dans
    // la barre de navigation année/mois/semaine/jour
    $conf['calendar_show_any'] = true;
     
    // calendar_show_empty : Le calendrier montre les semaines/mois et autres 
    // même vides
    $conf['calendar_show_empty'] = true;
     
    // calendar_month_cell_width, calendar_month_cell_height : défini
    // la hauteur et largeur des cellules de la vue mensuelle.
    // Un 0 indiquera que la vue ne sera pas affichée.
    // Recommandation largeur et hauteur égales et inférieures à celles des
    // miniatures. REMARQUE tn_width et tn_height
    // DEVRAIENT CORRESPONDRE APPROXIMATIVEMENT A LA TAILLE REELLE DES
    // MINIATURES, AUTREMENT LES IMAGES NE SERAIENT ÊTRE AFFICHÉES CORRECTEMENT.
    $conf['calendar_month_cell_width'] =80;
    $conf['calendar_month_cell_height']=80;
     
    // newcat_default_commentable : lors de sa création, une catégorie doit être
    // commentable ou non ?
    $conf['newcat_default_commentable'] = true;
     
    // newcat_default_visible : lors de sa création, une catégorie doit être
    // visible ou non ? Attention, si la catégorie parente est invisible, la
    // catégorie fille est automatiquement invisible (invisible = verrouillée)
    $conf['newcat_default_visible'] = true;
     
    // newcat_default_status : lors de sa création, une catégorie doit être
    // publique ou privée ? Attention, si la catégorie parente est privée,
    // alors la catégorie fille est automatiquement privée.
    $conf['newcat_default_status'] = 'public';
     
    // level_separator : chaîne de caractères séparant 2 niveaux
    // decatégorie. Suggestions : ' / ', ' » ', ' → ', ' - ', ' >'
    $conf['level_separator'] = ' / ';
     
    // paginate_pages_around : sur les barre de pagination, combien de pages
    // afficher avant et après la page courante ?
    $conf['paginate_pages_around'] = 2;
     
    // tn_width : largeur par défaut pour la création des miniatures
    $conf['tn_width'] = 128;
     
    // tn_height : hauteur par défaut pour la création des miniatures
    $conf['tn_height'] = 96;
     
    // tn_compression_level : niveau de compression lors de la création
    // des miniatures.
    // 0 est très petit, 100 est la meilleur qualité.
    $conf['tn_compression_level'] = 75;
     
    // show_version : afficher le numéro de version de Piwigo en bas de
    // chaque page ?
    $conf['show_version'] = false;
     
    // meta_ref : to reference multiple sets of incorporated pages or elements
    // Set it false to avoid referencing in google, and other search engines.
    $conf['meta_ref'] = true;
     
    // links : liste de liens externes à ajouter dans le menu. Un exemple valant
    // mieux qu'une longue explication (cas simple):
    //
    // $conf['links'] = array(
    //   'http://fr.piwigo.org' => 'Site Français Piwigo',
    //   'http://fr.piwigo.org/forum/' => 'Forum Français de Piwigo',
    //   'http://fr.piwigo.org/doc/' => 'Wiki Français de Piwigo'
    //   );
    //
    //  Chaque lien est référencé par une étiquette.
    //
    // Utilisation avancée:
    // Vous pouvez utiliser des options. Au lieu de donner une simple étiquette 
    // en paramètre, vous allez transmettre un tableau de plusieurs paramètres  
    //  Exemple:
    //  $conf['links'] = array(
    //    'http://fr.piwigo.org' => 
    //              array('label' => 'PWG website', 
    //                    'new_window' => false, 
    //                    'eval_visible' => 'return true;'),
    //    'http://fr.piwigo.org/forum/' => 
    //              array('label' => 'For ADMIN', 
    //                    'new_window' => true, 
    //                    'eval_visible' => 'return is_admin();'),
    //    'http://fr.piwigo.org/doc/' => 
    //              array('label' => 'For Guest', 
    //                    'new_window' => true, 
    //                    'eval_visible' => 'return $user[\'is_the_guest\'];'),
    //    'http://fr.piwigo.org/basics/downloads' => 
    //              array('label' => 'PopUp', 
    //                    'new_window' => true, 
    //                    'nw_name' => 'PopUp', 
    //                    'nw_features' =>
    // 'width=800,height=450,location=no,status=no,toolbar=no,scrollbars=no,menubar=no'),
    //    );
    //
    // Explications des paramètres :
    //  'label':
    //      l'étiquette à afficher dans le menu pour ce lien, obligatoire
    //  'new_window':
    //      si true alors Piwigo ouvrira une nouvelle fenêtre ou un onglet
    //      [true, si le paramètre est absent]
    //  'nw_name':
    //    Nom de la fenêtre si 'new_window' => true
    //    [Pas de nom pour cette fenêtre, si le paramètre est absent]
    //  'nw_features':
    //    options complémentaires si 'new_window' => true
    //    [Pas d'option particulière, si le paramètre est absent]
    //  'eval_visible':
    //    return d'une expression php afin de déterminer si le lien est à
    //    afficher ou non
    //    [return true, si le paramètre est absent]
    //
    // Equivalence:
    //  $conf['links'] = array(
    //    'http://fr.piwigo.org/' => 'PWG website',
    //    );
    //  $conf['links'] = array(
    //    'http://fr.piwigo.org/' => 
    //          array('label' => 'PWG website', 
    //                'new_window' => false, 
    //                'eval_visible' => 'return true;'),
    //    );
    //
    // Conseil : Faites valider votre 'Links' par un spécialiste php sur
    // notre forum
    //
    // Si la liste est vide, le sous menu "liens" n'apparaît pas.
    $conf['links'] = array();
    // random_index_redirect : redirection aléatoire en cas d'absence de
    // paramètre sur le lien index.php Un petit exemple en guise d'explication :
    //
    //  A chaque lien est associé une condition php en sachant que
    //            '' sera equivalent à 'return true;'
    //  $conf['random_index_redirect'] = array(
    //    PHPWG_ROOT_PATH.'index.php?/best_rated' => 'return true;',
    //    PHPWG_ROOT_PATH.'index.php?/recent_pics' => 'return $user[\'is_the_guest\'];',
    //    PHPWG_ROOT_PATH.'random.php' => '',
    //    PHPWG_ROOT_PATH.'index.php?/categories' => '',
    //    );
    // Conséquences : l'accueil sera aléatoire entre les quatres options
    // (sauf pour les membres qui n'auront pas l'accueil sur les dernières
    // images (c'est un exemple). 
    $conf['random_index_redirect'] = array();
    // reverse_home_title : Si Piwigo is votre page d'acceuil.
    // C'est un bon paramètre pour les robots indexeurs.
    // Nous vous recommandons de la mettre a "true" seulement la page "index"
    // changera de titre.
    $conf['reverse_home_title'] = false;
     
    // Un petit message en haut de chaque page où l'header est affiché
    // example $conf['header_notes']  = array('Test', 'Hello');
    $conf['header_notes']  = array();
     
    // show_thumbnail_caption : sur la page des miniatures, afficher une légende
    // sous chaque miniature ?
    $conf['show_thumbnail_caption'] = true;
     
    // show_picture_name_on_title : sur la page de visualisation d'une image,
    // afficher le nom de l'image en titre ?
    $conf['show_picture_name_on_title'] = true;
    // display_fromto : display the date creation bounds of a category.
    $conf['display_fromto'] = false;
    // allow_random_representative : pour représenter un album,
    // souhaitez-vous que Piwigo recherche parmi les éléments un nouveau
    // représentant toutes les X minutes ?
    // Si ce paramètre est à "false", un élément est choisi au hasard ou bien
    // manuellement pour chaque album et reste le représentant tant que
    // l'administrateur ne change pas de représentant.
    // Attention : mettre ce paramètre à "true" va être consommateur de
    // ressources serveur.
    ```
    
    ```php
    // Si vous décidez de changer la valeur de ce paramètre, un administrateur
    // doit mettre à jour les informations des albums  dans l'écran
    // [ Administration >> Outils >> Maintenance ]
    $conf['allow_random_representative'] = false;
    // allow_html_descriptions : autoriser les administrateurs à utiliser du
    // HTML dans les descriptions de la galerie, des catégories et des images.
    $conf['allow_html_descriptions'] = true;
     
    // prefix_thumbnail : chaîne de caractère préfixant le nom de fichier dans
    // le répertoire "thumbnail" de chaque répertoire d'images. Ce préfixe ne
    // peut contenir que des caractères parmi : a à z (sensible à la casse, "-"
    // ou "_".
    $conf['prefix_thumbnail'] = 'TN-';
     
    // dir_thumbnail : nom du sous-répertoire qui contient les miniatures.
    $conf['dir_thumbnail'] = 'thumbnail';
     
    // users_page : combien d'utilisateurs montrer par page sur l'écran
    // [Administration > Identification > Utilisateurs]
    $conf['users_page'] = 20;
     
    // available_permission_levels :
    // Les niveaux de permissions image disponibles dans l'interface
    // administrateur
    $conf['available_permission_levels'] = array(0,1,2,4,8);
     
    // mail_options : ne mettre à vrai que si un message d'erreur apparaît lors
    // de l'envoi d'un email.
    $conf['mail_options'] = false;
     
    // send_bcc_mail_webmaster : envoyer une copie masquée au webmaster. 
    // Mettre à true pour des tests ou pour analyser un problème
    $conf['send_bcc_mail_webmaster'] = false;
     
    // default_email_format :
    //  Indique le format par défaut à utiliser pour les messages
    //  Au choix : text/plain ou text/html
    $conf['default_email_format'] = 'text/html';
     
    // alternative_email_format: défini le format qui sera utilisé pour envoyez
    // les courriels. Doit être égale à : text/plain ou text/html
    $conf['alternative_email_format'] = 'text/plain';
     
    // mail_sender_name : défini le nom de l'expediteur du mail:
    // Si la valeur est vide, ca sera le nom de la galerie qui sera utilisé.
    $conf['mail_sender_name'] = '';
     
    // smtp configuration
    // (fonctionne si la fonction fsockopen est attribué au port SMTP
    // smtp_host: numéro du port smtp du serveur.
    //  Si NULL, la fonction mail du serveur sera utilisée.
    //   format: hoststring[:port]
    //   exemple: smtp.pwg.net:21
    // smtp_user/smtp_password: user & password for smtp identication
    $conf['smtp_host'] = '';
    $conf['smtp_user'] = '';
    $conf['smtp_password'] = '';
     
    // check_upgrade_feed: contrôle si une mise à jour de la BDD est requise.
    // Si true, un message vous encouragement vivement à mettre à jour votre BDD
    // si besoin était.
    //
    // Ce paramètre ne sert qu'à des fins de tests sur des version de Piwigo
    // qui sont en développement. Il n'y a aucune raison de placer ce paramètre
    // à true.
    $conf['check_upgrade_feed'] = false;
     
    // rate_items : valeurs des notes d'une image
    $conf['rate_items'] = array(0,1,2,3,4,5);
     
    // default_redirect_method : Méthode par défaut pour les redirections
    // ('http' ou 'html')
    $conf['default_redirect_method'] = 'http';
     
    // double_password_type_in_admin : défini s'il faut un second champs pour
    // confirmer la saisie d'un mot de passe dans le panneau d'administration
    // des utilisateurs.
    $conf['double_password_type_in_admin'] = false;
    // insensitive_case_logon : défini si le login doit être insensible à
    // la casse.
    // Si True, le login "user" équivaudra à "User" ou "USER" ou "uSer"...
    // Il ne sera plus possible de créer un nouvelle login sur cette base.
    $conf['insensitive_case_logon'] = false;
     
    // uniqueness_mode : par quel moyen de contrôle (comparaison) sera détecté
    // les nouvelles photos.
    // Doit être 'md5sum' ou 'filename'
    $conf['uniqueness_mode'] = 'md5sum';
     
    // +-----------------------------------------------------------------------+
    // | Les méta-données                                                      |
    // +-----------------------------------------------------------------------+
     
    // show_iptc: montrer les métadonnées IPTC sur picture.php si l'utilisateur
    // le demande.
    $conf['show_iptc'] = false;
     
    // show_iptc_mapping : correspondance entre un élément de langue et un
    // identifiant IPTC. Cette correspondance est utilisé pour montrer les IPTC
    // sur picture.php. Pour chaque clé du tableau, vous avez besoin d'avoir la
    // même clé dans le tableau de langue $lang.
    //
    // Par exemple, si ma première clé est "iptc_keywords" (associée à
    // l'identifiant IPTC 2#025) alors vous avez besoin de
    // $lang['iptc_keywords'] dans le fichier common.lang.php correspondant à la
    // langue de l'utilisateur. Si la clé n'est pas présente dans le tableau de
    // langue, alors la clé sera affichée non traduite.
    //
    // Pour savoir quels identifiants IPTC sont disponibles, utiliser l'outil
    // tools/metadata.php
    $conf['show_iptc_mapping'] = array(
      'iptc_keywords'        => '2#025',
      'iptc_caption_writer'  => '2#122',
      'iptc_byline_title'    => '2#085',
      'iptc_caption'         => '2#120'
      );
     
    // use_iptc : utiliser les métadonnées IPTC durant la synchronisation.
    $conf['use_iptc'] = false;
     
    // use_iptc_mapping : dans quelles métadonnées IPTC Piwigo va-t-il
    // trouver les informations de l'image ? Ce paramétrage est utilisé durant
    // la synchronisation. Chaque clé du tableau représente une colonne de la
    // table images, chaque valeur correspond à un identifiant IPTC.
    $conf['use_iptc_mapping'] = array(
      'keywords'        => '2#025',
      'date_creation'   => '2#055',
      'author'          => '2#122',
      'name'            => '2#005',
      'comment'         => '2#120'
      );
     
    // show_exif: montrer les métadonnées EXIF sur picture.php
    $conf['show_exif'] = true;
     
    // show_exif_fields : liste des métadonnées EXIF à afficher. Il est possible
    // de choisir des champs parmi des groupes. Par exemple
    // ['COMPUTED']['ApertureFNumber'], pour cela, créer une clé
    // 'COMPUTED;ApertureFNumber'.
    //
    // Le titre de l'information affichée sur picture.php sera une clé de
    // langue, comme $lang['exif_field_Make'] si elle existe. Pour les champs
    // composés, ne prendre en compte que le dernier niveau : pour la clé
    // 'COMPUTED;ApertureFNumber' vous avez besoin de
    // $lang['exif_field_ApertureFNumber']
    $conf['show_exif_fields'] = array(
      'Make',
      'Model',
      'DateTimeOriginal',
      'COMPUTED;ApertureFNumber'
      );
     
    // use_exif : utiliser les métadonnées EXIF lors de la synchronisation.
    $conf['use_exif'] = false;
     
    // use_exif_mapping : même comportement que $conf['use_iptc_mapping']
    $conf['use_exif_mapping'] = array(
      'date_creation' => 'DateTimeOriginal'
      );
     
    // Pour plus d'informations, lire : 
    // http://fr.piwigo.org/doc/doku.php?id=utiliser:utilisation:fonctionnalites:meta
     
     
    // +-----------------------------------------------------------------------+
    // | Les sessions                                                          |
    // +-----------------------------------------------------------------------+
     
    // session_use_cookies: indique si le "cookie" de la session
    // doit être enregistré du coté client
    $conf['session_use_cookies'] = true;
     
    // session_use_only_cookies: indique si le "cookie" de la session
    // doit être enregistré uniquement du coté client (rien sur le serveur)
    $conf['session_use_only_cookies'] = true;
     
    // session_use_trans_sid: utiliser la technique de transparent session id 
    $conf['session_use_trans_sid'] = false;
     
    // session_name: nom de la session utilisé pour sauver le cookie
    $conf['session_name'] = 'pwg_id';
     
    // session_save_handler: comment the line below
    // to use file handler for sessions.
    $conf['session_save_handler'] = 'db';
     
    // authorize_remembering : permet aux utilisateurs de rester connecter
    // longtemps. Cela créé un cookie longue durée sur le poste client.
    $conf['authorize_remembering'] = true;
     
    // remember_me_name: indique le nom du "cookie" pour rester connecté
    $conf['remember_me_name'] = 'pwg_remember';
     
    // remember_me_length : durée de validité pour le cookie longue durée, en
    // secondes.
    $conf['remember_me_length'] = 31536000;
     
    // session_length : durée de validité d'une session normale, en secondes.
    $conf['session_length'] = 3600;
    // +-----------------------------------------------------------------------+
    // | debugage/performances                                                 |
    // +-----------------------------------------------------------------------+
     
    // show_queries : montrer les requêtes SQL et le temps d'exécution
    // de chacune.
    $conf['show_queries'] = false;
     
    // show_gt : monter le temps de génération de chaque page, PHP + SQL.
    $conf['show_gt'] = true;
     
    // debug_l10n : affiche un avertissement à chaque fois qu'on tente d'accéder
    // à une clé inexistante.
    $conf['debug_l10n'] = false;
     
    // debug_template : activate template debugging - a new window will appear
    $conf['debug_template'] = false;
     
    // debug_mail : sauvegarde une copie des mails envoyés dans le répertoire
    // local. Ne sert qu'à des fins de tests.
    $conf['debug_mail'] = false;
     
    // die_on_sql_error: si un problème SQL intervient, faut-il tout arrêter ?
    $conf['die_on_sql_error'] = false;
    
    // compiled_template_cache_language : Si True, les chaînes de langages sont
    // remplacées durant la compilation des templates. Le résultat donne de
    // meilleures performances mais les changements intervenus sur les langues
    // ne seront pas pris en compte tant que les templates compilés ne seront
    // pas purgés.
    $conf['compiled_template_cache_language'] = false;
     
    // template_compile_check : 
    // Ce paramètre demande à Smarty s'il doit vérifier  de recompiler ou pas.
    // Il n'y a pas besoin de re-compilation tant qu'un modèle n'est pas
    // modifié.
    // Les performance sont meilleures mais le résultat (affichage) peut-être
    // faussé.
    $conf['template_compile_check'] = true;
    // template_force_compile : Force Smarty à re(compiler) les templates à
    // chaque demande. Utile uniquement à des fins de tests.
    $conf['template_force_compile'] = false;
    ```
    
    ```php
    
     
    // template_combine_files : Active la combinaison (minified) des fichiers
    // javascript et css.
    $conf['template_combine_files'] = true;
     
    // show_php_errors : cela permet de voir les erreur php.
    // Voir votre fichier de configuration php.ini section 'error_reporting'
    // pour trouver plus de valeurs possibles.
    // Pour désactiver, inscrire  ''
    $conf['show_php_errors'] = E_ALL;
     
    // +-----------------------------------------------------------------------+
    // | Authentication                                                        |
    // +-----------------------------------------------------------------------+
     
    // apache_authentication : utiliser l'authentification HTTP d'Apache comme
    // référence au lieu de la table des utilisateurs ?
    $conf['apache_authentication'] = false;
     
    // users_table : quelle table est la table de référence pour les
    // utilisateurs ? Peut être une table externe à Piwigo.
    //
    // Si vous décidez d'utiliser une table externe, vous devez préparer votre
    // base de données en supprimant certains données :
    //
    // delete from piwigo_user_access;
    // delete from piwigo_user_cache;
    // delete from piwigo_user_feed;
    // delete from piwigo_user_group;
    // delete from piwigo_user_infos;
    // delete from piwigo_sessions;
    // delete from piwigo_rate;
    // update piwigo_images set average_rate = NULL;
    // delete from piwigo_caddie;
    // delete from piwigo_favorites;
    //
    // Toutes les informations contenues dans ces tables sont relatives au
    // contenu de la table des utilisateurs.
    $conf['users_table'] = $prefixeTable.'users';
     
    // D'autres tables peuvent être changées si vous définissez une constante associée.
    // Example:
    //   define('USER_INFOS_TABLE', 'pwg_main'.'user_infos');
     
    // external_authentification : si vous passez par une identification
    // externe il faut changer la valeur pour True
    $conf['external_authentification'] = false;
     
    // D'autres tables peuvent être changées si vous définissez la constante
    // correspondante.
    // Example:
    //   define('USER_INFOS_TABLE', 'pwg_main'.'user_infos');
     
    // user_fields : Le mapping peux se faire sur des champs génériques dans la
    // table spécifique.
    // Par exemple dans Piwigo, le champs "mail adress" est nommé "mail_adress"
    // or dans punbb ce champs est appelé "email".
    $conf['user_fields'] = array(
      'id' => 'id',
      'username' => 'username',
      'password' => 'password',
      'email' => 'mail_address'
      );
     
    // pass_convert : fonction pour chiffrer ou hasher le mot de passe afin de
    // le stocker en base de donnée.
    $conf['pass_convert'] = create_function('$s', 'return md5($s);');
     
    // guest_id : identifiant de l'invité
    $conf['guest_id'] = 2;
     
    // default_user_id : id de l'utilisateur servant de modèle aux nouveaux
    // membres (lors
    // de la création de comptes).
    $conf['default_user_id'] = $conf['guest_id'];
     
    // browser_language : La processus d'enregistrement et de gestion des
    // membres guest/generic prend
    // par défaut la localisation (langue) du navigateur. Si celui-ci n'est pas
    // définissable (disponible),
    // Piwigo prendra par défaut PHPWG_DEFAULT_LANGUAGE
    $conf['browser_language'] = true;
     
    // webmaster_id : identifiant du webmaster
    $conf['webmaster_id'] = 1;
     
    // Est-ce que l'accès visiteur est accepté? (Ce n'est pas une garantie de
    // sécurité, vos catégories doivent être "privée" également)
    // false : l'accès à la galerie des simples visiteurs redirigera vers
    // la page identification.php
    $conf['guest_access'] = true;
    
    // +-----------------------------------------------------------------------+
    // |                               history                                 |
    // +-----------------------------------------------------------------------+
     
    // nb_logs_page : nombre de ligne d'historique à afficher par page
    $conf['nb_logs_page'] = 300;
     
    // +-----------------------------------------------------------------------+
    // |                                 urls                                  |
    // +-----------------------------------------------------------------------+
     
    // question_mark_in_urls : Générer un ? dans les URL. Ne peut être
    // à false uniquement si le champ PATH_INFO sera converti (ce qui dépend 
    // de la directive AcceptPathInfo de la configuration du serveur)
    $conf['question_mark_in_urls'] = true;
     
    // php_extension_in_urls : si true, les URLs génerées pour picture et
    // category n'intègreront plus l'extension .php . Ne fonctionne que si
    // .htaccess comporte un paramètre Options +MultiViews ou une règle de
    // ré-écriture d'url.
    $conf['php_extension_in_urls'] = true;
     
    // category_url_style : donne l'indication sur la forme de la catégorie
    // dans l'url
    $conf['category_url_style'] = 'id';
     
    // picture_url_style : 'id' (défaut), ou 'id-file' ou 'file'. 'id-file'
    // ou 'file' signifient que le nom de fichier sans extension apparaîtra
    // dans l'URL (l'adresse Internet).
    // Notez qu'une requête SQL supplémentaire sera exécutée si
    // 'file'/'id-file' indiqué.
    // Notez également que vous pourriez relever des anomalies de navigation 
    // si vous choisissiez 'file' et que vos noms de fichiers ne soient pas
    // uniques.
    $conf['picture_url_style'] = 'id';
     
    // tag_url_style : 'id-tag' (défaut), ou 'id' ou 'tag'.
    // Notez qu'en choisissant 'tag' la valeur ASCII de l'URL pourrait ne plus
    // correspondre à une valeur unique, le résultat serait de montrer tous les
    // tags correspondant à cette valeur.
    $conf['tag_url_style'] = 'id-tag';
    
    // +-----------------------------------------------------------------------+
    // |                                 tags                                  |
    // +-----------------------------------------------------------------------+
     
    // full_tag_cloud_items_number : Nombre de tags à faire apparaître dans le
    // nuage. Uniquement les tags les plus fréquents sont alors affichés.
    $conf['full_tag_cloud_items_number'] = 200;
     
    // menubar_tag_cloud_items_number : Nombre de tags pour ceux affichés dans
    // la barre de menu... (ceux qui représentent le plus d'images).
    $conf['menubar_tag_cloud_items_number'] = 100;
     
    // content_tag_cloud_items_number : Même chose mais dans la partie contenu 
    // (à droite), à l'exception du résultat de tags.php
    // lequel se gère par 'full_tag_cloud_items_number'
    // les tags ne sont pas toujours présents en 1.7 sur les contenus de
    // miniatures
    $conf['content_tag_cloud_items_number'] = 12;
     
    // tags_levels : nombre de niveaux à utiliser pour l'affichage. A chaque
    // niveau correspond une class CSS tagLevelX (tagLevel1, tagLevel2, etc.).
    $conf['tags_levels'] = 5;
     
    // tags_default_display_mode : par défaut, groupe les tags par lettres
    // (letter) ou affiche un nuage de tag (cloud).  'letters' ou 'cloud'.
    $conf['tags_default_display_mode'] = 'cloud';
     
    // tag_letters_column_number : nombre de colonnes à afficher dans la page
    // tag par lettres
    $conf['tag_letters_column_number'] = 4;
    
    // +-----------------------------------------------------------------------+
    // | Notification by mail                                                  |
    // +-----------------------------------------------------------------------+
     
    // nbm_default_value_user_enabled : Notification par courriel active ou non
    $conf['nbm_default_value_user_enabled'] = false;
     
    // nbm_list_all_enabled_users_to_send :
    // Liste de complète des inscrits (liste complete sans contrôle des
    // nouveautés)
    // Plus rapide à constituer, mais moins facile à utiliser
    $conf['nbm_list_all_enabled_users_to_send'] = false;
     
    // nbm_max_treatment_timeout_percent : ratio de Timeout (temps dépassé sur
    // le serveur). Seuil d'utilisation du temps écoulé par les envois d'email
    // lequel permet d'éviter des erreurs (Timeout) en cours d'envois.
    // Le processus est réinitialisé (sans les messages déjà expédiés).
    $conf['nbm_max_treatment_timeout_percent'] = 0.8;
     
    // nbm_treatment_timeout_default :
    // Si le timeout ne peut pas être anticipé par 
    // nbm_max_treatment_timeout_percent, nbm_treatment_timeout_default alors
    // on se basera sur un nombre de messages
    $conf['nbm_treatment_timeout_default'] = 20;
     
    // Paramètres utilisés dans get_recent_post_dates (période récente) pour les
    // 2 types de notification
    $conf['recent_post_dates'] = array(
      'RSS' => array('max_dates' => 5, 'max_elements' => 6, 'max_cats' => 6),
      'NBM' => array('max_dates' => 7, 'max_elements' => 3, 'max_cats' => 9)
      );
     
    // l'auteur montré dans le flux RSS (element <author>)
    $conf['rss_feed_author'] = 'Piwigo notifier';
    
    // +-----------------------------------------------------------------------+
    // | Paramètres propres à l'administration                                 |
    // +-----------------------------------------------------------------------+
     
    // admin_layout : thème par défaut pour l'administrateur.
    // ATTENTION: est différent du thème Yoga/Sylvia !
    $conf['admin_theme'] = 'roma';
     
    // enable_plugins : Doit-on charger les Plugins? true=oui, false=non
    $conf['enable_plugins']=true;
     
    // allow_web_services : Les Web services sont admis (true) ou totalement
    // interdits (false)
    $conf['allow_web_services'] = true;
     
    // ws_enable_log : Activer les logs pour les web services
    $conf['ws_enable_log'] = false;
     
    // ws_log_filepath : emplacement du fichier de log
    $conf['ws_log_filepath'] = '/tmp/piwigo_ws.log';
     
    // ws_max_images_per_page : Nombre maximum d'image retourné dans chaque
    // appel d'un web service
    $conf['ws_max_images_per_page'] = 500;
     
    // show_newsletter_subscription : Affiche un lien pour souscrire à la
    // newsletter
    // d'annonce de piwigo
    $conf['show_newsletter_subscription'] = true;
      
    ```
    
    ```php
    
    // +-----------------------------------------------------------------------+
    // | Filtres                                                               |
    // +-----------------------------------------------------------------------+
     
    // $conf['filter_pages'] contiendra la configuration des pages
    //   o Si les valeurs ne sont pas spécifiées pour une page, celles par
    //     défaut
    //     s'appliqueront
    //   o Les éléments du tableau correspondent au nom de chaque page sans le
    ///    .php
    //   o Différentes valeurs:
    //     - used: Le filtre est utilisable
    //       (si false aucun filtre ne sera appliqué [start, cancel, stop, ...]
    //     - cancel: (true) ignore le filtre actif
    //     - add_notes: Ajoute la note de haut de page indiquant que le filtre
    //       est actif
    //   o Une configuration vide désactivera le filtre
    //     Pas de filtre = Pas d'icone = pas de note... =>
    //     $conf['filter_pages'] = array();
    $conf['filter_pages'] = array
      (
        // Default page
        'default' => array(
          'used' => true, 'cancel' => false, 'add_notes' => false),
        // Real pages
        'index' => array('add_notes' => true),
        'tags' => array('add_notes' => true),
        'search' => array('add_notes' => true),
        'comments' => array('add_notes' => true),
        'admin' => array('used' => false),
        'feed' => array('used' => false),
        'notification' => array('used' => false),
        'nbm' => array('used' => false),
        'popuphelp' => array('used' => false),
        'profile' => array('used' => false),
        'ws' => array('used' => false),
        'identification' => array('cancel' => true),
        'install' => array('cancel' => true),
        'password' => array('cancel' => true),
        'register' => array('cancel' => true),
      );
     
    // +-----------------------------------------------------------------------+
    // | Diaporama                                                             |
    // +-----------------------------------------------------------------------+
     
    // slideshow_period : periode d'attente (par défaut) en seconde avant le 
    // chargement d'une nouvelle page pendant le diaporama automatique.
    // slideshow_period_min, slideshow_period_max sont les maximum que 
    // slideshow_period peut prendre.
    // slideshow_period_step est l'interval de navigation entre min et max
    $conf['slideshow_period_min'] = 1;
    $conf['slideshow_period_max'] = 10;
    $conf['slideshow_period_step'] = 1;
    $conf['slideshow_period'] = 4;
     
    // slideshow_repeat : diaporama en boucle des images
    $conf['slideshow_repeat'] = true;
     
    // $conf['light_slideshow'] indique l'utilisation de slideshow.tpl au lieu
    // de picture.tpl en mode diaporama. Attention vous devez avoir
    // slideshow.tpl dans tous les templates disponibles
    // ou alors le mettre à false.
    // Pensez à vérifier si les plugins d'images sont compatibles avec ce mode
    // Tout plugin à partir de la 1.7 devrait être conçu pour gérer
    // light_slideshow.
    $conf['light_slideshow'] = true;
     
    // +-----------------------------------------------------------------------+
    // | Autres paramètres                                                     |
    // +-----------------------------------------------------------------------+
     
    // local_data_dir : le répertoire local utilisé pour stocker les 
    // données comme les templates compilés ou d'autres variables de plugins,
    // etc.
    $conf['local_data_dir'] = dirname(dirname(__FILE__)).'/_data';
     
    // upload_dir : Où voullez-vous que l'API/UploadForm stock vos photos ?
    // Ce chemin doit être relatif au répertoire d'installation de Piwigo
    // (mais peut être à l'extérieur, du temps qu'il est accessible à partir de
    // votre serveur web).
    $conf['upload_dir'] = './upload';
     
    // no_photo_yet_url : Où peux-être guidé l'utilisateur quand la galerie ne
    // dispose d'aucune photos (cas lors de l'installation) ?
    $conf['no_photo_yet_url'] = 'admin.php?page=photos_add';
     
    // themes_dir : répertoire où sont stockés les thèmes
    $conf['themes_dir'] = PHPWG_ROOT_PATH.'themes';
     
    // pLoader direct download url for windows
    $conf['ploader_download_windows'] = 'http://piwigo.org/ext/download.php?eid=270';
     
    // pLoader direct download url for mac
    $conf['ploader_download_mac'] = 'http://piwigo.org/ext/download.php?eid=353';
     
    // pLoader direct download url for linux
    $conf['ploader_download_linux'] = 'http://piwigo.org/ext/download.php?eid=269';
     
    // enable_synchronization : Active la synchronisation pour l'ajout de
    // photos.
    $conf['enable_synchronization'] = true;
     
    // caractères autorisés pour la synchronisation
    $conf['sync_chars_regex'] = '/^[a-zA-Z0-9-_.]+$/';
     
    // alternative_pem_url : lien alternatif pour l'utilisation de PEM.
    // Laisser vide par défaut.
    $conf['alternative_pem_url'] = '';
     
    // upload_form_automatic_rotation : l'orientation automatique des photos
    // est basée sur le tags spécifique des informations EXIF de la photo.
    $conf['upload_form_automatic_rotation'] = true;
     
    // type de lien pour les images 'dérivées' 0-'auto', 1-'derivative' 2-'script'
    $conf['derivative_url_style']=0;
     
    $conf['chmod_value']= substr_compare(PHP_SAPI, 'apa', 0, 3)==0 ? 0777 : 0755;
     
    // type d'images par défaut pour la page picture.php : 'small', 'medium' or 'large'
    $conf['derivative_default_size'] = 'medium';
    ?>
    ```
