#include <stdio.h>

void findA(int xp, int yp, int xb, int yb, int *xa, int *ya) {
    *xa = 2*xp - xb;
    *ya = 2*yp - yb;
}

int main() {
    int xp=0, yp=4;
    int xb=-2, yb=3;
    int xa, ya;
    
    findA(xp, yp, xb, yb, &xa, &ya);
    
    printf("Coordinates of A: (%d, %d)\n", xa, ya);
    return 0;
}

