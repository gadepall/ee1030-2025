#include <stdio.h>
#include <math.h>

#define N 10  

int inverse(int n, double A[N][N], double Inv[N][N]) {
    double aug[N][2*N];

    // Form augmented matrix [A|I]
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            aug[i][j] = A[i][j];
        }
        for (int j = 0; j < n; j++) {
            aug[i][j+n] = (i==j) ? 1.0 : 0.0;
        }
    }

    // Forward elimination
    for (int i = 0; i < n; i++) {
        double pivot = aug[i][i];
        if (fabs(pivot) < 1e-12) {
            return 0; // singular
        }

        // Normalize row
        for (int j = 0; j < 2*n; j++) {
            aug[i][j] /= pivot;
        }

        // Eliminate other rows
        for (int k = 0; k < n; k++) {
            if (k != i) {
                double factor = aug[k][i];
                for (int j = 0; j < 2*n; j++) {
                    aug[k][j] -= factor * aug[i][j];
                }
            }
        }
    }

    // Extract inverse
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            Inv[i][j] = aug[i][j+n];
        }
    }

    return 1; 
}

void qr_iteration(int n, double A[N][N], double eigvals[N], int max_iter, double tol) {
    double Q[N][N], R[N][N], Ak[N][N];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            Ak[i][j] = A[i][j];

    for (int iter = 0; iter < max_iter; iter++) {
        // Gram-Schmidt to compute QR
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < n; i++) Q[i][j] = Ak[i][j];
            for (int k = 0; k < j; k++) {
                double dot = 0;
                for (int i = 0; i < n; i++) dot += Q[i][k] * Ak[i][j];
                for (int i = 0; i < n; i++) Q[i][j] -= dot * Q[i][k];
            }
            double norm = 0;
            for (int i = 0; i < n; i++) norm += Q[i][j]*Q[i][j];
            norm = sqrt(norm);
            for (int i = 0; i < n; i++) Q[i][j] /= norm;
        }

        // R = Q^T * A
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                R[i][j] = 0;
                for (int k = 0; k < n; k++) R[i][j] += Q[k][i] * Ak[k][j];
            }

        // Ak = R * Q
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                Ak[i][j] = 0;
                for (int k = 0; k < n; k++) Ak[i][j] += R[i][k] * Q[k][j];
            }
    }

    for (int i = 0; i < n; i++) eigvals[i] = Ak[i][i];
}

