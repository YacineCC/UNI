HEADERS_PATH=./headers
CFLAGS=-Wall -g -I $(HEADERS_PATH)

SRC=$(wildcard sources/*.c)
HEADERS=$(wildcard headers/*.h)
OBJ=$(patsubst sources/%.c, objets/%.o, $(SRC))

libgraphe.a: $(OBJ)
	ar -crs libgraphe.a $(OBJ)
	

objets/%.o: sources/%.c headers/%.h
	gcc $(CFLAGS) -c $< -o $@

clean:
	rm -f objets/*.o
proper:
	rm -f *.a
