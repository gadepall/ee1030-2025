#include <stdio.h>

#define N 3

void printMatrix(double mat[N][N + 1]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N + 1; j++) {
            printf("%8.3f ", mat[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

void gaussianElimination(double mat[N][N + 1], double result[N]) {
    for (int i = 0; i < N; i++) {
        // Make the diagonal element 1
        double diag = mat[i][i];
        for (int j = 0; j <= N; j++) {
            mat[i][j] /= diag;
        }

        // Eliminate other rows
        for (int k = 0; k < N; k++) {
            if (k != i) {
                double factor = mat[k][i];
                for (int j = 0; j <= N; j++) {
                    mat[k][j] -= factor * mat[i][j];
                }
            }
        }
    }

    // Extract solution
    for (int i = 0; i < N; i++) {
        result[i] = mat[i][N];
    }
}

void solve() {
    double mat[N][N + 1] = {
        {1, 1, 1, 21},
        {4, 3, 2, 60},
        {6, 2, 3, 70}
    };

    double result[N];

    gaussianElimination(mat, result);

    printf("Solution:\n");
    printf("x = %.2f\n", result[0]);
    printf("y = %.2f\n", result[1]);
    printf("z = %.2f\n", result[2]);
}
