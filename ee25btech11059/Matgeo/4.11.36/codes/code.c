#include <stdio.h>
#include <math.h>

#define N 3

// Gaussian elimination solver
void gaussElimination(double A[N][N], double b[N], double x[N]) {
    int i, j, k;
    double ratio;

    // Forward elimination
    for (i = 0; i < N - 1; i++) {
        for (j = i + 1; j < N; j++) {
            if (fabs(A[i][i]) < 1e-12) return;
            ratio = A[j][i] / A[i][i];
            for (k = 0; k < N; k++) {
                A[j][k] -= ratio * A[i][k];
            }
            b[j] -= ratio * b[i];
        }
    }

    // Back substitution
    for (i = N - 1; i >= 0; i--) {
        x[i] = b[i];
        for (j = i + 1; j < N; j++) {
            x[i] -= A[i][j] * x[j];
        }
        x[i] /= A[i][i];
    }
}

// Exposed function for Python
void solve_plane(double *out) {
    double A[N][N] = {
        {1, 2, 3},
        {4, 2, -3},
        {0, 4, 3}
    };
    double b[N] = {1, 1, 1};
    double n[N];

    gaussElimination(A, b, n);

    for (int i = 0; i < N; i++) {
        out[i] = n[i];
    }
}
