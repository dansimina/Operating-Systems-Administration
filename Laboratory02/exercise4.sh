#!/bin/bash

if test $# -ne 2
then 
    echo The program needs 2 arguments
    exit
fi

if ! test -d $1
then 
    echo The first argument must be the path to a directory
    exit
fi

path=$1
string=$2
files=$(ls $1)

for file in $files
do
    file_path="$path/$file"
    if test -f $file_path
    then
        echo $file
	    result=$(grep -n -i "$string" "$file_path")
        echo "Results for anywhere in line"
        echo "$result"
        if ! test "$result" = ""
        then 
            echo "Number of lines $(echo "$result" | wc -l)"
        else
            echo "0"
        fi
        echo

        result=$(grep -n -E "^$string"[.]* "$file_path")
        echo "Results for when is at the begining of line"
        echo "$result"
        if ! test "$result" = ""
        then 
            echo "Number of lines $(echo "$result" | wc -l)"
        else
            echo "0"
        fi
        echo

        result=$(grep -n -E [.]*"$string"$ "$file_path")
        echo "Results for when is at the end of line"
        echo "$result"
        if ! test "$result" = ""
        then 
            echo "Number of lines $(echo "$result" | wc -l)"
        else
            echo "0"
        fi
        echo

        result=$(grep -n -E [.]*[5-9][5-9][5-9]"$string" "$file_path")
        echo "Results for when is preceded by 3 digit number"
        echo "$result"
        if ! test "$result" = ""
        then 
            echo "Number of lines $(echo "$result" | wc -l)"
        else
            echo "0"
        fi
        echo
    fi
done