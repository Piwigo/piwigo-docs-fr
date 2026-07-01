# Les plugins sur Piwigo : présentation

Si vous utilisez déjà Piwigo et si avez déjà parcouru cette documentation, vous avez déjà compris que les plugins font partie intégrante de Piwigo.

Toutefois, on a pensé qu’il serait utile de refaire le tour du sujet dans cet article.

## Qu’est-ce qu’un plugin chez Piwigo ?

Un plugin est une extension qui ajoute ou modifie les fonctionnalités de base de Piwigo.

Lorsque vous installez Piwigo pour la première fois, vous avez accès au coeur de Piwigo, le socle technique et fonctionnel sur lequel repose tout le système :

- L’administration de Piwigo
- La galerie avec le thème par défaut Modus

Par défaut, certains plugins sont déjà installés sur votre Piwigo, selon qu'il s'agisse d'une galerie auto-hébergée ou d'un compte Piwigo Cloud.

- Vous avez installé vous-même Piwigo
    
    Si vous installez la dernière version de Piwigo sur votre environnement, les plugins suivants seront installés par défaut, mais non activés :
    
    - Admin Tools (permet aux administrateurs d'effectuer certaines actions d'administration à partir de la galerie)
    - Language Switch (permet de changer facilement la langue de la galerie)
    - LocalFiles Editor (permet de modifier les fichiers de configuration locaux à partir de l'administration)
    - Take A Tour of Your Piwigo (ajoute une visite guidée interactive de l'administration de Piwigo pour les nouveaux utilisateurs)
- Vous avez créé un compte sur Piwigo Cloud
    
    Si vous créez un compte sur Piwigo Cloud, les plugins suivants seront activés par défaut :
    
    - Stop Spammer (un plugin pour éviter le SPAM, à ne pas désactiver)
    - VideoJS (le plugin de gestion des vidéos, activé par défaut pour les clients d’une offre Piwigo Cloud depuis mars 2023).

**Mais il ne faut pas s’arrêter avec les plugins pré-installés.** 

Piwigo est un outil modulaire sur lequel vous pouvez choisir, ou pas, d’ajouter des fonctionnalités : c’est à ça que servent les plugins.

Si vous connaissez WordPress, c’est exactement le même principe. Vous observerez d’ailleurs que très peu de sites créés avec WordPress fonctionnent sans aucun plugin. De même, il serait vraiment dommage d’utiliser Piwigo sans l’enrichir avec les plugins répondant à vos besoins.

## Gestion des plugins : différence entre clients Piwigo Cloud et auto-hébergement

Le fonctionnement des plugins diffère selon que vous ayez un compte sur Piwigo Cloud ou que vous hébergiez vous-même votre Piwigo.

### Vous êtes client d’une offre Piwigo Cloud

Si vous êtes client d’une offre d’hébergement sur Piwigo Cloud, vous n’avez pas besoin d’installer ou de mettre à jour les plugins.

Vous avez accès à une liste limitées de plugins, en fonction de l’offre d’abonnement que vous avez choisie. Ils sont déjà installés sur votre Piwigo, et vous pouvez, selon votre choix, les activer ou les désactiver.

**Liste des plugins**

Pour retrouver vos plugins, rendez vous dans l’administration de votre Piwigo, Menu Plugins.

L’onglet Liste vous permet de visualiser les plugins déjà activés sur votre Piwigo, et de rechercher parmi l’ensemble des plugins.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-7b3f57e2.png)

Pour activer un nouveau plugin, il suffit de cliquer sur le bouton d’activation : le plugin est immédiatement activé. Vous avez alors accès à sa configuration.

**Plugins par offre tarifaire**

Le deuxième onglet liste les plugins disponibles pour chaque offre tarifaire. Vous ne pouvez activer que les plugins présents dans votre offre.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-2ce1e49f.png)

Sur cette page, les plugins sont triés par offre ; les icônes sur la droite permettent de savoir à tout moment sur quelles offres un plugin est disponible.

Si vous cherchez un plugin en particulier, combinez les toucher Ctrl+F de votre clavier pour rechercher dans la page le nom de ce plugin ou une fonctionnalité précise.

**Exemple** : pour le plugin User Custom Fields, la première icône est grisée, car il n’est accessible qu’à partir de l’offre Équipe.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-f455e07d.png)

### Vous hébergez vous-même votre Piwigo

Si vous utilisez un Piwigo installé sur votre propre infrastructure d’hébergement, et non sur Piwigo Cloud, les choses sont différentes.

Pour utiliser un nouveau plugin, vous devez d’abord l’installer sur votre serveur, puis l’activer.

**Liste des plugins installés**

Pour retrouver les plugins installés sur votre Piwigo, rendez vous dans l’administration de Piwigo, Menu Plugins.

L’onglet Liste vous permet de visualiser les plugins déjà activés sur votre Piwigo, et de rechercher parmi les plugins installés mais désactivés.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-dcee9539.png)

**Mettre à jour les plugins**

