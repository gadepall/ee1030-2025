#include <stdio.h>
#include <math.h>

void getCofactor(int n, double matrix[n][n], double temp[n-1][n-1], int p, int q) {
    int i = 0, j = 0;
    for (int row = 0; row < n; row++) {
        for (int col = 0; col < n; col++) {
            if (row != p && col != q) {
                temp[i][j++] = matrix[row][col];
                if (j == n - 1) {
                    j = 0;
                    i++;
                }
            }
        }
    }
}
double determinant(int n, double matrix[n][n]) {
    double det = 0;
    if (n == 1) {
        return matrix[0][0];
    }
    double temp[n-1][n-1];
    int sign = 1;
    for (int col = 0; col < n; col++) {
        getCofactor(n, matrix, temp, 0, col);
        det += sign * matrix[0][col] * determinant(n-1, temp);
        sign = -sign;
    }
    return det;
}
void adjoint(int n, double matrix[n][n], double adj[n][n]) {
    if (n == 1) {
        adj[0][0] = 1;
        return;
    }
    double temp[n-1][n-1];
    int sign = 1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            getCofactor(n, matrix, temp, i, j);
            sign = ((i + j) % 2 == 0) ? 1 : -1;
            adj[j][i] = (sign) * (determinant(n-1, temp));
        }
    }
}
void function(int n, double matrix[n][n], double inverse_matrix[n][n]) {
    double det = determinant(n, matrix);
    if (fabs(det) < 1e-9) {
        printf("Inverse doesn't exist.");
    }
    double adj[n][n];
    adjoint(n, matrix, adj);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            inverse_matrix[i][j] = adj[i][j] / det;
        }
    }
}
