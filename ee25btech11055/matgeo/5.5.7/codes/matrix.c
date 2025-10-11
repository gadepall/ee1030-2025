#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int find_inverse(const double *input_matrix, double *inverse_matrix, int n) {
    // Read up on memory
    double *augmented = (double *)malloc(n * 2 * n * sizeof(double));

    int i, j, k;
    const int width = 2 * n;

    for (i = 0; i < n; ++i) {
        for (j = 0; j < n; ++j) {
            augmented[i * width + j] = input_matrix[i * n + j];
        }
        for (j = n; j < width; ++j) {
            augmented[i * width + j] = (i == (j - n)) ? 1.0 : 0.0;
        }
    }

    for (i = 0; i < n; ++i) {
        // check why this matters. smtg to do with errors sir said iirc
        // numerical stability. Basically I don't want to divide by really small numbers, cuz that blows stuff up
        int max_row = i;
        for (k = i + 1; k < n; ++k) {
            if (fabs(augmented[k * width + i]) > fabs(augmented[max_row * width + i])) {
                max_row = k;
            }
        }
        if (max_row != i) {
            for (k = 0; k < width; ++k) {
                double temp = augmented[i * width + k];
                augmented[i * width + k] = augmented[max_row * width + k];
                augmented[max_row * width + k] = temp;
            }
        }

        // check singular
        if (fabs(augmented[i * width + i]) < 1e-9) {
            free(augmented);
            return 0;
        }

        // make 1
        double pivot = augmented[i * width + i];
        for (j = i; j < width; ++j) {
            augmented[i * width + j] /= pivot;
        }

        // make zero
        for (j = 0; j < n; ++j) {
            if (i != j) {
                double factor = augmented[j * width + i];
                // need to start k = 0 se, cuz right side is not dealt with, only left is
                for (k = 0; k < width; ++k) {
                    augmented[j * width + k] -= factor * augmented[i * width + k];
                }
            }
        }
    }

    // Output inverse
    for (i = 0; i < n; ++i) {
        for (j = 0; j < n; ++j) {
            inverse_matrix[i * n + j] = augmented[i * width + (j + n)];
        }
    }
    
    free(augmented);
    return 1;
}

void mul(const double *a, const double *b, double *c, int m, int n, int p) {
    for (int i = 0; i < m; i++) {
        for (int k = 0; k < p; k++) {
            double temp = 0.0;
            for (int j = 0; j < n; j++) {
                temp += a[i * n + j] * b[j * p + k];
            }
            c[i * p + k] = temp;
        }
    }
}