Contrairement aux clients de Piwigo Cloud, vous devez mettre à jour vos plugins vous-même lorsqu’une nouvelle version est disponible. Pour cela, vous disposez de l’onglet Rechercher les mises à jour, qui vous permet de voir si des mises à jour sont disponibles, et de les installer.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-208b1fad.png)

Si une mise à jour d’un plugin est disponible, vous pouvez l’installer directement en cliquant sur “Installer”. Vous pouvez également télécharger le fichier du plugin, ou choisir d’ignorer la mise à jour.

**Installer un plugin**

Si vous souhaitez installer un nouveau plugin, vous devez vous rendre sur le troisième onglet “Ajouter un plugin”.

Cette page vous permet de parcourir l’ensemble des plugins publiés sur piwigo.org, que vous pouvez également retrouver sur [la page Extensions du site](https://fr.piwigo.org/ext/).

Vous pouvez rechercher un plugin par mot-clé ou filtrer les plugins (par date, auteur, tag, note…).

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-99afc4a0.png)

Dans cette liste, on retrouve certains plugins qui ne sont pas disponibles sur Piwigo Cloud. Ce sont des plugins créés par la communauté, que l’équipe qui développe Piwigo n’a pas nécessairement testés ou validés : nous ne garantissons donc pas leur bon fonctionnement, ni leur compatibilité ! 

!!! info
    Les plugins que nous présentons dans la présente documentation sont les plugins disponibles sur Piwigo Cloud, que notre équipe a testés et validés. Mais cela ne veut pas dire que les autres plugins disponibles ne sont pas intéressants, bien sûr.


Pour installer un nouveau plugin, cliquez sur Ajouter.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-3a714243.png)

Vous pouvez directement activer un plugin après son installation en cliquant dans le bandeau sur le lien “L’activer maintenant”.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-fa64d45b.png)

Si vous ne le faites pas, le plugin est maintenant disponible dans l’onglet Liste, dans la catégorie “Désactivé”. Il suffit de cliquer sur le bouton d’activation pour l’activer.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-d9cc26e9.png)

## Configuration des plugins

La plupart du temps, les plugins disposent de leur page de configuration. Vous y avez accès depuis la liste des plugins activés sur votre Piwigo, en cliquant sur le bouton Configuration lorsqu’il est de couleur orange.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-ec4320de.png)

Parfois, cette page de configuration ne contient que quelques paramètres et vous n’aurez besoin de vous y rendre que très rarement.

Mais dans certains cas, la configuration du plugin donne accès à tout un pan de fonctionnalités importantes apportées par ce plugin. Il est donc capital de la visiter. D’ailleurs, dans les pages de cette documentation, à chaque fois que nous présentons un plugin, nous vous montrons un aperçu de sa page de configuration.

À l’inverse, certains plugins ne proposent pas de page de configuration : dans ce cas, le bouton Configuration est grisé. 

C’est le cas lorsque le plugin n’a pas besoin d’interface utilisateur pour fonctionner et ne propose aucun paramètre.

Par exemple, le plugin **Stop Spammers** fonctionne tout seul en tâche de fond : il n’a donc pas besoin de page de configuration.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-a479df06.png)

C’est également le cas lorsque le plugin ajoute une fonctionnalité accessible depuis un autre écran de Piwigo.

Par exemple, le plugin **Rotate Image** ajoute une fonctionnalité de rotation d’image dans la page d’édition d’une photo : il n’a donc pas besoin de page de configuration.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-d02f81cc.png)

Sommaire de l’article

---

## Des plugins pour tous vos besoins

Tout au long de cette documentation, nous présentons des plugins à chaque fois que c’est pertinent.

Retrouvez dans les articles ci-dessous quelques sélections de plugins pour répondre à vos besoins.

- [Personnaliser votre galerie avec des plugins](../personnaliser-ma-galerie/personnaliser-votre-galerie-avec-des-plugins)
- [Personnaliser la page Album avec des plugins](../naviguer-sur-votre-galerie-piwigo/les-albums-sur-votre-galerie)
- [Personnaliser la page Photo avec des plugins](../naviguer-sur-votre-galerie-piwigo/la-page-photo-sur-votre-galerie)
- [Personnaliser la gestion des tags avec des plugins](../naviguer-sur-votre-galerie-piwigo/les-tags-sur-votre-galerie)
- [Personnaliser la gestion des commentaires avec des plugins](../les-commentaires-et-notes/gerer-les-notes-votes)
- [Les plugins pour les administrateurs](../administrer-piwigo/plugins-pour-les-administrateurs)
- [Créer des collections avec le plugin User Collections](../docs/naviguer-sur-votre-galerie-piwigo/creer-des-collections-plugin-user-collections)
- [Créer des albums intelligents avec le plugin SmartAlbums](..//organiser-les-albums/smartalbums-albums-intelligents)
- [Gérer les contributeurs avec le plugin Community](../les-utilisateurs/gerer-les-contributeurs-plugin-community)
