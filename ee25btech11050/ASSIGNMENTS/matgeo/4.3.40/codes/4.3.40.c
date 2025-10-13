#include <stdio.h>

void line_point(double lambda, double result[3]) {
    // Point vector a
    double a[3] = {2.0, -1.0, 4.0};
    // Direction vector d
    double d[3] = {1.0, 2.0, -1.0};

    for (int i = 0; i < 3; i++) {
        result[i] = a[i] + lambda * d[i];
    }
}

