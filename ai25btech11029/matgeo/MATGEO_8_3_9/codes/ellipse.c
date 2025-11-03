#include <math.h>
#include "ellipse.h"

void generate_ellipse(double a, double b, int n, double* x, double* y) {
    for (int i = 0; i < n; ++i) {
        double theta = 2.0 * M_PI * i / n;
        x[i] = a * cos(theta);
        y[i] = b * sin(theta);
    }
}

