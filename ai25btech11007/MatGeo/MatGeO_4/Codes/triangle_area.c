#include <stdio.h>

// Define custom sqrt using Newton-Raphson
double sqrt_newton(double n) {
    double x = n;
    double y = 1.0;
    double e = 1e-9;  // tolerance

    while (x - y > e) {
        x = (x + y) / 2;
        y = n / x;
    }
    return x;
}

int main() {
    // Define vectors (B - A) and (C - A)
    int AB[3] = {1, -3, 1};
    int AC[3] = {3, 3, -4};

    // Compute norms squared
    int AB_sq = AB[0]*AB[0] + AB[1]*AB[1] + AB[2]*AB[2];   // 11
    int AC_sq = AC[0]*AC[0] + AC[1]*AC[1] + AC[2]*AC[2];   // 34

    // Dot product
    int dot = AB[0]*AC[0] + AB[1]*AC[1] + AB[2]*AC[2];     // -10

    // Using identity: |AB x AC|^2 = |AB|^2|AC|^2 - (AB · AC)^2
    int cross_sq = AB_sq * AC_sq - dot * dot;

    // Magnitude of cross product using custom sqrt
    double cross_norm = sqrt_newton((double)cross_sq);

    // Area of triangle
    double area = 0.5 * cross_norm;

    printf("||AB||^2 = %d\n", AB_sq);
    printf("||AC||^2 = %d\n", AC_sq);
    printf("AB · AC = %d\n", dot);
    printf("||AB x AC||^2 = %d\n", cross_sq);
    printf("||AB x AC|| = %.6f\n", cross_norm);
    printf("Area of triangle ABC = %.6f\n", area);

    return 0;
}
