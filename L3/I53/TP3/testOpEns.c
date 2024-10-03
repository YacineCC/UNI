#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <time.h>
#include "afd.h"
#include "afn.h"

int main()
{
    srand(time(NULL));
    int * R1 = random_set(5);
    int * R2 = random_set(5);
    //int R1[] = {2,3,4,7,8, -1};
    //int R2[] = {0,1,5,6,9, -1};
    set_print(R1);
    printf("   ");
    set_print(R2);
    printf("\n");
    
    int *RU = set_union(R1, R2);
    int *RI = set_intersection(R1, R2);
    set_print(RU);
    set_print(RI);
    
    printf("\n");
    return 0;
}