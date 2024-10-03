#include "complexe.h"
void Permuter(int& a, int& b)
{
    int aux = b;
    b = a;
    a = aux;
}

void Permuter(Complexe& a,Complexe& b)
{
    Complexe aux = b;
    b = a;
    a = aux;
}

