#include <stdio.h>

// Compute (x, y) for system:
// ax + by = c
// bx + ay = 1 + c

void solve_system(double a, double b, double c, double *x, double *y) {
    double denom = a*a - b*b;
    *x = (a*c - b*(1.0 + c)) / denom;
    *y = (-b*c + a*(1.0 + c)) / denom;
}

// Fills arrays with points on the line for fixed a, b, c, and range of x values
void generate_points(double a, double b, double c, double *xs, double *ys, int n) {
    double x_min = -5.0, x_max = 5.0;
    for(int i=0; i<n; ++i) {
        xs[i] = x_min + (x_max - x_min)*i/(n-1);
        ys[i] = (c - a*xs[i]) / b;
    }
}

