#!/bin/bash                                                                        

mkdir -p haystack && cdhaystack

i=0
for n in {1..10}
do
    dirname=hay$n
    mkdir -p $dirname
    for m in {1..10}
    do
        ((i++))
	filename=straw$i
        echo This is $filename > $dirname/$filename
    done
done

touch hay7/needle
