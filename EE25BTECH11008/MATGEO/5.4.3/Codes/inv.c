#include <stdio.h>
#include <stdlib.h>

void inverse(double *mat, double *inv, int n) {
    int i, j, k;
    double temp;

    // Create augmented matrix [mat | I]
    double **aug = (double **)malloc(n * sizeof(double *));
    for (i = 0; i < n; i++) {
        aug[i] = (double *)malloc(2 * n * sizeof(double));
        for (j = 0; j < n; j++) {
            aug[i][j] = mat[i*n + j];
            aug[i][j+n] = (i == j) ? 1.0 : 0.0; 
        }
    }

    for (i = 0; i < n; i++) {
        // Make the diagonal element 1
        temp = aug[i][i];
        for (j = 0; j < 2*n; j++)
            aug[i][j] /= temp;

        // Make other elements in column i zero
        for (k = 0; k < n; k++) {
            if (k != i) {
                temp = aug[k][i];
                for (j = 0; j < 2*n; j++)
                    aug[k][j] -= temp * aug[i][j];
            }
        }
    }

    // Copy inverse part to output
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            inv[i*n + j] = aug[i][j+n];

    // Free memory
    for (i = 0; i < n; i++)
        free(aug[i]);
    free(aug);
}
