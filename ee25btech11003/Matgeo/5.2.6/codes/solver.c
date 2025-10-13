#include <stdio.h>
#include <math.h> // Required for fabs()

// Define a small value for floating-point comparisons
#define EPSILON 1e-9

/**
 * @brief Solves a system of two linear equations: a1*x + b1*y = c1 and a2*x + b2*y = c2.
 * @return int Status: 1 for unique, 0 for none, -1 for infinite solutions.
 */
int solveLinearSystem(double a1, double b1, double c1, double a2, double b2, double c2, double* x, double* y) {
    double determinant = a1 * b2 - a2 * b1;

    // Unique solution
    if (fabs(determinant) > EPSILON) {
        *x = (c1 * b2 - c2 * b1) / determinant;
        *y = (a1 * c2 - a2 * c1) / determinant;
        return 1;
    }
    // No solution or infinite solutions
    else {
        if (fabs(c1 * b2 - c2 * b1) > EPSILON || fabs(a1 * c2 - a2 * c1) > EPSILON) {
             return 0; // No solution
        } else {
             return -1; // Infinite solutions
        }
    }
}
