
#include <stdio.h>

// Function to write first set of points (isosceles triangle)
void generate_points_isosceles(const char *filename) {
    FILE *fp = fopen(filename, "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return;
    }

    double A[3] = {0, 7, -10};
    double B[3] = {1, 6, -6};
    double C[3] = {4, 9, -6};

    fprintf(fp, "%lf %lf %lf\n", A[0], A[1], A[2]);
    fprintf(fp, "%lf %lf %lf\n", B[0], B[1], B[2]);
    fprintf(fp, "%lf %lf %lf\n", C[0], C[1], C[2]);

    fclose(fp);
}

// Function to write second set of points (right-angled triangle)
void generate_points_right(const char *filename) {
    FILE *fp = fopen(filename, "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return;
    }

    double P[3] = {0, 7, 10};
    double Q[3] = {-1, 6, 6};
    double R[3] = {-4, 9, 6};

    fprintf(fp, "%lf %lf %lf\n", P[0], P[1], P[2]);
    fprintf(fp, "%lf %lf %lf\n", Q[0], Q[1], Q[2]);
    fprintf(fp, "%lf %lf %lf\n", R[0], R[1], R[2]);

    fclose(fp);
}

