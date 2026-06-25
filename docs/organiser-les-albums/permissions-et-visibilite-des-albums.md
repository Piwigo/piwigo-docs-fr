# Permissions et visibilité des albums

Dans ce chapitre, nous allons voir comment gérer et modifier les permissions sur les albums dans Piwigo, c’est à dire le statut des albums (privé / public) et la gestion des droits utilisateurs sur les albums.

Nous verrons également comment il est possible de visualiser et modifier facilement les propriétés des albums :

- albums verrouillés / déverrouillés
- activation des commentaires sur les albums
- albums autorisés et interdits au téléchargement

## Comment fonctionnent les permissions sur les albums ?

Lorsque vous créez un nouvel album dans Piwigo, qui a le droit de voir son contenu ? Comment le modifier ? Quelles sont les règles applicables aux sous-albums ?

Il y a plusieurs choses à savoir.

### Albums privés et albums publics

Pour commencer, il faut comprendre que dans Piwigo, un album peut être privé ou public.

Les **albums publics** seront visibles par tous les visiteurs non connectés de votre photothèque (qui n’ont pas de compte : cela correspond à l’utilisateur spécial “guest”).

Dès lors qu’une personne consulte le site web de votre galerie sur internet sans se connecter, elle peut visualiser les albums publics, et uniquement ceux-ci.

Les **albums privés**, eux, sont accessibles uniquement aux utilisateurs identifiés, qui se seront connectés avec leur login et leur mot de passe.

Pour chaque album privé, on va pouvoir définir qui, parmi les utilisateurs et groupes d’utilisateurs, a le droit de le visualiser.

!!! info
    Lorsque vous créez un nouvel album à la racine de Piwigo, il est toujours public, par défaut. Si vous souhaitez modifier ce comportement, contactez le support si vous êtes client piwigo.com. Sinon, ajouter le paramètre suivant à votre configuration grâce à [LocalFiles Editor](../hebergez-votre-piwigo/modifier-la-configuration-locale-avec-localfiles-editor) : `$conf['newcat_default_status'] = 'private';`


### Modifier les permissions sur un album

Pour modifier les permissions sur un album, vous devez modifier cet album :

- Soit depuis votre galerie, en vous rendant sur la page de cet album et en cliquant sur l’icône d’édition ;
- Soit depuis l’administration, en vous rendant dans la liste des albums (menu Albums > Gérer) et en cliquant sur l’icône d’édition.

[En savoir plus sur la modification des albums](modifier-un-albu)

Depuis l’éditeur d’album, cliquez sur l’onglet “Permissions”. Cet onglet permet de définir le statut de votre album (public ou privé).

![fr-album-permissions.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-4df2ba8e.png)

Si vous choisissez de rendre un album privé, vous allez pouvoir définir qui, parmi les utilisateurs, a le droit de visualiser son contenu.

Vous avez la possibilité d’accorder des droits d’accès :

- à un ou plusieurs groupes d’utilisateurs
- à un ou plusieurs utilisateurs en particulier

![fr-permissions-albums.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-b0f55b03.png)

Pour en savoir plus sur les groupes d’utilisateurs, [lisez cet article](../les-utilisateurs/les-groupes-dutilisateurs).

!!! Warning "Attention"
    Attention ! Si un album est privé, personne ne le verra sur la galerie, pas même les administrateurs ! Pensez-donc bien à vous accorder les droits sur les albums privés que vous créez.


La case à cocher “Appliquer aux sous-albums” permet de modifier, en une seule fois, les permissions d’un album et d’appliquer ces modifications à tous ses sous-albums existants.

!!! Warning "Attention"
    Attention : cette modification ne s’applique pas aux sous-albums qui seront créés à l’avenir.


### Règles des permissions sur les hiérarchies d’albums

Lorsque vous créez un sous-album d’un album public, il sera public par défaut.

Lorsque vous créez un sous-album d’un album privé, il sera privé ; par ailleurs, il sera rendu accessible par défaut à tous les administrateurs, ainsi que tous ses albums parents.

Si vous rendez public un album dont les albums parents sont privés, cela rendra automatiquement les albums parents publics.

Si vous rendez privé un album dont les sous-albums sont publics, cela rendra automatiquement ses sous-albums privés.

En dehors du statut (privé / public), les sous-albums n’héritent pas automatiquement des permissions de leurs parents. 

Prenons un exemple : vous avez un album privé, accessible aux utilisateurs X et Y. Si vous créez un sous-album de cet album privé, par défaut, il ne sera pas accessible aux utilisateurs X et Y (uniquement aux administrateurs).

