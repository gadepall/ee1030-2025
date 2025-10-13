#include <stdio.h>

int main() {
    float mat[3][4] = {
        {1, -2, 3, -1},   // Equation 1
        {1, -3, 4, 1},    // Equation 2
        {-2, 4, -6, 0}    // Equation 3: RHS is k (we'll set this below)
    };

    float k;

    // We want to find value of k such that system has infinitely many solutions.
    // Let's denote RHS of third equation as 'k'
    // So after performing the row operations, the third row will become:
    // [0, 0, 0 | k - 2] ==> For infinite solutions, k - 2 = 0 => k = 2

    // Step 1: R2 = R2 - R1
    for (int i = 0; i < 4; i++) {
        mat[1][i] = mat[1][i] - mat[0][i];
    }

    // Step 2: R3 = R3 + 2*R1
    // RHS of R3 will be k, so we apply operation to it symbolically
    float rhs3 = k; // placeholder, we want to find the value of k

    // After row ops:
    // R3 = R3 + 2*R1
    // New RHS of row 3: k + 2*(-1) = k - 2
    // For infinite solutions, this must be zero:
    // => k - 2 = 0 => k = 2

    k = 2;  // This satisfies the condition

    // Output the result to solution.dat
    FILE *fp = fopen("solution.dat", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    fprintf(fp, "The value of k for which the system has infinitely many solutions is: %.1f\n", k);
    fclose(fp);

    printf("The value of k is: %.1f (also written to solution.dat)\n", k);
    return 0;
}

