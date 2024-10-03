#ifndef SEMANTIC_H
#define SEMANTIC_H

#include "ts.h"
#include "asa.h"
#include "codegen.h"

void semantic(asa *p);
void semantic_NB(asa * p);
void semantic_OP(asa * p);
void semantic_ROOT(asa*p);
void semantic_FCT(asa* p);
void semantic_AFFECTATION(asa* p);
void semantic_PARAM_FCT(asa* p);
void semantic_DECLA_VARS(asa* p);
void semantic_DECLAS_VARS(asa* p);
void semantic_DECLAS_FCT(asa* p);
void semantic_ID(asa* p);
void semantic_RETOURNER(asa* p);
void semantic_SI(asa* p);
void semantic_TQ(asa* p);
void semantic_INSTS(asa* p);
void semantic_ECRIRE(asa* p);
void semantic_LIRE(asa* p);
void semantic_NON(asa* p);
void semantic_TAB(asa* p);
void semantic_LISTE_NB(asa* p);

extern int pointeur_instruction;
extern table_symb TABLE_SYMBOLES;

#endif
