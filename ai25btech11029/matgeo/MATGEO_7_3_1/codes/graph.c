#include "graph.h"
#include <math.h>

static double a = 0.0;
static double b = 0.0;

void set_params(double a_val, double b_val) {
    a = a_val;
    b = b_val;
}

void compute_circle(double theta, double* x, double* y) {
    double cx = a / 2.0;
    double cy = b / 2.0;
    double r = sqrt(a * a + b * b) / 2.0;

    *x = cx + r * cos(theta);
    *y = cy + r * sin(theta);
}

