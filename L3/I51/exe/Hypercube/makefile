CFLAGS=-g -Wall

hypercube:	hypercube.o
	gcc $(CFLAGS) hypercube.o  -o hypercube -L$(LIBTAG) -lgraphe

hypercube.o: hypercube.c
	gcc $(CFLAGS) -c hypercube.c  -I$(HEADTAG)

