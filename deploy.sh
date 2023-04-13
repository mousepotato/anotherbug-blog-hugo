#!/bin/bash
echo -e "\033[0;32mDeploying updates to GitHub...\033[0m"

msg="rebuilding site `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi

# Push Hugo content
git add .
git commit -m "$msg"
git push origin master


# Build the project.
# modified theme at: https://github.com/mousepotato/mogege
# hugo -t mogege #if using a theme, replace by `hugo -t <yourtheme>`

#cp -rf /Users/$(whoami)/Dropbox/Projects/anotherbug-blog-hugo/public/* /Users/$(whoami)/Dropbox/Projects/mousepotato.github.io/
#cd /Users/$(whoami)/Dropbox/Projects/mousepotato.github.io/

cp -rf /Users/sli/Library/CloudStorage/Dropbox/Projects/anotherbug-blog-hugo/public/* /Users/sli/Library/CloudStorage/Dropbox/Projects/mousepotato.github.io/
cd /Users/sli/Library/CloudStorage/Dropbox/Projects/mousepotato.github.io

git add .
git commit -m "$msg"
git push origin master
