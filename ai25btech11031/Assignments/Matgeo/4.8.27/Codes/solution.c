#include "solution.h"

int main() {
    // Input point
    double x0, y0, z0;
    printf("Enter point (x0 y0 z0): ");
    scanf("%lf %lf %lf", &x0, &y0, &z0);

    // Input first plane coefficients
    double a1, b1, c1, d1;
    printf("Enter coefficients of plane1 (a1 b1 c1 d1): ");
    scanf("%lf %lf %lf %lf", &a1, &b1, &c1, &d1);

    // Input second plane coefficients
    double a2, b2, c2, d2;
    printf("Enter coefficients of plane2 (a2 b2 c2 d2): ");
    scanf("%lf %lf %lf %lf", &a2, &b2, &c2, &d2);

    // Normal vectors of plane1 and plane2
    double n1x = a1, n1y = b1, n1z = c1;
    double n2x = a2, n2y = b2, n2z = c2;

    // Compute required normal (cross product)
    double nx, ny, nz;
    cross_product(n1x, n1y, n1z, n2x, n2y, n2z, &nx, &ny, &nz);

    // Print required plane
    plane_equation(nx, ny, nz, x0, y0, z0);

    return 0;
}

