#include <stdio.h>
#include <math.h>

double distanceFromPointToPlane(double A, double B, double C, double D_plane,
                                double x0, double y0, double z0) {
    double numerator = fabs(A * x0 + B * y0 + C * z0 - D_plane);
    double denominator = sqrt(A * A + B * B + C * C);
    return numerator / denominator;
}

int main() {
    double A = 1, B = 2, C = -2;
    double alpha = 10;
    double x0 = 1, y0 = -2, z0 = 1;
    double distance = distanceFromPointToPlane(A, B, C, alpha, x0, y0, z0);
    printf("Distance from point to plane = %.2f\n", distance);
    return 0;
}
