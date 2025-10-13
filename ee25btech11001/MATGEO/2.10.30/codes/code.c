#include <stdio.h>

// Function to calculate 'a' for collinearity
double find_a(double x1, double y1, double x2, double y2, double y3) {
    // Vector differences
    double u1 = x2 - x1;
    double u2 = y2 - y1;
    double v2 = y3 - y1;

    // Collinearity condition: v = λu
    // So, v2 = λu2 -> λ = v2/u2
    double lambda = v2 / u2;

    // Use first component: (a - x1) = λ * u1
    double a = x1 + lambda * u1;
    return a;
}
