#include <stdio.h>

// Family of lines: parametrize p=t, q=1, r = -(3t + 2)/4.
// Generates n points on each such line passing through concurrency point (3/4, 1/2).
void generate_points(double *x, double *y, int n, double t) {
    double q = 1.0;
    double r = -(3.0*t + 2.0)/4.0;
    double x_start = -1.0;
    double x_end = 2.0;
    for (int i = 0; i < n; i++) {
        x[i] = x_start + (x_end - x_start)*i/(n-1);
        y[i] = (-t*x[i]-r)/q;
    }
}

