// points.c
#include <math.h>

// Compute dot product of two 2D vectors u and v
double dot_product(double u[2], double v[2]) {
    return u[0]*v[0] + u[1]*v[1];
}

// Compute squared norm of a 2D vector u
double norm_squared(double u[2]) {
    return u[0]*u[0] + u[1]*u[1];
}

// Compute vector difference: result = Q - P
void vector_diff(double P[2], double Q[2], double result[2]) {
    result[0] = Q[0] - P[0];
    result[1] = Q[1] - P[1];
}

