#include <stdio.h>
#include <math.h>

void hyperbola_params(double theta, double *arr) {
    double a = sin(theta);   // transverse semi-axis
    double b = cos(theta);   // conjugate semi-axis
    arr[0] = a * a;          // a^2
    arr[1] = b * b;          // b^2
}

