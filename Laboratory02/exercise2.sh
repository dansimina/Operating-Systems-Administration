#!/bin/bash

if test $# -ne 1
then
	echo "Function needs file path"
	exit
fi

if ! test -f $1
then
	echo "It's not a file"
	exit
fi

grep -c -E [.]* $1
