#include <stdio.h>

// Function to compute cross product of two 3D vectors
void cross_product(double a[3], double b[3], double result[3]) {
    result[0] = a[1]*b[2] - a[2]*b[1];
    result[1] = a[2]*b[0] - a[0]*b[2];
    result[2] = a[0]*b[1] - a[1]*b[0];
}

// Function to compute line equation point for given t
void line_equation(double t, double *x, double *y, double *z) {
    // Given point (1,2,-4)
    double p[3] = {1, 2, -4};

    // Given direction vectors of the two lines
    double d1[3] = {3, -16, 7};
    double d2[3] = {3, 8, -5};

    // Direction of required line = cross product of d1 and d2
    double d[3];
    cross_product(d1, d2, d);

    // Simplify direction vector by dividing by GCD factor if desired
    // For this case, (24,36,72) → (2,3,6)
    d[0] = 2; d[1] = 3; d[2] = 6;

    // Parametric equation
    *x = p[0] + d[0]*t;
    *y = p[1] + d[1]*t;
    *z = p[2] + d[2]*t;
}

// Convenience function for printing
void print_line(double t) {
    double x, y, z;
    line_equation(t, &x, &y, &z);
    printf("For t=%.2f -> (x, y, z) = (%.2f, %.2f, %.2f)\n", t, x, y, z);
}

// Main function (for standalone execution)
int main() {
    printf("Line passing through (1,2,-4) and perpendicular to given lines:\n");
    printf("Vector form: r(t) = (1,2,-4) + t(2,3,6)\n\n");

    // Print some sample points
    for (int i = 0; i <= 5; i++) {
        print_line((double)i);
    }
    return 0;
}

