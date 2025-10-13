#include <stdio.h>

int main() {
    // Fixed points
    int x1 = 3,  y1 = 2;   // A
    int x2 = -2, y2 = -3;  // B
    int x3 = 2,  y3 = 3;   // C

    // Vectors AB and AC
    int ABx = x2 - x1, ABy = y2 - y1;
    int ACx = x3 - x1, ACy = y3 - y1;

    // Dot product
    int dot = ABx*ACx + ABy*ACy;

    if(dot == 0) {
        printf("Triangle is right angled at A(3,2)\n");
    } else {
        printf("Triangle is not right angled\n");
    }

    return 0;
}

