#include <stdio.h>


void midpt(double x1, double y1, double x2, double y2, double* x, double* y) {
    *x = (x2 + x1) / (2);
    *y = (y2 + y1) / (2);
}