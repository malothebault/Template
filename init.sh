#!/bin/bash

OLD_USERNAME="malothebault"
NEW_USERNAME="USER INPUT"
OLD_PROJECT="template"
NEW_PROJECT="USER INPUT"
read -p "Enter your username (in lower case): " NEW_USERNAME
read -p "Enter your project name (in lower case): " NEW_PROJECT

find . -type f ! -regex '\(.*\/\.git.*\|.*\/assets.*\|.*\/build.*\)' -exec sed -i "s/$OLD_PROJECT/$NEW_PROJECT/g" {} +
find . -type f ! -regex '\(.*\/\.git.*\|.*\/assets.*\|.*\/build.*\)' -exec sed -i "s/${OLD_PROJECT^}/${NEW_PROJECT^}/g" {} +
find . -name "com.github.$OLD_USERNAME.$OLD_PROJECT*" -exec rename.ul "$OLD_USERNAME.$OLD_PROJECT" "$NEW_USERNAME.$NEW_PROJECT" '{}' \;

echo "Done! You can start working"
echo "Don't forget to change the description of the project"
echo "You can delete the file init.sh after that"