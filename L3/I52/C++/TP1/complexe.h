#ifndef _COMPLEXE_H
#define _COMPLEXE_H
typedef struct
{
    float reel;
    float imm;
	int ident; //identificateur
}Complexe;

typedef Complexe* ptComplexe;

void AfficherComplexe(const Complexe&);
Complexe Somme(const Complexe&, const Complexe&);
Complexe Produit(const Complexe&, const Complexe&);
float Module(const Complexe&);
Complexe Conjuge(const Complexe&);
void Init(Complexe&);
//void CreerComplexe(Complexe**);
//void CreerComplexe(ptComplexe&);
Complexe* CreerComplexe();
Complexe* CreerVecteurComplexe(int n);
#endif
