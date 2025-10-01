#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Plane equation: ax + by + cz + d = 0
    double a = 2.0, b = 1.0, c = -1.0, d = 5.0;

    // Intercepts on axes
    double x_intercept = -d / a;
    double y_intercept = -d / b;
    double z_intercept = -d / c;

    // Scalar sum of intercepts
    double sum_intercepts = x_intercept + y_intercept + z_intercept;

    // Print results to screen
    printf("Given plane equation: %.0lfx + %.0lfy + %.0lfz + %.0lf = 0\n\n", a, b, c, d);

    printf("Intercepts on the coordinate axes:\n");
    printf("x-intercept = -d/a = -%.0lf/%.0lf = %.2lf\n", d, a, x_intercept);
    printf("y-intercept = -d/b = -%.0lf/%.0lf = %.2lf\n", d, b, y_intercept);
    printf("z-intercept = -d/c = -%.0lf/%.0lf = %.2lf\n\n", d, c, z_intercept);

    printf("Sum of intercepts = x + y + z\n");
    printf("= %.2lf + %.2lf + %.2lf\n", x_intercept, y_intercept, z_intercept);
    printf("= %.2lf\n\n", sum_intercepts);

    printf("Conclusion: The sum of the intercepts cut off by the plane is %.2lf\n", sum_intercepts);

    // Write results into a file (values.dat)
    FILE *file;
    file = fopen("values.dat", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(file, "a\tb\tc\td\tx_int\ty_int\tz_int\tsum\n");
    fprintf(file, "%.0lf\t%.0lf\t%.0lf\t%.0lf\t%.2lf\t%.2lf\t%.2lf\t%.2lf\n",
            a, b, c, d, x_intercept, y_intercept, z_intercept, sum_intercepts);

    fclose(file);
    printf("Results have been written to values.dat\n");

    return 0;
}

