#include <stdio.h>

#define ROWS 3
#define COLS 4

// Simple row reduction for 3x4 augmented matrix
void row_reduce(double A[ROWS][COLS]) {
    // Eliminate below pivot (0,0)
    if (A[0][0] != 0) {
        for (int i = 1; i < ROWS; i++) {
            double factor = A[i][0] / A[0][0];
            for (int j = 0; j < COLS; j++) {
                A[i][j] -= factor * A[0][j];
            }
        }
    }

    // Eliminate below pivot (1,1)
    if (A[1][1] != 0) {
        for (int i = 2; i < ROWS; i++) {
            double factor = A[i][1] / A[1][1];
            for (int j = 0; j < COLS; j++) {
                A[i][j] -= factor * A[1][j];
            }
        }
    }
}

