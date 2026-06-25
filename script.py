import os
import re

abs = "/home/renarde/Documents/Work/Documentation/piwigo-docs-fr/"

flst = [
    "./administrer-piwigo.md",
    "./administrer-piwigo/consultez-les-statistiques-de-votre-piwigo.md",
    "./administrer-piwigo/maintenance-de-votre-piwigo.md",
    "./administrer-piwigo/plugins-pour-les-administrateurs.md",
    "./comment-naviguer-dans-cette-documentation.md",
    "./demarrer-avec-piwigo.md",
    "./demarrer-avec-piwigo/demarrer-avec-piwigo-en-15-minutes.md",
    "./demarrer-avec-piwigo/introduction-tout-comprendre-sur-piwigo-en-2-minutes.md",
    "./faq-questions-frequentes-piwigo.md",
    "./gerer-les-tags.md",
    "./gerer-les-tags/creer-et-gerer-les-tags.md",
    "./gerer-les-tags/les-tags-presentation.md",
    "./gerer-les-tags/tag-recognition-piwigo.md",
    "./hebergez-votre-piwigo.md",
    "./hebergez-votre-piwigo/deplacez-piwigo-vers-un-autre-serveur.md",
    "./hebergez-votre-piwigo/import-et-synchronisation-de-photos-ftp.md",
    "./hebergez-votre-piwigo/installer-piwigo.md",
    "./hebergez-votre-piwigo/installer-piwigo/installer-piwigo-en-local.md",
    "./hebergez-votre-piwigo/installer-piwigo/installer-piwigo-sur-debian.md",
    "./hebergez-votre-piwigo/installer-piwigo/installer-piwigo-sur-un-disque-dur-reseau.md",
    "./hebergez-votre-piwigo/installer-piwigo/installer-piwigo-sur-un-nas.md",
    "./hebergez-votre-piwigo/installer-piwigo/installer-piwigo-sur-un-serveur-freefr.md",
    "./hebergez-votre-piwigo/modifier-la-configuration-locale-avec-localfiles-editor.md",
    "./hebergez-votre-piwigo/problemes-generation-vignettes-miniatures.md",
    "./historique-modifications.md",
    "./importer-et-gerer-les-photos.md",
    "./importer-et-gerer-les-photos/gerez-les-proprietes-et-metadonnees-de-vos-fichiers.md",
    "./importer-et-gerer-les-photos/gerez-les-proprietes-et-metadonnees-de-vos-fichiers/mtadonnes-exif-et-iptc-pour-utilisateurs-avancs.md",
    "./importer-et-gerer-les-photos/gestion-par-lot-modifier-et-gerer-une-selection-de-photos.md",
    "./importer-et-gerer-les-photos/importer-des-photos-dans-piwigo.md",
    "./importer-et-gerer-les-photos/importer-des-photos-dans-piwigo/documentation-piwigo-remote-sync.md",
    "./importer-et-gerer-les-photos/importer-des-photos-dans-piwigo/documentation-plugin-piwigo-pour-lightroom.md",
    "./importer-et-gerer-les-photos/les-differents-formats-de-fichiers.md",
    "./importer-et-gerer-les-photos/les-formats-multiples.md",
    "./importer-et-gerer-les-photos/modifier-ou-supprimer-une-photo.md",
    "./les-applications-mobiles.md",
    "./les-applications-mobiles/lapplication-mobile-piwigo-ng-pour-android.md",
    "./les-applications-mobiles/lapplication-mobile-piwigo-pour-ios.md",
    "./les-commentaires-et-notes.md",
    "./les-commentaires-et-notes/commentaires-options-avancees.md",
    "./les-commentaires-et-notes/gerer-les-commentaires.md",
    "./les-commentaires-et-notes/gerer-les-notes-votes.md",
    "./les-plugins.md",
    "./les-plugins/les-plugins-sur-piwigo-presentation.md",
    "./les-themes.md",
    "./les-themes/les-themes-presentation.md",
    "./les-themes/le-theme-bootstrap-darkroom.md",
    "./les-themes/le-theme-modus.md",
    "./les-utilisateurs.md",
    "./les-utilisateurs/creer-et-gerer-les-utilisateurs.md",
    "./les-utilisateurs/envoyer-des-emails-de-notification-aux-utilisateurs.md",
    "./les-utilisateurs/gerer-les-contributeurs-plugin-community.md",
    "./les-utilisateurs/les-groupes-dutilisateurs.md",
    "./les-utilisateurs/les-niveaux-de-confidentialite.md",
    "./les-utilisateurs/les-statuts-utilisateurs.md",
    "./les-utilisateurs/se-connecter-a-piwigo.md",
    "./les-utilisateurs/se-connecter-a-piwigo/two-factor-authentication-activez-la-double-authentification-sur-piwigo.md",
    "./les-utilisateurs/utilisateurs-presentation.md",
    "./naviguer-sur-votre-galerie-piwigo.md",
    "./naviguer-sur-votre-galerie-piwigo/creer-des-collections-plugin-user-collections.md",
    "./naviguer-sur-votre-galerie-piwigo/gerer-ses-favoris.md",
    "./naviguer-sur-votre-galerie-piwigo/la-page-photo-sur-votre-galerie.md",
    "./naviguer-sur-votre-galerie-piwigo/les-albums-sur-votre-galerie.md",
    "./naviguer-sur-votre-galerie-piwigo/les-tags-sur-votre-galerie.md",
    "./naviguer-sur-votre-galerie-piwigo/rechercher-une-photo-sur-votre-galerie.md",
    "./naviguer-sur-votre-galerie-piwigo/rechercher-une-photo-sur-votre-galerie/archive-ancienne-version-de-la-recherche-piwigo.md",
    "./naviguer-sur-votre-galerie-piwigo/votre-galerie-presentation.md",
    "./organiser-les-albums.md",
    "./organiser-les-albums/albums-et-sous-albums-presentation.md",
    "./organiser-les-albums/comment-creer-un-album.md",
    "./organiser-les-albums/gerez-vos-albums.md",
    "./organiser-les-albums/modifier-un-album.md",
    "./organiser-les-albums/permissions-et-visibilite-des-albums.md",
    "./organiser-les-albums/smartalbums-albums-intelligents.md",
    "./personnaliser-ma-galerie.md",
    "./personnaliser-ma-galerie/ajouter-des-pages-a-votre-galerie.md",
    "./personnaliser-ma-galerie/ajouter-banniere-personnalisee-piwigo.md",
    "./personnaliser-ma-galerie/gerer-les-langues-disponibles-sur-votre-galerie.md",
    "./personnaliser-ma-galerie/options-de-personnalisation-de-votre-galerie.md",
    "./personnaliser-ma-galerie/personnaliser-le-css-de-votre-galerie.md",
    "./personnaliser-ma-galerie/personnaliser-le-menu-de-votre-galerie.md",
    "./personnaliser-ma-galerie/personnaliser-votre-galerie-avec-des-plugins.md",
    "./personnaliser-ma-galerie/personnaliser-votre-galerie-avec-des-plugins/pwg-stuff-ajouter-des-blocs-sur-votre-galerie.md",
    "./index.md",
]


def parse_line(line: str, target_dir: str) -> str:
    link_match_iter = re.finditer(r"!?\[([^\[\]]*)\]\((.*?)\)", line)
    for link_match in link_match_iter:
        if link_match.group(2).startswith("/"):
            relpath = os.path.relpath(
                os.path.join(
                    "/home/renarde/Documents/Work/Documentation/piwigo-docs-fr/docs",
                    link_match.group(2).lstrip("/"),
                ),
                target_dir,
            )
            line = line.replace(
                link_match.group(0),
                link_match.group(0).replace(link_match.group(2), relpath),
            )

    return line


for dirty_path in flst:
    path = dirty_path.strip("./")
    source_file = os.path.join(
        "/home/renarde/Documents/Work/Documentation/piwigo-docs-fr/docs_bck", path
    )
    target_file = os.path.join(
        "/home/renarde/Documents/Work/Documentation/piwigo-docs-fr/docs", path
    )
    target_folder = os.path.dirname(target_file)
    if not os.path.isdir(target_folder):
        os.makedirs(target_folder)
    with open(source_file, "r") as src, open(target_file, "w") as target:
        for line in src.readlines():
            target.write(parse_line(line, os.path.dirname(target_file)))
