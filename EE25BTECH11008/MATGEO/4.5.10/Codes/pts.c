#include <stdio.h>

void line_point(double kappa, double h[3], double m[3], double out[3]) {
    out[0] = h[0] + kappa * m[0];
    out[1] = h[1] + kappa * m[1];
    out[2] = h[2] + kappa * m[2];
}
