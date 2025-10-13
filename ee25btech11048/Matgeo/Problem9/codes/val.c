#include <stdio.h>

// Cross product u × v
void cross(double u[3], double v[3], double result[3]) {
    result[0] = u[1]*v[2] - u[2]*v[1];
    result[1] = u[2]*v[0] - u[0]*v[2];
    result[2] = u[0]*v[1] - u[1]*v[0];
}

// Dot product u · v
double dot(double u[3], double v[3]) {
    return u[0]*v[0] + u[1]*v[1] + u[2]*v[2];
}

// Compute lhs (always 0) and rhs
void compute(double a[3], double b[3], double c[3], double* lhs, double* rhs) {
    double cross_b_c[3];

    // b × c
    cross(b, c, cross_b_c);

    // LHS always 0 due to linear dependence
    *lhs = 0.0;

    // RHS = 2a · (b × c)
    *rhs = 2 * dot(a, cross_b_c);
}

