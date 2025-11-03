#include <stdio.h>
#include <math.h>

int main() {
    // Fixed point coordinates
    double a_x = 3.0;
    double a_y = -2.0;

    // Line coefficients (Ax + By + C = 0)
    double line_A = 5.0;
    double line_B = -12.0;
    double line_C = -3.0;

    // The constant multiplier from the denominator of the distance formula
    // This is sqrt(A^2 + B^2)
    double constant_mult = sqrt(line_A * line_A + line_B * line_B);

    // Case 1: Positive side of the line
    // Equation: constant_mult * ((x - a_x)^2 + (y - a_y)^2) = line_A*x + line_B*y + line_C
    double coeff_x1 = -2 * a_x * constant_mult - line_A;
    double coeff_y1 = -2 * a_y * constant_mult - line_B;
    double const_term1 = constant_mult * (a_x * a_x + a_y * a_y) - line_C;

    // Case 2: Negative side of the line
    // Equation: constant_mult * ((x - a_x)^2 + (y - a_y)^2) = -(line_A*x + line_B*y + line_C)
    double coeff_x2 = -2 * a_x * constant_mult + line_A;
    double coeff_y2 = -2 * a_y * constant_mult + line_B;
    double const_term2 = constant_mult * (a_x * a_x + a_y * a_y) + line_C;

    // Print the general form of the equations and the computed coefficients
    printf("The locus of the point is a pair of circles with the general equation:\n");
    printf("13x^2 + 13y^2 + (coeff_x)x + (coeff_y)y + (const_term) = 0\n\n");
    
    printf("Equation for Case 1:\n");
    printf("13x^2 + 13y^2 + %.0fx + %.0fy + %.0f = 0\n\n", coeff_x1, coeff_y1, const_term1);

    printf("Equation for Case 2:\n");
    printf("13x^2 + 13y^2 + %.0fx + %.0fy + %.0f = 0\n", coeff_x2, coeff_y2, const_term2);

    return 0;
}
