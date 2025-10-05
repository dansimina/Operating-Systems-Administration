#!/bin/bash

if test $# -ne 2
then
    echo Wrong number of args
    exit
fi

if ! test -d $1 
then 
    echo First arg must be a directory
    exit
fi

if test $(ls | grep -x $2 | wc -l) -ne 0
then 
    path="$1/$2"

    if test -d $path
    then
        echo Already exists as a directory
    else
        echo Already exists as a file
    fi
else
    initial_path=$(pwd)
    cd "$1"

    echo testing text > "$2.file"
    mkdir "$2.dir"

    no_chars=$(wc -c < "$2.file")

    echo There are $no_chars characters in the file

    cd "$initial_path"
fi


