# Consultez les statistiques de votre Piwigo

Piwigo fournit plusieurs moyens aux administrateurs, en standard ou via des plugins, de monitorer l’utilisation de leur photothèque et de suivre ses performances.

## Tableau de bord

La page d’accueil de l’administration de Piwigo est appelée Tableau de bord.

    

Le tableau de bord permet de visualiser en un coup d’oeil l’usage de votre galerie :

- Nombre de photos
- Nombre d’albums
- Nombre de tags
- Nombre d’utilisateurs
- Nombre de groupes
- Commentaires
- Notes
- Pages vues (depuis le début)
- Plugins installés
- Stockage utilisé
- Nombre de jours restant sur la période en cours (période d’essai, abonnement…)

Chaque icône est également un raccourci vers l’écran de gestion pour chaque thématique.

De plus, le tableau de bord vous donne un aperçu des pics d’activités sur votre Piwigo au cours de 4 dernières semaines.

Une bulle de couleur représente l’activité chaque jour de la semaine. En passant la souris sur cette bulle, vous pourrez voir les activités réalisées.

![en-activity-dashboard.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-79b0b62b.png)

Depuis la version 14 de Piwigo, vous pouvez également consulter sur le tableau de bord l’espace occupé pour chaque type et chaque format de fichier.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-27638894.png)

## Statistiques de l’historique des visites

Pour accéder aux statistiques des visites de votre Piwigo, rendez-vous dans l’administration, menu Outils > Historique.

Cette page affiche la courbe des visites de votre galerie Piwigo.

![fr-historique-stats.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-6cae9134.png)

Vous pouvez voir ces statistiques :

- jour par jour sur les 3 derniers mois
- heure par heure sur les 3 derniers jours
- mois par mois sur les 5 dernières années
- année par année depuis la création de votre Piwigo

En passant la souris sur la courbe, vous pouvez visualiser le nombre de pages vues pour chaque période.

En cliquant sur “Mode comparaison” en haut à droite, vous accéder à une autre visualisation des statistiques.

- La vue Année affiche une courbe par année, avec un code couleur par année ; chaque courbe affiche pour chaque année le nombre de visites par mois. Cela permet, par exemple, de voir si la fréquentation de votre galerie répond à une saisonnalité qui se répète chaque année.
    
    ![en-history-compare-month.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-bd711ced.png)
    
- La vue Mois affiche une courbe par mois sur les 3 derniers mois ainsi qu’une moyenne des 12 derniers mois, avec un code couleur par courbe ; chaque courbe affiche le nombre de visite par jour. Cela permet, par exemple, de voir si la fréquentation de votre galerie a évolué pendant ces derniers mois.
    
    ![en-history-compare-month.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-68fea989.png)
    

### Options des statistiques

Vous pouvez personnaliser le suivi des visites dans la page Configuration > Options de l’administration, onglet Général, Section Divers.

L’option “Historiser les visites des…” permet de définir quelles sont les visites qui sont enregistrées dans les statistiques :

- Visites des “simples visiteurs” (anonymes)
- Visites des utilisateurs enregistrés
- Visites des administrateurs

Vous pouvez bien sûr cocher toutes ces options ou n’en sélectionner que certaines.

Par exemple, si vous voulez que ces statistiques reflètent la popularité de votre galerie et pas le travail des administrateurs, il peut être pertinent de désactiver les statistiques des administrateurs.

### Recherche dans l’historique

Comment savoir ce que les utilisateurs font sur votre galerie ? Qui a téléchargé tel ou tel fichier ?

C’est un besoin récurrent, pour savoir quelles photos sont populaires, mais aussi, par exemple, pour savoir qui a téléchargé des fichiers soumis à un copyright par exemple.

C’est possible grâce à l’outil de **recherche dans l’historique**.

Depuis le menu Outils > Historique, l’onglet Recherche permet de visualiser un historique détaillé des actions effectuées sur votre Piwigo, et d’effectuer une recherche.

![fr-historique-recherche.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-fd5381fb.png)

Cette page liste de façon chronologique les actions effectuées sur votre galerie sur une période. Vous pouvez choisir la période grâce aux filtres par date.

Deux types d’action sont affichées ici :

- Les visites de page
- Les téléchargements de fichier

Vous pouvez choisir grâce au filtre “Action” de n’afficher que les visites, ou que les téléchargements.

