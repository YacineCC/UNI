static int comp(const void *a1, const void *a2)
{
    return *((int *) a1) - *((int *) a2);
}


void invariant(graphe * g)
{
    int *res;
    res = calloc(g->nbs, sizeof(int));
    // TODO( "à compléter", 1);
    for (int i = 0; i < g->nbs; i++)
    {
        res[i] = degre(i, g);
    }

    qsort(res, g->nbs, sizeof(int), comp);
    g->inv = res;
}
