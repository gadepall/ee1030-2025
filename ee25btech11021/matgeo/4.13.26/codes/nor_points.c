#include <stdio.h>
#include <stdlib.h>

// Line passing through (2,3) with slope m
void generate_line_points(double m, double* P, double* Q) {
    // X-intercept (y=0)
    double x_intercept = 2.0 - 3.0 / m;
    // Y-intercept (x=0)
    double y_intercept = 3.0 - 2.0 * m;

    P[0] = x_intercept; P[1] = 0.0;
    Q[0] = 0.0; Q[1] = y_intercept;
}

