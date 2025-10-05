#include <stdio.h>

void solve_lu(double A[9], double b[3], double z_out[3], double x_out[3]) {
    // --- 1. LU Decomposition (Doolittle's method, no pivoting) ---
    double L[3][3] = {{0}};
    double U[3][3] = {{0}};

    for (int i = 0; i < 3; i++) {
        // Upper Triangular (U)
        for (int k = i; k < 3; k++) {
            double sum = 0;
            for (int j = 0; j < i; j++) {
                sum += (L[i][j] * U[j][k]);
            }
            U[i][k] = A[i * 3 + k] - sum;
        }

        // Lower Triangular (L)
        for (int k = i; k < 3; k++) {
            if (i == k)
                L[i][i] = 1; // Diagonal as 1
            else {
                double sum = 0;
                for (int j = 0; j < i; j++) {
                    sum += (L[k][j] * U[j][i]);
                }
                L[k][i] = (A[k * 3 + i] - sum) / U[i][i];
            }
        }
    }

    // --- 2. Solve Lz = b (Forward Substitution) ---
    z_out[0] = b[0] / L[0][0];
    z_out[1] = (b[1] - L[1][0] * z_out[0]) / L[1][1];
    z_out[2] = (b[2] - L[2][0] * z_out[0] - L[2][1] * z_out[1]) / L[2][2];


    // --- 3. Solve Ux = z (Back Substitution) ---
    x_out[2] = z_out[2] / U[2][2];
    x_out[1] = (z_out[1] - U[1][2] * x_out[2]) / U[1][1];
    x_out[0] = (z_out[0] - U[0][1] * x_out[1] - U[0][2] * x_out[2]) / U[0][0];
}
