#include <stdio.h>
#include <stdlib.h>
#include "matfun.h"

double** createMat(int rows, int cols) {
    double **mat = (double **)malloc(rows * sizeof(double *));
    for (int i = 0; i < rows; i++)
        mat[i] = (double *)malloc(cols * sizeof(double));
    return mat;
}

double** Matmul(double **A, double **B, int r1, int c1, int c2){
    double **mat = createMat(r1, c2);
    for (int i = 0; i < r1; i++){
        for (int j = 0; j < c2; j++){
            mat[i][j] = 0.0;
            for (int k = 0; k < c1; k++){
                mat[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    return mat;
}

void freeMat(double **mat, int rows) {
    for (int i = 0; i < rows; i++) {
        free(mat[i]);
    }
    free(mat);
}
