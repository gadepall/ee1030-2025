#include <math.h>

/*
 * Calculates the real eigenvalues for a 2x2 matrix.
 * Matrix is defined as:
 * | a  b |
 * | c  d |
 * The results are stored in the memory locations pointed to by eig1 and eig2.
*/
void find_eigenvalues(double a, double b, double c, double d, double* eig1, double* eig2) {
    // For a 2x2 matrix, the characteristic equation is λ² - trace(A)λ + det(A) = 0
    double trace = a + d;
    double determinant = (a * d) - (b * c);

    // We solve for λ using the quadratic formula: [ -B ± sqrt(B² - 4AC) ] / 2A
    // Here, A=1, B=-trace, C=determinant
    double discriminant = trace * trace - 4 * determinant;

    // We assume real eigenvalues, so discriminant >= 0
    double sqrt_discriminant = sqrt(discriminant);

    *eig1 = (trace + sqrt_discriminant) / 2.0;
    *eig2 = (trace - sqrt_discriminant) / 2.0;
}