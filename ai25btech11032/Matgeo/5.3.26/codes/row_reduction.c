#include <stdio.h>

// Perform one step of row reduction on a 2x3 augmented matrix
void row_reduce(double A[2][3]) {
    if (A[0][0] != 0) {
        double factor = A[1][0] / A[0][0];
        for (int j = 0; j < 3; j++) {
            A[1][j] = A[1][j] - factor * A[0][j];
        }
    }
}


