#include <math.h>

/*
 * This function calculates the eigenvalues of a 2x2 matrix:
 * | a  b |
 * | c  d |
 *
 * The characteristic equation is lambda^2 - (a+d)lambda + (ad-bc) = 0.
 * We solve this using the standard quadratic formula.
 *
 * @param a, b, c, d The elements of the 2x2 matrix.
 * @param eig1 Pointer to a double to store the first eigenvalue.
 * @param eig2 Pointer to a double to store the second eigenvalue.
 */
void find_2x2_eigenvalues(double a, double b, double c, double d, double* eig1, double* eig2) {
    // For the equation x^2 + Bx + C = 0, the solutions are (-B +/- sqrt(B^2 - 4C)) / 2.
    // Here, B = -(a+d) and C = (ad-bc).
    double trace = a + d;
    double determinant = a * d - b * c;

    // Calculate the discriminant: sqrt(trace^2 - 4*determinant)
    double discriminant_sqrt = sqrt(trace * trace - 4 * determinant);

    // Calculate the two eigenvalues using the formula
    *eig1 = (trace + discriminant_sqrt) / 2.0;
    *eig2 = (trace - discriminant_sqrt) / 2.0;
}

