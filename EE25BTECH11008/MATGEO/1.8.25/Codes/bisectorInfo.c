#include <stdio.h>

// Function: computes perpendicular bisector coefficients (ax + by + c = 0)
void perpendicular_bisector(double x1, double y1, double x2, double y2,
                            double *a, double *b, double *c) {
    double mx = (x1 + x2) / 2.0;
    double my = (y1 + y2) / 2.0;

    double dx = x2 - x1;
    double dy = y2 - y1;

    *a = dx;
    *b = dy;
    *c = -((*a) * mx + (*b) * my);
}
