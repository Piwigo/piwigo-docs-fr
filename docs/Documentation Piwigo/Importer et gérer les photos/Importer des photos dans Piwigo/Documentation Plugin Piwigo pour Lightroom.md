# Documentation : Plugin Piwigo pour Lightroom

Si vous utilisez le gestionnaire de photos Adobe Lightroom, vous pouvez installer un plugin qui vous permettra de transférer vos photos directement vers votre Piwigo. Ce plugin n’est pas développé par Piwigo. Il est vendu 15$ par son concepteur.

- [Page officielle du plugin](https://alloyphoto.com/plugins/piwigo/)
- [Discussion sur le plugin sur le forum FR](http://fr.piwigo.org/forum/viewtopic.php?id=18981)
- [Discussion sur le plugin sur le forum EN (officiel)](http://alloyphoto.com/plugins/piwigo/)

<aside>
⚠️

Cette documentation date de la version 1.6.2 r1034 du plugin. Nous en sommes aujourd’hui à la version 3.1.0 (publiée en octobre 2021), elle peut donc être incomplète. 

</aside>

## Description du plugin

Ce module externe (plugin) pour Lightroom se présente sous la forme d'un service de publication qui va pouvoir communiquer entre Lightroom et votre galerie Piwigo.

L'utilisation de ce module n'est prévu que pour un poste de travail (mono-utilisateur).

## Fonctionnalités du plugin

- Création d'albums.
- Gestion des sous-albums.
- Alimentation manuel et automatique (Smart Albums).
- Synchronisation avec les commentaire en ligne et la notation de vos photos.
- Gestion des commentaires laissés par vos visiteurs. Réponse de votre part possible depuis LR.
- Respect de l'ordre d'affichage des photos dans LR lors de la publication (rang).
- Synchronisation rapide lors de changements mineurs sur les photographies.
- Importation d'albums et de photos qui ne proviennent pas de Lightroom.

## Limites

- Seuls les utilisateurs qui ont un status “Administrateur” ou “Webmaster” peuvent utiliser le module externe.
- Un déplacement d'album depuis Piwigo n'apparait pas dans Lightroom. Les arborescences sont indépendantes. Mais il n'y a pas de problème à ce que vous publiiez d'autre photos dans ce même album depuis LR. Même déplacé, le lien vers l'album est toujours opérant.
- La gestion du caractère privé ou public, tout comme le niveau de confidentialité, ne sont pas gérés par le plugin. Tout ce que vous publiez sera soumis au paramétrage de votre galerie (public par défaut).

## Installation du plugin Piwigo pour Lightroom

<aside>
💡

Bien que les modules externes pour Lightroom peuvent se trouver n'importe où sur votre disque dur, on vous recommande chaudement l'emplacement prévu à cet effet par Adobe :

```
C:\Users\xxxxx\AppData\Roaming\Adobe\Lightroom\Modules
```

*Remplacer “xxxxx” par le nom de votre session*

C'est utile lors de la sauvegarde de Lightroom. Pensez-y !

</aside>

1. Fermez Lightroom
2. Téléchargez le fichier zip sur votre ordinateur.
3. Décompressez le contenu dans le dossier de votre choix (voir le paragraphe plus haut).
4. Dans Lightroom, rendez-vous dans \[ Fichier » Gestionnaire de modules externes \] *(raccourcis CTRL + ALT + MAJ + ,)*

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-f3440844.png)

Sur la gauche, vous devriez voir apparaître le module externe nommé “Piwigo”.

Si tout va bien, ce dernier doit être signalé comme étant *installé et fonctionnant*.

<aside>
💡

Pour lever les limitations de la version gratuite (pas plus de 10 photos publiées à la fois) pensez à acheter votre licence 

</aside>

Vous pouvez fermer la fenêtre du gestionnaire.

## Configuration du plugin Piwigo pour Lightroom

Rendez-vous dans le module “Bibliothèque” *(raccourcis touche **E**)*

Vous devriez trouvez sur la gauche, dans le menu ”*Services de publication*” l'entrée **“Piwigo”** et en bout de ligne la notion *“Configurer”*. Cliquez dessus.

*Alternative* : fenêtre accessible aussi en faisant un clic droit sur le service de Piwigo, puis “Modifier les paramètres”

Une nouvelle fenêtre, propre au module externe, s'ouvre.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-3b2a5c7d.png)

Voici quelques explications sur les options de configuration.

### **Cadre Service de publication**

*Description* ⇒ Optionnel, donne une description au service de publication. Ce nom sera affiché dans la colonne des services de publication de Lightroom.

### **Cadre Piwigo**

*Adresse URL du serveur* ⇒ Adresse (URL) de votre galerie du type : `https://monsite.com/piwigo`

*Identifiant* ⇒ Votre nom d’utilisateur sur votre galerie. Doit avoir le status “Administrateur” ou “Webmaster”.

*Mot de passe* ⇒ Le mot de passe associé à l'identifiant.

Si vous lisez en rouge une ligne qui dit : Connexion à votre compte en ligne.

Cela signifie qu'il vous faut soit ressaisir les bons renseignements, soit tout simplement cliquer sur le bouton “**Connexion**”

### **Cadre Options de publication Piwigo**

*Créer un instantané à chaque publication* ⇒ Cette option va créer un “instantané” des photos que vous publierez. Cette instantané est visible dans le module “Développement” et correspond à la photo envoyé à la date indiquée avec les réglages correspondant.

C'est très pratique pour retrouver une version anciennement publiée. Tout le monde ne s'en sert pas.

*Synchronize photo comments and ratings on Publish* ⇒ Va synchroniser les commentaires et les notes laissées sur votre photo qui se trouve déjà en ligne dans votre galerie.

*Use chunked uploads* ⇒ Cette option permet d'éviter d'avoir des messages d'erreur lors de la publication de photos de taille trop importante vers votre galerie. Les hébergeurs (mutualisés surtout) ont tous des limites et cette option permet globalement de découper la photo en plusieurs petit fragments pour mieux les recoller sur le serveur et passer outre la limite de l'hébergeur en envoyant une grosse photo en une seule fois. Si vous n'avez pas ce genre de problème, il est préférable de laisser décochée cette case.

*Valider les paramètres “Dimensionnement de l'image” avant de publier* ⇒ Lors de la publication, le module vous demande de bien vouloir valider (confirmer) la dimension de vos photos à envoyer vers votre galerie. Si vous publiez toujours vos photos dans la même dimension, cocher cette case afin que le module ne vous demande plus de valider ce paramètre à chaque publication.

Validez vos changements en cliquant dans le bas de la fenêtre sur le bouton “Enregistrer”.

## Utilisation du plugin Piwigo pour Lightroom

A présent, vous voilà prêt pour publier vos photos depuis Lightroom vers votre galerie Piwigo !

Un premier album est automatiquement ajouté dans Lightroom (voir ci-dessous). Il ne sert que d'exemple.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-b5f9a0a5.png)

### **Les albums**

Si vous faites un clic droit sur le service de publication, vous pourrez alors choisir de créer 3 types d'albums :

- Créer Album : Ceci est un album tout simple dans lequel on ajoute manuellement (glisser/déposer) les photos de son choix.
- Créer Album dynamique : Il s'agit d'un album dynamique qui se remplira en fonction des règles que vous définirez. Faites un clic droit sur l'album pour en modifier les règles.
- Créer Ensemble de albums : Ce sont des albums dans lesquels on ajoutera uniquement d'autres albums. Vous aurez compris qu'ils servent à créer une arborescence.

A chaque fois qu'un album est créé dans Lightroom, il est instantanément créé dans votre galerie Piwigo.

### **La publication**

Lorsque vous aurez ajouté les photos de votre choix dans l'album correspondant, vous observerez une fenêtre semblable aux captures ci-dessous.

Notez la présences des éléments déjà publiés et ceux qui ne le sont pas encore. La fenêtre est séparée pour bien différencier les éléments.

En haut à droite, on trouve le bouton “Publier” avec à sa gauche, l'URL de l’album de destination.

On retrouvera aussi ce bouton “Publier” en bas à gauche de la fenêtre Lightroom (colonne tout à gauche).

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-9af84880.png)

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-47393e76.png)

