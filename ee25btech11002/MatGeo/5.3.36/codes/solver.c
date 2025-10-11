#include <stdio.h>
void solve_system(double A[2][2], double b[2], double* x_sol, double* y_sol) {
    // Solve the 2x2 system using Cramer's rule.
    // det(A)
    double determinant = A[0][0] * A[1][1] - A[0][1] * A[1][0];

    // Check if a unique solution exists.
    if (determinant != 0) {
        // det(Ax)
        double determinant_x = b[0] * A[1][1] - A[0][1] * b[1];
        // det(Ay)
        double determinant_y = A[0][0] * b[1] - b[0] * A[1][0];

        *x_sol = determinant_x / determinant;
        *y_sol = determinant_y / determinant;
    } else {
        // No unique solution, set results to 0 or an error indicator.
        *x_sol = 0;
        *y_sol = 0;
    }
}