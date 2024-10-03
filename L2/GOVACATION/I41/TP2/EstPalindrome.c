#include <stdio.h>
#include <string.h>

typedef enum {false,true} tbool;


tbool EstPalindrome(char *phrase)
{
    
    int i = 0;
    unsigned int n = strlen(phrase);

    while(i < n && phrase[i] == phrase[n-(i+1)])
    {
        i++;
    }


    return(i>(n/2)?true:false);
    
}
    

int main(int argc, char **argv)
{
    char *phrase = argv[1];
    printf("%s\n",phrase);
    printf("%d\n",EstPalindrome(phrase));

}
