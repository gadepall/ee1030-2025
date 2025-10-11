#include <stdio.h>
#include <math.h>

int main() {
    // Plane equation: Ax + By + Cz + D = 0
    double A = 2, B = -3, C = 4, D = -6;

    // Point (origin)
    double x0 = 0, y0 = 0, z0 = 0;

    // Distance formula: |Ax0 + By0 + Cz0 + D| / sqrt(A^2 + B^2 + C^2)
    double numerator = fabs(A*x0 + B*y0 + C*z0 + D);
    double denominator = sqrt(A*A + B*B + C*C);
    double distance = numerator / denominator;

    printf("Distance of plane %.0fx + (%.0f)y + %.0fz + (%.0f) = 0 from origin is: %lf\n",
           A, B, C, D, distance);

    return 0;
}