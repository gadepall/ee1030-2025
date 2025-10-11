#include <stdio.h>
#include <math.h> // Required for the absolute value function fabs()

/**
 * @brief Calculates the volume of a parallelepiped using the determinant formula.
 * This function directly computes the scalar triple product without helper functions.
 *
 * @param a The first edge vector (array of 3 doubles).
 * @param b The second edge vector (array of 3 doubles).
 * @param c The third edge vector (array of 3 doubles).
 * @return The volume of the parallelepiped.
 */
double volumeOfParallelepiped(double a[], double b[], double c[]) {
    // Calculate the 3x3 determinant directly
    double scalar_triple_product = a[0] * (b[1] * c[2] - b[2] * c[1]) -
                                 a[1] * (b[0] * c[2] - b[2] * c[0]) +
                                 a[2] * (b[0] * c[1] - b[1] * c[0]);

    // Volume is the absolute value of the scalar triple product
    return fabs(scalar_triple_product);
}


