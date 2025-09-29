#include <stdio.h>
int main() {
    // Given: line passes through A(-3, 0) and B(0, 2)
    float A[2] = {-3.0, 0.0};
    float B[2] = {0.0, 2.0};

    // We want to find normal vector n = (a, b) such that:
    // n^T * A = 1  => a*(-3) + b*0 = 1 => -3a = 1 => a = -1/3
    // n^T * B = 1  => a*0 + b*2 = 1  => 2b = 1 => b = 1/2

    float a = -1.0 / 3.0;
    float b = 1.0 / 2.0;

    printf("Given Points:\n");
    printf("A = (%.1f, %.1f)\n", A[0], A[1]);
    printf("B = (%.1f, %.1f)\n\n", B[0], B[1]);

    printf("Normal Vector n = (a, b) = (%.2f, %.2f)\n", a, b);

    // Equation of line in dot product form: a*x + b*y = 1
    printf("\nEquation of line in dot product form:\n");
    printf("%.2fx + %.2fy = 1\n", a, b);

    // Convert to standard form: Multiply both sides by LCM(3,2) = 6
    // Original: -x/3 + y/2 = 1
    // Multiply by 6: -2x + 3y = 6  --> Standard form: 2x - 3y + 6 = 0

    int A_coeff = 2;
    int B_coeff = -3;
    int C_coeff = 6;

    printf("\nEquation of line in standard form:\n");
    printf("%dx ", A_coeff);
    if (B_coeff < 0)
        printf("- %dy ", -B_coeff);
    else
        printf("+ %dy ", B_coeff);

    if (C_coeff < 0)
        printf("- %d = 0\n", -C_coeff);
    else
        printf("+ %d = 0\n", C_coeff);

    return 0;
}
