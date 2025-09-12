#include <stdio.h>
#include <stdlib.h>
#include <math.h>   // for fabs()

int main() {
    FILE *fp;
    double area;

    // Compute area = ∫ from -2 to 1 |3x+2| dx
    // Split into two parts: [-2, -2/3] and [-2/3, 1]

    double x0 = -2.0/3.0;

    // Antiderivative F(x) = (3/2)x^2 + 2x
    double F_at_x0 = (1.5 * x0 * x0) + (2.0 * x0);
    double F_at_neg2 = (1.5 * (-2) * (-2)) + (2.0 * (-2));
    double F_at_1 = (1.5 * 1 * 1) + (2.0 * 1);

    // Left interval [-2, -2/3] -> integrand is negative
    double left = -(F_at_x0 - F_at_neg2);

    // Right interval [-2/3, 1] -> integrand is positive
    double right = (F_at_1 - F_at_x0);

    area = left + right; // total geometric area

    // Open file area.dat
    fp = fopen("area.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write output
    fprintf(fp, "Line equation in matrix form: [3  -1] [x y]^T = -2\n");
    fprintf(fp, "Area of the region = %.6f (exact = 41/6)\n", area);

    fclose(fp);

    printf("Area successfully written to area.dat\n");
    return 0;
}

