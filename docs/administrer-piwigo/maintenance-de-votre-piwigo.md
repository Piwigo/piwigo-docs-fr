# Maintenance de votre Piwigo

Pour les administrateurs “techniques” de Piwigo, un menu Maintenance est à votre disposition, accessible uniquement aux utilisateurs ayant le statut de Webmaster.

Pour y accéder, rendez-vous dans l’administration, menu Outils > Maintenance.

Il vous donne accès à plusieurs actions et informations détaillées dans cet article :

- Effectuer des actions de maintenance sur votre Piwigo
- Visualiser des informations techniques sur votre Piwigo
- Visualiser l’historique des activités système.

## Actions de maintenance disponibles sur Piwigo

Le premier onglet “Actions” offre de nombreuses actions pour administrer votre Piwigo.

![fr-piwigo-maintenance.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-a0aa53d6.png)

L’action la plus utilisée dans le cadre d’une utilisation “normale” de Piwigo est l’action “Verrouiller la galerie” (voir chapitre suivant) qui permet de rendre la galerie indisponible (par exemple, lorsque vous effectuez un travail de réorganisation).

Les autres actions servent principalement à supprimer des données inutilisées ou à rafraîchir les informations affichées sur Piwigo.

<aside>
💡 **Pourquoi ces actions peuvent-elles être nécessaires ?**

Pour optimiser le temps de génération des pages, Piwigo utilise des informations en cache. Par exemple, au lieu de compter le nombre de photos contenus dans chaque album à chaque rechargement de page, cette information est stockée dans la base de données. En théorie, cette information est toujours correcte, mais parfois une erreur peut survenir et l'information en cache devient fausse. Dans ce cas, supprimer et regénérer le cache peut être utile.

De plus, certaines informations deviennent inutiles avec le temps. Les supprimer de la base de données libère de l'espace disque.

</aside>

### Actions sur la galerie

Voici les actions disponibles dans la section “Actions sur la galerie”.

- **Verrouiller la galerie**

Cette action permet de mettre votre galerie en “mode maintenance”.

Une galerie verrouillée n’est visible que des administrateurs. Tant que la galerie est verrouillée, un message d’alerte s’affichera sur toutes les pages de l’administration de Piwigo.

![fr-piwigo-verrouiller.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-f6c84ffc.png)

Les visiteurs de la galerie, eux, ne pourront pas naviguer sur le site qui affichera le message suivant : *La galerie est verrouillée pour cause de maintenance. Merci de revenir plus tard.*

- **Mettre à jour les informations des albums**

Cette action peut être utile si jamais vous avez un message d’erreur qui apparaît sur votre galerie. Elle vérifie et éventuellement corrige certaines informations enregistrées sur les albums dans la base de données.

- **Mettre à jour les informations des photos**

Cette action peut être utile si jamais vous avez un message d’erreur qui apparaît sur votre galerie.

Elle vérifie et éventuellement corrige certaines informations enregistrées sur les photos dans la base de données. 

- **Réparer et optimiser la base de données :**

Cette action peut être utile si jamais vous avez un message d’erreur qui apparaît sur votre galerie.

Elle exécute une opération de maintenance sur votre base de données : optimisation (suppression des espaces marqués vides ayant contenu des données) et réparation (vérification et réparation des structures de tables). Elle permet aussi de compacter un peu la taille de la base de données. 

- **Réinitialiser les contrôles d'intégrité**

Normalement, vous ne devrez pas avoir besoin d’effectuer cette action.

Elle permet de remettre à zéro les compteurs d'erreurs éventuellement détectées par les contrôles d'intégrité, dont les résultats affichés sur la page d'accueil du panneau d'administration. 

### Actions de purge

Voici les actions disponibles dans la section “Actions de purge”.

- **Purger le cache utilisateur**

Cette action peut être utile si un utilisateur voit sur la galerie des éléments qu’il ne devrait pas voir (par exemple, si on constate un mauvais respect des droits utilisateurs). Normalement, vous ne devrez pas avoir besoin d’effectuer cette action.

- **Supprimer les tags orphelins**

Cette action permet de supprimer tous les tags qui ne sont associés à aucune photo.

- **Purger le détail de l'historique**

Cette action supprime tout l’historique des visites. L'écran de recherche dans l’historique (accessible depuis le menu Outils > Historique > Recherche) ne montrera plus aucune donnée. 

<aside>
⚠️ Attention : toutes les données seront perdues, sans aucun possibilité de récupération. En revanche, les courbes disponibles depuis l’onglet Statistiques seront toujours affichées, sauf si vous supprimez aussi le récapitulatif de l’historique (paragraphe suivant).

</aside>

