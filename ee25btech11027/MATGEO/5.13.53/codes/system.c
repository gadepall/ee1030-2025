#include <stdio.h>
#include <math.h>

// Function to perform Gaussian elimination on a 3x4 augmented matrix [A|B]
// Returns 0 for No Solution (Inconsistent), 1 for Solvable (Unique/Infinite).
int solve_system_c(double matrix[3][4]) {
    const int N = 3; // Number of variables
    int i, j, k;
    double factor;
    const double TOLERANCE = 1e-9; // Tolerance for floating point zero checks

    // --- Forward Elimination ---
    for (i = 0; i < N; i++) {
        // Find pivot (for robustness, a full pivot search would be better, but we assume simple pivots)
        if (fabs(matrix[i][i]) < TOLERANCE) {
            for (k = i + 1; k < N; k++) {
                if (fabs(matrix[k][i]) > TOLERANCE) {
                    // Swap R_i and R_k
                    for (j = i; j < N + 1; j++) {
                        double temp = matrix[i][j];
                        matrix[i][j] = matrix[k][j];
                        matrix[k][j] = temp;
                    }
                    break;
                }
            }
            if (fabs(matrix[i][i]) < TOLERANCE) continue; // Skip if no good pivot found
        }

        // Eliminate
        for (k = i + 1; k < N; k++) {
            factor = matrix[k][i] / matrix[i][i];
            for (j = i; j < N + 1; j++) {
                matrix[k][j] -= factor * matrix[i][j];
            }
        }
    }

    // --- Check for Inconsistency (No Solution) ---
    // Look for a row [0 0 0 | k] where k != 0
    if (fabs(matrix[N-1][N-1]) < TOLERANCE && fabs(matrix[N-1][N]) > TOLERANCE) {
        return 0; // No Solution
    }
    
    return 1; // Solvable (Could be unique or infinite, but not 'no solution')
}
