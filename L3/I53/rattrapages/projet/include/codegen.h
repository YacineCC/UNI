#ifndef CODEGEN_H
#define CODEGEN_H

#include "ts.h"
#include "asa.h"
#include "ram_os.h"

extern FILE * exefile;
extern char CTX[32];
extern table_symb TABLE_SYMBOLES;

void codegen(asa *p);

void codeNB(asa * p);
void codeOP(asa * p);
void code_ROOT(asa* p);
void code_DECLAS_VARS(asa* p);
void code_DECLA_VARS(asa* p);
void code_DECLAS_FCT(asa* p);
void code_FCT(asa* p);
void code_ID(asa* p);
void code_INSTS(asa* p);
void code_AFFECTATION(asa* p);
void code_ECRIRE(asa* p);
void code_LIRE(asa* p);
void RAM_OS();
void code_SI(asa* p);
void code_TQ(asa* p);
void code_RETOURNER(asa* p);
void code_NON(asa* p);


#endif
