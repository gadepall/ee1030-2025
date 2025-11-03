// linear.c
#include <stdio.h>

// Function to solve system of 2 equations:
// a1*x + b1*y = c1
// a2*x + b2*y = c2
// Returns solution in x_out and y_out
void solve_linear(float a1, float b1, float c1,
                  float a2, float b2, float c2,
                  float *x_out, float *y_out) {
    float det = a1*b2 - a2*b1;
    if (det == 0) {
        *x_out = 0;
        *y_out = 0;
        return;
    }
    *x_out = (c1*b2 - c2*b1) / det;
    *y_out = (a1*c2 - a2*c1) / det;
}
