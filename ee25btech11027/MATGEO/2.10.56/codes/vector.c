#include <stdio.h>
#include <math.h>

// Dot product of two 2D vectors
double dot(double a[], double b[]) {
    return a[0]*b[0] + a[1]*b[1];
}

// Magnitude of a 2D vector
double magnitude(double a[]) {
    return sqrt(dot(a, a));
}

// Compute max length M and unit vector u using matrix method
void compute(double a[], double b[], double *M, double u[]) {
    double c = dot(a, b);        // a · b
    *M = sqrt(1 + c);            // largest eigenvalue's sqrt

    // Direction = a + b
    double temp[2] = {a[0] + b[0], a[1] + b[1]};
    double norm = magnitude(temp);
    u[0] = temp[0] / norm;
    u[1] = temp[1] / norm;
}
