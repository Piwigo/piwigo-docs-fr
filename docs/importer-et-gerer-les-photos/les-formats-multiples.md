# Les formats multiples

Les formats multiples permettent, pour une même photo ou image, de proposer plusieurs versions en téléchargement, par exemple :

- une version JPG et une version PNG ;
- une version JPG, une version PSD et une version PDF
- etc.

!!! info
    Si vous êtes client d’une offre piwigo.com, cette fonctionnalité n’est accessible qu’à partir de l’offre Entreprise.


## Comment activer les formats multiples ?

La réponse est différente suivant que vous hébergiez vous-même votre galerie ou que vous soyez un client d’une offre piwigo.com.

- J’héberge moi-même ma galerie (ou mon organisation le fait)
    
    Pour activer cette option, vous devez utilisez [LocalFile Editor](/hebergez-votre-piwigo/modifier-la-configuration-locale-avec-localfiles-editor) et ajouter le code ci-dessous dans votre fichier de configuration. Si vous n’en avez pas la possibilité, faites la demande au webmaster qui gère votre galerie.
    
    ```php
    // enable_formats: should Piwigo search for multiple formats?
    $conf['enable_formats'] = true;
    ```
    
    Vous pouvez modifier les formats acceptés par défaut avec le paramètre de configuration suivant.
    
    ```php
    // photo (or nay other file). Formats are in sub-directory pwg_format.
    $conf['format_ext'] = array('cr2', 'tif', 'tiff', 'nef', 'dng', 'ai', 'psd');
    ```
    
- Je suis client d’une offre piwigo.com
    
    Cette fonctionnalité est accessible aux clients [piwigo.com](http://piwigo.com) qui ont souscrit à une offre Entreprise ou VIP. Pour l’activer sur votre galerie, vous devez en faire la demande au support.
    

## Ajouter des formats multiples sur une photo

Une fois l’option “formats multiples” activée, un nouvel onglet “Formats” apparaît lorsque vous éditez une photo dans l’administration de Piwigo.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-2e23a7e2.png)

Cliquez sur “Ajouter des formats” pour ajouter une ou plusieurs versions de la photo en cours.

Vous arrivez alors sur le formulaire d’ajout de photo. La photo à associer aux nouveaux formats est rappelée. Vous pouvez ajouter autant de formats que vous le souhaitez parmi ceux qui sont acceptés par votre configuration.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-7ad48c64.png)

Cliquez sur “Démarrer le transfert” pour envoyer les fichiers sur le serveur.

Une fois les formats ajoutés, vous pouvez les visualiser depuis l’onglet Formats de votre photo dans l’administration.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-faf53ce7.png)

Notez qu’une fois l’option “formats multiples” activée, vous pouvez également ajouter de nouveaux formats depuis la page d’ajout de photos, en cochant l’option “Télécharger des formats”. Dans ce cas, les noms de fichiers doivent être les mêmes que le fichier pour lequel vous voulez ajouter ces nouveaux formats.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-2cb229b0.png)

## Afficher les formats multiples sur ma galerie

Pour pouvoir afficher les différents formats disponibles pour une photo sur votre galerie, vous devez installer le plugin **Download Formats Buttons.**

Une fois ce plugin activé, le bouton de téléchargement d’un fichier affiche les différents formats disponibles ainsi que la taille du fichier. Cliquez sur le format choisi pour le télécharger.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-df8c2a73.png)

Sommaire de l’article

---

← Précédent

[Gérez les propriétés et métadonnées de vos fichiers](/importer-et-gerer-les-photos/gerez-les-proprietes-et-metadonnees-de-vos-fichiers)
