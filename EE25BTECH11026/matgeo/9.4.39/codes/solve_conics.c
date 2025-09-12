#include <stdio.h>
#include <math.h>

void solve_conics(double *results) {
    // Quadratic in x: x^2 - 8x - 180 = 0
    double a = 1, b = -8, c = -180;
    double disc = b*b - 4*a*c;

    if (disc < 0) {
        // No real solution
        results[0] = results[1] = results[2] = results[3] = NAN;
        return;
    }

    // Roots of quadratic
    double sqrt_disc = sqrt(disc);
    double x1 = (-b + sqrt_disc) / (2*a);
    double x2 = (-b - sqrt_disc) / (2*a);

    // Solutions
    int idx = 0;
    double xs[2] = {x1, x2};
    for (int i=0; i<2; i++) {
        double x = xs[i];
        if (x < 0) continue; // y^2 = 8x requires x >= 0
        double y2 = 8*x;
        double y = sqrt(y2);
        results[idx++] = x;
        results[idx++] = y;
        results[idx++] = x;
        results[idx++] = -y;
    }

    // If fewer than 4 values filled, pad with NAN
    while (idx < 4) {
        results[idx++] = NAN;
    }
}

