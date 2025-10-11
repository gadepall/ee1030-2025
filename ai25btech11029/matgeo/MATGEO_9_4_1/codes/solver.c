// solver.c
#include <stdio.h>
#include <math.h>

// Solve x^2 - 6x + 8 = 0
void solve_quadratic(double* roots) {
    double a = 1, b = -6, c = 8;
    double discriminant = b*b - 4*a*c;

    if (discriminant >= 0) {
        roots[0] = (-b + sqrt(discriminant)) / (2*a);
        roots[1] = (-b - sqrt(discriminant)) / (2*a);
    } else {
        roots[0] = roots[1] = NAN;
    }
}

