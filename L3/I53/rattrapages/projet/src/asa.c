#include "asa.h"

static const char str_type[][16] = {"NB","ID","OP", "INSTS", "AFFECTATION", "DECLAS_VARS", "DECLA_VARS", "FCT", "DECLAS_FCT","PARAM_FCT", "ROOT", "SI", "TQ", "RETOURNER", "ECRIRE", "LIRE", "NON"};
static const char line[36] = "-----------------------------------";

static char buffer[32];
static char TABULATION[256] = "";
static int indent = 0;


/*La creation de noeud suit la même logique pour tous les noeuds, on alloue le noeud, on lui donne son type, et en fonction du type, on affecte
les différents champs.*/

asa * creer_feuilleNB(int val)
{
  asa *p;

  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");

  p->type = typeNB;
  p->nb.val = val;
  return p;
}

asa* creer_feuille_ID(char* nom)
{
  asa *p;

  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");
  
  p->type = type_ID;
  strcpy(p->id.nom, nom);
  return p;
}

asa * creer_noeudOP( int ope, asa * p1, asa * p2)
{
  asa * p;

  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");

  p->type = typeOP;
  p->op.ope = ope;
  p->op.noeud[0]=p1;
  p->op.noeud[1]=p2;
    
  return p;
}

asa* creer_noeud_INSTS(asa* p1, asa* p2)
{
  asa * p;

  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");
  
  p->type = type_INSTS;
  p->insts.instruction = p1;
  p->insts.instruction_svt = p2;
  return p;
}

asa* creer_noeud_AFFECTATION(char* p1, asa* p2)
{
  asa * p;

  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");
  
  p->type = type_AFFECTATION;
  strcpy(p->affectation.id, p1);
  p->affectation.exp = p2;
  return p;
}

asa* creer_noeud_DECLAS_VARS(asa* p1, asa* p2)
{
  asa * p;

  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");
  
  p->type = type_DECLAS_VARS;
  p->declas_vars.decla_var = p1;
  p->declas_vars.decla_var_svt = p2;
  
  return p;
}

asa* creer_noeud_DECLA_VARS(char* p1, asa* p2, asa* p3)
{
  asa * p;

  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");
  
  p->type = type_DECLA_VARS;
  strcpy(p->decla_vars.id, p1);
  p->decla_vars.exp = p2;
  p->decla_vars.var_svt = p3;

  
  return p;
}

asa* creer_noeud_FCT(char* p1, asa* p2, asa* p3, asa* p4)
{
  asa * p;

  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");
  
  p->type = type_FCT;
  strcpy(p->fct.id, p1);
  p->fct.param = p2;
  p->fct.decla_var = p3;
  p->fct.liste_insts = p4;

  return p;
}



asa* creer_noeud_DECLAS_FCT(asa* p1, asa* p2)
{
  asa * p;

  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");
  
  p->type = type_DECLAS_FCT;
  p->declas_fct.fct = p1;
  p->declas_fct.fct_svt = p2;

  return p;
}


asa* creer_noeud_PARAM_FCT(char* p1, asa* p2)
{
  asa * p;

  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");
  
  p->type = type_PARAM_FCT;
  strcpy(p->param_fct.id, p1);
  p->param_fct.param_svt = p2;

  return p;
}

asa* creer_noeud_ROOT(asa* p1, asa* p2, asa* p3)
{
  asa * p;

  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");
  p->type = type_ROOT;
  p->root.declas_vars = p1;
  p->root.declas_fcts = p2;
  p->root.main = p3;

  return p;
}

asa* creer_noeud_SI(asa* p1, asa* p2, asa* p3)
{
  asa * p;

  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");
  
  p->type = type_SI;
  p->si.condition = p1;
  p->si.liste_insts_si = p2;
  p->si.liste_insts_sinon = p3;


  return p;
}

asa* creer_noeud_TQ(asa* p1, asa* p2)
{
  asa * p;

  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");
  
  p->type = type_TQ;
  p->tq.condition = p1;
  p->tq.liste_insts = p2;

  return p;
}

