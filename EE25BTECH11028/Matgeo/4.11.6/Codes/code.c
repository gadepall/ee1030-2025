#include <stdio.h>
#include <math.h>

int main() {
    // Coefficients of the final plane: y - 3z + 6 = 0
    double A = 0, B = 1, C = -3, D = 6;

    // A point on X-axis (0,0,0)
    double x0 = 0, y0 = 0, z0 = 0;

    double numerator = fabs(A*x0 + B*y0 + C*z0 + D);
    double denominator = sqrt(A*A + B*B + C*C);
    double distance = numerator / denominator;

    printf("Equation of the plane: y - 3z + 6 = 0\n");
    printf("Distance of plane from X-axis: %.4f\n", distance);

    return 0;
}