CFLAGS=-g -Wall

coloration:	coloration.o
	gcc $(CFLAGS) coloration.o  -o coloration -L$(LIBTAG) -lgraphe

coloration.o: coloration.c
	gcc $(CFLAGS) -c coloration.c  -I$(HEADTAG)

