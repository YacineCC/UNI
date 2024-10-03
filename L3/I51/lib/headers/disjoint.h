#ifndef DISJOINT_H
#define DISJOINT_H
#include <stdio.h>
#include <stdlib.h>

typedef struct ed
{
	struct ed* rep;
	int rang;
	int num;
}enred, *ed;

ed singleton(int);
void reunion(ed, ed);
ed representant(ed);

#endif