- **Purger le récapitulatif de l'historique :**

Cette action supprime les courbes statistiques accessibles depuis le menu Outils > Historique > Statistiques. 

<aside>
⚠️ Si vous ne supprimez pas aussi le détail de l’historique (paragraphe précédent), les courbes seront recalculées à partir des informations présentes dans l’historique détaillé.

</aside>

- **Purger les sessions**

La connexion des visiteurs d'une galerie génère une *session* avec un identifiant unique, mémorisé dans une table de la base de données et dans un cookie (sa validité est de 30 minutes pour le cookie). Cet identifiant de session est utilisé pour diverses fonctions, notamment les statistiques, et il peut être nécessaire de purger les sessions non utilisées depuis longtemps.

Cela peut notamment diminuer la taille de la base de données.

- **Purger les flux de notification jamais utilisés**

Le flux de notification RSS est personnalisé pour tous les visiteurs (nouveaux éléments, nouveaux commentaires etc). Cette fonction permet de supprimer la “personnalisation” pour les visiteurs qui n'utilisent pas le flux d'information.

- **Purger l'historique des recherches**

Piwigo mémorise les critères de recherches effectuées par les visiteurs sur votre galerie. Cette fonction permet de purger cet historique.

Cela peut notamment diminuer la taille de la base de données.

### Purger le cache

Voici les actions disponibles dans la section “Purger le cache”.

**Calculer la taille du cache**

Vous pouvez cliquer sur “Rafraîchir” pour mettre à jour ce calcul.

**Purger les templates compilés**

Utilisez cette fonction pour régénérer l'affichage de la galerie si celui-ci n'est pas conforme, généralement suite à une manipulation sur les templates ou une modification de thème.

### **Supprimer les tailles multiples des photos**

Chaque fois qu’un utilisateur demande à afficher une version d’une photo sur la galerie, cette version est sauvegardée. Au bout d’un moment, cela peut prendre de la place dans votre base de données. Cette section affiche le volume pris par ces versions et permet de les supprimer. Elles seront ensuite re-générées à la demande.

## Environnement : informations de votre Piwigo

L’onglet “Environnement” affiche des informations sur votre Piwigo.

Pour les clients hébergés sur piwigo.com, seules les informations ci-dessous sont disponibles :

- Version de Piwigo utilisée
- Liste des plugins activés

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-98f74807.png)

Pour les Piwigo auto-hébergés, des informations complémentaires sont disponibles :

- Date d’installation
- Système d’exploitation
- Version de PHP
- Version de MySQL
- Bibliothèque graphique utilisée et version
- Taille du cache

Il est d’ailleurs possible de vérifier depuis cette page si une mise à jour de Piwigo est disponible.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-5e2155a2.png)

## Activités systèmes

Le troisième onglet “Activités Système” (introduit dans la version 15 de Piwigo) vous permet de visualiser l’historique détaillé et horodatées de tous les évènements suivants :

- Modification d’un paramètre de configuration de Piwigo
- Installation / activation / désactivation d’un plugin
- Installation / activation / désactivation d’un thème
- Mise à jour d’un thème ou d’un plugin
- Mise à jour du noyau de Piwigo
- Changement du thème par défaut
- Actions de maintenance

Pour chaque action, vous pouvez voir l’objet concerné (Noyau, plugin ou thème), le type d’action (configuration, mise à jour, activation…), l’utilisateur à l’origine de l’action, la date et l’heure, ainsi que des détail (version, etc.).

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-816a7337.png)

## **Delete Hit/Rate :** Supprimer les vues (hits) et les notes des photos

Si vous souhaitez remettre à zéro les vues et les notes des photos, vous pouvez installer le plugin **Delete Hit/Rate**.

- Hits : ce sont les vues des photos. Elles sont affichées sur la galerie si vous avez activé cette option. C’est ce qui est utilisé pour trier les photos par nombre de vues.
- Rates : ce sont les notes des photos. Elles sont affichées si vous avez activé l’option “Permettre les notations” dans la page Configurations > Options.

[En savoir plus sur les notes](../Les commentaires et notes/Gérer les notes (votes).md)

Une fois le plugin Delete Hit/Rate activé, deux nouvelles actions de purge sont disponibles dans l’écran de Maintenance :

- Purger tous les hits de la galerie (supprimer les visites)
- Purger toutes les notes de la galerie

![fr-delete-hit-rate.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-5b1d79e3.png)

Sommaire de l’article

---

← Précédent

[Consultez les statistiques de votre Piwigo](/administrer-piwigo/consultez-les-statistiques-de-votre-piwigo)

Suivant →

[Plugins pour les administrateurs](/administrer-piwigo/plugins-pour-les-administrateurs)
