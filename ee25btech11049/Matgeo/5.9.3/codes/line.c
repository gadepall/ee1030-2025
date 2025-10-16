#include <stdio.h>
#include <math.h> // Required for fabs()

// This function solves a system of two linear equations using an augmented matrix
// and Gaussian elimination.
// a*x + b*y = e
// c*x + d*y = f
void solve_system(double a, double b, double c, double d, double e, double f, double* x, double* y) {
    // Create the augmented matrix: [ a b | e ]
    //                               [ c d | f ]
    double aug_matrix[2][3] = {
        {a, b, e},
        {c, d, f}
    };

    // --- Forward Elimination to get Row-Echelon Form ---

    // If the pivot (a) is zero, swap the rows to avoid division by zero.
    if (fabs(aug_matrix[0][0]) < 1e-9) {
        for (int i = 0; i < 3; i++) {
            double temp = aug_matrix[0][i];
            aug_matrix[0][i] = aug_matrix[1][i];
            aug_matrix[1][i] = temp;
        }
    }

    // Check if the pivot is still zero, which means no unique solution exists.
    if (fabs(aug_matrix[0][0]) < 1e-9) {
        *x = -1.0/0.0; // Represents NaN
        *y = -1.0/0.0; // Represents NaN
        return;
    }

    // Perform the row operation: R2 -> R2 - (c/a) * R1
    double factor = aug_matrix[1][0] / aug_matrix[0][0];
    aug_matrix[1][0] = 0.0; // This is the goal
    aug_matrix[1][1] -= factor * aug_matrix[0][1];
    aug_matrix[1][2] -= factor * aug_matrix[0][2];

    // --- Back Substitution ---

    // Check if the second pivot element is zero. If so, there's no unique solution.
    if (fabs(aug_matrix[1][1]) < 1e-9) {
        *x = -1.0/0.0; // NaN
        *y = -1.0/0.0; // NaN
        return;
    }

    // Solve for y from the second row: (d')*y = f'
    *y = aug_matrix[1][2] / aug_matrix[1][1];

    // Solve for x from the first row: a*x + b*y = e  => x = (e - b*y) / a
    *x = (aug_matrix[0][2] - aug_matrix[0][1] * (*y)) / aug_matrix[0][0];
}


