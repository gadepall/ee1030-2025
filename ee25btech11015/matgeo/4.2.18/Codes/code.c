#include <stdio.h>

// Function to compute direction and normal vectors for a line y = x - 2
// General form: x - y - 2 = 0
// Normal vector = (a, b) = (1, -1)
// Direction vector = (b, -a) = (-1, -1)

void line_vectors(float *dx, float *dy, float *nx, float *ny) {
    float a = 1, b = -1;   // coefficients of x - y - 2 = 0

    // Normal vector
    *nx = a;
    *ny = b;

    // Direction vector
    *dx = b;
    *dy = -a;
}
