#include <stdio.h>

int main(void) {
    double Ax = 2.0, Ay = 3.0;
    printf("A = (%.1f, %.1f)\n\n", Ax, Ay);

    double a1 = 0.0, b1 = 1.0, rhs1 = 3.0;
    printf("Case 1 (parallel to x-axis):\n");
    printf("[%.0f %.0f] · x = %.0f\n\n", a1, b1, rhs1);

    double a2 = 1.0, b2 = 0.0, rhs2 = 2.0;
    printf("Case 2 (parallel to y-axis):\n");
    printf("[%.0f %.0f] · x = %.0f\n\n", a2, b2, rhs2);

    double a = 4.0, b = -1.0;
    double rhs = Ax * a + Ay * b;
    printf("General case (a=%.0f, b=%.0f):\n", a, b);
    printf("[%.0f %.0f] · x = %.0f\n", a, b, rhs);

    return 0;
}
