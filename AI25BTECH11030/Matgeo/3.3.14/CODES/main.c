#include <stdio.h>
#include "trianglefun.h"

int main() {
    Point A, B, C;

    construct_right_triangle(&A, &B, &C);

    printf("Coordinates of triangle vertices:\n");
    printf("A: (%.2f, %.2f)\n", A.x, A.y);
    printf("B: (%.2f, %.2f)\n", B.x, B.y);
    // Print symbolic expression alongside evaluated coordinate for C
    printf("C: (6 * cos(90°) = %.2f, 8 * sin(90°) = %.2f)\n", C.x, C.y);

    return 0;
}

