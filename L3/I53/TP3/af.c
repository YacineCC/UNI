#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#include "afd.h"
#include "afn.h"

#define AFD_TYPE 0
#define AFN_TYPE 1

int main(int argc, char *argv[]){
  int opt;
  int af_type;
  char data[128], af_file[64];
    
    while  ((opt=getopt(argc,argv,"d:n:s:"))!=-1){
      switch(opt){
      case 'd':
	af_type = AFD_TYPE;
	strcpy(af_file,optarg);
	break;
      case 'n':
	af_type = AFN_TYPE;
	strcpy(af_file,optarg);
	break;
      case 's':
	strcpy(data, optarg);
	break;
      default:
	break;
      }
    }

  if (af_type==AFD_TYPE){
    AFD  A;
    A = afd_finit(af_file);
    afd_print(A);
    
    if (afd_simuler(A,data)){
      printf("'%s' est accepté\n",data);
    } else {
      printf("'%s' est rejeté\n",data);
      }
    afd_free(A);
  } else {
    AFN  B;
    
    B = afn_finit(af_file);
    afn_print(B);
    int R[] = {0, 2, -1};
    afn_epsilon_fermeture(B, R);
    afn_determinisation(B);
    afn_free(B);
  }
  
  return 0;
}
