#!/bin/bash

if [ $# -lt 3 ]; then exit; fi
max=$1
pas=$3
sample=$2
for((n=0; n<max; n=n+pas))
do
	./randconnexe "$n" "$sample"
done > ../../entrees/rand.dat
gnuplot 'rand.plt'
