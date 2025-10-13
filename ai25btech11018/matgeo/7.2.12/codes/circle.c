#include <stdio.h>
#include <math.h>

int main() {
    // Define the coefficient matrix A and the constant vector B
    // Corresponding to the system:
    // 2x - 3y = 5
    // 3x - 4y = 7
    double A[2][2] = {{2.0, -3.0}, {3.0, -4.0}};
    double B[2] = {5.0, 7.0};

    // Calculate the determinant of the coefficient matrix A
    double determinant = A[0][0] * A[1][1] - A[0][1] * A[1][0];

    // Check if a unique solution exists
    if (determinant == 0) {
        printf("The lines are parallel or coincident; no unique solution exists.\n");
        return 1;
    }

    // Solve for x and y using Cramer's Rule
    // Determinant for x (replace first column with B)
    double det_x = B[0] * A[1][1] - B[1] * A[0][1];

    // Determinant for y (replace second column with B)
    double det_y = A[0][0] * B[1] - A[1][0] * B[0];

    double center_x = det_x / determinant;
    double center_y = det_y / determinant;

    // --- Part 2: Calculate radius and find the circle's equation ---

    // Given area of the circle
    double area = 154.0;
    const double PI = 22.0 / 7.0;

    // Calculate the radius squared from the area formula: Area = PI * r^2
    double r_squared = area / PI;
    
    // The equation of a circle can be expressed as: x^2 + y^2 - 2hx - 2ky + h^2 + k^2 - r^2 = 0
    // where (h, k) is the center of the circle.
    
    // The general form parameters (as used in the provided solution) are:
    // 2gx = -2hx  =>  g = -h
    // 2fy = -2ky  =>  f = -k
    // c = h^2 + k^2 - r^2
    
    double h = center_x;
    double k = center_y;
    double c = h * h + k * k - r_squared;

    // Print the final equation
    printf("The equation of the circle is:\n");
    printf("x^2 + y^2 - %.0fx - %.0fy + %.0f = 0\n", 2*h, 2*k, c);
    
    return 0;
}