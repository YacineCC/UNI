CFLAGS=-Wall -g

testio: testio.o
	gcc $(CFLAGS) $^ -o $@ -L $(LIBTAG) -lgraphe
testio.o: testio.c 
	gcc $(CFLAGS) $^ -c -I $(HEADTAG)