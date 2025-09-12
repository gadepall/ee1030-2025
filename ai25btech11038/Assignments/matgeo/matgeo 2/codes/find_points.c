#include <math.h>
#include <stdio.h>

// Function to find the two X-axis points
// Inputs: point (x0, y0), distance d
// Outputs: x1 and x2 (roots)
void find_x_axis_points(double x0, double y0, double d, double *x1, double *x2) {
    // Equation: (x - x0)^2 + (0 - y0)^2 = d^2
    // => (x - x0)^2 = d^2 - y0^2
    double rhs = d*d - y0*y0;
    if (rhs < 0) {
        // No real solutions
        *x1 = NAN;
        *x2 = NAN;
        return;
    }
    double root = sqrt(rhs);
    *x1 = x0 + root;
    *x2 = x0 - root;
}

// For standalone testing
int main() {
    double x1, x2;
    find_x_axis_points(7.0, -4.0, 2.0*sqrt(5.0), &x1, &x2);
    printf("X-axis points: (%.2f, 0) and (%.2f, 0)\n", x1, x2);
    return 0;
}