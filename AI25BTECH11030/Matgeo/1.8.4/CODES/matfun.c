#include <math.h>
#include "matfun.h"

void mat_scalar_mul(const double in[3], double scalar, double out[3]) {
    for (int i=0; i<3; i++) {
        out[i] = in[i] * scalar;
    }
}

void mat_subtract(const double a[3], const double b[3], double out[3]) {
    for (int i=0; i<3; i++) {
        out[i] = a[i] - b[i];
    }
}

double mat_norm(const double v[3]) {
    return sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
}

void solve_y_coordinate(const double P[3], double distance, double roots[2]) {
    double base = distance*distance - P[0]*P[0] - P[2]*P[2];
    if (base < 0) {
        roots[0] = roots[1] = NAN;
        return;
    }
    double sqrt_base = sqrt(base);
    roots[0] = P[1] + sqrt_base;
    roots[1] = P[1] - sqrt_base;
}
