#include <stdio.h>
#include <math.h>

int main() {
    FILE *fp;
    double magnitude, l, m, n;
    double dr1, dr2, dr3;  // direction ratios
    double k;              // normalization factor
    double comp_x, comp_y, comp_z;

    // Open file vector.dat
    fp = fopen("vector.dat", "r");
    if (fp == NULL) {
        printf("Error! Could not open file.\n");
        return 1;
    }

    // Reading magnitude and direction ratios
    fscanf(fp, "%lf %lf %lf %lf", &magnitude, &dr1, &dr2, &dr3);
    fclose(fp);

    // Calculate normalization factor
    k = sqrt(dr1*dr1 + dr2*dr2 + dr3*dr3);

    // Direction cosines
    l = dr1 / k;
    m = dr2 / k;
    n = dr3 / k;

    //  Verify that angle with X-axis is acute
    if (l <= 0) {
        printf("Error: The vector does not make an acute angle with the X-axis.\n");
        return 1;
    }

    // Components of vector
    comp_x = magnitude * l;
    comp_y = magnitude * m;
    comp_z = magnitude * n;

    // Display results
    printf("Direction Cosines: l = %.3f, m = %.3f, n = %.3f\n", l, m, n);
    printf("Components of vector r: (%.3f, %.3f, %.3f)\n", comp_x, comp_y, comp_z);

    return 0;
}

