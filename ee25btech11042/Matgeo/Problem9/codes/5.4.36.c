#include <stdio.h>

#define N 3   // matrix size (you can generalize)

void inverse(double A[N][N], double inv[N][N]) {
    // Step 1: Create augmented matrix [A|I]
    double aug[N][2*N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            aug[i][j] = A[i][j];          // copy A
            aug[i][j+N] = (i == j) ? 1 : 0; // identity
        }
    }

    // Step 2: Gauss–Jordan elimination
    for (int i = 0; i < N; i++) {
        // Make pivot = 1
        double pivot = aug[i][i];
        for (int j = 0; j < 2*N; j++) {
            aug[i][j] /= pivot;
        }

        // Eliminate other rows
        for (int k = 0; k < N; k++) {
            if (k != i) {
                double factor = aug[k][i];
                for (int j = 0; j < 2*N; j++) {
                    aug[k][j] -= factor * aug[i][j];
                }
            }
        }
    }

    // Step 3: Extract inverse from augmented matrix
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            inv[i][j] = aug[i][j+N];
        }
    }
}
