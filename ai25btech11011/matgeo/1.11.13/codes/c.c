#include <math.h>

double degree(int n){
    double d = (n * M_PI) / 180;
    return d;
}

void find_direction_cosines(int alpha_deg, int beta_deg, int gamma_deg, double *l, double *m, double *n) {
    *l = cos(degree(alpha_deg));
    *m = cos(degree(beta_deg));
    *n = cos(degree(gamma_deg));
}

