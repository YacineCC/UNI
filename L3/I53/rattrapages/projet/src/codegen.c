#include "codegen.h"

// Valeur en direct du compteur ordinal de la machine RAM.
int pointeur_instruction = 0;

/* Parcours en profondeur de l'ASA pour produire le code.*/
void codegen(asa *p)
{
  if(!p) return;
  
  switch (p->type){
  case typeNB:
    codeNB(p);
    break;
  case typeOP:
    codeOP(p);
    break;
  case type_ROOT:
    code_ROOT(p);
    break;
  case type_DECLAS_VARS:
    code_DECLAS_VARS(p);
    break;
  case type_DECLA_VARS:
    code_DECLA_VARS(p);
    break;
  case type_DECLAS_FCT:
    code_DECLAS_FCT(p);
    break;
  case type_FCT:
    code_FCT(p);
    break;
  case type_ID:
    code_ID(p);
    break;
  case type_INSTS:
    code_INSTS(p);
    break;
  case type_AFFECTATION:
    code_AFFECTATION(p);
    break;
  case type_ECRIRE:
    code_ECRIRE(p);
    break;
  case type_LIRE:
    code_LIRE(p);
    break;
  case type_SI:
    code_SI(p);
    break;
  case type_TQ:
    code_TQ(p);
    break;
  case type_RETOURNER:
    code_RETOURNER(p);
    break;
  case type_NON:
    code_NON(p);
    break;
  default:
    break;
  }

}

/*Initialisation du début de mémoire statique et du début de pile.*/
void RAM_OS(void)
{
  fprintf(exefile,"LOAD #%-7d ; RAM_OS\n", RAM_OS_EMPILER_ADR);
  fprintf(exefile,"STORE %-7d ; RAM_OS\n", RAM_OS_STK_REG);
  fprintf(exefile,"LOAD #%-7d ; RAM_OS\n", RAM_OS_STATIC_ADR);
  fprintf(exefile,"STORE %-7d ; RAM_OS\n", RAM_OS_STATIC_REG);
  pointeur_instruction += 4;

}

/* On produit le code de chaques champs du noeud, le dernier code éffectué est dans l'accumulateur.*/
void code_ROOT(asa* p)
{
  RAM_OS();
  codegen(p->root.declas_vars);
  codegen(p->root.declas_fcts);
  codegen(p->root.main);
  fprintf(exefile,"STOP ;\n");
  pointeur_instruction += 1;

  
}

void code_DECLAS_VARS(asa* p)
{
  codegen(p->declas_vars.decla_var);
  codegen(p->declas_vars.decla_var_svt);
}


/* On stocke la valeur de l'accumulateur dans l'adresse de la variable.*/
void code_DECLA_VARS(asa* p)
{
  codegen(p->decla_vars.exp);
  symbole* s = ts_rechercher_identificateur(TABLE_SYMBOLES, p->decla_vars.id, CTX);
  int adr = s->adr;
  fprintf(exefile,"STORE %-9d ; DECLA_VAR %s\n", adr, p->decla_vars.id);
  pointeur_instruction += 1;

  codegen(p->decla_vars.var_svt);
;
}

void code_DECLAS_FCT(asa* p)
{
  
  codegen(p->declas_fct.fct);
  codegen(p->declas_fct.fct_svt);
}

void code_FCT(asa* p)
{
  // Changement du contexte au nom de la fonction, le contexte sera remis à GLOBAL en sorti de fonction.
  strcpy(CTX, p->fct.id);
  codegen(p->fct.param);
  codegen(p->fct.decla_var);
  codegen(p->fct.liste_insts);
  strcpy(CTX, "GLOBAL");

}

void code_INSTS(asa* p)
{
  codegen(p->insts.instruction);
  codegen(p->insts.instruction_svt);
}

void code_ID(asa* p)
{
  // On cherche l'adresse d'un ID avec la fonction rechercher_identificateur, on cherche d'abord dans son contexte, pui en GLobal.
  symbole* s = ts_rechercher_identificateur(TABLE_SYMBOLES, p->id.nom, CTX);
  if(s == NULL)
    s = ts_rechercher_identificateur(TABLE_SYMBOLES, p->id.nom, "GLOBAL");
  int adr = s->adr;

  fprintf(exefile,"LOAD %-7d ;   ID\n", adr);
  pointeur_instruction += 1;



}

void codeNB(asa * p){
  //on stocke la valeur de l'entier dans l'ACC
  fprintf(exefile,"LOAD #%-7d ;  NB\n", p->nb.val);
  pointeur_instruction += 1;

}

