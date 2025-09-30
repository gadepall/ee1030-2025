#include <stdio.h>

void get_points_and_line(double* A, double* B, double* n, double* k) {
    // Input points:
    A[0] = 3;  A[1] = 4;  A[2] = -7;
    B[0] = 1;  B[1] = -1; B[2] = 6;
    // Precalculated normal vector and constant for these points
    n[0] = -12; n[1] = 23; n[2] = 7;
    *k = 7;
}

