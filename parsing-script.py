import hashlib
import os
import re
import urllib.parse

img_checksum_lst_path = "20260525-mapping-image-doc.txt"
source_path = "20260525-notion-piwigo-doc-fr"
export_path = "docs-fr"


def handle_md_link(raw_line: str, re_match: re.Match, folder: str):
    if (
        re_match.group(2).startswith("http")
        or re_match.group(2) == "mailto:support@piwigo.com"
    ):
        return raw_line  # No need to modify urls links

    # Decode local links
    link = urllib.parse.unquote(re_match.group(2), errors="strict")

    # Replace link with ressource url for images and cleanup filename for md files
    if link.endswith(".md"):
        # Remove trailing blurb
        link = re.sub(r" +\w*\.md", ".md", link)
    else:
        link = img_checksum_dict[
            hashlib.md5(open(os.path.join(folder, link), "rb").read()).hexdigest()
        ]
    new_anchor = f"{'!' if re_match.group(0).startswith('!') else ''}[{re_match.group(1)}]({link})"
    return raw_line.replace(re_match.group(0), new_anchor)


def parse_md(source_md_folder: str, source_md_path: str, export_md_path: str):
    with open(source_md_path, "r") as source, open(export_md_path, "w") as export:
        for line in source.readlines():
            link_match_iter = re.finditer(r"!?\[([^\[\]]*)\]\((.*?)\)", line)
            for link_match in link_match_iter:
                # Convert link as needed
                line = handle_md_link(line, link_match, source_md_folder)
            # Write line in export
            export.write(line)


def parse_dir(origin: str, folder_relative_path: str = ".", recurse: bool = True):
    folder_path = os.path.join(origin, folder_relative_path)
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            # Create a directory in export
            os.mkdir(os.path.join(export_path, folder_relative_path, item))
            if recurse:
                parse_dir(origin, os.path.join(folder_relative_path, item))
        elif item.endswith(".md"):
            # Remove trailing blurb
            md_new_name = re.sub(r" +\w*\.md", ".md", item)
            parse_md(
                os.path.join(origin, folder_relative_path),
                item_path,
                os.path.join(export_path, folder_relative_path, md_new_name),
            )


def main():
    # Create map for images
    with open(img_checksum_lst_path, "r") as img_checksum_lst:
        for line in img_checksum_lst.read().splitlines():
            checksum, link = line.split(" ")
            img_checksum_dict[checksum] = link

    os.mkdir(export_path)
    # Recursively iterate over dirs
    parse_dir(source_path)


img_checksum_dict = {}

if __name__ == "__main__":
    main()
