#include <stdio.h>

int main() {
    // Coefficients and constants for the system of linear equations
    // Equation 1: x + y = 6
    double a1 = 1.0;
    double b1 = 1.0;
    double c1 = 6.0;

    // Equation 2: 2x - 3y = 4
    double a2 = 2.0;
    double b2 = -3.0;
    double c2 = 4.0;

    // Use Cramer's Rule to solve for x and y
    // Determinant of the coefficient matrix
    double determinant = a1 * b2 - a2 * b1;

    // Check if the determinant is close to zero, which means no unique solution exists
    if (determinant == 0) {
        printf("The system has no unique solution.\n");
        return 1;
    }

    // Determinant for x
    double determinant_x = c1 * b2 - c2 * b1;
    
    // Determinant for y
    double determinant_y = a1 * c2 - a2 * c1;

    // Solve for x and y
    double x = determinant_x / determinant;
    double y = determinant_y / determinant;

    // Print the results
    printf("The solution to the system is:\n");
    printf("x = %.2f\n", x);
    printf("y = %.2f\n", y);

    return 0;
}
