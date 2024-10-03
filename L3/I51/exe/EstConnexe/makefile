CFLAGS=-Wall -g

estconnexe: estconnexe.o
	gcc $(CFLAGS) $^ -o $@ -L $(LIBTAG) -lgraphe
estconnexe.o: estconnexe.c
	gcc $(CFLAGS) $^ -c -I $(HEADTAG)