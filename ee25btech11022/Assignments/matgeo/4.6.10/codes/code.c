
// code.c
#include <stdio.h>

void line_points(double* xs, double* ys, double* zs, int n) {
    double x0 = 1, y0 = -3, z0 = 2;  // given point
    double dx = 1, dy = 1, dz = 1;   // direction vector
    for (int i = 0; i < n; ++i) {
        double lambda = (i - n/2);   // range [-n/2, n/2]
        xs[i] = x0 + lambda * dx;
        ys[i] = y0 + lambda * dy;
        zs[i] = z0 + lambda * dz;
    }
}

void normal_vector(double* normal) {
    normal[0] = 1;
    normal[1] = 1;
    normal[2] = 1;
}


