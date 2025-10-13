#include <math.h>

double calculate_tangent(double a, double b) {
    // Calculate the denominator of the formula.
    double denominator = (a * a) - (b * b);

    // Check if the denominator is zero. This happens when the lines are
    // perpendicular, and the tangent would be undefined (division by zero).
    if (denominator == 0.0) {
        return NAN; // Return "Not a Number" to indicate an undefined result.
    }

    // Calculate the numerator.
    double numerator = 2.0 * a * b;

    // Return the final calculated tangent.
    return numerator / denominator;
}

