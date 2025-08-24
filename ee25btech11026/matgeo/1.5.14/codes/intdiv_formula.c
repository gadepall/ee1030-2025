// section_formula.c
#include <stdio.h>

void find_section_point(double x1, double y1, double x2, double y2, double m, double n, double* x, double* y) {
    *x = (m * x2 + n * x1) / (m + n);
    *y = (m * y2 + n * y1) / (m + n);
}


