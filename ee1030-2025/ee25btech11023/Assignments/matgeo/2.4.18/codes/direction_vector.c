#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main() {

    double p;
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

    double m1_final[3];
    double m2_final[3];

    m1_final[0] = m1_consts[0] + m1_p_coeffs[0] * p;
    m1_final[1] = m1_consts[1] + m1_p_coeffs[1] * p;
    m1_final[2] = m1_consts[2] + m1_p_coeffs[2] * p;

    m2_final[0] = m2_consts[0] + m2_p_coeffs[0] * p;
    m2_final[1] = m2_consts[1] + m2_p_coeffs[1] * p;
    m2_final[2] = m2_consts[2] + m2_p_coeffs[2] * p;


    FILE *file = fopen("values.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(file, "%.4f %.4f %.4f\n", m1_final[0], m1_final[1], m1_final[2]);
    fprintf(file, "%.4f %.4f %.4f\n", m2_final[0], m2_final[1], m2_final[2]);

    fclose(file);
    printf("Direction vectors calculated and written to values.dat\n");
    printf("(The calculated value of p was: %.4f)\n", p);

    return 0;
}