asa* creer_noeud_RETOURNER(asa* p1)
{
  asa * p;

  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");
  
  p->type = type_RETOURNER;
  p->retourner.exp = p1; 
  return p;
}

asa* creer_noeud_ECRIRE(asa* p1)
{
  asa * p;

  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");
  
  p->type = type_ECRIRE;
  p->ecrire.exp = p1; 
  return p;
}

asa* creer_noeud_LIRE(void)
{
  asa * p;

  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");
  
  p->type = type_LIRE;
  return p;
}

asa* creer_noeud_NON(asa* p1)
{
  asa * p;

  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");
  
  p->type = type_NON;
  p->non.exp = p1;
  return p;
}


/*Fonction récursive pour libérer la mémoire allouée, parcours en profondeur de l'arbre.*/
void free_asa(asa *p)
{
  if (p == NULL) return;
  switch (p->type) {
  case typeOP:
    free_asa(p->op.noeud[0]);
    free_asa(p->op.noeud[1]);
    break;
  case typeNB:
    break;
  case type_AFFECTATION:
    free_asa(p->affectation.exp);
    break;
  case type_DECLA_VARS:
    free_asa(p->decla_vars.var_svt);
    free_asa(p->decla_vars.exp);

    break;
  case type_DECLAS_FCT:
    free_asa(p->declas_fct.fct);
    free_asa(p->declas_fct.fct_svt);
    break;
  case type_DECLAS_VARS:
    free_asa(p->declas_vars.decla_var);
    free_asa(p->declas_vars.decla_var_svt);
    break;
  case type_FCT:
    free_asa(p->fct.param);
    free_asa(p->fct.decla_var);
    free_asa(p->fct.liste_insts);
    break;
  case type_ID:
    break;
  case type_INSTS:
    free_asa(p->insts.instruction);
    free_asa(p->insts.instruction_svt);
    break;
  case type_RETOURNER:
    free_asa(p->retourner.exp);
    break;
  case type_ROOT:
    free_asa(p->root.declas_vars);
    free_asa(p->root.declas_fcts);
    free_asa(p->root.main);
    break;
  case type_SI:
    free_asa(p->si.condition);
    free_asa(p->si.liste_insts_si);
    free_asa(p->si.liste_insts_sinon);

    break;
  case type_TQ:
    free_asa(p->tq.condition);
    free_asa(p->tq.liste_insts);
    break;

  case type_PARAM_FCT:
    free_asa(p->param_fct.param_svt);
    break;
  case type_ECRIRE:
    free_asa(p->ecrire.exp);
    break;
  case type_LIRE:
    break;
  case type_NON:
    free_asa(p->non.exp);
    break;

  default:
    break;
  }
  free(p);
}


/*Affichage sur le terminal de l'ASA. On affiche le nom du noeud, son type son adresse éventuelle, et son codelen, puis un gros switch
pour afficher les différents champs en fonction du type.*/
static void print_field(char * field_name, char * field_val, char *TABULATION, char *escape_seq)
{		   
  char buffer[128] = "";
  sprintf(buffer, "%s|%s%*s| ",
	  TABULATION,
	  field_name,
	  MAX_SIZE_FIELD_NAME-(int)strlen(field_name),"");
  printf("%s%s%s" TXT_NULL "%*s\n",
	 buffer,
	 escape_seq,
	 field_val,
	 MAX_SIZE_FIELD_VAL-MAX_SIZE_FIELD_NAME-(int)strlen(field_val),"|");
}

