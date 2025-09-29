#include <stdio.h>

int main() {
    // Point through which the line passes
    double x0 = 5, y0 = 2, z0 = -4;
    // Direction vector
    double a = 3, b = 2, c = -8;

    printf("The vector equation of the line is:\n");
    printf("r = (%.1f, %.1f, %.1f) + t(%.1f, %.1f, %.1f)\n", x0, y0, z0, a, b, c);

    printf("\nParametric form:\n");
    printf("x = %.1f + %.1f t\n", x0, a);
    printf("y = %.1f + %.1f t\n", y0, b);
    printf("z = %.1f + %.1f t\n", z0, c);

    return 0;
}