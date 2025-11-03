#include <stdio.h>
#include <math.h>

int main() {
    // Vector components
    int x = 3, y = -2, z = 6;
    double magnitude, l, m, n;

    // Calculate magnitude
    magnitude = sqrt(x*x + y*y + z*z);

    // Direction cosines
    l = x / magnitude;
    m = y / magnitude;
    n = z / magnitude;

    // Open file for writing
    FILE *fp = fopen("dc.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(fp, "Direction cosines of vector (3, -2, 6):\n");
    fprintf(fp, "l = %.4f\n", l);
    fprintf(fp, "m = %.4f\n", m);
    fprintf(fp, "n = %.4f\n", n);

    fclose(fp);
    printf("Output written to dc.dat successfully.\n");

    return 0;
}

