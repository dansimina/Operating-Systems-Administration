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

