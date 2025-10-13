#include <math.h>

int solve_quadratic(double a, double b, double c, double* root1, double* root2) {
    if (a == 0) {
        // Not a quadratic equation
        return 0;
    }

    double discriminant = b * b - 4 * a * c;

    if (discriminant < 0) {
        // No real roots
        return 0;
    } else if (discriminant == 0) {
        // One real root
        *root1 = -b / (2 * a);
        return 1;
    } else {
        // Two real roots
        double sqrt_discriminant = sqrt(discriminant);
        *root1 = (-b + sqrt_discriminant) / (2 * a);
        *root2 = (-b - sqrt_discriminant) / (2 * a);
        return 2;
    }
}

