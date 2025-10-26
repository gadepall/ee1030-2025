#include <math.h>

#ifndef M_PI
#define M_PI 3.14159265358
#endif


void generate_ellipse(double a, double b, int n_points, double* x_out, double* y_out) {
    double dt = 2.0 * M_PI / (n_points - 1);
    for (int i = 0; i < n_points; ++i) {
        double t = i * dt;
        x_out[i] = a * cos(t);
        y_out[i] = b * sin(t);
    }
}

void generate_circle(double r, int n_points, double* x_out, double* y_out) {
    double dt = 2.0 * M_PI / (n_points - 1);
    for (int i = 0; i < n_points; ++i) {
        double t = i * dt;
        x_out[i] = r * cos(t);
        y_out[i] = r * sin(t);
    }
}

void generate_line(double m, double c, double x_min, double x_max, int n_points, double* x_out, double* y_out) {
    double dx = (x_max - x_min) / (n_points - 1);
    for (int i = 0; i < n_points; ++i) {
        double x = x_min + i * dx;
        x_out[i] = x;
        y_out[i] = m * x + c;
    }
}
