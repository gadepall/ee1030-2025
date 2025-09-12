#include <stdio.h>

int main() {
    FILE *fp;
    fp = fopen("vector.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // The determinant expansion:
    // | λ   λ   2 |
    // | 1   λ  -1 |
    // | 2  -1   λ |
    //
    // Det = -λ^3 + λ^2 + 5λ - 4

    fprintf(fp, "Determinant condition for coplanarity:\n");
    fprintf(fp, "(-λ^3 + λ^2 + 5λ - 4) = 0\n\n");

    fprintf(fp, "Checking integer values of λ from -10 to 10:\n");

    for (int lambda = -10; lambda <= 10; lambda++) {
        int val = -lambda*lambda*lambda + lambda*lambda + 5*lambda - 4;
        if (val == 0) {
            fprintf(fp, "λ = %d is a solution.\n", lambda);
        }
    }

    fclose(fp);
    printf("Results written to vector.dat\n");
    return 0;
}
