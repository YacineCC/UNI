#include <stdio.h>
#include <string.h>
typedef enum {FAUX = 0, VRAI = 1} tbool;


tbool EstPrefixe(char *pre, char *mot)
{
    
    if(strlen(pre) > strlen(mot))
    {
        return FAUX;
    }
    int i = 0;
    while(i < strlen(pre) && pre[i] == mot[i])
    {
        i++;
    }

    if(i >= strlen(pre))
    {
        return VRAI;
    }
    else
    {
        return FAUX;
    }


}

tbool BienParenthesee(char *expr)
{
    int i = 0;
    int tac = 0;
    while(i < strlen(expr) && tac >= 0)
    {
        if(expr[i] == '(')
        {
            tac += 1;
        }
        else if(expr[i] == ')')
        {
            tac -= 1;
        }
        i += 1;
    }

    if( tac < 0 || tac > 0)
    {
        return FAUX;
    }
    else
    {
        return VRAI;
    }
}




int main(int argc, char **argv)
{
    //printf("%d\n",EstPrefixe(argv[1],argv[2]));
    printf("%d\n",BienParenthesee(argv[1]));

    
}
