import os
import re

filemap = {
    "/Documentation Piwigo/Administrer Piwigo.md": "/administrer-piwigo.md",
    "/Documentation Piwigo/Administrer Piwigo/Consultez les statistiques de votre Piwigo.md": "/administrer-piwigo/consultez-les-statistiques-de-votre-piwigo.md",
    "/Documentation Piwigo/Administrer Piwigo/Maintenance de votre Piwigo.md": "/administrer-piwigo/maintenance-de-votre-piwigo.md",
    "/Documentation Piwigo/Administrer Piwigo/Plugins pour les administrateurs.md": "/administrer-piwigo/plugins-pour-les-administrateurs.md",
    "/Documentation Piwigo/Comment naviguer dans cette documentation.md": "/comment-naviguer-dans-cette-documentation.md",
    "/Documentation Piwigo/Démarrer avec Piwigo.md": "/demarrer-avec-piwigo.md",
    "/Documentation Piwigo/Démarrer avec Piwigo/Démarrer avec Piwigo en 15 minutes.md": "/demarrer-avec-piwigo/demarrer-avec-piwigo-en-15-minutes.md",
    "/Documentation Piwigo/Démarrer avec Piwigo/Introduction tout comprendre sur Piwigo en 2 minut.md": "/demarrer-avec-piwigo/introduction-tout-comprendre-sur-piwigo-en-2-minutes.md",
    "/Documentation Piwigo/FAQ - Les questions les plus fréquentes sur Piwigo.md": "/faq-questions-frequentes-piwigo.md",
    "/Documentation Piwigo/Gérer les tags.md": "/gerer-les-tags.md",
    "/Documentation Piwigo/Gérer les tags/Créer et gérer les tags.md": "/gerer-les-tags/creer-et-gerer-les-tags.md",
    "/Documentation Piwigo/Gérer les tags/Les tags présentation.md": "/gerer-les-tags/les-tags-presentation.md",
    "/Documentation Piwigo/Gérer les tags/Tag Recognition Taguez automatiquement vos photos.md": "/gerer-les-tags/tag-recognition-piwigo.md",
    "/Documentation Piwigo/Hébergez votre Piwigo.md": "/hebergez-votre-piwigo.md",
    "/Documentation Piwigo/Hébergez votre Piwigo/Déplacez Piwigo vers un autre serveur emplacement.md": "/hebergez-votre-piwigo/deplacez-piwigo-vers-un-autre-serveur.md",
    "/Documentation Piwigo/Hébergez votre Piwigo/Import et synchronisation de photos FTP.md": "/hebergez-votre-piwigo/import-et-synchronisation-de-photos-ftp.md",
    "/Documentation Piwigo/Hébergez votre Piwigo/Installer Piwigo.md": "/hebergez-votre-piwigo/installer-piwigo.md",
    "/Documentation Piwigo/Hébergez votre Piwigo/Installer Piwigo/Installer Piwigo en local.md": "/hebergez-votre-piwigo/installer-piwigo/installer-piwigo-en-local.md",
    "/Documentation Piwigo/Hébergez votre Piwigo/Installer Piwigo/Installer Piwigo sur Debian.md": "/hebergez-votre-piwigo/installer-piwigo/installer-piwigo-sur-debian.md",
    "/Documentation Piwigo/Hébergez votre Piwigo/Installer Piwigo/Installer Piwigo sur un disque dur réseau.md": "/hebergez-votre-piwigo/installer-piwigo/installer-piwigo-sur-un-disque-dur-reseau.md",
    "/Documentation Piwigo/Hébergez votre Piwigo/Installer Piwigo/Installer Piwigo sur un NAS.md": "/hebergez-votre-piwigo/installer-piwigo/installer-piwigo-sur-un-nas.md",
    "/Documentation Piwigo/Hébergez votre Piwigo/Installer Piwigo/Installer Piwigo sur un serveur free fr.md": "/hebergez-votre-piwigo/installer-piwigo/installer-piwigo-sur-un-serveur-freefr.md",
    "/Documentation Piwigo/Hébergez votre Piwigo/Modifier la configuration locale avec LocalFiles E.md": "/hebergez-votre-piwigo/modifier-la-configuration-locale-avec-localfiles-editor.md",
    "/Documentation Piwigo/Hébergez votre Piwigo/Problèmes de génération des vignettes et des minia.md": "/hebergez-votre-piwigo/problemes-generation-vignettes-miniatures.md",
    "/Documentation Piwigo/Historique des modifications.md": "/historique-modifications.md",
    "/Documentation Piwigo/Importer et gérer les photos.md": "/importer-et-gerer-les-photos.md",
    "/Documentation Piwigo/Importer et gérer les photos/Gérez les propriétés et métadonnées de vos fichier.md": "/importer-et-gerer-les-photos/gerez-les-proprietes-et-metadonnees-de-vos-fichiers.md",
    "/Documentation Piwigo/Importer et gérer les photos/Gérez les propriétés et métadonnées de vos fichier/Métadonnées EXIF et IPTC pour utilisateurs avancés.md": "/importer-et-gerer-les-photos/gerez-les-proprietes-et-metadonnees-de-vos-fichiers/mtadonnes-exif-et-iptc-pour-utilisateurs-avancs.md",
    "/Documentation Piwigo/Importer et gérer les photos/Gestion par lot Modifier et gérer une sélection de.md": "/importer-et-gerer-les-photos/gestion-par-lot-modifier-et-gerer-une-selection-de-photos.md",
    "/Documentation Piwigo/Importer et gérer les photos/Importer des photos dans Piwigo.md": "/importer-et-gerer-les-photos/importer-des-photos-dans-piwigo.md",
    "/Documentation Piwigo/Importer et gérer les photos/Importer des photos dans Piwigo/Documentation Piwigo Remote Sync.md": "/importer-et-gerer-les-photos/importer-des-photos-dans-piwigo/documentation-piwigo-remote-sync.md",
    "/Documentation Piwigo/Importer et gérer les photos/Importer des photos dans Piwigo/Documentation Plugin Piwigo pour Lightroom.md": "/importer-et-gerer-les-photos/importer-des-photos-dans-piwigo/documentation-plugin-piwigo-pour-lightroom.md",
    "/Documentation Piwigo/Importer et gérer les photos/Les différents formats de fichiers.md": "/importer-et-gerer-les-photos/les-differents-formats-de-fichiers.md",
    "/Documentation Piwigo/Importer et gérer les photos/Les formats multiples.md": "/importer-et-gerer-les-photos/les-formats-multiples.md",
    "/Documentation Piwigo/Importer et gérer les photos/Modifier ou supprimer une photo.md": "/importer-et-gerer-les-photos/modifier-ou-supprimer-une-photo.md",
    "/Documentation Piwigo/Les applications mobiles.md": "/les-applications-mobiles.md",
    "/Documentation Piwigo/Les applications mobiles/L’application mobile Piwigo NG pour Android.md": "/les-applications-mobiles/lapplication-mobile-piwigo-ng-pour-android.md",
    "/Documentation Piwigo/Les applications mobiles/L’application mobile Piwigo pour iOS.md": "/les-applications-mobiles/lapplication-mobile-piwigo-pour-ios.md",
    "/Documentation Piwigo/Les commentaires et notes.md": "/les-commentaires-et-notes.md",
    "/Documentation Piwigo/Les commentaires et notes/Gérer les commentaires.md": "/les-commentaires-et-notes/commentaires-options-avancees.md",
    "/Documentation Piwigo/Les commentaires et notes/Gérer les notes (votes).md": "/les-commentaires-et-notes/gerer-les-commentaires.md",
    "/Documentation Piwigo/Les commentaires et notes/Personnaliser la gestion des commentaires avec des.md": "/les-commentaires-et-notes/gerer-les-notes-votes.md",
    "/Documentation Piwigo/Les plugins.md": "/les-plugins.md",
    "/Documentation Piwigo/Les plugins/Les plugins sur Piwigo présentation.md": "/les-plugins/les-plugins-sur-piwigo-presentation.md",
    "/Documentation Piwigo/Les thèmes.md": "/les-themes.md",
    "/Documentation Piwigo/Les thèmes/Les thèmes Piwigo présentation.md": "/les-themes/les-themes-presentation.md",
    "/Documentation Piwigo/Les thèmes/Le thème Bootstrap Darkroom.md": "/les-themes/le-theme-bootstrap-darkroom.md",
    "/Documentation Piwigo/Les thèmes/Le thème Modus.md": "/les-themes/le-theme-modus.md",
    "/Documentation Piwigo/Les utilisateurs.md": "/les-utilisateurs.md",
    "/Documentation Piwigo/Les utilisateurs/Créer et gérer les utilisateurs.md": "/les-utilisateurs/creer-et-gerer-les-utilisateurs.md",
    "/Documentation Piwigo/Les utilisateurs/Envoyer des emails de notification aux utilisateur.md": "/les-utilisateurs/envoyer-des-emails-de-notification-aux-utilisateurs.md",
    "/Documentation Piwigo/Les utilisateurs/Gérer les contributeurs (plugin Community).md": "/les-utilisateurs/gerer-les-contributeurs-plugin-community.md",
    "/Documentation Piwigo/Les utilisateurs/Les groupes d’utilisateurs.md": "/les-utilisateurs/les-groupes-dutilisateurs.md",
    "/Documentation Piwigo/Les utilisateurs/Les niveaux de confidentialité.md": "/les-utilisateurs/les-niveaux-de-confidentialite.md",
    "/Documentation Piwigo/Les utilisateurs/Les statuts utilisateurs.md": "/les-utilisateurs/les-statuts-utilisateurs.md",
    "/Documentation Piwigo/Les utilisateurs/Se connecter à Piwigo.md": "/les-utilisateurs/se-connecter-a-piwigo.md",
    "/Documentation Piwigo/Les utilisateurs/Se connecter à Piwigo/Two Factor Authentication activez la double authen.md": "/les-utilisateurs/se-connecter-a-piwigo/two-factor-authentication-activez-la-double-authentification-sur-piwigo.md",
    "/Documentation Piwigo/Les utilisateurs/Utilisateurs présentation.md": "/les-utilisateurs/utilisateurs-presentation.md",
    "/Documentation Piwigo/Naviguer sur votre galerie Piwigo.md": "/naviguer-sur-votre-galerie-piwigo.md",
    "/Documentation Piwigo/Naviguer sur votre galerie Piwigo/Créer des collections (plugin User Collections).md": "/naviguer-sur-votre-galerie-piwigo/creer-des-collections-plugin-user-collections.md",
    "/Documentation Piwigo/Naviguer sur votre galerie Piwigo/Gérer ses favoris.md": "/naviguer-sur-votre-galerie-piwigo/gerer-ses-favoris.md",
    "/Documentation Piwigo/Naviguer sur votre galerie Piwigo/La page Photo sur votre galerie.md": "/naviguer-sur-votre-galerie-piwigo/la-page-photo-sur-votre-galerie.md",
    "/Documentation Piwigo/Naviguer sur votre galerie Piwigo/Les albums sur votre galerie.md": "/naviguer-sur-votre-galerie-piwigo/les-albums-sur-votre-galerie.md",
    "/Documentation Piwigo/Naviguer sur votre galerie Piwigo/Les tags sur votre galerie.md": "/naviguer-sur-votre-galerie-piwigo/les-tags-sur-votre-galerie.md",
    "/Documentation Piwigo/Naviguer sur votre galerie Piwigo/Rechercher une photo sur votre galerie.md": "/naviguer-sur-votre-galerie-piwigo/rechercher-une-photo-sur-votre-galerie.md",
    "/Documentation Piwigo/Naviguer sur votre galerie Piwigo/Rechercher une photo sur votre galerie/[Archive] Ancienne version de la recherche Piwigo.md": "/naviguer-sur-votre-galerie-piwigo/rechercher-une-photo-sur-votre-galerie/archive-ancienne-version-de-la-recherche-piwigo.md",
    "/Documentation Piwigo/Naviguer sur votre galerie Piwigo/Votre galerie présentation.md": "/naviguer-sur-votre-galerie-piwigo/votre-galerie-presentation.md",
    "/Documentation Piwigo/Organiser les albums.md": "/organiser-les-albums.md",
    "/Documentation Piwigo/Organiser les albums/Albums et sous-albums présentation.md": "/organiser-les-albums/albums-et-sous-albums-presentation.md",
    "/Documentation Piwigo/Organiser les albums/Comment créer un album.md": "/organiser-les-albums/comment-creer-un-album.md",
    "/Documentation Piwigo/Organiser les albums/Gérez vos albums.md": "/organiser-les-albums/gerez-vos-albums.md",
    "/Documentation Piwigo/Organiser les albums/Modifier un album.md": "/organiser-les-albums/modifier-un-album.md",
    "/Documentation Piwigo/Organiser les albums/Permissions et visibilité des albums.md": "/organiser-les-albums/permissions-et-visibilite-des-albums.md",
    "/Documentation Piwigo/Organiser les albums/SmartAlbums (albums intelligents).md": "/organiser-les-albums/smartalbums-albums-intelligents.md",
    "/Documentation Piwigo/Personnaliser ma galerie.md": "/personnaliser-ma-galerie.md",
    "/Documentation Piwigo/Personnaliser ma galerie/Ajouter des pages à votre galerie.md": "/personnaliser-ma-galerie/ajouter-des-pages-a-votre-galerie.md",
    "/Documentation Piwigo/Personnaliser ma galerie/Ajouter une bannière personnalisée à votre galerie.md": "/personnaliser-ma-galerie/ajouter-banniere-personnalisee-piwigo.md",
    "/Documentation Piwigo/Personnaliser ma galerie/Gérer les langues disponibles sur votre galerie.md": "/personnaliser-ma-galerie/gerer-les-langues-disponibles-sur-votre-galerie.md",
    "/Documentation Piwigo/Personnaliser ma galerie/Options de personnalisation de votre galerie.md": "/personnaliser-ma-galerie/options-de-personnalisation-de-votre-galerie.md",
    "/Documentation Piwigo/Personnaliser ma galerie/Personnaliser le CSS de votre galerie.md": "/personnaliser-ma-galerie/personnaliser-le-css-de-votre-galerie.md",
    "/Documentation Piwigo/Personnaliser ma galerie/Personnaliser le menu de votre galerie.md": "/personnaliser-ma-galerie/personnaliser-le-menu-de-votre-galerie.md",
    "/Documentation Piwigo/Personnaliser ma galerie/Personnaliser votre galerie avec des plugins.md": "/personnaliser-ma-galerie/personnaliser-votre-galerie-avec-des-plugins.md",
    "/Documentation Piwigo/Personnaliser ma galerie/Personnaliser votre galerie avec des plugins/PWG Stuffs ajouter des blocs sur votre galerie.md": "/personnaliser-ma-galerie/personnaliser-votre-galerie-avec-des-plugins/pwg-stuff-ajouter-des-blocs-sur-votre-galerie.md",
    "/Documentation Piwigo.md": "/index.md",
}

dbck_abs_path = "/home/renarde/Documents/Work/Documentation/piwigo-docs-fr/docs_bck"


def parse_line(line: str, source_file_path: str) -> str:
    link_match_iter = re.finditer(r"!?\[([^\[\]]*)\]\((.*?)\)", line)
    for link_match in link_match_iter:
        if link_match.group(2).endswith(".md"):
            resolved_link = os.path.relpath(
                os.path.abspath(
                    os.path.join(os.path.dirname(source_file_path), link_match.group(2))
                ),
                dbck_abs_path,
            )

            line = line.replace(
                link_match.group(0),
                link_match.group(0).replace(
                    link_match.group(2), filemap["/" + resolved_link].rstrip(".md")
                ),
            )
    return line


for source, target in filemap.items():
    source_file = "docs_bck" + source
    target_file = "docs" + target
    target_folder = os.path.dirname(target_file)
    if not os.path.isdir(target_folder):
        os.makedirs(target_folder)
    with open(source_file, "r") as src, open(target_file, "w") as target:
        for line in src.readlines():
            target.write(parse_line(line, source_file))
