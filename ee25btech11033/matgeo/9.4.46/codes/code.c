// File: solver.c
#include <math.h>


void solve_quadratic(double a, double b, double c, double* root1, double* root2) {
    // Calculate the discriminant
    double discriminant = b*b - 4*a*c;

    // The roots are real only if the discriminant is non-negative
    if (discriminant >= 0) {
        *root1 = (-b + sqrt(discriminant)) / (2*a);
        *root2 = (-b - sqrt(discriminant)) / (2*a);
    } else {
        // If roots are not real, set them to Not a Number (NaN)
        *root1 = NAN;
        *root2 = NAN;
    }
}
