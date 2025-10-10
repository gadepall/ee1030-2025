#include <stdio.h>

// Function to compute perpendicular line coefficients
// Original line: ax + by + c = 0
// Perpendicular line through (x0, y0): A*x + B*y + C = 0
void perpendicularLine(int a, int b, int c, int x0, int y0, int *A, int *B, int *C) {
    *A = b;
    *B = -a;
    *C = -((*A) * x0 + (*B) * y0);
}