#include <stdio.h>


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
