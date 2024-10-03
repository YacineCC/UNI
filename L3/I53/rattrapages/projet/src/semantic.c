#include "semantic.h"
#include "codegen.h"
char CTX[32] = "GLOBAL";
int pointeur_mem_statique = RAM_OS_STATIC_ADR;

/*Fonction qui fait un parcours en profondeur pour verifier la sémantique des noeud, donner une adresse au variables global,
et vérifier la bonne déclaration des variables et si les id rencontrés existent bien dans le contexte, ou dans le contexte global.

Le codelen est égal au codelen des champs + le nombre d'instructions imprimées par codgen sur le fichier de sortie.*/
void semantic(asa *p){
  if(!p)
  return;
  switch (p->type){
  case typeNB:
    semantic_NB(p);
    break;
  case typeOP:
    semantic_OP(p);
    break;
  case type_ROOT:
    semantic_ROOT(p);
    break;
  case type_AFFECTATION:
    semantic_AFFECTATION(p);
    break;
  case type_DECLA_VARS:
    semantic_DECLA_VARS(p);
    break;
  case type_DECLAS_FCT:
    semantic_DECLAS_FCT(p);
    break;
  case type_DECLAS_VARS:
    semantic_DECLAS_VARS(p);
    break;
  case type_FCT:
    semantic_FCT(p);
    break;
  case type_ID:
    semantic_ID(p);
    break;
  case type_INSTS:
    semantic_INSTS(p);
    break;
  case type_PARAM_FCT:
    semantic_PARAM_FCT(p);
    break;
  case type_RETOURNER:
    semantic_RETOURNER(p);
    break;
  case type_SI:
    semantic_SI(p);
    break;
  case type_TQ:
    semantic_TQ(p);
    break;

  case type_ECRIRE:
    semantic_ECRIRE(p);
    break;
  case type_LIRE:
    semantic_LIRE(p);
    break;
  case type_NON:
    semantic_NON(p);
    break;
  default:
    break;
  }
}
void semantic_NB(asa * p)
{
  p->codelen = 1;
  p->memadr = 0;
}



void semantic_OP(asa * p)
{
  p->memadr = 0;

  semantic(p->op.noeud[0]);
  semantic(p->op.noeud[1]);
  p->codelen = p->op.noeud[0]->codelen + p->op.noeud[1]->codelen;

  switch (p->op.ope){
  case '+':  // operateur binaire associatif a gauche (+ - * / % )
  case '-':
  case '*':
  case '/':
  case '%':
    p->codelen += 4;
    break;
  case '>':
  case '<':
  case 'd':
  case '=':
    p->codelen += 8;
    break;
  case 's':
  case 'i':
  case 'o':
    p->codelen += 9;
    break;
  case 'e':
    p->codelen += 10;
    break;
  default:
    break;
  }
}

void semantic_ROOT(asa* p)
{
  int ramos = 4;
  p->codelen = ramos;
  p->memadr = 0;
  semantic(p->root.declas_vars);
  semantic(p->root.declas_fcts);
  semantic(p->root.main);

  // Prise en charge des cas où il n'y a pas de déclarations de variables global, ou de déclarations de fonctions.
  if(p->root.declas_vars == NULL && p->root.declas_fcts == NULL)
    p->codelen += p->root.main->codelen;
  else
    if(p->root.declas_fcts == NULL)
      p->codelen += p->root.declas_vars->codelen + p->root.main->codelen;
    else
      if(p->root.declas_vars == NULL)
      p->codelen += p->root.declas_fcts->codelen + p->root.main->codelen;
      else
        p->codelen += p->root.declas_vars->codelen + p->root.declas_fcts->codelen + p->root.main->codelen;

}

void semantic_DECLAS_VARS(asa* p)
{
  p->memadr = 0;

  semantic(p->declas_vars.decla_var);
  semantic(p->declas_vars.decla_var_svt);
  // Prise en charge du cas où il n'y a pas de declas_vars suivante. Les autres fonctions suivent la même logique.
  if(p->declas_vars.decla_var_svt == NULL)
    p->codelen = p->declas_vars.decla_var->codelen;
  else
    p->codelen = p->declas_vars.decla_var->codelen + p->declas_vars.decla_var_svt->codelen;
}

void semantic_DECLAS_FCT(asa* p)
{
  p->memadr = pointeur_instruction;

  semantic(p->declas_fct.fct);
  semantic(p->declas_fct.fct_svt);
  if(p->declas_fct.fct_svt == NULL)
    p->codelen = p->declas_fct.fct->codelen;
  else
    p->codelen = p->declas_fct.fct->codelen + p->declas_fct.fct_svt->codelen;
}

void semantic_FCT(asa* p)
{
  p->memadr = pointeur_instruction;

  // On vérifie si la fonction n'a pas déjà été déclaré. Si oui on met un warning sinon on l'ajoute à une table de symbole.
  if(ts_rechercher_identificateur(TABLE_SYMBOLES, p->fct.id, CTX) == NULL)
  {
    ts_ajouter_identificateur(TABLE_SYMBOLES, CTX, p->param_fct.id, 'f', 1, p->memadr);

  }
  else
  {
    printf("\x1b[31m[Warning %s déja déclaré ]\x1b[0m\n", p->fct.id);
    exit(EXIT_FAILURE);
  }



  // On ajoute le nom de la fonction comme contexte à la table de symbole.
  // Puis on change le contexte courant par le nom de la fonction. Une fois
  // sortie de la fonction on remet le contexte courant à GLOBAL.
  ts_ajouter_contexte(TABLE_SYMBOLES, p->fct.id);
  strcpy(CTX, p->fct.id);
  semantic(p->fct.param);
  semantic(p->fct.decla_var);
  semantic(p->fct.liste_insts);
  strcpy(CTX, "GLOBAL");
  
  if(p->fct.decla_var == NULL && p->fct.param == NULL)
    p->codelen = p->fct.liste_insts->codelen;
  else
    if(p->fct.param == NULL)
      p->codelen = p->fct.decla_var->codelen + p->fct.liste_insts->codelen;
    else
      if(p->fct.decla_var == NULL)
        p->codelen = p->fct.liste_insts->codelen + p->fct.param->codelen;
      else
        p->codelen = p->fct.decla_var->codelen + p->fct.liste_insts->codelen + p->fct.param->codelen;
  
}