Le tableau affiche :

- Date : La date et l’heure de l’action
- Utilisateur : L’utilisateur à l’origine de l’action (si c’est un visiteur anonyme, on affiche “guest”) et son adresse IP
- Object : L’album ou le fichier concerné. Les visites de la page d’accueil sont identifiées par le libellé “Racine”.
- Détails :  Pour les simples visites, on affiche ici l’album concerné ; pour les téléchargements, on affiche le libellé “Téléchargé”.

![fr-historique-recherche2.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-78f551b9.png)

Il est possible de filtrer la liste sur un utilisateur en particulier en cliquant sur le nom de cet utilisateur dans la barre au dessus du tableau.

L’utilisateur choisi apparaît alors dans les filtres additionnels. Vous pouvez réinitialiser les filtres en cliquant sur la croix à côté de l’utilisateur.

![fr-historique-recherche3.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-b0dd1189.png)

Il est enfin possible de filtrer les actions sur une photo en particulier : pour cela, cliquez sur les 3 points à côté d’une vignette et cliquez sur “Ajouter en temps que filtre”.

![fr-historique-recherche4.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-9cd9e100.png)

Vous pourrez ainsi visualiser tous les téléchargements d’une même photo sur la période de votre choix.

## Visualiser l’activité des administrateurs de Piwigo

Pour visualiser l’historique détaillé de toutes les actions des utilisateurs dans l’administration de Piwigo, vous avez juste à vous rendre dans l’onglet Activité de la page Utilisateurs.

!!! info
    Si vous êtes client d’une offre Piwigo Cloud, cette fonctionnalité n’est accessible qu’à partir de l’offre Équipe.

Cette page affiche toutes les activités réalisées par des utilisateurs dans votre Piwigo :

- Connexion / déconnexion
- Import / modification / suppression de photo (et autres fichiers)
- Création / modification / suppression / déplacement d’album
- Création / modification / suppression d’utilisateur et de groupe d’utilisateur
- Création / modification / suppression de tag

Vous pouvez filtrer cette liste par utilisateur.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-c70b3e56.png)

## AStat.2 : Statistiques détaillées

Pour accéder à des statistiques plus avancées, vous pouvez télécharger le plugin **AStat.2**.

Une fois ce plugin installé, il vous permet de visualiser le nombre de pages vues, d’images vues, d’albums vus, selon de nombreux critères. Il donne accès :

- à des statistiques par période
- à des statistiques par adresse IP
- à des statistiques par album
- à des statistiques par fichier

Des options permettent de personnaliser la présentation des données.

Enfin, ce plugin permet de “nettoyer” les statistiques pour qu’elles soient plus complètes lorsque des utilisateurs, des fichiers ou des albums ont été supprimés.

Il permet enfin de purger votre historique si nécessaire.

![Statistiques par album](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-cbec47bb.png)

Statistiques par album

![Statistiques par photo](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-0b0b921b.png)

Statistiques par photo

![Statistiques par mois](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-feaedf58.png)

Statistiques par mois

## **Statistics :** Intégrer un outil de statistiques externe sur Piwigo

Vous souhaitez suivre les statistiques de votre galerie avec un outil de Web Analytics que vous utilisez déjà comme Google Analytics, Matomo, Piwik ou bien d’autres ?

C’est possible : pour cela il suffit d’activer le plugin **Statistics**.

Une fois ce plugin activé, il vous permet de connecter Piwigo à votre outil statistique externe. Vous devrez récupérer le code de suivi (ou script) de votre outil et le copier dans la configuration du plugin. 

Vous pouvez choisir l’emplacement du code (header ou footer); vous pouvez également choisir d’exclure les administrateurs ou les utilisateurs non connectés des statistiques.

!!! Warning "Attention"
    Pour être conforme à la règlementation, nous vous conseillons de suivre les recommandations de la CNIL en matière de suivi des données et de collecte du consentement des utilisateurs. [Voir les recommandations de la CNIL](https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies-solutions-pour-les-outils-de-mesure-daudience)

## **No Stats for Robots :** Exclure les robots des statistiques

Il arrive que les statistiques de Piwigo soient “polluées” par les visites des robots (moteurs de recherche etc). 

Pour les exclure, il suffit d’activer le plugin **No Stats for Robots**.

Ce plugin exclut les passages des robots connus de vos statistiques de visite.
