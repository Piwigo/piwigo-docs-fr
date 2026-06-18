# Tag Recognition : Taguez automatiquement vos photos par IA

Vous avez une quantité importante de photos et vous souhaitez les taguer de façon rapide et automatique ? C’est possible avec le plugin Tag Recognition.

<aside>
⚠️ Si vous êtes client d’une offre piwigo.com, ce plugin n’est accessible qu’à partir de l’offre Entreprise.

</aside>

## Choix de l’API à utiliser

Une fois le plugin Tag Recognition installé et activé, rendez vous dans les paramètres du plugin.

Vous devez d’abord choisir quelle solution vous allez utiliser pour la génération automatique des tags. 

En effet, le plugin fait appel à une API tierce de reconnaissance d’image, qui se charge d’analyser vos photos et de générer des tags. Vous pouvez choisir entre deux solutions :

- [Imagga](https://imagga.com/)
- [Microsoft Azure AI Vision](https://azure.microsoft.com/fr-fr/products/ai-services/ai-vision/)

Le choix dépend de vos préférences et du volume de photos à analyser. Ces deux solutions proposent en effet une offre gratuite, et des offres payantes au delà d’un certain volume. Tous les détails sont disponibles sur les sites des prestataires.

<aside>
⚠️ Comme ce plugin utilise une API externe, nous ne pouvons pas vous assurer que vos données ne seront pas utilisées ou vendues. Nous vous recommandons de vérifier la politique de données de chaque API externe que vous utilisez avec ce plugin.

</aside>

## Paramétrer Tag Recognition avec Imagga

Si vous choisissez Imagga, voici la procédure à suivre.

Tout d’abord vous devez créer un compte sur le site [https://imagga.com/](https://imagga.com/).

Dans le tableau de bord de votre compte, vous allez retrouver deux informations dont vous avez besoin : votre clé API (*API key*) et votre clé secrète (*API Secret*). 

![piwigo-tag-reco-imagga.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-0a928d8f.png)

Copiez ces deux clés et collez les dans l’écran de configuration du plugin Tag Recognition. Cliquez sur Enregistrer les paramètres.

![piwigo-tag-reco-imagga2.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-631474b6.png)

[Documentation Imagga](https://docs.imagga.com/)

## Paramétrer Tag Recognition avec Azure AI Vision

Si vous choisissez Azure AI Vision, voici la procédure à suivre.

Tout d’abord, créez un compte sur le site [https://azure.microsoft.com/fr-fr/free/](https://azure.microsoft.com/fr-fr/free/)

Une fois identifié avec votre compte, vous devez vous rendre dans le service Computer Vision. Si vous n’avez pas d’abonnement, choisissez la période d’essai pour commencer. Vous pourrez alors récupérer votre API Endpoint et votre API Key pour les saisir dans la configuration du plugin Tag Recognition.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-3c10df32.png)

[Documentation Azure AI Vision (en anglais)](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview?wt.mc_id=searchAPI_azureportal_inproduct_rmskilling&sessionId=8acf0be16fd54e18a988e52fa4dc2edd)

## Utiliser Tag Recognition pour suggérer des tags sur une photo

Une fois le plugin correctement configuré, vous pourrez l’utiliser pour générer des tags automatiquement.

Pour cela, choisissez une photo que vous souhaitez taguer, et modifiez-la.

Dans le champs de saisie des tags associés à cette photo, cliquez sur l’icône en forme de robot.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-140cd18b.png)

Vous pouvez alors choisir combien de tags vous souhaitez générer, et en quelle langue.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-41ce7edb.png)

Essayons de générer 10 tags pour cette photo de lapin, en français.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-0d73d649.png)

L’API propose les tags suivants :

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-673f726b.png)

Cliquez sur les tags qui vous conviennent, et cliquez sur “Appliquer les tags” : les tags sont ajoutés à votre photo. N’oubliez pas de cliquer sur “Enregistrer les paramètres”.

## Utiliser Tag Recognition pour appliquer des tags en masse à une sélection

Si vous souhaitez aller vite, vous pouvez générer des tags en masse avec la [Gestion par lot.](/importer-et-gerer-les-photos/gestion-par-lot-modifier-et-gerer-une-selection-de-photos)

En effet, une nouvelle action est rendue possible dans le gestionnaire de lot : “Génération de tags”.

Choisissez votre sélection de photos, choisissez l’action “Génération de tags”. Choisissez le nombre de tags à générer et la langue.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-4cc7ee03.png)

Cliquez sur “Appliquer l’action” : le processus se lance. Les photos sont traitées une par une.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-56f59494.png)

Une fois le lot traité, les photos sont taguées ! Vous pouvez vous rendre dans l’onglet “Mode unitaire” du gestionnaire de lot pour vérifier si les tags choisis vous conviennent.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-6afeff08.png)

Sommaire de l’article

---

← Précédent

[Créer et gérer les tags](/gerer-les-tags/creer-et-gerer-les-tags)