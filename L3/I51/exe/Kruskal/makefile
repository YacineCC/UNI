main: main.o
	gcc $(CFLAGS) main.o -o main -L $(TAG)/lib -lgraphe -lm

main.o: main.c
	gcc $(CFLAGS) -c main.c -I $(TAG)/lib/headers/
