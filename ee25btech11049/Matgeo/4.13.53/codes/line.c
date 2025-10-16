#include <stdio.h>

/**
 * @brief Reflects a source line across a mirror line.
 *
 * @param a1, b1, c1 Coefficients of the source line to be reflected.
 * @param a2, b2, c2 Coefficients of the mirror line.
 * @param new_a, new_b, new_c Output pointers for the reflected line's coefficients.
 */
void reflect_line(double a1, double b1, double c1,
                  double a2, double b2, double c2,
                  double* new_a, double* new_b, double* new_c)
{
    // K1 is related to the dot product of the lines' normal vectors.
    double K1 = a1 * a2 + b1 * b2;

    // K2 is the squared magnitude of the mirror line's normal vector.
    double K2 = a2 * a2 + b2 * b2;

    // Prevent division by zero if the mirror line is invalid (0x + 0y + c = 0).
    if (K2 == 0) {
        *new_a = a1; *new_b = b1; *new_c = c1;
        return;
    }
    
    // Standard formula for line reflection.
    *new_a = 2 * a2 * K1 - a1 * K2;
    *new_b = 2 * b2 * K1 - b1 * K2;
    *new_c = 2 * c2 * K1 - c1 * K2;
}
