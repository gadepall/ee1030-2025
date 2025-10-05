#include <stdio.h>

void get_roots(double *root1, double *root2) {
    double a = 3.0;
    double b = -24.0;
    double c = -3840.0;
    double D = b*b - 4*a*c;
    if (D < 0) {
        *root1 = 0.0;
        *root2 = 0.0;
    } else {
        double sqrtD = sqrt(D);
        *root1 = (-b + sqrtD) / (2*a);
        *root2 = (-b - sqrtD) / (2*a);
    }
}

