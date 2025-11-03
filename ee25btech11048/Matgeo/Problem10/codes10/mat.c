#include <stdio.h>

#define N 3   // matrix size

void inverse(double A[N][N], double inv[N][N]) {
    double aug[N][2*N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            aug[i][j] = A[i][j];
            aug[i][j+N] = (i == j) ? 1 : 0;
        }
    }
    for (int i = 0; i < N; i++) {
        double pivot = aug[i][i];
        for (int j = 0; j < 2*N; j++) {
            aug[i][j] /= pivot;
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
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            inv[i][j] = aug[i][j+N];
        }
    }
}

int main() {
    double A[N][N] = {
        {1, -1, 2},
        {0, 2, -3},
        {3, -2, 4}
    };
    double inv[N][N];
    inverse(A, inv);
    printf("Inverse of the given matrix is:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%8.3f ", inv[i][j]);
        }
        printf("\n");
    }
    return 0;
}

