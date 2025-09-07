#include <stdio.h>

void find_point(double *px, double *py) {
    // A(-6,10), B(3,-8)
    double x1 = -6, y1 = 10, x2 = 3, y2 = -8;
    int m = 2, n = 7; // ratio

    *px = (m*x2 + n*x1) / (m+n);
    *py = (m*y2 + n*y1) / (m+n);
}
