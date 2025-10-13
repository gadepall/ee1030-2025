// parabola.c
// Compile: gcc -shared -o parabola.so -fPIC parabola.c -lm

#include <math.h>

// Parabola equation: y^2 = 4x
void parabola_points(double *y_vals, double *x_vals, int n) {
    for (int i = 0; i < n; i++) {
        x_vals[i] = (y_vals[i] * y_vals[i]) / 4.0;
    }
}

// Normal line from point (x0, y0) with slope m
void normal_line(double x0, double y0, double m, double *t_vals, double *x_vals, double *y_vals, int n) {
    for (int i = 0; i < n; i++) {
        x_vals[i] = x0 + t_vals[i];
        y_vals[i] = y0 + m * t_vals[i];
    }
}

// Circle equation: (x-h)^2 + (y-k)^2 = r^2
void circle_points(double h, double k, double r, double *theta, double *x_vals, double *y_vals, int n) {
    for (int i = 0; i < n; i++) {
        x_vals[i] = h + r * cos(theta[i]);
        y_vals[i] = k + r * sin(theta[i]);
    }
}