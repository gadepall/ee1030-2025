#include <stdio.h>

void matmul_transpose(double A[3][3], double result[3][3]) {
    // Compute result = A^T * A
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            result[i][j] = 0.0;
            for (int k = 0; k < 3; k++) {
                result[i][j] += A[k][i] * A[k][j];
            }
        }
    }
}

