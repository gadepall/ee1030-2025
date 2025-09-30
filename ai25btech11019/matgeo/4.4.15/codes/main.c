#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Plane equation: -r · (2,1,-1) - 5 = 0
    // Equivalent: 2x + y - z + 5 = 0

    // X-intercept (x, 0, 0)
    double x = -5.0 / 2.0;

    // Y-intercept (0, y, 0)
    double y = -5.0;

    // Z-intercept (0, 0, z)
    double z = 5.0;

    // Sum of intercepts
    double sum = x + y + z;

    // Print results to screen
    printf("Plane equation: 2x + y - z + 5 = 0\n\n");

    printf("X-intercept: (%.2f, 0, 0)\n", x);
    printf("Y-intercept: (0, %.2f, 0)\n", y);
    printf("Z-intercept: (0, 0, %.2f)\n\n", z);

    printf("Intercepts: x = %.2f, y = %.2f, z = %.2f\n", x, y, z);
    printf("Sum of intercepts = %.2f\n\n", sum);

    printf("Conclusion: The sum of the intercepts cut off by the plane is %.2f\n", sum);

    // Write results into a file
    FILE *file;
    file = fopen("values.dat", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(file, "X\tY\tZ\tSum\n");
    fprintf(file, "%.2f\t%.2f\t%.2f\t%.2f\n", x, y, z, sum);

    fclose(file);
    printf("Results have been written to values.dat\n");

    return 0;
}

