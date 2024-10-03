#include <stdio.h>

unsigned char encode(unsigned char r, unsigned char g, unsigned char b){
    
    r = r << 5;
    g = g << 2;
    return ((r|g)|b);
    }
void decode(unsigned char color, unsigned char* r, unsigned char* g, unsigned char* b) {
    
    *r = (color >> 5) & 7;
    *g = (color >> 2) & 7;
    *b = color & 3;
    }

int main() {
    unsigned char r,g,b;
    unsigned char enc;
    printf("Saisir une couleur au format RGB :");
    scanf("%d %d %d", &r, &g, &b);
    enc = encode(r,g,b);
    printf("%d\n",enc);
    printf("Decodage\n");
    unsigned char r1,g1,b1;
    scanf("%d %d %d", &r, &g, &b);
    decode(enc, &r, &g, &b);
    printf("%d %d %d\n", r, g, b);
    return 0;
    }
