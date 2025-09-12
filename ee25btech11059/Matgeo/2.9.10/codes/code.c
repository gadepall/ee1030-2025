#include <stdio.h>
#include <math.h>

#define EPS 1e-6

// Compute dot product of two 2D vectors stored as 1×2 matrices
// a: array double a[2]; b: array double b[2]
double dot2(const double a[2], const double b[2]) {
    return a[0]*b[0] + a[1]*b[1];
}

// Solve the question using matrix-like vector operations
// returns 1 if (a + 2b) is perpendicular to a under the condition ||a + b|| == ||b||, else 0
int solve_matrix_vectors(double a0, double a1, double b0, double b1) {
    double a_vec[2] = { a0, a1 };
    double b_vec[2] = { b0, b1 };

    double ab_vec[2] = { a0 + b0, a1 + b1 };     // a + b
    double b_norm2 = dot2(b_vec, b_vec);         // ||b||^2
    double ab_norm2 = dot2(ab_vec, ab_vec);       // ||a + b||^2

    if (fabs(ab_norm2 - b_norm2) > EPS) {
        // Condition ||a + b|| == ||b|| fails
        return 0;
    }

    double a2b_vec[2] = { a0 + 2.0 * b0, a1 + 2.0 * b1 };  // a + 2b

    double dp = dot2(a_vec, a2b_vec);    // a · (a + 2b)

    if (fabs(dp) < EPS) {
        // Perpendicular
        return 1;
    } else {
        return 0;
    }
}


