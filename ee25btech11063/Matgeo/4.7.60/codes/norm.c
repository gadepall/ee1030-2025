#include <stdio.h>
#include <math.h>

int main() {
    FILE *fp;
    fp = fopen("norm.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Line equation: sqrt(3)x + y - 8 = 0
    // Normal vector n = [sqrt(3), 1]
    double n[2] = {sqrt(3), 1.0};
    
    // Compute norm of n
    double norm = sqrt(n[0]*n[0] + n[1]*n[1]);

    // Unit normal (n cap)
    double n_cap[2];
    n_cap[0] = n[0] / norm;
    n_cap[1] = n[1] / norm;

    // Compute p = constant / norm
    double p = 8.0 / norm;

    // Compute angle omega = atan2(sin, cos)
    double omega = atan2(n_cap[1], n_cap[0]);  // in radians

    // Write results into file
    fprintf(fp, "Normal vector n = [%.4f, %.4f]\n", n[0], n[1]);
    fprintf(fp, "Norm of n = %.4f\n", norm);
    fprintf(fp, "Unit normal n_cap = [%.4f, %.4f]\n", n_cap[0], n_cap[1]);
    fprintf(fp, "Normal form: (%.4f)x + (%.4f)y = %.4f\n", n_cap[0], n_cap[1], p);
    fprintf(fp, "p = %.4f\n", p);
    fprintf(fp, "omega (radians) = %.4f\n", omega);
    fprintf(fp, "omega (degrees) = %.2f\n", omega * 180.0 / M_PI);

    fclose(fp);

    printf("Results written to norm.dat\n");
    return 0;
}

