#include <stdio.h>
#include <math.h>

#define N 400  // Number of points for the ellipse

// Function to generate ellipse coordinates
void ellipse_points(double *x_vals, double *y_upper, double *y_lower, double a, double b) {
    double step = (2 * a) / (N - 1);  // Step size between x-values

    for (int i = 0; i < N; i++) {
        x_vals[i] = -a + i * step;  // X values range from -a to +a
        double value = 1.0 - (x_vals[i] * x_vals[i]) / (a * a);

        if (value < 0)
            value = 0;  // Avoid sqrt of small negative rounding errors

        y_upper[i] = b * sqrt(value);   // Upper half of ellipse
        y_lower[i] = -y_upper[i];       // Lower half (mirror)
    }
}

// Main function callable from Python
void generate_ellipse(double *x_vals, double *y_upper, double *y_lower) {
    double a = 6.0;             // Semi-major axis (x-axis)
    double c = 4.0;             // Distance to focus
    double b = sqrt(a * a - c * c);  // Semi-minor axis (y-axis)

    ellipse_points(x_vals, y_upper, y_lower, a, b);
}

