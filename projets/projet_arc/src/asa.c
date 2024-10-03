#include "asa.h"

static const char str_type[][16] = {"ROOT","LISTES_DECLAS", "DECLA_FCT", "LISTE_PARAM", "DECLA_VARS", "DECLA_VAR",
"INIT_INT", "INIT_TAB", "STATIC_TAB","CORPS_FCT", "LISTE_INST", "INST", "SI", "TQ", "RETOURNER", "EXP", "AFFECTATION", "ID", "NB"};
static const char line[36] = "-----------------------------------";

static char buffer[32];
static char TABULATION[256] = "";
static int indent = 0;

asa* creer_noeud_ROOT(asa* p1, asa* p2)
{
  asa* p;
  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");
  
  p->type = type_ROOT;
  p->root.listes_declas = p1;
  p->root.main = p2;
  
  return p;
  }

asa* creer_noeud_LISTES_DECLAS(asa* p1, asa* p2)
{
  asa* p;
  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");

  p->type = type_LISTES_DECLAS;
  p->listes_declas.declaration_svt = p1;
  p->listes_declas.declaration_svt = p2;

  return p;
}

asa* creer_noeud_DECLA_FCT(asa* p1, asa* p2, asa* p3)
{
  asa* p;
  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");

  p->type = type_DECLA_FCT;
  p->decla_fct.id = p1;
  p->decla_fct.liste_param = p2;
  p->decla_fct.corps_fct = p3;

  return p;
}

asa* creer_noeud_LISTE_PARAM(asa* p1, asa* p2)
{
  asa* p;
  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");

  p->type = type_LISTE_PARAM;
  p->liste_param.param_svt = p1;
  p->liste_param.param = p1;

  return p;
}

asa* creer_noeud_DECLA_VARS(asa* p1, asa* p2)
{
  asa* p;
  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");

  p->type = type_DECLA_VARS;
  p->decla_vars.decla_var_svt = p1;
  p->decla_vars.decla_var = p2;

  return p;
}

asa* creer_noeud_DECLA_VAR(asa* p1)
{
  asa* p;
  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");

  p->type = type_DECLA_VAR;
  p->decla_var.var = p1;

  return p;
}

asa* creer_noeud_INIT_INT(asa* p1, asa* p2)
{
  asa* p;
  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");

  p->type = type_INIT_INT;
  p->init_int.id = p1;
  p->init_int.exp = p2;

  return p;
}

asa* creer_noeud_INIT_TAB(asa* p1,asa* p2, asa* p3)
{
  asa* p;
  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");

  p->type = type_INIT_TAB;
  p->init_tab.id = p1;
  p->init_tab.taille = p2;
  p->init_tab.liste_int = p3;

  return p;
}

asa* creer_noeud_STATIC_TAB(asa* p1)
{
  asa* p;
  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");
  p->type = type_STATIC_TAB;
  p->static_tab.liste_int = p1;

  return p;
}

asa* creer_noeud_LISTE_INT(asa* p1, asa* p2)
{
  asa* p;
  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");

  p->type = type_LISTE_INT;
  p->liste_int.nb_svt = p1;
  p->liste_int.nb = p2;


  return p;
}

asa* creer_noeud_CORPS_FCT(asa* p1)
{
  asa* p;
  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");

  p->type = type_CORPS_FCT;
  p->corps_fct.liste_inst = p1;

  return p;
}

asa* creer_noeud_LISTE_INST(asa* p1, asa* p2)
{
  asa* p;
  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");

  p->type = type_LISTE_INST;
  p->liste_inst.inst_svt = p1;
  p->liste_inst.inst = p2;

  return p;
}

asa* creer_noeud_INST(asa* p1)
{
  asa* p;
  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");

  p->type = type_INST;
  p->inst.inst = p1;

  return p;
}

asa* creer_noeud_SI(asa* p1, asa* p2)
{
  asa* p;
  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");

  p->type = type_SI;
  p->si.condition = p2;
  p->si.liste_inst = p1;

  return p;
}

asa* creer_noeud_TQ(asa* p1, asa* p2)
{
  asa* p;
  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");

  p->type = type_TQ;
  p->tq.condition = p2;
  p->tq.liste_inst = p1;

  return p;
}

asa* creer_noeud_RETOURNER(asa* p1)
{
  asa* p;
  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");

  p->type = type_RETOURNER;
  p->retourner.exp = p1;

  return p;
}

asa* creer_noeud_EXP(asa* p1)
{
  asa* p;
  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");

  p->type = type_EXP;
  p->exp.exp = p1;

  return p;
}

asa* creer_noeud_OP(asa* ope, asa* p1, asa* p2)
{
  asa* p;
  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");

  p->type = type_OP;
  p->op.ope = ope;
  p->op.noeud[0]=p1;
  p->op.noeud[1]=p2;
    
  return p;
}

asa * creer_noeud_AFFECTATION(asa* p1, asa* p2)
{
  asa * p;

  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");

  p->type = type_AFFECTATION;
  p->affectation.id = p1;
  p->affectation.exp = p2;
    
  return p;
}

