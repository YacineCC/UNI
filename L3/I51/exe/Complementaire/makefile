CFLAGS=-g -Wall

complementaire:	complementaire.o
	gcc $(CFLAGS) complementaire.o  -o complementaire -L$(LIBTAG) -lgraphe

complementaire.o: complementaire.c
	gcc $(CFLAGS) -c complementaire.c  -I$(HEADTAG)

