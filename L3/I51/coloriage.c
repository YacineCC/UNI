int coloriage(Graph* g, int k){
    // Pour tous les sommets
    for(int i=0; i<g->nbVertices; i++){
        // liste vide de k+1 couleurs (0=noir)
        int attrib[k+1];
        for(int j=0; j<k+1; j++) attrib[j]=0; // aucune couleur attrib avant parcours des voisins
        // pour chaques voisins
        Node* tmp = g->adjLists[i];
        while(tmp!=NULL){
            if(attrib[g->colors[tmp->vertex]]==0) // si la couleur du voisin n'est pas attrib
                attrib[g->colors[tmp->vertex]] = 1; // eole deviens attrib
            tmp = tmp->next; //  voisin suivant
        }
        int newcolor=0; // nouvelle couleur = noir
        // parcours des couleurs attrib
        for(int j=1; j<k; j++){
            if(attrib[j]==0 && newcolor==0) // si couleur non attrib et newcolor tjr noir
                newcolor = j; // newcolor prend l'indice de la couleur libre
        //( le sommet prendras forcement la promière couleur non attrib si il y en a une )
        } 

        // si le sommet courant est toujours noir
        if(newcolor==0){    
            // coloriage impossible
            fprintf(stderr, "%d-coloriage IMPOSSIBLE !!", k);
            return 0; // coloriage possible
        }else
            // modif dans la structure de la couleur du sommet (par defaut noir)
            g->colors[i] = newcolor;

    }
    return 1; // coloriage impossible
}
