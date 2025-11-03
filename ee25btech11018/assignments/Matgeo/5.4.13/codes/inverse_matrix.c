#include <stdio.h>

#define N 2  // Matrix size

void inverse(double A[N][N], double inv[N][N]) {
    double aug[N][2*N];

    // Forming augmented matrix [A | I]
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            aug[i][j] = A[i][j];
            aug[i][j + N] = (i == j) ? 1 : 0;
        }
    }

    // Applying Gauss–Jordan elimination
    for (int i = 0; i < N; i++) {
        double pivot = aug[i][i];
        for (int j = 0; j < 2*N; j++) {
            aug[i][j] /= pivot;  // Make pivot element = 1
        }

        for (int k = 0; k < N; k++) {
            if (k != i) {
                double factor = aug[k][i];
                for (int j = 0; j < 2*N; j++) {
                    aug[k][j] -= factor * aug[i][j];
                }
            }
        }
    }

    // Obtaining inverse matrix
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            inv[i][j] = aug[i][j + N];
        }
    }
}


