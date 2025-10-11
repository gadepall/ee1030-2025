#include <math.h>
#include "matfun.h"

void compute_eigenvalues(double tr, double det, double* lambda1, double* lambda2) {
    double sum = tr;
    double prod = det;
    double disc = sqrt(sum * sum - 4 * prod);
    *lambda1 = (sum + disc) / 2.0;
    *lambda2 = (sum - disc) / 2.0;
}

double characteristic_b(double lambda1, double lambda2) {
    return (lambda1 + lambda2 + 2) / ((lambda1 + 1) * (lambda2 + 1));
}

double characteristic_c(double lambda1, double lambda2) {
    return 1.0 / ((lambda1 + 1) * (lambda2 + 1));
}

double ratio_b_c(double b, double c) {
    return b / c;
}
