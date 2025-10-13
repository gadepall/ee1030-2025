#include <stdio.h>
#include <math.h>

int main() {
    FILE *fp;
    double m;

    // Calculation based on derived formula: m^3 = 1/8
    m = cbrt(1.0/8.0);  // cube root

    // Open file slope.dat for writing
    fp = fopen("slope.dat", "w");
    if(fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write slope value into file
    fprintf(fp, "The slope of the common tangent is: %lf\n", m);

    fclose(fp);

    printf("Result written to slope.dat successfully.\n");
    return 0;
}

