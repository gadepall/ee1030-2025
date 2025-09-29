// section_point.c
#include <stdio.h>

// Function to compute section formula
void section_point(double ax, double ay, double bx, double by, int m, int n, double *px, double *py) {
    *px = (m*bx + n*ax) / (double)(m+n);
    *py = (m*by + n*ay) / (double)(m+n);
}
