#include<stdio.h>

void line_point(double lambda, double *out) {
    // Line: r = A + lambda*d
    double A[3] = {3.0, 4.0, 5.0};
    double d[3] = {2.0, 1.0, -3.0};

    for(int i=0; i<3; i++) {
        out[i] = A[i] + lambda * d[i];
    }
}
