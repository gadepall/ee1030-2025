#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// Function to find eigenvalues of a 3x3 matrix.
// Assumes at least one integer root exists.
void find_eigenvalues_3x3(double* A, double* roots) {
    // The characteristic polynomial is: λ³ - tr(A)λ² + Cλ - det(A) = 0
    // We will find the coefficients for: λ³ + bλ² + cλ + d = 0

    // b = -tr(A)
    double b = -(A[0] + A[4] + A[8]);

    // c = sum of the principal minors
    double c = (A[0]*A[4] - A[1]*A[3]) + (A[0]*A[8] - A[2]*A[6]) + (A[4]*A[8] - A[5]*A[7]);

    // d = -det(A)
    double d = -(A[0]*(A[4]*A[8] - A[5]*A[7]) - A[1]*(A[3]*A[8] - A[5]*A[6]) + A[2]*(A[3]*A[7] - A[4]*A[6]));

    // Find one integer root using the Rational Root Theorem.
    // An integer root must be a divisor of the constant term 'd'.
    int root1_found = 0;
    for (int i = 1; i <= abs((int)round(d)); ++i) {
        if (fmod(d, i) == 0) {
            // Test positive divisor
            if (pow(i, 3) + b*pow(i, 2) + c*i + d < 1e-9) {
                roots[0] = i;
                root1_found = 1;
                break;
            }
            // Test negative divisor
            if (pow(-i, 3) + b*pow(-i, 2) + c*(-i) + d < 1e-9) {
                roots[0] = -i;
                root1_found = 1;
                break;
            }
        }
    }
    
    // Check for root at zero
    if (!root1_found && fabs(d) < 1e-9) {
        roots[0] = 0;
        root1_found = 1;
    }


    if (!root1_found) {
        // Could not find an integer root, exiting.
        // A more robust solver (e.g., Cardano's method) would be needed here.
        roots[0] = NAN;
        roots[1] = NAN;
        roots[2] = NAN;
        return;
    }

    // Perform polynomial division to get a quadratic equation: λ² + pλ + q = 0
    double p = b + roots[0];
    double q = c + p * roots[0];

    // Use the quadratic formula to find the other two roots
    double discriminant = p*p - 4*q;
    roots[1] = (-p + sqrt(discriminant)) / 2.0;
    roots[2] = (-p - sqrt(discriminant)) / 2.0;
}