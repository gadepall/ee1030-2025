#include <stdio.h>

#define N 4   // number of variables

// Gaussian elimination solver
// A = coefficient matrix (N x N)
// b = RHS vector (N)
// x = solution vector (N)
void gauss_solve(double A[N][N], double b[N], double x[N]) {
    int i, j, k;
    double ratio;

    // Forward elimination
    for (i = 0; i < N-1; i++) {
        for (j = i+1; j < N; j++) {
            if (A[i][i] == 0.0) {
                printf("Mathematical Error: zero pivot\n");
                return;
            }
            ratio = A[j][i] / A[i][i];
            for (k = 0; k < N; k++) {
                A[j][k] -= ratio * A[i][k];
            }
            b[j] -= ratio * b[i];
        }
    }

    // Back substitution
    x[N-1] = b[N-1] / A[N-1][N-1];
    for (i = N-2; i >= 0; i--) {
        x[i] = b[i];
        for (j = i+1; j < N; j++) {
            x[i] -= A[i][j] * x[j];
        }
        x[i] /= A[i][i];
    }
}


void solve_problem(double result[2]) {
    double A[N][N] = {
        { 1, -1, 0,  0},   
        {-2,  0, 1,  0},   
        { 0,  1, 0, -2},   
        { 0,  0, 1, -1}   
    };
    double b[N] = {3, 0, 0, 30};  
    double x[N];

    gauss_solve(A, b, x);

    result[0] = x[0];  // Ani
    result[1] = x[1];  // Bijoya
}

