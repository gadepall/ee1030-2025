// main.c
#include <stdio.h>
#include <math.h>

// Function to generate points for parabola y^2 = -8x
// Arrays x[] and y[] will be filled, up to n points
// Returns number of points actually filled
int generate_points(double x[], double y[], int n) {
    double xmin = -10.0;  // start of x range
    double xmax = 0.0;    // parabola is defined for x <= 0
    double step = (xmax - xmin) / (n/2); // half because we store ±y

    int idx = 0;
    for (int i = 0; i <= n/2 && idx < n-1; i++) {
        double xval = xmin + i * step;
        double yval = sqrt(-8.0 * xval);

        x[idx] = xval;
        y[idx] = yval;
        idx++;

        x[idx] = xval;
        y[idx] = -yval;
        idx++;
    }

    return idx;
}
