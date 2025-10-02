
#include <stdio.h>
#include <math.h>

// Solve quadratic ax^2 + bx + c = 0
void solve_quadratic(double a, double b, double c, double *r1, double *r2) {
    double d = b*b - 4*a*c;
    if (d < 0) {
        *r1 = NAN;
        *r2 = NAN;
        return;
    }
    *r1 = (-b + sqrt(d)) / (2*a);
    *r2 = (-b - sqrt(d)) / (2*a);
}

// Compute slopes and constants for required lines
void get_line_params(double *a1, double *a2, double *c1, double *c2) {
    double A = 1.0, B = 25.0/12.0, C = 1.0;
    double r1, r2;
    solve_quadratic(A, B, C, &r1, &r2);

    a1[0] = r1;
    a2[0] = r2;

    // Constants c = 2a + 3, intersection point fixed at (2,3)
    c1[0] = 2*r1 + 3;
    c2[0] = 2*r2 + 3;
}

