#include <stdio.h>

int main() {
    FILE *fp;
    float a, b;
    float X1, X2, Y1, Y2, Z1, Z2;
    int k = 2;  // Ratio 2:1 (external division)

    // Input a and b
    printf("Enter values of a and b: ");
    scanf("%f %f", &a, &b);

    // Position vectors
    X1 = 3 * a;
    X2 = b;
    Y1 = a;
    Y2 = -3 * b;

    // External division formula: Z = (kY - X) / (k - 1)
    Z1 = (k * Y1 - X1) / (k - 1);
    Z2 = (k * Y2 - X2) / (k - 1);

    // Open file to write output
    fp = fopen("solution.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write result to file
    fprintf(fp, "External Division of XY in ratio 2:1\n");
    fprintf(fp, "Given:\n");
    fprintf(fp, "X = (3a, b)\nY = (a, -3b)\n");
    fprintf(fp, "Computed position vector of Z:\n");
    fprintf(fp, "Z = (%.2fa, %.2fb)\n", Z1/a, Z2/b); // symbolic form
    fprintf(fp, "Or numerically: (%.2f, %.2f)\n", Z1, Z2);

    fclose(fp);

    printf(" Output written to 'solution.dat'\n");
    return 0;
}