void print_asa(asa * p){
  int i;
  if (!p) return;
  for (i=0; i<indent; i++){ TABULATION[i] = '\t'; }
  TABULATION[i]='\0';

  printf("%s%s\n", TABULATION, line); 
  
  sprintf(buffer, "%p", p);
  print_field("  noeud", buffer, TABULATION,TXT_BLUE TXT_BOLD);

  sprintf(buffer, "%s", str_type[p->type]);
  print_field("  typeNoeud", buffer, TABULATION,"");

  printf("%s%s\n" \
	 "%s|%*s|%*s|\n",TABULATION, line,
	 TABULATION, MAX_SIZE_FIELD_NAME,"",MAX_SIZE_FIELD_VAL-MAX_SIZE_FIELD_NAME,"");

  sprintf(buffer, "%d", p->memadr);
  print_field("adr mem", buffer, TABULATION,"");
  
  sprintf(buffer, "%d", p->codelen);
  print_field("taille code", buffer, TABULATION,"");

  switch (p->type) {
  case typeOP:
    print_typeOP(p);
    break;
  case type_ID:
    print_ID(p);
    break;
  case typeNB:
    print_typeNB(p);  
    break;
  case type_INSTS:
    print_INSTS(p);
    break;
  case type_AFFECTATION:
    print_AFFECTATION(p);
    break;
  case type_DECLAS_VARS:
    print_DECLAS_VARS(p);
    break;
  case type_DECLA_VARS:
    print_DECLA_VARS(p);
    break;
  case type_FCT:
    print_FCT(p);
    break;

  case type_DECLAS_FCT:
    print_DECLAS_FCT(p);
    break;
  case type_PARAM_FCT:
    print_PARAM_FCT(p);
    break;
  case type_ROOT:
    print_ROOT(p);
    break;
  case type_SI:
    print_SI(p);
    break;
  case type_TQ:
    print_TQ(p);
    break;
  case type_RETOURNER:
    print_RETOURNER(p);
    break;
  case type_ECRIRE:
    print_ECRIRE(p);
    break;
  case type_LIRE:
    print_LIRE(p);
    break;
  case type_NON:
    print_NON(p);
    break;
  default:
    break;
  }
}

/*Toutes les fonctions d'affichages suivent la même logique, on utilise un buffer pour print les différents champs,
 puis on parcours en profondeur pour print la suite.*/
void print_typeOP(asa *p)
{
  sprintf(buffer, "%c", p->op.ope);
  print_field("operateur", buffer, TABULATION,"");

  sprintf(buffer, "%p", p->op.noeud[0]);
  print_field("ope gauche", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->op.noeud[1]);
  print_field("ope droite", buffer, TABULATION,TXT_GREEN);
    
  printf("%s%s\n", TABULATION,line);
  indent++; print_asa(p->op.noeud[0]); indent--;
  indent++; print_asa(p->op.noeud[1]); indent--;
  
}

void print_INSTS(asa* p)
{
  sprintf(buffer, "%p", p->insts.instruction);
  print_field("Instruction", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->insts.instruction_svt);
  print_field("Instruction_svt", buffer, TABULATION,TXT_GREEN);
  indent++; print_asa(p->insts.instruction); indent--;
  indent++; print_asa(p->insts.instruction_svt); indent--;

}

void print_AFFECTATION(asa* p)
{
  sprintf(buffer, "%s", p->affectation.id);
  print_field("ID", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->affectation.exp);
  print_field("EXP", buffer, TABULATION,TXT_GREEN);
  indent++; print_asa(p->affectation.exp); indent--;
}

void print_DECLAS_VARS(asa* p)
{
  sprintf(buffer, "%p", p->declas_vars.decla_var);
  print_field("DECLA_VAR", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->declas_vars.decla_var_svt);
  print_field("DECLA_VAR_SVT", buffer, TABULATION,TXT_GREEN);
  indent++; print_asa(p->declas_vars.decla_var); indent--;
  indent++; print_asa(p->declas_vars.decla_var_svt); indent--;
}

void print_DECLA_VARS(asa* p)
{
  sprintf(buffer, "%s", p->decla_vars.id);
  print_field("ID", buffer, TABULATION,TXT_BLUE);
  sprintf(buffer, "%p", p->decla_vars.exp);
  print_field("EXP", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->decla_vars.var_svt);
  print_field("VAR_SVT", buffer, TABULATION,TXT_GREEN);
  indent++; print_asa(p->decla_vars.exp); indent--;
  indent++; print_asa(p->decla_vars.var_svt); indent--;
}

