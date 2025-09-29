#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "/home/dhanush-kumar-a/ee1030-2025/ai25btech11010/matgeo/1.11.12/codes/libs/matfun.h"

int main() {
    // Vectors as 2x1 matrices
    double **a = createMat(2,1);
    double **b = createMat(2,1);

    a[0][0] = 1.0;  a[1][0] = 0.0;  
    b[0][0] = cos(M_PI * 120.0 / 180.0);  
    b[1][0] = sin(M_PI * 120.0 / 180.0);

    // Normalize
    a = Matunit(a, 2);
    b = Matunit(b, 2);

    // Operations
    double **sum = Matadd(a, b, 2, 1);
    double **diff = Matsub(a, b, 2, 1);
    double **neg_b = Matscale(b, 2, 1, -1);

    // Magnitudes
    printf("|a+b| = %.3f\n", Matnorm(sum, 2));
    printf("|a-b| = %.3f\n", Matnorm(diff, 2));
    printf("|-b|  = %.3f\n", Matnorm(neg_b, 2));

    // Save results to file
    FILE *fp = fopen("vectors_data.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    fprintf(fp, "Vector\tX\tY\tMagnitude\n");
    fprintf(fp, "a\t%.4f\t%.4f\t%.4f\n", a[0][0], a[1][0], Matnorm(a,2));
    fprintf(fp, "b\t%.4f\t%.4f\t%.4f\n", b[0][0], b[1][0], Matnorm(b,2));
    fprintf(fp, "-b\t%.4f\t%.4f\t%.4f\n", neg_b[0][0], neg_b[1][0], Matnorm(neg_b,2));
    fprintf(fp, "a+b\t%.4f\t%.4f\t%.4f\n", sum[0][0], sum[1][0], Matnorm(sum,2));
    fprintf(fp, "a-b\t%.4f\t%.4f\t%.4f\n", diff[0][0], diff[1][0], Matnorm(diff,2));
    fclose(fp);

    printf("Data saved to vectors_data.dat\n");
    return 0;
}
