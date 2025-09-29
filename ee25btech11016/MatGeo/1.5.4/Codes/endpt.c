#include <stdio.h>

void other_end(double cx, double cy, double x1, double y1, double *x2, double *y2) {
    *x2 = 2*cx - x1;
    *y2 = 2*cy - y1;
}
