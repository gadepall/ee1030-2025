#include <stdio.h>

void line3d(double x1, double y1, double z1,
            double x2, double y2, double z2,
            double lambda,
            double *x, double *y, double *z) {

    *x = x1 + lambda * (x2 - x1);
    *y = y1 + lambda * (y2 - y1);
    *z = z1 + lambda * (z2 - z1);
}
