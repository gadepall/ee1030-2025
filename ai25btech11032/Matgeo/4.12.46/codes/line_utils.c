#include <stdio.h>
#include <math.h>

// Compute norm of a 2D vector
double norm(double *vec) {
    return sqrt(vec[0]*vec[0] + vec[1]*vec[1]);
}

// Normalize a 2D vector
void normalize(double *vec, double *out) {
    double n = norm(vec);
    out[0] = vec[0]/n;
    out[1] = vec[1]/n;
}

// Compute p = -c / norm(n)
double compute_p(double *vec, double c) {
    double n = norm(vec);
    return -c / n;
}

