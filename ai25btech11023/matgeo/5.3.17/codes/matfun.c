#include "matfun.h"
#include <stdio.h>
#include <stdlib.h>

// Create a matrix with m rows and n columns
double** createMat(int m, int n) {
    double **a = (double**)malloc(m * sizeof(double*));
    for (int i = 0; i < m; ++i) {
        a[i] = (double*)malloc(n * sizeof(double));
    }
    return a;
}

// Print matrix
void printMat(double **p, int m, int n) {
    for(int i=0; i<m; ++i) {
        for(int j=0; j<n; ++j) {
            printf("%lf ", p[i][j]);
        }
        printf("\n");
    }
}

// Gaussian elimination for 2x2 system: Solves Ax = b
void solve2x2(double **A, double *b, double *x) {
    double det = A[0][0]*A[1][1] - A[0][1]*A[1][0];
    x[0] = ( b[0]*A[1][1] - b[1]*A[0][1] ) / det;
    x[1] = ( A[0][0]*b[1] - A[1][0]*b[0] ) / det;
}

// Helper to free matrix
void freeMat(double **a, int m) {
    for(int i=0; i<m; ++i)
        free(a[i]);
    free(a);
}
