// geometry.c
#include <stdio.h>

// Compute midpoint of A and B
void midpoint(double A[3], double B[3], double M[3]) {
    M[0] = (A[0] + B[0]) / 2.0;
    M[1] = (A[1] + B[1]) / 2.0;
    M[2] = (A[2] + B[2]) / 2.0;
}

// Compute normal vector (B - A)
void normal(double A[3], double B[3], double N[3]) {
    N[0] = B[0] - A[0];
    N[1] = B[1] - A[1];
    N[2] = B[2] - A[2];
}

// Compute plane constant: d = -(N · M)
double plane_constant(double N[3], double M[3]) {
    return -(N[0]*M[0] + N[1]*M[1] + N[2]*M[2]);
}
