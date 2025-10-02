#include <stdio.h>

int main() {
    // Given point
    double x = 1, y = 1;

    // Circle equations:
    // C1: x^2 + y^2 - 6 = 0
    // C2: x^2 + y^2 - 6x + 8 = 0

    // General circle through intersection: C1 + λ*C2 = 0
    // => (x^2 + y^2 - 6) + λ(x^2 + y^2 - 6x + 8) = 0

    // Plug point (1,1) into equation to solve for λ
    double valC1 = (x*x + y*y - 6);          // = -4
    double valC2 = (x*x + y*y - 6*x + 8);    // = 4
    double lambda = -valC1 / valC2;          // λ = 1

    // Expand equation:
    // (1+λ)(x^2 + y^2) - 6λx + (8λ - 6) = 0
    double A = 1 + lambda;   // coefficient of (x^2 + y^2)
    double B = -6*lambda;    // coefficient of x
    double C = 8*lambda - 6; // constant term

    printf("Equation of circle: ");
    printf("%.0fx^2 + %.0fy^2 %+.0fx %+.0f = 0\n", A, A, B, C);

    return 0;
}
