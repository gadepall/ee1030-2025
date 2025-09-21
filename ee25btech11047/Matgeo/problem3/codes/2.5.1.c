#include <stdio.h>
#include <math.h>

int main() {
    // Coordinates of the points
    int Ax = 7, Ay = 10;
    int Bx = -2, By = 5;
    int Cx = 3, Cy = 4;

    // Squared lengths of sides
    int AB2 = (Ax - Bx) * (Ax - Bx) + (Ay - By) * (Ay - By);
    int AC2 = (Ax - Cx) * (Ax - Cx) + (Ay - Cy) * (Ay - Cy);
    int BC2 = (Bx - Cx) * (Bx - Cx) + (By - Cy) * (By - Cy);

    // Dot products (for right angle check)
    int dot_AB_AC = (Ax - Bx) * (Ax - Cx) + (Ay - By) * (Ay - Cy);
    int dot_AB_BC = (Ax - Bx) * (Bx - Cx) + (Ay - By) * (By - Cy);
    int dot_AC_BC = (Ax - Cx) * (Bx - Cx) + (Ay - Cy) * (By - Cy);

    printf("Squared side lengths:\n");
    printf("AB^2 = %d\n", AB2);
    printf("AC^2 = %d\n", AC2);
    printf("BC^2 = %d\n", BC2);

    printf("\nDot products:\n");
    printf("(A-B)·(A-C) = %d\n", dot_AB_AC);
    printf("(A-B)·(B-C) = %d\n", dot_AB_BC);
    printf("(A-C)·(B-C) = %d\n", dot_AC_BC);

    // Check isosceles right triangle
    if ((AB2 == AC2 && dot_AB_AC == 0) ||
        (AB2 == BC2 && dot_AB_BC == 0) ||
        (AC2 == BC2 && dot_AC_BC == 0)) {
        printf("\nThe points form an ISOSCELES RIGHT triangle.\n");
    } else {
        printf("\nThe points DO NOT form an isosceles right triangle.\n");
    }

    return 0;
}
