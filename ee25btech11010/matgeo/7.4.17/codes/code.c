#include <math.h>

// Function to solve circle given two lines on diameter and circumference
void circle_from_diameter_lines(double a1, double b1, double c1,
                                double a2, double b2, double c2,
                                double circumference,
                                double coeffs[5]) {
    // Find intersection point of the two lines (midpoint of diameter)
    double det = a1*b2 - a2*b1;
    double x0 = (b1*c2 - b2*c1)/det;
    double y0 = (a2*c1 - a1*c2)/det;

    // Radius from circumference: 2*pi*r = circumference
    double r = circumference / (2*M_PI);
    double r2 = r*r;

    // Circle equation: (x - x0)^2 + (y - y0)^2 = r^2
    // Expand: x^2 + y^2 - 2*x0*x - 2*y0*y + (x0^2 + y0^2 - r^2) = 0
    coeffs[0] = -2*x0;                    // D
    coeffs[1] = -2*y0;                    // E
    coeffs[2] = x0*x0 + y0*y0 - r2;      // F
    coeffs[3] = 1.0;                      // Coefficient of x^2
    coeffs[4] = 1.0;                      // Coefficient of y^2
}
