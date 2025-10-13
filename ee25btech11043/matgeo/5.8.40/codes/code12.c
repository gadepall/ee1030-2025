#include <stdio.h>

// Function to solve a 2x2 system of linear equations using Cramer's Rule
// a1*x + b1*y = c1
// a2*x + b2*y = c2
//   a1, b1, c1: Coefficients and constant for the first equation
//   a2, b2, c2: Coefficients and constant for the second equation
//   *x_solution: Pointer to store the solution for x
//   *y_solution: Pointer to store the solution for y
int solve_2x2_system(double a1, double b1, double c1,
                      double a2, double b2, double c2,
                      double *x_solution, double *y_solution) {

    double determinant = a1 * b2 - a2 * b1;

    // Check if a unique solution exists
    if (determinant == 0) {
        // No unique solution (parallel lines or same line)
        return 0;
    }

    double det_x = c1 * b2 - c2 * b1;
    double det_y = a1 * c2 - a2 * c1;

    *x_solution = det_x / determinant;
    *y_solution = det_y / determinant;

    return 1; // Unique solution found
}