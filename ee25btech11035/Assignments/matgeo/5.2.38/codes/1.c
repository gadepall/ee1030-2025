#include <stdio.h>
int solve_system(double a1, double b1, double c1, double a2, double b2, double c2, double *x_sol, double *y_sol) {
    // Calculate the determinant of the coefficient matrix
    double determinant = a1 * b2 - a2 * b1;

    // Use Cramer's rule to find p and q (where u = 1/x and q = 1/y)
    double p = (c1 * b2 - c2 * b1) / determinant;
    double q = (a1 * c2 - a2 * c1) / determinant;

    // Store the results in the output pointers
    *x_sol = 1.0 / p;
    *y_sol = 1.0 / q;

    return 1; // Success
}