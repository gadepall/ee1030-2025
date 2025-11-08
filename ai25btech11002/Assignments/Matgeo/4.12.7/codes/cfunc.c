#include <stdio.h>
#include <math.h>

void polar_to_cartesian(double r, double theta_deg, double *x, double *y) {
    double theta_rad = theta_deg * M_PI / 180.0;  // convert to radians
    *x = r * cos(theta_rad);
    *y = r * sin(theta_rad);
}
