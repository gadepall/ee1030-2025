#include <stdio.h>
#include <math.h>

void find_magnitude(double *x, double *x_norm) {
    double p[2] = {1.0, 0.0};
    double given_value = 80.0;


    double p_norm_sq = p[0]*p[0] + p[1]*p[1];


    double x_norm_sq = given_value + p_norm_sq;
    *x_norm = sqrt(x_norm_sq);

    x[0] = *x_norm;
    x[1] = 0.0;
}
