#include "matfun.h"

// Solve 2x2 system using Cramer's rule (appropriate for this fixed size)
void solve_linear_system(double A[2][2], double B[2], double X[2]) {
    double det = A[0][0]*A[1][1] - A[0][1]*A[1][0];
    if (det == 0) {
        // No unique solution
        X[0] = X[1] = 0;
        return;
    }
    X[0] = (B[0]*A[1][1] - B[1]*A[0][1]) / det;
    X[1] = (A[0][0]*B[1] - A[1][0]*B[0]) / det;
}

