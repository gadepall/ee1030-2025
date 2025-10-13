#include <stdio.h>

#define N 100

// Function must be exactly named `generate_line`
void generate_line(double *x, double *y, int n) {
    for (int i = 0; i < n; i++) {
        x[i] = i;        // x values
        y[i] = x[i] + 26; // y = x + 26
    }
}

// Optional: function for conic points
void generate_conic(double *x, double *y, int n) {
    for (int i = 0; i < n; i++) {
        x[i] = i + 0.1;      // avoid division by zero
        y[i] = 360.0 / (x[i] + 3.0) - 3.0;
    }
}

