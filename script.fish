#!/usr/bin/fish

# Snipets used to get metadata


# Get all html pages
for file in $(find docs/ -name '*.md')
    set filepath $(echo $file | perl -pe "s/^docs//" | perl -pe 's/(\/index)?\.md$//')
    set dir $(dirname $file | perl -pe 's/^docs(\/)?//')
    mkdir -p "html/$dir"
    curl "https://doc-fr.piwigo.org$filepath" > "html$(echo $file | perl -pe 's/^docs//')"
end

# Get metadata from webpage
for file in $(find html/ -name '*.md')
    set filepath $(echo $file | perl -pe "s/^html//")
    set metadata $(cat html/$filepath | pcregrep --buffer-size=256K -o '<title>.*?<\\/title><meta name="description" content="(.|\n)*?\\/>')
    set title $(echo $metadata | pcregrep -io1 '<title>(.*?)</title>')
    set desc $(echo $metadata | pcregrep -io1 '<meta name="description" content="((?:.|\n)*?)"\/>')
    if string length --quiet $metadata;
        sed -ie "1s;^;---\ntitle: $title\ndescription: $desc\n---\n\n;" docs$filepath
        if not test $status -eq 0;
            echo docs$filepath
            #echo $desc;
        end
    end
end

# Manual parse with regex to remove double prefix :
#
# ---\n+---\n
#
#

# Manual parsing for a few files that didn't pass in the first script

# for item in $doclst;
#         set filepath $(echo $item | perl -pe "s/^docs//")
#         set metadata_v1 $(cat html/$filepath | pcregrep --buffer-size=256K -o '<title>.*?<\\/title><meta name="description" content="(.|\n)*?\\/>');
#         set metadata $(cat html/$filepath | pcregrep --buffer-size=256K -o '<meta name="description" content="(.|\n)*?\\/>');
#         set title $(echo $metadata_v1 | pcregrep -io1 '<title>(.*?)</title>')
#         set desc $(echo $metadata | pcregrep -io1 '<meta name="description" content="((?:.|\n)*?)"\/>')
#         set title $(string unescape $title | perl -pe 's/&#x27;/\'/g');
#         set desc $(string unescape $desc | perl -pe 's/&#x27;/\'/g');
#         echo "
#     ---
#     title: \"$title\"
#     description: \"$desc\"
#     ---"
# end
# Manual edit for documents that the script didn't match