!!! info
    Si vous voulez que les sous-albums héritent automatiquement des permissions de leurs parents, contactez le support si vous êtes client piwigo.com.  Sinon, ajoutez le paramètre suivant à votre configuration grâce à [LocalFiles Editor](../hebergez-votre-piwigo/modifier-la-configuration-locale-avec-localfiles-editor) : `$conf['inheritance_by_default'];`


## Gérer en masse l’accès aux albums (public / privé)

Pour visualiser en un coup d’oeil et modifier les types d’accès (public/privé) de vos albums, rendez-vous dans l’administration, Menu Albums > Propriétés.

Le premier onglet permet de passer facilement un album du statut public au statut privé, et vice-versa.

![fr-proprietes-albums-permissions.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-e4556491.png)

Sur cet écran, vous pouvez voir la liste de tous les albums et sous-albums de votre photothèque dans la colonne qui correspond à leur statut (Albums publics et Albums privés).

!!! info
    Les sous-albums sont reconnaissables car leur nom apparaît ainsi : Album racine / Sous-album 1 / Sous-album 2


Pour passer un album du statut public au statut privé, il vous suffit de cliquer sur cet album et de cliquer sur la flèche en dessous de la première colonne : il est alors déplacé dans la colonne “Albums privés”. Pour passer en public un album privé, c’est l’inverse !

Vous pouvez sélectionner plusieurs albums, de la même façon que vous le feriez dans un dossier de votre ordinateur :

- Modifier une liste d’albums qui se suivent : Cliquez sur le premier album souhaité, puis appuyez sur la touche Majuscule (Shift) de votre clavier, puis cliquez sur le dernier voulu : tous les albums de la liste sont sélectionnés
- Modifier plusieurs albums qui ne se suivent pas dans la liste : Cliquer sur le premier album souhaité, puis appuyez sur la touche Ctrl ou Cmd de votre clavier, cliquez sur un autre album, et continuez ainsi jusqu’à ce que tous les albums voulus soient sélectionnés.

### **Cas particulier des albums avec des sous-albums**

Si vous passez au statut Privé un album qui contient des sous-albums, alors tous ses sous-albums passeront également en privé.

Mais si vous passez au statut Public un sous-album, alors son album parent passera automatiquement au statut public également, car il est nécessaire d’avoir accès à un album pour avoir accès à l’un de ses sous-albums.

Vous pouvez voir un exemple concret ci-dessous.

![fr-statut-album.gif](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-8aeadd37.gif)

## Gérer en masse la visibilité des albums (verrouillé / déverrouillé)

Pour verrouiller ou déverrouiller une liste d’albums sur votre galerie, rendez-vous dans l’administration, Menu Albums > Propriétés.

Le deuxième onglet a exactement le même fonctionnement que le premier (voir paragraphe précédent), sauf qu’il permet de verrouiller / déverrouiller des albums.

!!! info
    Un album verrouillé est inaccessible sur la galerie, sauf pour les administrateurs. Le plus souvent, le statut verrouillé est utilisé lorsqu’un album n’est pas encore prêt à être rendu public sur la galerie, parce d’un administrateur est en train de travailler dessus (préparation avant publication, maintenance…). C’est donc un statut “de travail”, temporaire.


Pour verrouiller ou déverrouiller un album unitairement, vous pouvez aussi tout simplement éditer cet album.

## Gérer en masse les commentaires sur les albums

Si vous avez activé les commentaires sur votre galerie, vous pouvez visualiser en un coup d’oeil quels albums sont ouverts ou pas aux commentaires. Pour cela, rendez-vous dans l’administration, Menu Albums > Propriétés.

Le troisième onglet fonctionne exactement de la même manière que les deux autres (voir chapitres précédents). 

Pour en savoir plus sur les commentaires, [lisez cet article](../les-commentaires-et-notes/commentaires-options-avancees).

## **Download Permissions :** Gérer les droits au téléchargement album par album

Par défaut, dans Piwigo, les utilisateurs habilités à télécharger des photos peuvent télécharger toutes les photos de la galerie.

Si vous avez besoin de gérer des droits album par album, vous pouvez installer le plugin **Download Permissions**.

!!! info
    Si vous êtes client d’une offre piwigo.com, ce plugin est accessible à partir de l’offre Équipe.


Il ajoutera à la page Albums > Propriétés un nouvel onglet, permettant de définir, sur le même principe que les autres onglets, dans quels albums les utilisateurs sont autorisés à télécharger les photos.

![fr-album-download-permissions.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-551907de.png)
