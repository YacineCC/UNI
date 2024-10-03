#ifndef SEMANTIC_H
#define SEMANTIC_H

#include "ts.h"
#include "asa.h"
#include "codegen.h"

void semantic(asa *p);
void semantic_NB(asa * p);
void semantic_OP(asa * p);
void semantic_AFFECTATION(asa * p);
void semantic_ID(asa * p);
void semantic_DECLAVAR(asa * p);
void semantic_INST(asa * p);
void semantic_LISTE_INST(asa * p);
void semantic_SI(asa * p);
void semantic_TQ(asa * p);
void semantic_RETOURNER(asa *p);

extern table_symb TABLE_SYMBOLES;


//char CTX[32];

#endif
