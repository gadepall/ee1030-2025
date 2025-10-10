#include <stdio.h>

int main(void) {
    /* Given point A and direction d */
    double A_x =  2.0, A_y = -1.0, A_z =  4.0;
    double d_x =  1.0, d_y =  1.0, d_z = -2.0;

    /* Print the vector equation (symbolically) */
    printf("Vector equation of the line:\n");
    printf("  r = A + lambda * d\n");
    printf("  A = (%.1f, %.1f, %.1f)\n", A_x, A_y, A_z);
    printf("  d = (%.1f, %.1f, %.1f)\n\n", d_x, d_y, d_z);

    /* Print the explicit parametric form */
    printf("Parametric form (components):\n");
    printf("  x = %.1f + lambda * %.1f  -> x = 2 + lambda\n", A_x, d_x);
    printf("  y = %.1f + lambda * %.1f  -> y = -1 + lambda\n", A_y, d_y);
    printf("  z = %.1f + lambda * %.1f  -> z = 4 - 2*lambda\n\n", A_z, d_z);

    /* Print the symmetric form */
    printf("Symmetric form (if denominators non-zero):\n");
    printf("  (x - 2)/1 = (y + 1)/1 = (z - 4)/(-2)\n\n");

    /* Read a lambda value from the user and compute the point on the line */
    double lambda;
    printf("Enter a value for lambda (e.g. 0, 1, -1, 2.5): ");
    if (scanf("%lf", &lambda) != 1) {
        fprintf(stderr, "Invalid input. Exiting.\n");
        return 1;
    }

    double x = A_x + lambda * d_x;
    double y = A_y + lambda * d_y;
    double z = A_z + lambda * d_z;

    printf("\nFor lambda = %.4g:\n", lambda);
    printf("  Point on line: (x, y, z) = (%.6g, %.6g, %.6g)\n", x, y, z);

    /* Optionally, show a few sample lambda values */
    double samples[] = {-2.0, -1.0, 0.0, 1.0, 2.0};
    int n = sizeof(samples) / sizeof(samples[0]);
    printf("\nSample points on the line:\n");
    for (int i = 0; i < n; ++i) {
        double t = samples[i];
        double xs = A_x + t * d_x;
        double ys = A_y + t * d_y;
        double zs = A_z + t * d_z;
        printf("  lambda = %5.2g -> (%.6g, %.6g, %.6g)\n", t, xs, ys, zs);
    }

    return 0;
}


