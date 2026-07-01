# Les thèmes Piwigo : présentation

## Qu’est-ce qu’un thème sur Piwigo ?

Comme vous le savez déjà sans doute, Piwigo est séparé en deux interfaces :

- l’administration, qui n’est accessible qu’aux administrateurs ;
- la galerie, qui peut être accessible aux simples utilisateurs, et même à tous les visiteurs si votre galerie est publique.

Votre galerie Piwigo est un site Internet qui peut être personnalisé : couleurs, polices, organisation des pages…

Mais pour personnaliser votre galerie, vous devez d’abord choisir un thème, ou “template” : c’est le modèle de votre galerie.

Pour voir différents exemples de personnalisation, basés sur différents thèmes, vous pouvez visiter notre [page de Démos](https://fr.piwigo.com/demo).

Vous pouvez également découvrir un article de blog, qui présente [8 exemples de personnalisation graphique de Piwigo](https://fr.piwigo.org/blog/2022/02/03/8-exemples-personnalisation-graphique-piwigo/).

## Les thèmes par défaut

Piwigo est toujours installé par défaut avec deux thèmes activés :

- Modus, dans sa version noir et blanc, est le thème utilisé par votre galerie lorsque vous y accédez depuis un ordinateur ;
    
    ![fr-theme-modus.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-04e3510e.png)
    
- Smart Pocket, un thème qui ne s’affichera que depuis un mobile ou une tablette.
    
    ![fr-theme-smart-pocket.PNG](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-10272d65.png)
    

Mais vous pouvez tout à fait choisir :

- de modifier les couleurs du thème Modus
- d’utiliser un autre thème pour votre galerie
- de désactiver le thème mobile Smart Pocket (dans ce cas, sur un écran mobile, votre galerie utilisera le même thème que sur ordinateur. Cela ne pose pas de problème avec les thèmes Modus et Bootstrap Darkroom, qui sont *responsive*, c’est à dire qu’ils s’adaptent à toutes les tailles d’écran).

## Clients Piwigo Cloud et auto-hébergement : les différences pour ajouter un nouveau thème

Vous souhaitez ajouter un nouveau thème ? Tout d’abord, sachez que les choses sont légèrement différentes selon que vous ayez un compte sur [Piwigo Cloud](http://piwigo.org) ou que vous hébergiez vous-même votre Piwigo.

- J’héberge moi-même mon Piwigo
    
    Si vous hébergez vous-même votre Piwigo, vous pouvez ajouter vous-même un nouveau thème depuis l’administration, menu Configuration > Thèmes, onglet “Ajouter un thème”.
    
    Vous pouvez également télécharger un thème sur [piwigo.org](https://fr.piwigo.org/ext/index.php?cid=10) et l’ajouter via FTP sur votre Piwigo.
    
    Vous devez également penser à mettre à jour vos thèmes installés lorsqu’une mise à jour est disponible.
    
- J’ai un compte Piwigo hébergé sur Piwigo Cloud
    
    Si vous avez créé un compte sur Piwigo Cloud, votre Piwigo est hébergé sur nos serveurs. 
    
    Votre compte a été initialisé avec une liste de thèmes déjà installés. Vous ne pouvez pas en installer un nouveau. Vous n’avez pas besoin de mettre à jour vos thèmes.
    

## Gérer les thèmes dans Piwigo

Pour visualiser, modifier et configurer votre thème dans Piwigo, rendez vous dans l’administration et depuis le menu de gauche, cliquez sur Configuration > Thèmes.

En haut de l’écran, sous “Thèmes activés” vous pouvez voir le ou les thèmes activés sur votre galerie.

Plus bas, sous “Thèmes désactivés”, vous pouvez voir les autres thèmes installés, mais non activés.

![piwigo-themes-fr.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-b2d60e66.png)

Lorsqu’un thème est activé, cela signifie qu’il peut s’afficher sur Piwigo. 

Si on le définit “par défaut”, alors c’est lui qui s’affichera par défaut pour tous les nouveaux utilisateurs. 

Mais pour chaque utilisateur, on peut définir quel thème s’affiche pour lui spécifiquement : c’est pour cette raison qu’il est possible d’activer en parallèle plusieurs thèmes.

!!! info
    Dans la grande majorité des cas, on n’active qu’un seul thème, le même pour tous les utilisateurs (en dehors du thème Smart Pocket qui, lorsqu’il est activé, s’affiche automatiquement quand on consulte la galerie depuis un mobile).


## Changer de thème par défaut

Si vous souhaitez changer de thème par défaut sur votre galerie, c’est très simple.

Depuis l’écran disponible depuis le menu Configuration > Thèmes, choisissez le thème que vous souhaitez afficher sur votre galerie et cliquez sur le bouton Activer.

![activer-bootstrap-fr.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-bbfed930.png)

Une fois activé, ce thème est disponible sur votre galerie, mais il ne s’affiche pas encore pas défaut : pour cela, vous devez cliquer sur “Définir par défaut”.

![bootstrap-defaut-fr.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-5ceb73ec.png)

Rendez-vous sur votre galerie : le nouveau thème est pris en compte.

## Configurez votre thème

Choisir un thème n’est qu’une première étape dans la personnalisation de votre galerie : la plupart des thèmes propose en effet des options de configuration qui permettent : 

- de modifier les couleurs de votre galerie
- de modifier certaines options d’affichage
- d’ajouter des éléments de personnalisation (logo, bandeau…)
- d’activer des composants optionnels

Les thèmes les plus récents, [Modus](le-theme-modus) et [Bootstrap Darkroom](le-theme-bootstrap-darkroo), proposent de nombreux styles de couleurs et options de configuration. D’autres, plus anciens, ne sont pas configurables.

On vous conseille d’explorer les options des principaux thèmes pour faire votre choix.

## Présentation des principaux thèmes

### Modus

Modus est le thème par défaut activé sur Piwigo. C’est un thème moderne, responsive, qui offre une compatibilité garantie avec un maximum de plugins. Son menu de navigation est horizontal.

![fr-theme-modus.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-04e3510e.png)

Il offre 18 jeux de couleurs différents que vous pouvez choisir dans ses options de configuration.

![modus-styles-fr.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-8f320e16.png)

Il permet également :

- de personnaliser la taille et le format des miniatures de vos albums (par défaut, des miniatures carrées de 250x250 pixels)
- d’ajouter une bannière sur votre galerie

[Lire la documentation du thème Modus](le-theme-modus)

### Bootstrap Darkroom

Après Modus, c’est le deuxième thème le plus populaire actuellement.

Bootstrap Darkroom est un thème moderne, responsive, très personnalisable. Il s’appuie sur le framework Bootstrap 4, un projet open source très populaire dans le monde de la création d’interfaces web. Son menu de navigation est horizontal.

![fr-theme-boostrap-darkoom.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-c400f924.png)

Bootstrap Darkoom comporte pas moins de 30 styles de couleurs très variés.

![fr.theme-boostrap.gif](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-321bdb27.gif)

En plus de ces styles de couleurs, Bootstrap Darkroom offre de nombreuses options de configuration :

- Ajouter un logo
- Ajouter une bannière (image, texte)
- Modifier de nombreuses options d’affichage
- Ajouter du code CSS personnalisé
- Ajouter des icônes de partage sur les réseaux sociaux
- …

[Lire la documentation du thème Bootstrap Darkroom](le-theme-bootstrap-darkroo)

### Elegant

Elegant est un thème qui a été très populaire pendant de nombreuses années et qui est toujours très utilisé. Il se caractérise par un menu de navigation vertical, à gauche de l’écran. Les albums sont affichés sous forme de blocs larges et non de miniatures, ce qui permet si on le souhaite d’afficher un texte descriptif pour chaque album.

![fr-theme-elegant.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-6f9298df.png)

Les couleurs ne peuvent pas être modifiées directement depuis la configuration du thème Elegant : les clients d’une offre sur [Piwigo Cloud](http://Piwigo.org) doivent contacter le support pour en faire la demande ou pour avoir accès à la feuille de style de Piwigo.

Elegant offre quelques options de configuration :

- Afficher ou masquer le panneau latéral de menu
- Afficher ou masquer le panneau latéral de description d’une photo
- Afficher ou masquer le panneau des commentaires

## Comment tester un thème sans le rendre visible à tous ?

Comme on l’a vu, il est possible d’activer plusieurs thèmes sur Piwigo, mais seul le thème par défaut est affiché pour tous les utilisateurs.

Ainsi, si vous souhaitez tester un thème sans le rendre accessible à tous, c’est très simple.

Il suffit de l’activer depuis l’administration, Configuration > Thèmes.

Ensuite, rendez-vous sur votre galerie et sur le menu “Personnaliser”. Ce menu vous permet de modifier vos préférences. Vous pouvez ainsi changer de thème : cette modification ne sera visible que par vous.

![fr-personnaliser-changer-theme.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-c28690a1.png)

## Changer de thème facilement avec Theme Switch

Si vous souhaitez rendre encore plus facile le changement de thème sur votre galerie, vous pouvez activer le plugin Theme Switch.

Une fois activé, ce plugin ajoute une icône en forme de pinceau sur votre galerie, qui permet de changer de thème en un clic.

!!! info
    Attention : cette icône est visible par tous les visiteurs, pas seulement les administrateurs.


![fr-plugin-theme-switch.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-5b2a92e9.png)

## Changer de thème facilement avec Admin Tools

Le plugin Admin Tools offre de nombreuses possibilités pour accéder à des actions d’administration depuis votre galerie.

Entre autres, il permet de facilement changer de thème.

Lorsque ce plugin est activé, lorsqu’un administrateur se connecte à la galerie Piwigo, un menu supplémentaire est ajouté. Le bouton Option, en haut à droite, vous permet de changer le thème actif en un clic. Ce n’est visible que pour vous.

![fr-plugin-admin-tools-theme.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-b9976377.png)

!!! info
    Ce plugin permet également de changer de langue en un clic ou de voir votre galerie en tant que n’importe quel autre utilisateur : il est donc très utile pour faire des tests.


[En savoir plus sur le plugin Admin Tools](../administrer-piwigo/plugins-pour-les-administrateurs)
