SHELL=bash
CC=gcc
CFLAGS=-Wall
GP=gnuplot

crible.exe: crible.c
	$(CC) $(CFLAGS) -o $@ $^

data.dat: crible.exe
	./crible.exe -p100 -l10 | tr -d "pi()"| tr = " " > data.dat

timing.png: crible.exe timing.plot
	i=10; >timing.dot;
	while[[$$i -le 28]];do
		./crible.exe -t -l$$i >> timing.dot;
	done
	$(GP) timing.plot
		