void semantic_PARAM_FCT(asa* p)
{
  p->memadr = 0;
  // On verifie qu'il n'y a pas deux fois le même paramètre.
  if(ts_rechercher_identificateur(TABLE_SYMBOLES, p->param_fct.id, CTX) == NULL)
  {
    ts_ajouter_identificateur(TABLE_SYMBOLES, CTX, p->param_fct.id, 'e', 1, p->memadr);

  }
  else
  {
    printf("\x1b[31m[Warning %s déja déclaré ]\x1b[0m\n", p->param_fct.id);
    exit(EXIT_FAILURE);
  }
  semantic(p->param_fct.param_svt);
  if(p->param_fct.param_svt == NULL)
     p->codelen = 1;
  else
    p->codelen = 1 + p->param_fct.param_svt->codelen;
}

void semantic_DECLA_VARS(asa* p)
{

  // On vérifie que la variable n'est pas déclarée deux fois dans un même contexte.
  if(ts_rechercher_identificateur(TABLE_SYMBOLES, p->decla_vars.id, CTX) == NULL)
  {
    p->codelen = 1;
    // La variable est mise en mémoire global
    if(strcmp(CTX, "GLOBAL") == 0)
      p->memadr = pointeur_mem_statique++;
    else
      p->memadr = 0;
    ts_ajouter_identificateur(TABLE_SYMBOLES, CTX, p->decla_vars.id, 'e', 1, p->memadr);

  }
  else
  {
    printf("\x1b[31m[Warning %s déja déclaré ]\x1b[0m\n", p->decla_vars.id);
    exit(EXIT_FAILURE);
  }
  semantic(p->decla_vars.exp);
  semantic(p->decla_vars.var_svt);
  int codelen_exp;
  if(p->decla_vars.exp == NULL)
    codelen_exp = 0;
  else
    codelen_exp = p->decla_vars.exp->codelen; 
  if(p->decla_vars.var_svt == NULL)
    p->codelen = 1 + codelen_exp;
  else
    p->codelen = 1 + p->decla_vars.var_svt->codelen + codelen_exp;
}


void semantic_ID(asa* p)
{
  p->codelen = 1;
  p->memadr = 0;

  // On regarde si la variable a déjà été déclaré dans le contexte courant. Sinon on regarde en GLOBAL. Sinon erreur/warning.
  if(ts_rechercher_identificateur(TABLE_SYMBOLES, p->id.nom, CTX) == NULL)
  {
    if(ts_rechercher_identificateur(TABLE_SYMBOLES, p->id.nom, "GLOBAL") == NULL)
    {
      printf("\x1b[31m[Warning %s n'est déclaré nulle part ]\x1b[0m\n", p->id.nom);
      exit(EXIT_FAILURE);
    }
  }
  return;
  
}



void semantic_SI(asa* p)
{
  p->memadr = 0; 
  semantic(p->si.condition);
  semantic(p->si.liste_insts_si);
  semantic(p->si.liste_insts_sinon);
  if(p->si.liste_insts_sinon == NULL)
    p->codelen = p->si.condition->codelen + p->si.liste_insts_si->codelen + 1;
  else
    p->codelen = p->si.condition->codelen + p->si.liste_insts_sinon->codelen + p->si.liste_insts_si->codelen + 2;

}

void semantic_TQ(asa* p)
{
  p->memadr = 0;
  p->codelen = 2;
  semantic(p->tq.condition);
  semantic(p->tq.liste_insts);
  p->codelen += p->tq.condition->codelen + p->tq.liste_insts->codelen;

}

void semantic_RETOURNER(asa* p)
{
  semantic(p->retourner.exp);
  p->codelen = p->retourner.exp->codelen + 1;
}

void semantic_AFFECTATION(asa* p)
{
  // Vérification de l'existence de la variable qui va être affectée.
  if(ts_rechercher_identificateur(TABLE_SYMBOLES, p->affectation.id, CTX) == NULL)
  {
    if(ts_rechercher_identificateur(TABLE_SYMBOLES, p->affectation.id, "GLOBAL") == NULL)
    {
      printf("\x1b[31m[Warning %s n'est déclaré nulle part ]\x1b[0m\n", p->id.nom);
      exit(EXIT_FAILURE);
    }
  }
  p->memadr = 0;
  semantic(p->affectation.exp);
  p->codelen = 1 + p->affectation.exp->codelen;
}

void semantic_INSTS(asa* p)
{
  p->memadr = 0;

  semantic(p->insts.instruction);
  semantic(p->insts.instruction_svt);
  if(p->insts.instruction_svt == NULL)
    p->codelen = p->insts.instruction->codelen;
  else 
    p->codelen = p->insts.instruction->codelen + p->insts.instruction_svt->codelen;
}

void semantic_ECRIRE(asa* p)
{
  p->memadr = 0;

  semantic(p->ecrire.exp);
  p->codelen = p->ecrire.exp->codelen + 1;
}

void semantic_LIRE(asa* p)
{
  p->memadr = 0;
  p->codelen = 1;
}

void semantic_NON(asa* p)
{
  p->memadr = 0;
  semantic(p->non.exp);
  p->codelen = 6 + p->non.exp->codelen;
}

