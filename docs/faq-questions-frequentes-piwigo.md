# FAQ - Les questions les plus fréquentes sur Piwigo

**Nous avons récapitulé dans cette page toutes les réponses aux questions qu’on nous pose souvent sur l’utilisation de Piwigo.** 

**Si vous avez un problème, commencez par regarder ici !**

Cliquez sur la flèche pour afficher la réponse à une question.

---

- Au secours, je ne vois pas mes photos / mes albums !
    
    Vous avez créé un album et ne le voyez pas sur votre galerie ?
    
    Pas de panique ! C’est sans doute une question de permissions. 
    
    Si votre album est privé, et que vous ne vous êtes pas accordé les droits sur cet album, alors il est normal que vous ne le voyez pas sur la galerie.
    
    Pour vérifier, rendez-vous dans l’administration, Albums > Gérer. Recherchez votre album et éditez-le. Rendez-vous dans l’onglet “Permissions”. Si votre album est privé, vérifiez que vous avez la permission de le voir.
    
    [En savoir plus sur les permissions sur les albums](organiser-les-albums/permissions-et-visibilite-des-albums)
    
    Si vous avez bien la permission de visualiser cet album, assurez-vous qu’il n’est pas vide (sans aucune photo). Les albums vides ne sont pas visibles sur la galerie.
    
    Si vous voyez un album mais qu’un autre utilisateur ne le voit pas, alors qu’il a bien les permissions sur cet album : vérifiez que l’album n’est pas verrouillé !
    
- Les emails envoyés par mon Piwigo n’arrivent pas (ou arrivent dans les SPAMs)
    
    Les emails de notification envoyés par Piwigo ont pour expéditeur l’email de l’administrateur principal (webmestre) de Piwigo, c’est à dire le premier utilisateur créé. 
    
    Parfois, le serveur qui héberge votre Piwigo n’a pas le droit d’envoyer des emails avec cette adresse, alors ils arrivent en SPAM ou n’arrivent pas du tout à destination.
    
    Pour régler ce problème, vous avez plusieurs solutions :
    
    - Modifier l’adresse email du webmestre : Pour que les emails arrivent à destination, il faut que votre site Piwigo soit autorisé à envoyer des emails avec l’adresse du webmestre de votre site. Si cette adresse est une adresse de type Gmail, Yahoo, etc, l’envoi d’email depuis Piwigo risque de ne pas fonctionner. L’idéal est que l’adresse email du webmestre soit associée au même nom de domaine que celui de votre galerie. Par exemple, si votre galerie a pour adresse photos.monsite.com, l’idéal est que l’adresse email du webmestre soit une adresse de type *@monsite.com.
    - Installer le plugin Protect Notification : Le plugin Protect Notification remplace l’expéditeur des emails par une adresse de type no-reply@monsite.com (monsite.com étant remplacé par le nom de domaine de votre galerie). En général, l’installation de ce plugin résout les problèmes d’emails. Depuis février 2024, Protect Notification est activé par défaut sur les nouveaux comptes Piwigo.
    - ⚠️ Ces solutions ne résolvent pas les problèmes de réception des emails envoyés par le plugin Contact Form, car ceux-ci ont pour expéditeur l’adresse mail saisie dans le formulaire. Pour résoudre les problèmes avec le plugin Contact Form, [consultez cette page](personnaliser-ma-galerie/ajouter-des-pages-a-votre-galerie).
- Comment supprimer mon compte piwigo.com ?
    
    Contactez le support à l’adresse support@piwigo.com.
    