### **La re-publication**

Il y a plusieurs manières de re-publier une photo.

- L'auto-détection : Le module détecte immédiatement lorsqu'une photo qui se trouve déjà en ligne à été modifié dans Lightroom et requiert une mise à jour vers Piwigo. À partir de là il est possible de mettre à jour le fichier entier en cliquant sur le bouton “Publier”.
- L'action manuelle : Rien de plus simple pour re-publier une photo. Faites un clic droit sur celle-ci et choisissez l'option “Marquer pour republication”.

### **Supprimer le marquer de re-publication**

Il est parfois nécessaire de ne pas re-publier des photos marquées comme telles : pour cela, clic droit sur vos photos et choisissez l'option “Marquer comme à jour”.

### **Les commentaires et notation**

Dans le module “Bibliothèque”, colonne de droite, vous trouverez une zone qui regroupe les informations sur les commentaires laissés ainsi que les notes attribuées à votre photo.

Il vous est possible de répondre aux commentaires directement via Lightroom via le champs prévu à cet effet.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-04b30e1b.png)

### **Ordre d'affichage des photos**

Ce sujet est important car assez complexe.

Sachez que pour commencer, lorsque l'on édite un album dans le service de publication il est possible de filtrer les photos. Sauf que cette option ne… fonctionne pas (v1.6.2 r1034) Ne perdez donc pas votre temps à chercher comment cela fonctionne.

<aside>
💡

L’information précédente est peut-être obsolète à l’heure où vous lisez ces lignes.

</aside>

Ce qui est sûr, c'est que l'ordre de vos photos est très important notement lors de la première publication. Une fois vos photos en ligne, seul Piwigo pourra modifier l'ordonnancement.

Donc avant de publier, triez bien vos photos dans l'ordre que vous souhaitez.

Lors de la publication, le plugin va commencer par publier vos images en partant de la fin de votre liste de photos.

De ce fait, une fois dans Piwigo il devient facile de trier les photos soit par date d'envoi ou bien alors par rang.

[En savoir plus : discussion sur le forum](https://fr.piwigo.org/forum/viewtopic.php?pid=159797#p159797)

### Lenteurs

Des cas de lenteurs peuvent intervenir. Certaines options sont très gourmandes en ressources et demandent donc beaucoup de temps.

- C'est le cas notement de l'option “*Synchronize photo comments and ratings on Publish*”. À chaque fois que vous publiez une photo, le module va alors chercher à synchroniser tous les commentaires / notes laissés sur les photos qui composent l'album en cours de publication. Donc en fonction du nombres de photos concernées, le temps s'allongera.
- La première photo qui sera publiée sera toujours plus longue que les suivantes. Ce temps est incompressible.

### Astuces

Dans le document ci-dessous, [Mr Denis Gadenne](http://gadenne.eu/) partage son tutoriel pour vous aider à mieux appréhender le plugin Piwigo pour Lightroom.

[procedure_installation_lr_piwigo.pdf](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/05/25/20260525140116-7978c7e5.pdf)
