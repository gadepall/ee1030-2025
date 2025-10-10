#include <stdio.h>
int main() {
    // Augmented matrix for the system:
    // 3λ - 2μ = -5
    // -λ      = -1
    // -3μ     = 0
    
    double A[3][3] = {
        {3, -2, -5},
        {-1, 0, -1},
        {0, -3, 0}
    };

    // Perform Gaussian elimination
    for (int i = 0; i < 3; i++) {
        // Normalize row i if pivot nonzero
        if (A[i][i] != 0) {
            double pivot = A[i][i];
            for (int j = i; j < 3; j++) {
                A[i][j] /= pivot;
            }
        }
        // Eliminate column i from other rows
        for (int k = 0; k < 3; k++) {
            if (k != i) {
                double factor = A[k][i];
                for (int j = i; j < 3; j++) {
                    A[k][j] -= factor * A[i][j];
                }
            }
        }
    }

    // After elimination, check last row
    if (A[2][0] == 0 && A[2][1] == 0 && A[2][2] != 0) {
        printf("System is inconsistent -> No solution. Lines are skew.\n");
    } else {
        double lambda = A[0][2];
        double mu = A[1][2];
        printf("Solution: lambda = %.2f, mu = %.2f\n", lambda, mu);
    }

    return 0;
}
