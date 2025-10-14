#!/bin/bash

if ! (test $# -eq 2 && test -d "$2")
then
	echo "The script requires exactly two parameters: a user id and a directory path"
	exit
fi

echo "User id: $(id -u $1)"
echo "User directory: $(eval echo ~"$1")"

function compute_size() {
	sum=0
	for file in "$1"/*
	do

		if test -d "$file"
		then
			res=$(compute_size "$file" $2)
			sum=`expr $sum + $res`
		elif test -f "$file"
		then
			user=$(ls -l "$file" | cut -d ' ' -f 3)
			if test "$user" = "$2"
			then 
				res=$(wc -c < "$file")
				if test "$res" != ""
				then
					sum=`expr $sum + $res`
				fi
			fi
		fi
	done

	echo "$sum"
}

compute_size $2 $1
