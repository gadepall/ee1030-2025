#include <stdio.h>
#include <math.h>
void ellipse(double *theta, double *x, double *y, int n, double a, double b) {
    for (int i = 0; i < n; i++) {
        x[i] = b * cos(theta[i]);   // x = b cos θ
        y[i] = a * sin(theta[i]);   // y = a sin θ
    }
}
