#include <math.h>

void solve_quadratic(double a, double b, double c, double *r1, double *r2) {
    double d = b*b - 4*a*c;

    if (d >= 0) {
        *r1 = (-b + sqrt(d)) / (2*a);
        *r2 = (-b - sqrt(d)) / (2*a);
    } else {
        *r1 = *r2 = -b / (2*a);  // only real part returned
    }
}

