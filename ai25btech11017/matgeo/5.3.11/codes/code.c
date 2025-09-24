#include <stdio.h>

int main() {
    // Coefficients of equations
    // 5x - 3y = 11  -> a1=5, b1=-3, c1=11
    // -10x + 6y = 22 -> a2=-10, b2=6, c2=22
    float a1 = 5, b1 = -3, c1 = 11;
    float a2 = -10, b2 = 6, c2 = 22;

    // Ratios
    float ratio1 = a1 / a2;
    float ratio2 = b1 / b2;
    float ratio3 = c1 / c2;

    if (ratio1 == ratio2 && ratio2 == ratio3) {
        printf("The equations are consistent and have infinitely many solutions.\n");
    } 
    else if (ratio1 == ratio2 && ratio2 != ratio3) {
        printf("The equations are inconsistent (no solution).\n");
    } 
    else {
        printf("The equations are consistent and have a unique solution.\n");
    }

    return 0;
}
