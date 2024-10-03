#include "disjoint.h"

ed singleton(int s)
{
	ed e =(ed)malloc(sizeof(enred));
	e->num = s;
	e->rang = 0;
	e->rep = e;
	return e;
}

void reunion(ed x, ed y)
{
	if(x->rang == y->rang)
		x->rang++;
	if(y->rang < x->rang)
		y->rep = x;
	else
		x->rep = y;
}

ed representant(ed x)
{
	ed final = x;
	while(final->rep != final)
		final = final->rep;
	ed tmp;
	while(x != final)
	{
		tmp = x;
		x = x->rep;
		tmp->rep = final;
	}
	return final;
}



