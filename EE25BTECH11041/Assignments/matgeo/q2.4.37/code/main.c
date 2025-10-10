#include <math.h>

// Compute cross product of two 3D vectors
void cross_product(double *a, double *b, double *result) {
    result[0] = a[1]*b[2] - a[2]*b[1];
    result[1] = a[2]*b[0] - a[0]*b[2];
    result[2] = a[0]*b[1] - a[1]*b[0];
}

// Compute magnitude of a 3D vector
double magnitude(double *v) {
    return sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
}

// Given a, b, and desired magnitude, compute two perpendicular vectors of that magnitude
// Output: v1[3], v2[3]
void perpendicular_vectors(double *a, double *b, double mag, double *v1, double *v2) {
    double c[3];
    cross_product(a, b, c);

    double norm_c = magnitude(c);

    if (norm_c == 0.0) { 
        // Parallel vectors → cross product is zero
        v1[0] = v1[1] = v1[2] = 0.0;
        v2[0] = v2[1] = v2[2] = 0.0;
        return;
    }

    // Normalize c
    double c_hat[3];
    c_hat[0] = c[0] / norm_c;
    c_hat[1] = c[1] / norm_c;
    c_hat[2] = c[2] / norm_c;

    // Scale to desired magnitude
    v1[0] = mag * c_hat[0];
    v1[1] = mag * c_hat[1];
    v1[2] = mag * c_hat[2];

    v2[0] = -v1[0];
    v2[1] = -v1[1];
    v2[2] = -v1[2];
}
