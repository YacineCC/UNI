CFLAGS=-Wall -g

esteulerien: esteulerien.o
	gcc $(CFLAGS) $^ -o $@ -L $(LIBTAG) -lgraphe
esteulerien.o: esteulerien.c
	gcc $(CFLAGS) $^  -c -I $(HEADTAG)