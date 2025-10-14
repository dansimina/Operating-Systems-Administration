#!/bin/bash
#!/bin/bash

if test $# -ne 2 
then 
    echo "The script requires 2 arguments (dir path, string)"
    exit
fi

if ! test -d $1
then 
    echo "The first parameter must be a directory"
    exit
fi

function verifica () {
    if test $(ls -a $1 2> /dev/null | grep -c -x "$1") -gt 0 && test -f $1
    then 
        return 0
    else 
        return 1
    fi
}

function calculeaza_dimensiune() {
    echo $(wc -c < "$1")
}

function calculeaza_dimensiune_rec() {
    file_path="$1/$2"
    sum=0
    if verifica $file_path
    then  
        sum=$(calculeaza_dimensiune $file_path)
    fi

    for f in $1/*
    do 
        if test -d $f
        then 
            res=$(calculeaza_dimensiune_rec $f $2)
            sum=`expr $res + $sum`
        fi
    done

    echo $sum
}

calculeaza_dimensiune_rec $1 $2
