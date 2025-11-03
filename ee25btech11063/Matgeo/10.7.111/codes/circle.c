#include <stdio.h>
#include <math.h>

int main() {
    FILE *fp;
    double a, r;
    double A1x, A1y, B1x, B1y;

    // Given relation: a + r = 5 + sqrt(5)
    // and r = a / sqrt(5)
    // So we solve for a and r
    a = 5;
    r = sqrt(5);

    // Coordinates of A1 (point of tangency)
    A1x = 2;
    A1y = 4;

    // Coordinates of B1 (diametrically opposite point)
    B1x = -2;
    B1y = 6;

    // Open file to write output
    fp = fopen("circle.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(fp, "Results of the circle problem:\n");
    fprintf(fp, "--------------------------------\n");
    fprintf(fp, "(A) a = %.2f\n", a);
    fprintf(fp, "(B) r = %.5f\n", r);
    fprintf(fp, "(C) A1 = (%.2f, %.2f)\n", A1x, A1y);
    fprintf(fp, "(D) B1 = (%.2f, %.2f)\n", B1x, B1y);
    fprintf(fp, "\nMatching options:\n(A)->(4), (B)->(2), (C)->(5), (D)->(3)\n");
    fprintf(fp, "Correct Option: (c)\n");

    fclose(fp);

    printf("Results written successfully to circle.dat\n");

    return 0;
}

