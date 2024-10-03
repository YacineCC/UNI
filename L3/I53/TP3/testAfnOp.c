#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include "afn.h"
#include "stdlib.h"

int main()
{
    
    // char sigma[2] = {'a','b'};
    // AFN A = afn_char(sigma[0], sigma);
    // afn_print(A);
    // AFN B = afn_char(sigma[1], sigma);
    // afn_print(B);
    // AFN C = afn_union(A, B);
    // afn_print(C);
    // C = afn_concat(A, B);
    // afn_print(C);

    char* sigma = "abc";
    AFN A = afn_char(sigma[0], sigma);
    AFN B = afn_char('b', sigma);
    AFN C = afn_char('c', sigma);

    AFN ABB = afn_concat(A,B);
    ABB = afn_concat(ABB,B);
    AFN U = afn_union(ABB, C);

    AFN R = afn_kleene(U);

    

    
    afn_print(R);
    
    return 0;
}