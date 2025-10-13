#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "matfun.h"

// Matrix utility implementations

double **createMat(int m, int n) {
    double **mat = malloc(m * sizeof(double *));
    for (int i = 0; i < m; i++) {
        mat[i] = calloc(n, sizeof(double));
    }
    return mat;
}

double **Mateye(int m) {
    double **I = createMat(m, m);
    for (int i = 0; i < m; i++) {
        I[i][i] = 1.0;
    }
    return I;
}

double **Matscale(double **a, int m, int n, double k) {
    double **res = createMat(m, n);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            res[i][j] = k * a[i][j];
        }
    }
    return res;
}

double **Matadd(double **a, double **b, int m, int n) {
    double **res = createMat(m, n);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            res[i][j] = a[i][j] + b[i][j];
        }
    }
    return res;
}

// Exported function callable via ctypes
void mat_power_formula(double a, double b, int n, double* result) {
    double **I = Mateye(2);
    double **A = createMat(2, 2);
    A[0][0] = 0; A[0][1] = 1;
    A[1][0] = 0; A[1][1] = 0;

    double **part_I = Matscale(I, 2, 2, pow(a, n));
    double **part_A = Matscale(A, 2, 2, n * pow(a, n-1) * b);
    double **out = Matadd(part_I, part_A, 2, 2);

    // Copy to result (row-major)
    result[0] = out[0][0];
    result[1] = out[0][1];
    result[2] = out[1][0];
    result[3] = out[1][1];

    // Free allocated memory
    for (int i = 0; i < 2; i++) {
        free(I[i]);
        free(A[i]);
        free(part_I[i]);
        free(part_A[i]);
        free(out[i]);
    }
    free(I);
    free(A);
    free(part_I);
    free(part_A);
    free(out);
}