asa* creer_feuille_ID(char* nom)
{
  asa* p;
  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");

  p->type = type_ID;
  strcpy(p->id.nom, nom);

  return p;
}

asa* creer_feuille_NB(int val)
{
  asa* p;
  if ((p = malloc(sizeof(asa))) == NULL)
    error_asa("echec allocation mémoire");

  p->type = type_NB;
  p->nb.val = val;

  return p;
}


void free_asa(asa *p)
{
  if (!p) return;
  switch (p->type) {
  case type_OP:
    free_asa(p->op.noeud[0]);
    free_asa(p->op.noeud[1]);
    break;
  case type_NB:
  default: break;
  }
  free(p);
}

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
  case type_ROOT:
    print_ROOT(p);
    break;
  case type_LISTES_DECLAS:
    print_LISTES_DECLAS(p);
    break;
  case type_DECLA_FCT:
    print_DECLA_FCT(p);
    break;
  case type_LISTE_PARAM:
    print_LISTE_PARAM(p);
    break;
  case type_DECLA_VARS:
    print_DECLA_VARS(p);  
    break;
  case type_DECLA_VAR:
    print_DECLA_VAR(p);
    break;
  case type_INIT_INT:
    print_INIT_INT(p);
    break;
  case type_INIT_TAB:
    print_INIT_TAB(p);
    break;
  case type_LISTE_INT:
    print_LISTE_INT(p);
    break;
  case type_CORPS_FCT:
    print_CORPS_FCT(p);
    break;
  case type_LISTE_INST:
    print_LISTE_INST(p);
    break;
  case type_INST:
    print_INST(p);
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
  case type_EXP:
    print_EXP(p);
    break;
  case type_OP:
    print_OP(p);
    break;
  case type_AFFECTATION:
    print_AFFECTATION(p);
    break;
  case type_ID:
    print_ID(p);
    break;
  case type_NB:
    print_NB(p);
    break;
  default:
    break;
  }
}

void print_ROOT(asa* p)
{
 
 
  sprintf(buffer, "%p", p->root.listes_declas);
  print_field("LISTES_DECLAS", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->root.main);
  print_field("MAIN", buffer, TABULATION,TXT_GREEN);
    
  printf("%s%s\n", TABULATION,line);
  indent++; print_asa(p->root.listes_declas); indent--;
  indent++; print_asa(p->root.main); indent--;

}

void print_LISTES_DECLAS(asa* p)
{
 
  sprintf(buffer, "%p", p->listes_declas.declaration_svt);
  print_field("DECLA_SVT", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->listes_declas.declaration);
  print_field("DECLA", buffer, TABULATION,TXT_GREEN);
    
  printf("%s%s\n", TABULATION,line);
  indent++; print_asa(p->listes_declas.declaration_svt); indent--;
  indent++; print_asa(p->listes_declas.declaration); indent--;

}

void print_DECLA_FCT(asa* p)
{
 
  sprintf(buffer, "%p", p->decla_fct.id);
  print_field("ID", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->decla_fct.liste_param);
  print_field("LISTE_PARAM", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->decla_fct.corps_fct);
  print_field("CORPS_FCT", buffer, TABULATION,TXT_GREEN);
    
  printf("%s%s\n", TABULATION,line);
  indent++; print_asa(p->decla_fct.id); indent--;
  indent++; print_asa(p->decla_fct.liste_param); indent--;
  indent++; print_asa(p->decla_fct.corps_fct); indent--;


}

void print_LISTE_PARAM(asa* p)
{
  

  sprintf(buffer, "%p", p->liste_param.param_svt);
  print_field("PARAM_SVT", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->liste_param.param);
  print_field("PARAM", buffer, TABULATION,TXT_GREEN);
    
  printf("%s%s\n", TABULATION,line);
  indent++; print_asa(p->liste_param.param_svt); indent--;
  indent++; print_asa(p->liste_param.param); indent--;
}

void print_DECLA_VARS(asa* p)
{

  sprintf(buffer, "%p", p->decla_vars.decla_var_svt);
  print_field("DECLA_VAR_SVT", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->decla_vars.decla_var);
  print_field("DECLA_VAR", buffer, TABULATION,TXT_GREEN);
    
  printf("%s%s\n", TABULATION,line);
  indent++; print_asa(p->decla_vars.decla_var_svt); indent--;
  indent++; print_asa(p->decla_vars.decla_var); indent--;
}

void print_DECLA_VAR(asa* p)
{

  sprintf(buffer, "%p", p->decla_var.var);
  print_field("VAR", buffer, TABULATION,TXT_GREEN);
  
  printf("%s%s\n", TABULATION,line);
  indent++; print_asa(p->decla_var.var); indent--;
}

void print_INIT_INT(asa* p)
{

  sprintf(buffer, "%p", p->init_int.id);
  print_field("ID", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->init_int.exp);
  print_field("EXP", buffer, TABULATION,TXT_GREEN);
  
    
  printf("%s%s\n", TABULATION,line);
  indent++; print_asa(p->init_int.id); indent--;
  indent++; print_asa(p->init_int.exp); indent--;
}

