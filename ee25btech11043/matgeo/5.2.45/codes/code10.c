#include <stdio.h>

// Function to solve a 2x2 system of linear equations
// a1, b1, c1: coefficients for the first equation (a1*x + b1*y = c1)
// a2, b2, c2: coefficients for the second equation (a2*x + b2*y = c2)
// x_sol, y_sol: pointers to store the solutions for x and y
void solveLinearSystem(double a1, double b1, double c1,
                       double a2, double b2, double c2,
                       double *x_sol, double *y_sol) {
    double determinant = a1 * b2 - a2 * b1;

    *x_sol = (c1 * b2 - c2 * b1) / determinant;
    *y_sol = (a1 * c2 - a2 * c1) / determinant;
}