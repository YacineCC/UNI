CFLAGS=-g -Wall


dijkstra : dijkstra.o
	gcc $(CFLAGS) dijkstra.o -o dijkstra -L $(LIBTAG) -lgraphe
dijkstra.o : dijkstra.c
	gcc $(CFLAGS) -c dijkstra.c -I $(HEADTAG)
