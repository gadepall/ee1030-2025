#include <stdio.h>

/*
 * This function solves a system of two linear equations:
 * a1*x + b1*y = c1
 * a2*x + b2*y = c2
 *
 * It uses Cramer's rule.
 * The function returns 0 on success and -1 if no unique solution exists.
*/
int solve_system(double a1, double b1, double c1, double a2, double b2, double c2, double* x_result, double* y_result) {
    // Calculate the determinant of the coefficient matrix
    double determinant = a1 * b2 - a2 * b1;

    // If the determinant is zero, the lines are parallel or coincident,
    // so there is no unique solution.
    if (determinant == 0) {
        return -1; // Indicate failure
    }

    // Use Cramer's rule to find the solution for x and y
    *x_result = (c1 * b2 - c2 * b1) / determinant;
    *y_result = (a1 * c2 - a2 * c1) / determinant;

    return 0; // Indicate success
}
