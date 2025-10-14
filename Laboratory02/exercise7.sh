#!/bin/bash

echo -e "Executable files which starts with pass:\n$(find pass* -maxdepth 0 -executable 2> /dev/null)"

echo -e "Files from /tmp with permison 777:\n$(sudo find /tmp -perm 1777)"

echo -e "Files from /home which were modified in the last 10 minutes:\n$(find /home/* -cmin -10 -type f)"

echo "Removing files with .jpg extension from /home:"
for file in $(find /home -name "*.jpg" -size +1M)
do
	echo "$file"
	rm "$file"
done
