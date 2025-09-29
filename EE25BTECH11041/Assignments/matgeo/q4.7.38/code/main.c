#include <stdio.h>

// Function to calculate midpoint
void midpoint(double x1, double y1, double x2, double y2, double *mx, double *my) {
    *mx = (x1 + x2) / 2.0;
    *my = (y1 + y2) / 2.0;
}

