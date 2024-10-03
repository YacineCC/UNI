static void parcours(int s, graphe * g)
{
    int t;
    classe[s] = numero;
    taille++;
    // TODO( "compléter la fonction parcours", 1);
    for (t = 0; t < g->nbs; t++)
    {
        if (g->mat[s][t] && !classe[t]) parcours(t, g);
    }
}


Stack* promenade(Graph* g, int s){
    Stack* p = createStack(g->nbVertices);
    while(degre(g, s)>0){
        int y = g->adjLists[s]->vertex;
        push(p, y);
        removeEdge(g, s, y);
        s = y;
    }
    return p;
}


void Euler(Graph* g, int s){
    Stack* p = promenade(g, s);
    while(!isEmpty(p)){
        s = pop(p);
        if(degre(g, s)>0)
            Euler(g, s);
        else
            printf("%d ", s);
    }
}
