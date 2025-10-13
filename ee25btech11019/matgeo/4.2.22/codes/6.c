/* parallel_funcs.c */
#include <stdio.h>
#include <math.h>

#define EPS 1e-9

// Return 1 if lines are parallel (a1*b2 - a2*b1 approx 0), else 0
int is_parallel(double a1, double b1, double a2, double b2) {
    double det = a1*b2 - a2*b1;
    if (fabs(det) < EPS) return 1;
    return 0;
}

// Evaluate line a*x + b*y + c = 0 for an array of x values.
// x_in and y_out are arrays of length n. Assumes b != 0.
void eval_line(double a, double b, double c, double *x_in, double *y_out, int n) {
    for (int i = 0; i < n; ++i) {
        y_out[i] = (-a * x_in[i] - c) / b;
    }
}
