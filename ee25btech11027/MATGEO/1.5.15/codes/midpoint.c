#include <stdio.h>

// Function to calculate midpoint
void midpoint(float x1, float y1, float x2, float y2, float *mx, float *my) {
    *mx = (x1 + x2) / 2.0;
    *my = (y1 + y2) / 2.0;
}
