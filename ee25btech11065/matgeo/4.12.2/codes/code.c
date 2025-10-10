#include<stdio.h>
double solve_for_k(void) {
    double a1 = 3.0;
    double b1 = 1.0;
    double c1 = 1.0;

    double a2_k_coeff = 2.0;
    double a2_const = -1.0;

    double b2_k_coeff = 1.0;
    double b2_const = -1.0;

    double c2_k_coeff = 2.0;
    double c2_const = 1.0;

    double k_coeff_det = a1 * b2_k_coeff - b1 * a2_k_coeff;
    double const_det = a1 * b2_const - b1 * a2_const;

    double k = -const_det / k_coeff_det;

    return k;
}