void print_FCT(asa* p)
{
  sprintf(buffer, "%s", p->fct.id);
  print_field("ID", buffer, TABULATION,TXT_BLUE);
  sprintf(buffer, "%p", p->fct.param);
  print_field("PARAMS", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->fct.decla_var);
  print_field("DECLAS_VARS", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->fct.liste_insts);
  print_field("LISTE_INSTS", buffer, TABULATION,TXT_GREEN);
  indent++; print_asa(p->fct.param); indent--;
  indent++; print_asa(p->fct.decla_var); indent--;
  indent++; print_asa(p->fct.liste_insts); indent--;
}


void print_DECLAS_FCT(asa* p)
{
  sprintf(buffer, "%p", p->declas_fct.fct);
  print_field("FCT", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->declas_fct.fct_svt);
  print_field("FCT_SVT", buffer, TABULATION,TXT_GREEN);
  indent++; print_asa(p->declas_fct.fct); indent--;
  indent++; print_asa(p->declas_fct.fct_svt); indent--;
}

void print_PARAM_FCT(asa* p)
{
  sprintf(buffer, "%s", p->param_fct.id);
  print_field("ID", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->param_fct.param_svt);
  print_field("PARAM_SVT", buffer, TABULATION,TXT_GREEN);
  indent++; print_asa(p->param_fct.param_svt); indent--;
}

void print_ROOT(asa* p)
{
  sprintf(buffer, "%p", p->root.declas_vars);
  print_field("DECLAS_VARS", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->root.declas_fcts);
  print_field("DECLAS_FCTS", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->root.main);
  print_field("MAIN", buffer, TABULATION,TXT_GREEN);
  indent++; print_asa(p->root.declas_vars); indent--;
  indent++; print_asa(p->root.declas_fcts); indent--;
  indent++; print_asa(p->root.main); indent--;
}

void print_SI(asa* p)
{
  sprintf(buffer, "%p", p->si.condition);
  print_field("CONDITION", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->si.liste_insts_si);
  print_field("LISTE_INSTS_SI", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->si.liste_insts_sinon);
  print_field("LISTE_INSTS_SINON", buffer, TABULATION,TXT_GREEN);
  indent++; print_asa(p->si.condition); indent--;
  indent++; print_asa(p->si.liste_insts_si); indent--;
  indent++; print_asa(p->si.liste_insts_sinon); indent--;

}

void print_TQ(asa* p)
{
  sprintf(buffer, "%p", p->tq.condition);
  print_field("CONDITION", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->tq.liste_insts);
  print_field("LISTE_INSTS", buffer, TABULATION,TXT_GREEN);
  indent++; print_asa(p->tq.condition); indent--;
  indent++; print_asa(p->tq.liste_insts); indent--;
}

void print_RETOURNER(asa* p)
{
  sprintf(buffer, "%p", p->retourner.exp);
  print_field("EXP", buffer, TABULATION,TXT_GREEN);
  indent++; print_asa(p->retourner.exp); indent--;
}


void print_typeNB(asa *p)
{
  sprintf(buffer, "%d", p->nb.val);
  print_field("val", buffer, TABULATION,"");
  printf("%s%s\n", TABULATION,line);
}

void print_ID(asa* p)
{
  sprintf(buffer, "%s", p->id.nom);
  print_field("nom", buffer, TABULATION,"");
  printf("%s%s\n", TABULATION,line);
}


void print_ECRIRE(asa* p)
{
  sprintf(buffer, "%p", p->ecrire.exp);
  print_field("EXP", buffer, TABULATION,TXT_GREEN);
  indent++; print_asa(p->ecrire.exp); indent--;
}


void print_LIRE(asa* p)
{
}


void error_asa(const char * s){
  fprintf(stderr, TXT_BOLD TXT_RED "[erreur ASA]" TXT_NULL " %s", s);
  exit(1);
}

void print_NON(asa* p)
{
  sprintf(buffer, "%p", p->non.exp);
  print_field("EXP", buffer, TABULATION,TXT_GREEN);
  indent++; print_asa(p->non.exp); indent--;
}
