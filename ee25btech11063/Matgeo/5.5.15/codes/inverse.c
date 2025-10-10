#include <stdio.h>

#define SIZE 3

int main() {
    FILE *fp;
    double A[SIZE][SIZE] = {
        {1, 2, 3},
        {2, 5, 7},
        {-2, -4, -5}
    };

    double I[SIZE][SIZE] = { {1,0,0}, {0,1,0}, {0,0,1} };

    int i, j, k;
    double factor;

    // Convert A to identity, apply same operations to I
    for (i = 0; i < SIZE; i++) {
        // Make sure pivot is not zero
        if (A[i][i] == 0.0) {
            printf("Pivot is zero, cannot continue.\n");
            return 1;
        }

        // Scale pivot row to make pivot = 1
        factor = A[i][i];
        for (j = 0; j < SIZE; j++) {
            A[i][j] /= factor;
            I[i][j] /= factor;
        }

        // Eliminate other rows
        for (k = 0; k < SIZE; k++) {
            if (k != i) {
                factor = A[k][i];
                for (j = 0; j < SIZE; j++) {
                    A[k][j] -= factor * A[i][j];
                    I[k][j] -= factor * I[i][j];
                }
            }
        }
    }

    // Write result to file
    fp = fopen("inverse.dat", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    fprintf(fp, "Inverse of the matrix is:\n");
    for (i = 0; i < SIZE; i++) {
        for (j = 0; j < SIZE; j++) {
            fprintf(fp, "%8.3f ", I[i][j]);
        }
        fprintf(fp, "\n");
    }

    fclose(fp);
    printf("Inverse written to inverse.dat\n");

    return 0;
}