void print_INIT_TAB(asa* p)
{

  sprintf(buffer, "%p", p->init_tab.id);
  print_field("ID", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->init_tab.taille);
  print_field("TAILLE", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->init_tab.liste_int);
  print_field("LISTE_INT", buffer, TABULATION,TXT_GREEN);
  
    
  printf("%s%s\n", TABULATION,line);
  indent++; print_asa(p->init_tab.id); indent--;
  indent++; print_asa(p->init_tab.taille); indent--;
  indent++; print_asa(p->init_tab.liste_int); indent--;
}

void print_LISTE_INT(asa* p)
{

  sprintf(buffer, "%p", p->liste_int.nb_svt);
  print_field("NB_SVT", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->liste_int.nb);
  print_field("NB", buffer, TABULATION,TXT_GREEN);
  
    
  printf("%s%s\n", TABULATION,line);
  indent++; print_asa(p->liste_int.nb_svt); indent--;
  indent++; print_asa(p->liste_int.nb); indent--;
}

void print_CORPS_FCT(asa* p)
{

  sprintf(buffer, "%p", p->corps_fct.liste_inst);
  print_field("LISTE_INST", buffer, TABULATION,TXT_GREEN);
  
  printf("%s%s\n", TABULATION,line);
  indent++; print_asa(p->corps_fct.liste_inst); indent--;
}

void print_LISTE_INST(asa* p)
{

  sprintf(buffer, "%p", p->liste_inst.inst_svt);
  print_field("INST_SVT", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->liste_inst.inst);
  print_field("INST", buffer, TABULATION,TXT_GREEN);
  
    
  printf("%s%s\n", TABULATION,line);
  indent++; print_asa(p->liste_inst.inst_svt); indent--;
  indent++; print_asa(p->liste_inst.inst); indent--;
}

void print_INST(asa* p)
{

  sprintf(buffer, "%p", p->inst.inst);
  print_field("INST", buffer, TABULATION,TXT_GREEN);
  
  printf("%s%s\n", TABULATION,line);
  indent++; print_asa(p->inst.inst); indent--;
}

void print_SI(asa* p)
{

  sprintf(buffer, "%p", p->si.condition);
  print_field("CONDITION", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->si.liste_inst);
  print_field("LIST_INST", buffer, TABULATION,TXT_GREEN);
  
    
  printf("%s%s\n", TABULATION,line);
  indent++; print_asa(p->si.condition); indent--;
  indent++; print_asa(p->si.liste_inst); indent--;
}

void print_TQ(asa* p)
{

  sprintf(buffer, "%p", p->tq.condition);
  print_field("CONDITION", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->tq.liste_inst);
  print_field("LIST_INST", buffer, TABULATION,TXT_GREEN);
  
    
  printf("%s%s\n", TABULATION,line);
  indent++; print_asa(p->tq.condition); indent--;
  indent++; print_asa(p->tq.liste_inst); indent--;
}

void print_RETOURNER(asa* p)
{

  sprintf(buffer, "%p", p->retourner.exp);
  print_field("EXP", buffer, TABULATION,TXT_GREEN);
    
  printf("%s%s\n", TABULATION,line);
  indent++; print_asa(p->retourner.exp); indent--;
}

void print_EXP(asa* p)
{

  sprintf(buffer, "%p", p->exp.exp);
  print_field("EXP", buffer, TABULATION,TXT_GREEN);
    
  printf("%s%s\n", TABULATION,line);
  indent++; print_asa(p->exp.exp); indent--;
}



void print_OP(asa *p)
{
  sprintf(buffer, "%p", p->op.ope);
  print_field("operateur", buffer, TABULATION,"");

  sprintf(buffer, "%p", p->op.noeud[0]);
  print_field("ope gauche", buffer, TABULATION,TXT_GREEN);
  sprintf(buffer, "%p", p->op.noeud[1]);
  print_field("ope droite", buffer, TABULATION,TXT_GREEN);
    
  printf("%s%s\n", TABULATION,line);
  indent++; print_asa(p->op.ope); indent--;
  indent++; print_asa(p->op.noeud[0]); indent--;
  indent++; print_asa(p->op.noeud[1]); indent--;
  
}

void print_AFFECTATION(asa *p)
{
  sprintf(buffer, "%p", p->affectation.id);
  print_field("ID", buffer, TABULATION,"");

  sprintf(buffer, "%p", p->affectation.exp);
  print_field("EXP", buffer, TABULATION,TXT_GREEN);
    
  printf("%s%s\n", TABULATION,line);
  indent++; print_asa(p->affectation.exp); indent--;
  indent++; print_asa(p->affectation.id); indent--;
  
}

void print_ID(asa *p)
{
  sprintf(buffer, "%s", p->id.nom);
  print_field("ID", buffer, TABULATION,"");
  printf("%s%s\n", TABULATION,line);
  
}

void print_NB(asa *p)
{
  sprintf(buffer, "%c", p->nb.val);
  print_field("VAL", buffer, TABULATION,"");
  printf("%s%s\n", TABULATION,line);
}


void error_asa(const char * s){
  fprintf(stderr, TXT_BOLD TXT_RED "[erreur ASA]" TXT_NULL " %s", s);
  exit(1);
}
