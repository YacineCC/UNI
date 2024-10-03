CFLAGS=-g -Wall

adjoint: adjoint.o
	gcc $(CFLAGS) adjoint.o  -o adjoint -L$(LIBTAG) -lgraphe

adjoint.o: adjoint.c
	gcc $(CFLAGS) -c adjoint.c  -I$(HEADTAG)

