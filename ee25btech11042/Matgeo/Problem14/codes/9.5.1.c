#include <math.h>

/**
 * @brief Calculates the real roots of a quadratic equation ax^2 + bx + c = 0.
 *
 * @param a The coefficient of the x^2 term.
 * @param b The coefficient of the x term.
 * @param c The constant term.
 * @param root1 Pointer to a double where the first root will be stored.
 * @param root2 Pointer to a double where the second root will be stored.
 */
void find_roots(double a, double b, double c, double* root1, double* root2) {
    // Calculate the discriminant
    double discriminant = b*b - 4*a*c;

    // Check if real roots exist
    if (discriminant >= 0) {
        // Calculate the two roots using the quadratic formula
        *root1 = (-b + sqrt(discriminant)) / (2 * a);
        *root2 = (-b - sqrt(discriminant)) / (2 * a);
    }
}
