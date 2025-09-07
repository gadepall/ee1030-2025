#include <stdio.h>
// Solve for p such that m1 ⋅ m2 = 0
// m1 = (-3, p, 2)
// m2 = (-3p, 1, -5)
//
// dot = (-3)(-3p) + p*1 + 2*(-5) = 9p + p - 10 = 10p - 10
// => p = 1
//

void solve_equations(double *p_out) {
    double p;
    // Equation: 10p - 10 = 0 => p = 1
    p = 10.0 / 10.0;
    *p_out = p;
}

// Function to compute dot product of two 3D vectors
double dot_product(double *a, double *b) {
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
}
