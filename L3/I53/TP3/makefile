CC=gcc
CFLAGS=-Wall -g
LIBS = -lm
OBJS = afd.o afn.o

all: af testOpEns testAjoutEns testEpsFer testAfnOp

af: af.c $(OBJS)
	$(CC) $(CFLAGS) $^ $(LIBS) -o $@

afd.o: afd.c
	$(CC) $(CFLAGS) -c -g $^

afn.o: afn.c
	$(CC) $(CFLAGS) -c -g $^

testOpEns: testOpEns.c $(OBJS)
	$(CC) $(CFLAGS) $^ $(LIBS) -o $@

testAjoutEns: testAjoutEns.c $(OBJS)
	$(CC) $(CFLAGS) $^ $(LIBS) -o $@

testEpsFer:	testEpsFer.c $(OBJS)
	$(CC) $(CFLAGS) $^ $(LIBS) -o $@

testAfnOp: testAfnOp.c $(OBJS)
	$(CC) $(CFLAGS) $^ $(LIBS) -o $@

clean:
	rm -f *~ *.o
