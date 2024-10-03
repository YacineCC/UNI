#include "semantic.h"
char CTX[32] = "GLOBAL";

void semantic(asa *p){
  if(!p) return;
  switch (p->type){
  case type_NB:
    semantic_NB(p);
    break;
  case type_OP:
    semantic_OP(p);
    break;
  
  case type_ID:
    semantic_ID(p);
    break;
  case type_INST:
    semantic_INST(p);
    break;
  case type_LISTE_INST:
    semantic_LISTE_INST(p);
    break;
  case type_AFFECTATION:
    semantic_AFFECTATION(p);
    break;
  case type_SI:
    semantic_SI(p);
    break;
  case type_TQ:
    semantic_TQ(p);
    break;
  case type_RETOURNER:
    semantic_RETOURNER(p);
    break;
  default:
    break;
  }
}

void semantic_NB(asa * p)
{
  p->codelen = 1;
}



void semantic_OP(asa * p)
{
  p->codelen = 4;
  switch ('+'){
  case '+':  // operateur binaire associatif a gauche (+ - * / % )
    
  case '-':
    
  case '*':
    
  case '/':
    
  case '%':
    semantic(p->op.noeud[0]);
    semantic(p->op.noeud[1]);
    break;
  }
}

void semantic_ID(asa * p)
{
  
  p->codelen = 1;
  if(ts_rechercher_identificateur(TABLE_SYMBOLES, p->id.nom, CTX) == NULL)
    ts_ajouter_identificateur(TABLE_SYMBOLES, CTX, p->id.nom, type_ID, 1);
  else
    return;
    /* warning*/
}

void semantic_DECLAVAR(asa * p)
{
  p->codelen = 1;
  if(ts_rechercher_identificateur(TABLE_SYMBOLES, p->id.nom, CTX) == NULL)
    return;
    /* warning*/
  else
   ts_ajouter_identificateur(TABLE_SYMBOLES, CTX, p->id.nom, type_ID, 1);
}

void semantic_INST(asa * p)
{

}
void semantic_LISTE_INST(asa * p)
{
  
}
void semantic_AFFECTATION(asa * p)
{
  
}
void semantic_SI(asa * p)
{
  
}
void semantic_TQ(asa * p)
{
  
}
void semantic_RETOURNER(asa * p)
{
  
}