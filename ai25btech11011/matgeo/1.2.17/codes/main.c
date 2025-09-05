#include <stdio.h>

int main() {
    double A[3] = {3, -1, 2};
    double B[3] = {1, -2, 4};
    double C[3] = {-1, 1, 2};
    double D[3];

    D[0] = A[0] + C[0] - B[0];
    D[1] = A[1] + C[1] - B[1];
    D[2] = A[2] + C[2] - B[2];

    FILE *fp = fopen("coords.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(fp, "%lf %lf %lf\n", A[0], A[1], A[2]);
    fprintf(fp, "%lf %lf %lf\n", B[0], B[1], B[2]);
    fprintf(fp, "%lf %lf %lf\n", C[0], C[1], C[2]);
    fprintf(fp, "%lf %lf %lf\n", D[0], D[1], D[2]);

    fclose(fp);

    printf("Fourth vertex D: (%.2lf, %.2lf, %.2lf)\n", D[0], D[1], D[2]);

    return 0;
}

