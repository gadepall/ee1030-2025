#include<stdio.h>

int main() {
    int Bx=0, By=0, Cx=3, Cy=0, Dx=0, Dy=4;
    int Ax, Ay;

    // Formula: A = B + D - C
    Ax = Bx + Dx - Cx;
    Ay = By + Dy - Cy;

    printf("Coordinates of A: (%d, %d)\n", Ax, Ay);
    return 0;