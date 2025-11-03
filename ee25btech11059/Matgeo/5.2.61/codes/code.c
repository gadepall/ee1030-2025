#include <stdio.h>

#define N 3  // number of equations

// Function to perform Gaussian elimination
void gaussian_elimination(double A[N][N+1], double x[N]) {
    int i, j, k;

    // Forward elimination
    for (i = 0; i < N-1; i++) {
        for (k = i+1; k < N; k++) {
            double factor = A[k][i] / A[i][i];
            for (j = i; j <= N; j++) {
                A[k][j] -= factor * A[i][j];
            }
        }
    }

    // Back-substitution
    for (i = N-1; i >= 0; i--) {
        x[i] = A[i][N];
        for (j = i+1; j < N; j++) {
            x[i] -= A[i][j] * x[j];
        }
        x[i] = x[i] / A[i][i];
    }
}

// Exposed function for ctypes
void solve_system(double *solution) {
    // Augmented matrix for given system:
    // x - y + 2z = 1
    // 0x + 2y - 3z = 1
    // 3x - 2y + 4z = 2
    double A[N][N+1] = {
        {1, -1,  2, 1},
        {0,  2, -3, 1},
        {3, -2,  4, 2}
    };

    double x[N];
    gaussian_elimination(A, x);

    for (int i = 0; i < N; i++) {
        solution[i] = x[i];
    }
}
