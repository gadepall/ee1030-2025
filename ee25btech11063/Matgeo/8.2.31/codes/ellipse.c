#include <stdio.h>

int main() {
    FILE *fp;

    // Open file ellipse.dat for writing
    fp = fopen("ellipse.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write the equation of ellipse into the file
    fprintf(fp, "Equation of the ellipse:\n");
    fprintf(fp, "(x^2)/9 + (y^2)/4 = 1\n");

    // Optionally write the matrix form as well
    fprintf(fp, "\nMatrix form:\n");
    fprintf(fp, "[x y] * [[1/9  0]\n");
    fprintf(fp, "          [0   1/4]] * [x y]^T = 1\n");

    fclose(fp);
    printf("Equation successfully written to ellipse.dat\n");

    return 0;
}