void codeOP(asa * p){

  /*
   * On commence par générer le code des noeuds dans l'ordre de l'associativité
   */
  switch (p->op.ope){
    /*
     * Operateurs associatifs à gauche, on génère d'abord la partie droite
     * on l'empile et on génère la partie gauche
     */
  case '+':
  case '-':
  case '*':
  case '/':
  case '%':
  case '>':
  case '<':
  case '=':
  case 's':
  case 'i':
  case 'd':
  case 'e':
  case 'o':  
    codegen(p->op.noeud[1]);
    fprintf(exefile,"INC %-9d ; PILE++\n", RAM_OS_STK_REG);
    pointeur_instruction += 1;
    fprintf(exefile,"STORE @%-9d ; STOCKAGE AU SOMMET DE PILE\n", RAM_OS_STK_REG);
    pointeur_instruction += 1;

    codegen(p->op.noeud[0]);
    break;
  
  default:
    break;
  }

  /*
   * On gère ensuite les opérateurs au cas par cas et on dépile
   */

  switch (p->op.ope){
  case '+':
    fprintf(exefile,"ADD @%-8d ; ADDITION\nDEC %-9d ; PILE--\n", RAM_OS_STK_REG, RAM_OS_STK_REG);
    pointeur_instruction += 2;

    break;
  case '-':
    fprintf(exefile,"SUB @%-8d ; SOUSTRACTION\nDEC %-9d ; PILE--\n", RAM_OS_STK_REG, RAM_OS_STK_REG);
    pointeur_instruction += 2;
    
    break;
  case '*':
    fprintf(exefile,"MUL @%-8d ; MULTIPLICATION\nDEC %-9d ; PILE--\n", RAM_OS_STK_REG, RAM_OS_STK_REG);
    pointeur_instruction += 2;
  
    break;
  case '/':
    fprintf(exefile,"DIV @%-8d ; DIVISION\nDEC %-9d ; PILE--\n", RAM_OS_STK_REG, RAM_OS_STK_REG);
    pointeur_instruction += 2;

    break;
  case '%':
    fprintf(exefile,"MOD @%-8d ; MODULO\nDEC %-9d ; PILE--\n", RAM_OS_STK_REG, RAM_OS_STK_REG);
    pointeur_instruction += 2;

    break;
  case '>':
    // On soustrait l'accumulateur avec le sommet de pile, si le résultat est positif alors a > b.
    fprintf(exefile,"SUB @%-8d ; >\n", RAM_OS_STK_REG);
    pointeur_instruction += 1;
    fprintf(exefile,"JUMG %-8d ; >\n", pointeur_instruction+3);
    pointeur_instruction += 1;
    fprintf(exefile, "LOAD #0 ; >\n");
    pointeur_instruction += 1;
    fprintf(exefile, "JUMP %-8d; >\n", pointeur_instruction+2);
    pointeur_instruction += 1;
    fprintf(exefile, "LOAD #1 ; >\n" );
    pointeur_instruction += 1;
    fprintf(exefile, "DEC %-9d ; PILE--\n", RAM_OS_STK_REG);
    pointeur_instruction += 1;

    break;
  case '<':
    // On soustrait l'accumulateur avec le sommet de pile, si le résultat est négatif alors a < b.
    fprintf(exefile,"SUB @%-8d ; <\n", RAM_OS_STK_REG);
    pointeur_instruction += 1;
    fprintf(exefile,"JUML %-8d ; <\n", pointeur_instruction+3);
    pointeur_instruction += 1;
    fprintf(exefile, "LOAD #0 ; <\n");
    pointeur_instruction += 1;
    fprintf(exefile, "JUMP %-8d; <\n", pointeur_instruction+2);
    pointeur_instruction += 1;
    fprintf(exefile, "LOAD #1 ; <\n" );
    pointeur_instruction += 1;
    fprintf(exefile, "DEC %-9d ; PILE--\n", RAM_OS_STK_REG);
    pointeur_instruction += 1;

    break;
  case '=':
    // On soustrait l'accumulateur avec le sommet de pile, si le résultat est nul alors a = b.
    fprintf(exefile,"SUB @%-8d ; =\n", RAM_OS_STK_REG);
    pointeur_instruction += 1;
    fprintf(exefile,"JUMZ %-8d ; =\n", pointeur_instruction+3);
    pointeur_instruction += 1;
    fprintf(exefile, "LOAD #0 ; =\n");
    pointeur_instruction += 1;
    fprintf(exefile, "JUMP %-8d; =\n", pointeur_instruction+2);
    pointeur_instruction += 1;
    fprintf(exefile, "LOAD #1 ; =\n" );
    pointeur_instruction += 1;
    fprintf(exefile, "DEC %-9d ; PILE--\n", RAM_OS_STK_REG);
    pointeur_instruction += 1;

    break;
  case 's':
    // s pour supérieur ou égal.
    // On soustrait l'accumulateur avec le sommet de pile, si le résultat est positif ou nul alors a >= b
    fprintf(exefile,"SUB @%-8d ; >=\n", RAM_OS_STK_REG);
    pointeur_instruction += 1;
    fprintf(exefile,"JUMG %-8d ; >=\n", pointeur_instruction+4);
    pointeur_instruction += 1;
    fprintf(exefile,"JUMZ %-8d ; >=\n", pointeur_instruction+3);
    pointeur_instruction += 1;
    fprintf(exefile, "LOAD #0 ; >=\n");
    pointeur_instruction += 1;
    fprintf(exefile, "JUMP %-9d ; >=\n", pointeur_instruction+2);
    pointeur_instruction += 1;
    fprintf(exefile, "LOAD #1 ; >=\n" );
    pointeur_instruction += 1;
    fprintf(exefile, "DEC %-9d ; PILE--\n", RAM_OS_STK_REG);
    pointeur_instruction += 1;
    break;
  case 'i':
    // i pour inférieur ou supérieur ou égal.
    // On soustrait l'accumulateur avec le sommet de pile, si le résultat est négatif ou nul alors a <= b
    fprintf(exefile,"SUB @%-8d ; <=\n", RAM_OS_STK_REG);
    pointeur_instruction += 1;
    fprintf(exefile,"JUML %-8d ; <=\n", pointeur_instruction+4);
    pointeur_instruction += 1;
    fprintf(exefile,"JUMZ %-8d ; <=\n", pointeur_instruction+3);
    pointeur_instruction += 1;
    fprintf(exefile, "LOAD #0 ; <=\n");
    pointeur_instruction += 1;
    fprintf(exefile, "JUMP %-9d ; <=\n", pointeur_instruction+2);
    pointeur_instruction += 1;
    fprintf(exefile, "LOAD #1 ; <=\n" );
    pointeur_instruction += 1;
    fprintf(exefile, "DEC %-9d ; PILE--\n", RAM_OS_STK_REG);
    pointeur_instruction += 1;
    break;
  case 'd':
    // d pour différent de.
    // On soustrait l'accumulateur avec le sommet de pile, si le résultat est nul on load #0, sinon on load #1.
    fprintf(exefile,"SUB @%-8d ; !=\n", RAM_OS_STK_REG);
    pointeur_instruction += 1;
    fprintf(exefile,"JUMZ %-8d ; !=\n", pointeur_instruction+3);
    pointeur_instruction += 1;
    fprintf(exefile, "LOAD #1 ; !=\n");
    pointeur_instruction += 1;
    fprintf(exefile, "JUMP %-8d; !=\n", pointeur_instruction+2);
    pointeur_instruction += 1;
    fprintf(exefile, "LOAD #0; !=\n" );
    pointeur_instruction += 1;
    fprintf(exefile, "DEC %-9d ; PILE--\n", RAM_OS_STK_REG);
    pointeur_instruction += 1;

    break;
  case 'e':
    // e pour ET.
    // On regarde si l'ACC est positif, si oui on load le sommet de pile, si lui aussi est positif,
    // on saute sur load #1, si l'ACC ou le sommet de pile ne sont pas positif, on saute sur load #0. 
    fprintf(exefile,"JUMG %-8d ; ET\n", pointeur_instruction+3);
    pointeur_instruction += 1;
    fprintf(exefile, "LOAD #0 ; ET\n");
    pointeur_instruction += 1;
    int tmp = pointeur_instruction; // Pour savoir où JUMP
    fprintf(exefile, "JUMP %-8d; ET\n", pointeur_instruction+6);
    pointeur_instruction += 1;
    fprintf(exefile, "LOAD @%-8d ; ET\n", RAM_OS_STK_REG);
    pointeur_instruction += 1;
    fprintf(exefile,"JUMG %-8d ; ET\n", pointeur_instruction+2);
    pointeur_instruction += 1;
    fprintf(exefile,"JUMP %-8d ; ET\n", tmp);
    pointeur_instruction += 1;
    fprintf(exefile, "LOAD #1 ; ET\n");
    pointeur_instruction += 1;
    fprintf(exefile, "DEC %-9d ; PILE--\n", RAM_OS_STK_REG);
    pointeur_instruction += 1;
   

    break;
  case 'o':
    // o pour OU
    // On regarde si l'ACC est positif, si oui saute sur load #1,
    // sinon on regarde le sommet de pile, si il est positif on load #1, si ni l'ACC ni le sommet de pile sont positf, on load #0.
    fprintf(exefile,"JUMG %-8d ; OU\n", pointeur_instruction+5);
    pointeur_instruction += 1;
    fprintf(exefile, "LOAD @%-8d ; OU\n", RAM_OS_STK_REG);
    pointeur_instruction += 1;
    fprintf(exefile,"JUMG %-8d ; OU\n", pointeur_instruction+3);
    pointeur_instruction += 1;
    fprintf(exefile, "LOAD #0 ; OU\n");
    pointeur_instruction += 1;
    fprintf(exefile, "JUMP %-8d; OU\n", pointeur_instruction+2);
    pointeur_instruction += 1;
    fprintf(exefile, "LOAD #1 ; OU\n");
    pointeur_instruction += 1; 
    fprintf(exefile, "DEC %-9d ; PILE--\n", RAM_OS_STK_REG);
    pointeur_instruction += 1;
   

    break;   
  default:
    break;
  }  
}

