#include <stdio.h>

// Print 2x3 matrix
void printMatrix(float mat[2][3]) {
    for(int i=0; i<2; i++) {
        for(int j=0; j<3; j++) {
            printf("%6.2f ", mat[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

// Gaussian Elimination
void gaussElimination(float mat[2][3]) {
    // Normalize first row
    float factor = mat[0][0];
    if (factor != 0) {
        for(int j=0; j<3; j++)
            mat[0][j] /= factor;
    }

    // Eliminate below
    factor = mat[1][0];
    for(int j=0; j<3; j++)
        mat[1][j] -= factor * mat[0][j];

    // Normalize second row
    factor = mat[1][1];
    if (factor != 0) {
        for(int j=0; j<3; j++)
            mat[1][j] /= factor;
    }

    // Eliminate above
    factor = mat[0][1];
    for(int j=0; j<3; j++)
        mat[0][j] -= factor * mat[1][j];
}
