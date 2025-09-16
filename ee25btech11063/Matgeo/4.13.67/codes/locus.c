#include <stdio.h>

int main() {
    FILE *fp;

    // Open the file locus.dat in write mode
    fp = fopen("locus.dat", "w");

    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write the solution into the file
    fprintf(fp, "The locus of P is given by the equation:\n");
    fprintf(fp, "(y - 1)^2 = 4x^2\n");
    fprintf(fp, "Which represents two intersecting straight lines:\n");
    fprintf(fp, "1) y - 1 = 2x  -->  y = 2x + 1\n");
    fprintf(fp, "2) y - 1 = -2x -->  y = -2x + 1\n");

    // Close the file
    fclose(fp);

    printf("Locus has been written successfully into locus.dat\n");

    return 0;
}

