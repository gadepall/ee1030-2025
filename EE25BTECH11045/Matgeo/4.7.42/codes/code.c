#include <stdio.h>
#include <math.h>

void foot_and_length(double px, double py, double pz,
                     double a, double b, double c, double d,
                     double *x0, double *y0, double *z0, double *dist) {
    // Normal vector n = (a, b, c)
    double numerator = a*px + b*py + c*pz + d;
    double denominator = a*a + b*b + c*c;
    double lambda = - numerator / denominator;

    *x0 = px + lambda * a;
    *y0 = py + lambda * b;
    *z0 = pz + lambda * c;

    *dist = fabs(numerator) / sqrt(denominator);
}

// For testing
int main() {
    double px = 1, py = 1.5, pz = 2;
    double a = 2, b = -2, c = 4, d = 5;
    double x0, y0, z0, dist;

    foot_and_length(px, py, pz, a, b, c, d, &x0, &y0, &z0, &dist);

    printf("Foot of perpendicular: (%.4f, %.4f, %.4f)\n", x0, y0, z0);
    printf("Perpendicular length: %.4f\n", dist);

    return 0;
}