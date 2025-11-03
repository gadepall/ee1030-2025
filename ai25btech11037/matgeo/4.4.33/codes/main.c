#include <stdio.h>

// Function to calculate the scalar triple product condition for coplanarity
double scalar_triple_product_condition(double x) {
    // Components of vectors AB, AC, AD based on x
    // A = (3, 2, 1)
    // B = (4, x, 5)
    // C = (4, 2, -2)
    // D = (6, 5, -1)

    // AB = B - A = (1, x-2, 4)
    double AB_x = 1;
    double AB_y = x - 2;
    double AB_z = 4;

    // AC = C - A = (1, 0, -3)
    double AC_x = 1;
    double AC_y = 0;
    double AC_z = -3;

    // AD = D - A = (3, 3, -2)
    double AD_x = 3;
    double AD_y = 3;
    double AD_z = -2;

    // Cross product AC x AD
    double cross_x = AC_y * AD_z - AC_z * AD_y; // 0*(-2) - (-3)*3 = 9
    double cross_y = AC_z * AD_x - AC_x * AD_z; // (-3)*3 - 1*(-2) = -7
    double cross_z = AC_x * AD_y - AC_y * AD_x; // 1*3 - 0*3 = 3

    // Dot product AB . (AC x AD)
    double scalar_triple = AB_x * cross_x + AB_y * cross_y + AB_z * cross_z;

    return scalar_triple;
}

int main() {
    // From the math, we have linear equation 35 - 7x = 0 => x = 5
    // But let's also verify numerically:

    double x = 5.0;
    double result = scalar_triple_product_condition(x);

    printf("Value of x for coplanarity: %.2f\n", x);
    printf("Scalar triple product at x=%.2f: %.2f (should be close to 0)\n", x, result);

    return 0;
}
