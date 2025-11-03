#include <stdio.h>

int main() {
// The given system of equations is:
// 2x + 1y = 5
// 3x + 2y = 8

// Define the coefficients and constants from the equations
// Equation 1: a1*x + b1*y = c1
double a1 = 2.0, b1 = 1.0, c1 = 5.0;
// Equation 2: a2*x + b2*y = c2
double a2 = 3.0, b2 = 2.0, c2 = 8.0;

// Variables to store the solution
double x, y;

// Calculate the determinant of the coefficient matrix
// D = (a1 * b2) - (a2 * b1)
double determinant = a1 * b2 - a2 * b1;

// Check if a unique solution exists (determinant is non-zero)
if (determinant != 0) {
// Find x and y using Cramer's rule
x = (c1 * b2 - c2 * b1) / determinant;
y = (a1 * c2 - a2 * c1) / determinant;

// Print the result
printf("The solution is:\n");
printf("x = %.2f\n", x);
printf("y = %.2f\n", y);
    } else {
// If the determinant is zero, there is no unique solution.
printf("The system does not have a unique solution.\n");
    }
    return 0;
}