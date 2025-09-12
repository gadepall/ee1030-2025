#include <stdlib.h>
#include "matfun.h"

// Create a rows x cols matrix with dynamically allocated memory
double** createMat(int rows, int cols) {
    double** mat = (double**)malloc(rows * sizeof(double*));
    if (!mat) return NULL;
    for (int i = 0; i < rows; i++) {
        mat[i] = (double*)malloc(cols * sizeof(double));
        if (!mat[i]) {
            // Free previously allocated memory on failure
            for (int j = 0; j < i; j++) free(mat[j]);
            free(mat);
            return NULL;
        }
    }
    return mat;
}

// Subtract matrix B from A: result = A - B (both rows x cols)
double** Matsub(double** A, double** B, int rows, int cols) {
    double** result = createMat(rows, cols);
    if (!result) return NULL;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            result[i][j] = A[i][j] - B[i][j];
        }
    }
    return result;
}

// Free matrix memory allocated by createMat
void freeMat(double** mat, int rows) {
    if (!mat) return;
    for (int i = 0; i < rows; i++) {
        free(mat[i]);
    }
    free(mat);
}

