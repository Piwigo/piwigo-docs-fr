# Ajouter des pages à votre galerie

Vous souhaitez ajouter des pages personnalisées à votre galerie Piwigo ? C’est possible avec l’aide de quelques plugins.

## Additional Pages : Ajouter des pages HTML

Le plugin Additional Pages permet d’ajouter de nouvelles pages dans votre galerie et de les rendre accessible via le [menu de navigation](Personnaliser le menu de votre galerie.md).

Une fois ce plugin activé, rendez vous dans sa page de Configuration.

### Ajouter une nouvelle page

Le premier onglet permet d’ajouter une nouvelle page sur votre galerie.

Vous pouvez repartir de zéro ou charger un modèle de page existant fourni avec le plugin.

Vous pouvez définir les attributs et options de cette page :

- Choisir un modèle de page (par défaut, seul le modèle “Standalone Homepage” est disponible)
- Nom de la page
- Lien permanent (URL)
- Choisir si cette page remplace ou pas votre page d’accueil
- Choisir si cette page est autonome ou pas (si elle est autonome, elle n’est pas reliée au style de votre galerie Piwigo et ne récupère donc pas les styles CSS définis).

Le champ “Contenu” permet de saisir le code HTML de votre page.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-fc7ea018.png)

Si vous avez installé le plugin FCKEditor, on affichera un éditeur HTML qui vous permettra de visualiser le résultat par défaut, mais vous pouvez afficher le code HTML en désactivant FCKEditor en bas à droite de la fenêtre.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-c7d441e0.png)

### Créer une page d’accueil pour votre galerie Piwigo

Le plugin Additional Pages est fréquemment utilisé pour créer une page d’accueil dédiée pour une galerie Piwigo.

La page proposée par défaut avec le modèle *Standalone Homepage* est conçue pour créer une page d’accueil qui affiche une photo au choix sur votre galerie, comme dans cet exemple : [https://endangeredarts.com/](https://endangeredarts.com/) 

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-f3d57b74.png)

Si vous souhaitez faire de même, vous devez installer le plugin Extended Description, qui permettra d’afficher sur la page du contenu issu de votre galerie. 

[En savoir plus sur Extended Description](Personnaliser votre galerie avec des plugins.md)

Ensuite, dans le code HTML présent par défaut lorsque vous créez la page, vous devez modifier le contenu de la balise (`[photo id=12345 size=L link=no]`) pour l’adapter à ce que vous souhaitez :

- Remplacer 12345 par l’identifiant numérique de la photo que vous souhaitez afficher sur la page d’accueil
- Modifier la taille de l’image affichée (SQ, TH, XXS, XS, S, M, L, XL, ou XXL)
- Ne modifiez pas “link=no”

Vous pouvez également remplacer cette balise par `[random album=xx]`, en remplaçant xx par l’identifiant de l’album de votre choix : cela affichera sur votre page d’accueil une photo choisie aléatoirement dans l’album sélectionné.

Vous pouvez également remplacer cette balise par `[slider album=xx]`, en remplaçant xx par l’identifiant de l’album de votre choix : cela affichera sur votre page d’accueil un diaporama des photos de l’album sélectionné. Vous pouvez régler toutes les options du diaporama en utilisant les possibilités du plugin Extended Descriptions.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-4ee672eb.png)

Enfin, dès lors que vous maîtrisez un minimum HTML, les possibilités sont infinies ! Vous pouvez par exemple créer un menu de navigation sur mesure en haut ou en bas de page.

### Gérer les pages existantes

Une fois que vous avez créé une première page, vous pouvez la visualiser et la modifier dans l’onglet “Gérer”. Vous pouvez également réordonner les pages créées.

### Configuration des pages additionnelles

L’onglet configuration vous offre quelques options.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-904fb135.png)

**Gestion des droits**

Il est possible d’activer la gestion des droits d’accès aux pages additionnelles : par niveau de confidentialité, par type d’utilisateur (statut), par groupe d’utilisateur, par langue. Si vous activez une de ces options, vous pourrez définir les droits d’accès à chaque page en modifiant celle-ci.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-ac40979a.png)

**Affichage des pages additionnelles sur votre galerie**

Ces options sont valables pour toutes vos pages additionnelles.

