#include <math.h>
#include "matfun.h"

#define MEDIAN_COEFF 3.0

double compute_cos_theta(void) {
    return cos(2.0 * M_PI / 3.0);
}

double compute_coefficient_sq(void) {
    double cos_theta = compute_cos_theta();
    double diff = cos_theta - 1.0;
    return diff * diff;
}

double compute_r_squared_coeff(void) {
    double num = MEDIAN_COEFF * MEDIAN_COEFF;            // 3² = 9
    double denom = compute_coefficient_sq();             // (cosθ-1)² = 9/4
    return num / denom;                                  // 9 / (9/4) = 4
}
