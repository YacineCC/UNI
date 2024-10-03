#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include "afn.h"
#include "stdlib.h"



int main()
{
    
    stack s = init_stack(1);
    push(&s,2);
    stack_print(s); 
    printf("%d\n", pop(&s));
    stack_print(s);
    printf("%d\n", pop(&s));
    stack_print(s);
    printf("%d\n", pop(&s));
  
    
    return 0;
}