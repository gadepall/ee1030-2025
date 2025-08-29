#include <stdio.h>

// Function to find coordinates of P dividing AB in ratio m:n
void divide_point(float x1, float y1, float x2, float y2, float m, float n, float *out) {
    out[0] = (m*x2 + n*x1) / (m + n);  // x-coordinate of P
    out[1] = (m*y2 + n*y1) / (m + n);  // y-coordinate of P
}