void code_AFFECTATION(asa* p)
{
  codegen(p->affectation.exp);
  // On cherche l'adresse de l'id pour store le résultat de l'ACC.
  symbole* s = ts_rechercher_identificateur(TABLE_SYMBOLES, p->affectation.id, CTX);
  if(s == NULL)
    s = ts_rechercher_identificateur(TABLE_SYMBOLES, p->affectation.id, "GLOBAL");
  int adr = s->adr;
  fprintf(exefile,"STORE %-9d ; <-\n", adr);
  pointeur_instruction += 1;


}

void code_ECRIRE(asa* p)
{
  codegen(p->ecrire.exp);
  fprintf(exefile,"WRITE ;\n");
  pointeur_instruction += 1;


}
void code_LIRE(asa* p)
{
  
  fprintf(exefile,"READ ;\n");
  pointeur_instruction += 1;


}

void code_SI(asa* p)
{
  // Le cas d'un SI SINON.
  if(p->si.liste_insts_sinon != NULL)
  {
    codegen(p->si.condition);
    // Si la condition est remplie on fait la première liste d'instruction, sinon on saute à la deuxième. 
    fprintf(exefile,"JUMZ %-9d ; SI\n", pointeur_instruction + p->si.liste_insts_si->codelen + 2);
    pointeur_instruction += 1;
    codegen(p->si.liste_insts_si);
    fprintf(exefile,"JUMP %-9d ; SI\n", pointeur_instruction + p->si.liste_insts_sinon->codelen + 1);
    pointeur_instruction += 1;
    codegen(p->si.liste_insts_sinon);
  }
  // Le cas d'un SI simple.
  else
  {
    codegen(p->si.condition);
    // Si la condition n'est pas remplie on saute la liste d'instruction.
    fprintf(exefile,"JUMZ %-9d ; SI\n", pointeur_instruction + p->si.liste_insts_si->codelen + 1);
    pointeur_instruction += 1;
    codegen(p->si.liste_insts_si);
  }



}

