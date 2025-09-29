#include <stdio.h>

int find_intersection(double *x, double *y) {
    double a1 = 1, b1 = 2, c1 = 10;
    double a2 = 2, b2 = 1, c2 = -5;

    double det = a1*b2 - a2*b1;
    if(det == 0) return 0; // parallel

    *x = (c1*b2 - c2*b1) / det;
    *y = (a1*c2 - a2*c1) / det;

    if(5*(*x) + 4*(*y) == 0)
        return 1; // passes
    else
        return 2; // does not pass
}
