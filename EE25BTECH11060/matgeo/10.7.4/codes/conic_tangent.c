#include <stdio.h>
#include <math.h>

// Define square root of 3
#define SQRT3 1.73205080757

// Function to check if a line is tangent to a conic
int check_tangent() {
    double A, B, C, D;
    double discriminant;

    // For Parabola: y = 2x + 2√3 into y^2 = 16√3 x
    A = 1;
    B = -2 * SQRT3;
    C = 3;
    discriminant = B*B - 4*A*C;

    if (fabs(discriminant) > 1e-6) return 0; // Not a tangent to parabola

    // For Ellipse: y = 2x + 2√3 into 2x^2 + y^2 = 4
    A = 6;
    B = 8 * SQRT3;
    C = 8;
    discriminant = B*B - 4*A*C;

    if (fabs(discriminant) > 1e-6) return 0; // Not a tangent to ellipse

    return 1; // Common tangent
}
