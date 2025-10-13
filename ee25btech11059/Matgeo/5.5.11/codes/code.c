#include <stdio.h>

void invert_matrix(double A[3][3], double inv[3][3]) {
    int i, j, k;
    double aug[3][6];
    // Build augmented matrix [A | I]
    for (i = 0; i < 3; ++i) {
        for (j = 0; j < 3; ++j) {
            aug[i][j] = A[i][j];
            aug[i][j+3] = (i == j) ? 1.0 : 0.0;
        }
    }
    // Forward elimination
    for (i = 0; i < 3; ++i) {
        double f = aug[i][i];
        for (j = 0; j < 6; ++j)
            aug[i][j] /= f;
        for (k = 0; k < 3; ++k) {
            if(k != i) {
                double f2 = aug[k][i];
                for (j = 0; j < 6; ++j)
                    aug[k][j] -= f2 * aug[i][j];
            }
        }
    }
    // Extract inverse
    for (i = 0; i < 3; ++i)
        for(j = 0; j < 3; ++j)
            inv[i][j] = aug[i][j+3];
}
