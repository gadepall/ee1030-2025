#include <stdio.h>

int main() {
    // Point on line
    int x0 = 2, y0 = -1, z0 = 4;
    // Direction vector
    int a = 1, b = 1, c = -2;

    printf("Equation of the line passing through (2, -1, 4)\n");
    printf("and parallel to vector (1, 1, -2):\n\n");

    // Vector form
    printf("Vector form:\n");
    printf("r = (2, -1, 4) + t(1, 1, -2)\n\n");

    // Parametric form
    printf("Parametric form:\n");
    printf("x = %d + t\n", x0);
    printf("y = %d + t\n", y0);
    printf("z = %d - 2t\n\n");

    // Symmetric form
    printf("Symmetric form:\n");
    printf("(x - %d)/%d = (y - %d)/%d = (z - %d)/%d\n",
           x0, a, y0, b, z0, c);

    return 0;
}