void code_TQ(asa* p)
{
  int tmp = pointeur_instruction;
  codegen(p->tq.condition);


   // Pour savoir où JUMP pour boucler.
  // Si la condtion est fausse/ égale à 0, on jump à après la liste d'instruction.
  fprintf(exefile,"JUMZ %-9d ; TQ\n", pointeur_instruction + p->tq.liste_insts->codelen + 2);
  pointeur_instruction += 1;
  codegen(p->tq.liste_insts);
  fprintf(exefile,"JUMP %-9d;  FTQ\n", tmp);
  pointeur_instruction += 1;


}


void code_RETOURNER(asa* p)
{
  codegen(p->retourner.exp);
  fprintf(exefile,"LOAD 0; RETURN\n");
  pointeur_instruction += 1;
}


void code_NON(asa* p)
{
    // Si la valeur de l'accumulateur est égale à 1 on jump pour LOAD #0 sinon on fait l'inverse.
    codegen(p->non.exp);
    fprintf(exefile,"JUMG %-8d ; NON\n", pointeur_instruction+2);
    pointeur_instruction += 1;
    fprintf(exefile,"JUMZ %-8d ; NON\n", pointeur_instruction+3);
    pointeur_instruction += 1;
    fprintf(exefile, "LOAD #0 ; NON\n");
    pointeur_instruction += 1;
    fprintf(exefile, "JUMP %-8d; NON\n", pointeur_instruction+2);
    pointeur_instruction += 1;
    fprintf(exefile, "LOAD #1 ; NON\n");
    pointeur_instruction += 1; 
    fprintf(exefile, "DEC %-9d ; PILE--\n", RAM_OS_STK_REG);
    pointeur_instruction += 1;
  
}