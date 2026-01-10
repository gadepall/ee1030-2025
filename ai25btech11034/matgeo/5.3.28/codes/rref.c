// rref.c
#include <stdio.h>

void rref(int rows, int cols, double mat[rows][cols]) {
    int i, j, k;
    double pivot, factor;

    for(i = 0; i < rows; i++) {
        // Find pivot in current row
        pivot = mat[i][i];
        if (pivot == 0) {
            // Swap with a lower row with non-zero pivot
            for(k = i + 1; k < rows; k++) {
                if(mat[k][i] != 0) {
                    // swap rows
                    for(j = 0; j < cols; j++) {
                        double temp = mat[i][j];
                        mat[i][j] = mat[k][j];
                        mat[k][j] = temp;
                    }
                    pivot = mat[i][i];
                    break;
                }
            }
        }

        if(pivot == 0) continue; // skip if entire column is zero

        // Normalize pivot row
        for(j = 0; j < cols; j++)
            mat[i][j] /= pivot;

        // Eliminate other rows
        for(k = 0; k < rows; k++) {
            if(k == i) continue;
            factor = mat[k][i];
            for(j = 0; j < cols; j++)
                mat[k][j] -= factor * mat[i][j];
        }
    }
}

