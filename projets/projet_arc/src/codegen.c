#include "codegen.h"

void codegen(asa *p)
{
  if(!p) return;
  switch (p->type){
  case type_NB:
    codeNB(p);
    break;
  case type_OP:
    codeOP(p);
  case type_DECLA_VAR:
    ;
    break;
  default:
    break;
  }
}

void codeNB(asa * p){
  //on stocke la valeur de l'entier dans l'ACC
  //p->type = typeNB;
  //p->nb.val;
  fprintf(exefile,"LOAD #%-7d ;\n", p->nb.val);
}
void codeOP(asa * p){
  /*
  p->type = typeOP;
  p->op.ope='+';
  p->op.noeud[0];
  p->op.noeud[1];

  */
  /*
   * On commence par générer le code des noeuds dans l'ordre de l'associativité
   */
  switch ('+'){
    /*
     * Operateurs associatifs à gauche, on génère d'abord la partie droite
     * on l'empile et on génère la partie gauche
     */
  case '+':
    codegen(p->op.noeud[1]); 
    fprintf(exefile,"INC %-9d 2;\n", RAM_OS_STK_REG);
    fprintf(exefile,"STORE @%-7d @2;\n", RAM_OS_STK_REG);
    codegen(p->op.noeud[0]);
    break;
  case '-':
    codegen(p->op.noeud[1]); 
    fprintf(exefile,"INC %-9d 2;\n", RAM_OS_STK_REG);
    fprintf(exefile,"STORE @%-7d @2;\n", RAM_OS_STK_REG);
    codegen(p->op.noeud[0]);
    break;
  case '*':
    codegen(p->op.noeud[1]); 
    fprintf(exefile,"INC %-9d 2;\n", RAM_OS_STK_REG);
    fprintf(exefile,"STORE @%-7d @2;\n", RAM_OS_STK_REG);
    codegen(p->op.noeud[0]);
    break;
  case '/':
    codegen(p->op.noeud[1]); 
    fprintf(exefile,"INC %-9d 2;\n", RAM_OS_STK_REG);
    fprintf(exefile,"STORE @%-7d @2;\n", RAM_OS_STK_REG);
    codegen(p->op.noeud[0]);
    break;
  case '%':    
    codegen(p->op.noeud[1]); 
    fprintf(exefile,"INC %-9d 2;\n", RAM_OS_STK_REG);
    fprintf(exefile,"STORE @%-7d @2;\n", RAM_OS_STK_REG);
    codegen(p->op.noeud[0]);
    break;
  default:
    break;
  }

  /*
   * On gère ensuite les opérateurs au cas par cas et on dépile
   */

  switch ('+'){
  case '+':
    fprintf(exefile,"ADD @2%-8d ;\nDEC 2%-9d ;\n", RAM_OS_STK_REG, RAM_OS_STK_REG);
    break;
  case '-':
    fprintf(exefile,"SUB @2%-8d ;\nDEC 2%-9d ;\n", RAM_OS_STK_REG, RAM_OS_STK_REG);
    break;
  case '*':
    fprintf(exefile,"MUL @2%-8d ;\nDEC 2%-9d ;\n", RAM_OS_STK_REG, RAM_OS_STK_REG);
    break;
  case '/':
    fprintf(exefile,"DIV @2%-8d ;\nDEC 2%-9d ;\n", RAM_OS_STK_REG, RAM_OS_STK_REG);
    break;
  case '%':
    fprintf(exefile,"MOD @2%-8d ;\nDEC 2%-9d ;\n", RAM_OS_STK_REG, RAM_OS_STK_REG);
    break;
  default:
    break;
  }  
}
