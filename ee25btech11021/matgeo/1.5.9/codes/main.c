#include <stdio.h>

int main() {
    // Points
    double A[2] = {5, -6};
    double B[2] = {-1, -4};
    double P[2] = {0, -13.0/3.0}; // intersection point

    // Open file for writing
    FILE *fp = fopen("points.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write points into file
    fprintf(fp, "%.2f %.2f\n", A[0], A[1]); // A
    fprintf(fp, "%.2f %.2f\n", B[0], B[1]); // B
    fprintf(fp, "%.2f %.2f\n", P[0], P[1]); // P

    fclose(fp);
    printf("points.dat file generated successfully.\n");

    return 0;
}

