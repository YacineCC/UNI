CFLAG=-Wall -g
OBJETS=complexe.o vecteurcomplexe.o

libcomplexe.a: $(OBJETS)
	ar crs libcomplexe.a $(OBJETS)
	ranlib libcomplexe.a



vecteurcomplexe.o: vecteurcomplexe.cc vecteurcomplexe.h complexe.h
	g++ $(CFLAGS) -c vecteurcomplexe.cc

complexe.o: complexe.cc complexe.h
	g++ $(CFLAG) -c complexe.cc

