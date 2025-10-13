#include <stdio.h>
#include <math.h>

int main() {
    // Given 2x2 matrix
    float a = 5, b = 3, c = 1, d = 4;
    
    // Variables for trace, determinant, and eigenvalues
    float trace, det, lambda1, lambda2, discriminant;

    // Trace = a + d
    trace = a + d;

    // Determinant = ad - bc
    det = a * d - b * c;

    // Characteristic equation: λ² - (trace)λ + det = 0
    // => λ = [trace ± sqrt(trace² - 4det)] / 2
    discriminant = trace * trace - 4 * det;

    // Check if discriminant is positive
    if (discriminant >= 0) {
        lambda1 = (trace + sqrt(discriminant)) / 2;
        lambda2 = (trace - sqrt(discriminant)) / 2;

        printf("Eigenvalues are: %.2f and %.2f\n", lambda1, lambda2);
    } else {
        printf("Eigenvalues are complex.\n");
    }
    return 0;
}