- Comment associer ma galerie piwigo.com à un nom de domaine personnalisé ?
    
    Par défaut tous les comptes piwigo.com ont une adresse web de la forme *.piwigo.com. Vous pouvez ajouter votre propre nom de domaine, ou un simple sous-domaine.
    
    Etant donné que [Piwigo.com](http://piwigo.com/) ne vend pas de noms de domaine, il faudra l'acheter auprès d'un fournisseur de noms de domaine, comme OVH.
    Envoyez nous un email à [support@piwigo.com](mailto:support@piwigo.com) et dites nous quel est votre nom de domaine (ou sous-domaine). Nous configurerons les serveurs piwigo.com et nous vous expliquerons comment configurer votre nom de domaine.
    Une fois que la configuration DNS sera propagée, nous ajouterons une couche de sécurité avec HTTPS.
    
- Comment renommer mon compte piwigo.com ?
    
    Contactez le support à l’adresse support@piwigo.com.
    
- Comment modifier le titre de ma galerie Piwigo ?
    
    Pour modifier le titre de votre galerie, rendez-vous dans l’administration de votre Piwigo, menu Configuration > Option. Sur le premier onglet, vous pouvez modifier le nom de votre galerie dans le premier champ “Titre de la galerie”.
    
- Comment faire pour que ma galerie soit visible sur les moteurs de recherche ?
    
    Une fois votre galerie créée, elle devrait être visible sur les moteurs de recherche. Mais si votre nom de domaine est récent, ou si vous n’avez pas beaucoup de trafic, cela peut prendre un certain temps. 
    
    Pour dire aux moteurs de recherche que votre galerie Piwigo existe, voici quelques conseils :
    
    - Ajoutez des liens vers votre galerie sur des sites web qui ont déjà des visiteurs
    - Partagez votre galerie sur les réseaux sociaux
    - Ajoutez votre galerie à l’outil [Google Search Console](https://search.google.com/search-console) (pour Google) ou bien [Bing Webmaster Tools](https://www.bing.com/webmasters/) (pour Bing).
- Comment faire pour que ma galerie ne soit PAS visible sur les moteurs de recherche ?
    
    Si vous voulez que votre galerie ne soit pas visible sur les moteurs de recherche, vous pouvez créer un fichier robots.txt à la racine de votre site (si vous hébergez vous-même votre Piwigo) et ajouter dans ce fichier les lignes suivantes :
    
    ```html
    User-agent: *
    Disallow: /
    ```
    
    Vous pouvez également régler la visibilité de votre galerie sur les moteurs de recherche en installant le plugin Meta. Ce plugin permet de paramétrer au global et page par page les métadonnées de votre site pour les moteurs de recherche. 
    
    Pour désactiver complètement l’indexation de votre galerie Piwigo sur les moteurs de recherche avec le plugin Meta, rendez-vous dans la configuration du plugin, et sur le premier onglet, sélectionner la métadonnée “robots”. Éditez la métadonnée et saisissez la valeur `noindex`, puis cliquez sur Insérer la métadonnée.
    
    [En savoir plus sur les plugins pour le référencement de votre galerie](administrer-piwigo/plugins-pour-les-administrateurs)
    
- Comment régler le titre et la description de ma galerie sur les moteurs de recherche ?
    
    Pour personnaliser la façon dont s’affichent les pages de votre galerie sur les moteurs de recherche, installez les plugins Title et plugin Meta.
    
    Le plugin Title permet de modifier le titre qui s’affiche pour chaque page sur les moteurs de recherche.
    
    Le plugin Meta permet de modifier la description qui s’affiche pour chaque page sur les moteurs de recherche.
    
    ![meta.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-f2f860b7.png)
    
    [En savoir plus sur les plugins pour le référencement de votre galerie](administrer-piwigo/plugins-pour-les-administrateurs)
    
- Comment modifier l’apparence de ma galerie lorsque je la partage sur les réseaux sociaux ?
    
    Pour personnaliser l’apparence (titre, de description, image…) des pages de votre galerie lorsque vous les partagez sur les réseaux sociaux, vous pouvez installer le plugin **Meta Open Graph**. [En savoir plus](administrer-piwigo/plugins-pour-les-administrateurs)
    
- Comment modifier le pied de page (footer) de ma galerie ?
    
    Par défaut, votre galerie affiche un texte en pied de page avec un lien vers piwigo.com ou piwigo.org (selon que votre galerie soit hébergée chez piwigo.com ou sur votre hébergement).
    
    Si vous souhaitez personnaliser le pied de page (footer) de votre galerie, vous pouvez installer le plugin **Perso Footer** ([en savoir plus](personnaliser-ma-galerie/personnaliser-votre-galerie-avec-des-plugins)).
    
    Si vous voulez complètement masquer le pied de page (et ne pas faire de pub à Piwigo 😢) vous pouvez ajouter le code suivant dans le fichier CSS du site via le plugin LocalFiles Editor ([en savoir plus sur LocalFiles Editor](hebergez-votre-piwigo/modifier-la-configuration-locale-avec-localfiles-editor)). Toutefois, ce serait dommage de le faire.
    
    ```css
    #copyright{display: none;}
    ```
    
    Enfin, vous pouvez également créer un pied de page personnalisé en plus du pied de page par défaut en créant un bloc personnalisé avec le plugin [PWG Stuff](personnaliser-ma-galerie/personnaliser-votre-galerie-avec-des-plugins/pwg-stuff-ajouter-des-blocs-sur-votre-galerie).
    
- Comment ajouter une bannière / photo personnalisée sur mon site Piwigo ?
    
    Il existe plusieurs moyens de personnaliser votre Piwigo en ajoutant une image de fond sur la page d’accueil ou une bannière sur les pages de votre site.
    
    Pour savoir comment, lisez cet article :
    
    [Ajouter une bannière personnalisée à votre galerie](personnaliser-ma-galerie/ajouter-banniere-personnalisee-piwigo)
    
- Comment obtenir une facture sur piwigo.com ?
    
    Vous avez besoin d’une facture pour votre abonnement sur piwigo.com? 
    
    - Si vous avez besoin d’une facture avant de réaliser paiement : faites une demande au support ; attention : demander une facture vous engage à la régler.
    - Si vous avez besoin d’une facture après le paiement : pas d’inquiétude, elle est disponible automatiquement dans votre administration Piwigo, menu Mon Compte > Gérer, onglet Facturation.