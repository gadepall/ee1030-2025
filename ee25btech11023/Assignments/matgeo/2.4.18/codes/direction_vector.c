// vector_calculator.c
// Library version of the vector calculation code.

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

void calculate_vectors(double* m1_out, double* m2_out) {
    double p;

    // These definitions are taken directly from your C code
    double m1_p_coeffs[3] = {0.0, 2.0/7.0, 0.0};
    double m1_consts[3] = {-3.0, 0.0, 2.0};
    double m2_p_coeffs[3] = {-3.0/7.0, 0.0, 0.0};
    double m2_consts[3] = {0.0, 1.0, -5.0};
    
    // Calculate A (the total coefficient for 'p') from the dot product expansion.
    double p_coefficient = (m1_consts[0] * m2_p_coeffs[0]) + (m1_p_coeffs[0] * m2_consts[0]) +
                         (m1_consts[1] * m2_p_coeffs[1]) + (m1_p_coeffs[1] * m2_consts[1]) +
                         (m1_consts[2] * m2_p_coeffs[2]) + (m1_p_coeffs[2] * m2_consts[2]);

    // Calculate B (the total constant term) from the dot product expansion.
    double constant_term = (m1_consts[0] * m2_consts[0]) +
                         (m1_consts[1] * m2_consts[1]) +
                         (m1_consts[2] * m2_consts[2]);

    p = -constant_term / p_coefficient;

    // Write results to the output arrays passed by reference from Python
    m1_out[0] = m1_consts[0] + m1_p_coeffs[0] * p;
    m1_out[1] = m1_consts[1] + m1_p_coeffs[1] * p;
    m1_out[2] = m1_consts[2] + m1_p_coeffs[2] * p;

    m2_out[0] = m2_consts[0] + m2_p_coeffs[0] * p;
    m2_out[1] = m2_consts[1] + m2_p_coeffs[1] * p;
    m2_out[2] = m2_consts[2] + m2_p_coeffs[2] * p;
}