#include <stdio.h>

void line_point(double lambda, double h[3], double m[3], double x[3]) {
    x[0] = h[0] + lambda * m[0];
    x[1] = h[1] + lambda * m[1];
    x[2] = h[2] + lambda * m[2];
}