Vous pouvez définir :

- Si les pages additionnelles intègrent un bouton de retour vers l’accueil
- Si les pages additionnelles sont accessibles via un point de menu, et le nom de ce point de menu dans chaque langue de votre galerie.

## Contact Form : ajoutez un formulaire de contact sur votre galerie

Le plugin Contact Form permet d’ajouter une page contenant un formulaire de contact sur votre galerie.

Chaque fois qu’un visiteur de votre galerie remplira ce formulaire, un email de notification vous sera envoyé par votre Piwigo.

Une fois ce plugin activé, rendez vous dans sa page de Configuration.

### Configuration du formulaire de contact

L’onglet Configuration vous permet de paramétrer votre formulaire et sa visibilité.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-38c11d9d.png)

Cette page permet de choisir :

- Si on ajoute ou pas un lien Contact dans le menu
- Si on autorise les invités (visiteurs anonymes de votre galerie) à voir le formulaire
- Si on redirige l’utilisateur vers une URL spécifique après soumission du formulaire
- Le format de l’email envoyé à l’administrateur après soumission du formulaire
- Le texte (optionnel) affiché au-dessus et au-dessous du formulaire sur la page.

### Choix des destinataires des emails

L’onglet E-mails permet de définir qui sera destinataire des emails de notification lorsqu’une personne remplit le formulaire de contact.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-a8f6fa0d.png)

Par défaut, tous les administrateurs et webmasters sont destinataires, mais vous pouvez en supprimer en cliquant sur la croix.

Vous pouvez ajouter de nouveaux destinataires en cliquant sur la liste déroulante “Sélectionner un nouvel utilisateur”. 

Vous pouvez enfin ajouter de nouveaux destinataires à droite, même si ils ne sont pas utilisateurs sur votre Piwigo.

### Affichage du formulaire sur votre galerie

Si vous avez coché cette option, le formulaire est accessible depuis un point de menu Contacter accessible depuis le bloc de menu Spéciales ([en savoir plus sur les menus](Personnaliser le menu de votre galerie.md)).

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-0a684208.png)

Si vous souhaitez afficher le lien vers le formulaire directement depuis le menu principal de votre galerie, c’est possible avec le plugin **Contact 1 Menu**.

Ce plugin déplace le menu “Contacter” directement dans la barre de navigation principale.

![contact1.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-d4e33328.png)

### Crypto Captcha : Protéger votre formulaire du SPAM

Malheureusement, les formulaires sur le web sont souvent générateurs de SPAM car ils sont remplis par des robots.

Pour éviter ce problème, vous pouvez installer le plugin **Crypto Captcha.**

Ce plugin oblige les utilisateurs à saisir un Captcha avant d’envoyer le formulaire. Plusieurs options sont disponibles pour paramétrer votre Captcha.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-e95f122c.png)

<aside>
💡 Ce plugin permet également d’ajouter un Captcha pour la saisie d’un commentaire ou la création d’un nouvel utilisateur.

</aside>

### ⚠️ Problèmes fréquents avec le plugin Contact Form

Lorsqu’un contact vous écrit un message via le formulaire Contact Form, l’email de notification a pour expéditeur l’adresse email saisie dans le formulaire.

Or, votre site Piwigo n’est pas autorisé à envoyer des emails provenant d’une adresse Gmail, Yahoo, ou encore Orange. Certains fournisseurs d’emails vont donc bloquer ces emails.

En conséquence, il arrive parfois que les emails envoyés via ce formulaire n’arrivent pas à destination : c’est notamment le cas lorsque l’expéditeur écrit depuis une adresse Gmail, et que l’email du destinataire est aussi une adresse Gmail.

Si vous rencontrez ce type de problème, vous pouvez tenter de le résoudre en modifiant l’adresse destinataire des emails (évitez les adresses Gmail ou Yahoo).

Si vous ne réussissez pas à résoudre le problème, nous vous conseillons de désactiver Contact Form.

Sommaire de l’article

---

← Précédent

[Personnaliser le menu de votre galerie](Personnaliser le menu de votre galerie.md)

Suivant →

[Personnaliser votre galerie avec des plugins](Personnaliser votre galerie avec des plugins.md)