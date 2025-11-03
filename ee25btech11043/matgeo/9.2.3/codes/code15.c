#include <stdio.h>

// Function to calculate the definite integral of a linear function (mx + c)
double calculate_integral(double m, double c, double a, double b) {
    // Integral of mx + c is (m/2)x^2 + cx
    return ((m / 2.0) * b * b + c * b) - ((m / 2.0) * a * a + c * a);
}