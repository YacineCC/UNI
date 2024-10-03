CFLAG=-Wall -g
MAKEFLAGS += --no-print-directory
LIB_PATH=$(CPP)/libs
OBJETS=main.o


main.exe: main.o
	g++ $(CFLAG) $(OBJETS) -L $(CPP)/libs/complexe -L $(CPP)/libs/polynome -o main.exe -lcomplexe -lpolynome
main.o: main.cc libs
	g++ $(OPTIONS) -c main.cc -I $(LIB_PATH)/complexe -I $(LIB_PATH)/polynome

libs: libcomplexe libpolynome

libcomplexe: $(CPP)/libs/complexe/libcomplexe.a
	make -C $(CPP)/libs/complexe/

libpolynome: $(CPP)/libs/polynome/libpolynome.a
	make -C $(CPP)/libs/polynome/





