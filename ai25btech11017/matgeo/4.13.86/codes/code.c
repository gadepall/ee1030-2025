#include <stdio.h>
#include <math.h>

int main() {
    // Normals of given planes
    double n1[3] = {2, -2, 1};
    double n2[3] = {1, -1, 2};

    // Cross product to get required plane normal
    double a = n1[1]*n2[2] - n1[2]*n2[1];
    double b = n1[2]*n2[0] - n1[0]*n2[2];
    double c = n1[0]*n2[1] - n1[1]*n2[0];

    // Point through which plane passes
    double x0 = 1, y0 = -2, z0 = 1;

    // Plane equation: a(x-x0) + b(y-y0) + c(z-z0) = 0
    double d = -(a*x0 + b*y0 + c*z0);

    printf("Equation of required plane: %.1fx + %.1fy + %.1fz + %.1f = 0\n", a, b, c, d);

    // Point from which distance is required
    double x1 = 1, y1 = 2, z1 = 2;

    // Distance formula
    double numerator = fabs(a*x1 + b*y1 + c*z1 + d);
    double denominator = sqrt(a*a + b*b + c*c);
    double distance = numerator / denominator;

    printf("Distance = %.4f\n", distance);

    return 0;
}
