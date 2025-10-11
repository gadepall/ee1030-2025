
#include <stdio.h>
#include <stdlib.h>

// Function to perform Gaussian elimination
void gaussianElimination(double A[][3], double b[], double x[], int n) {
    int i, j, k;
    double ratio, temp;

    // Forward elimination
    for (i = 0; i < n-1; i++) {
        for (k = i+1; k < n; k++) {
            ratio = A[k][i] / A[i][i];
            for (j = 0; j < n; j++) {
                A[k][j] = A[k][j] - ratio * A[i][j];
            }
            b[k] = b[k] - ratio * b[i];
        }
    }

    // Back substitution
    for (i = n-1; i >= 0; i--) {
        x[i] = b[i];
        for (j = i+1; j < n; j++) {
            x[i] = x[i] - A[i][j] * x[j];
        }
        x[i] = x[i] / A[i][i];
    }
}

int main() {
    int n = 3;

    // Coefficient matrix from the circuit analysis
    double A[3][3] = {
        {-7.0, 2.0, 1.0},
        {2.0, -4.0, 2.0},
        {-1.0, -2.0, 7.0}
    };

    // Constants vector
    double b[3] = {-10.0, -5.0, 10.0};

    // Solution vector
    double x[3];

    // Solve the system
    gaussianElimination(A, b, x, n);

    // Write results to main.dat
    FILE *datFile = fopen("main.dat", "w");
    if (datFile == NULL) {
        printf("Error: Cannot create main.dat file\n");
        return 1;
    }

    fprintf(datFile, "Circuit Current Analysis Results\n");
    fprintf(datFile, "================================\n");
    fprintf(datFile, "Branch Currents:\n");
    fprintf(datFile, "I1 = %.10f A = 25/8 A\n", x[0]);
    fprintf(datFile, "I2 = %.10f A = 35/8 A\n", x[1]);
    fprintf(datFile, "I3 = %.10f A = 25/8 A\n", x[2]);
    fprintf(datFile, "\n");
    fprintf(datFile, "System of Equations Solved:\n");
    fprintf(datFile, "-7*I1 + 2*I2 + 1*I3 = -10\n");
    fprintf(datFile, " 2*I1 - 4*I2 + 2*I3 = -5\n");
    fprintf(datFile, "-1*I1 - 2*I2 + 7*I3 = 10\n");
    fprintf(datFile, "\n");
    fprintf(datFile, "Coefficient Matrix:\n");
    fprintf(datFile, "| -7   2   1 |\n");
    fprintf(datFile, "|  2  -4   2 |\n");
    fprintf(datFile, "| -1  -2   7 |\n");
    fprintf(datFile, "\n");
    fprintf(datFile, "Constants Vector: [-10, -5, 10]\n");

    // Verify solution
    fprintf(datFile, "\n");
    fprintf(datFile, "Verification (substituting back into equations):\n");
    double check1 = -7*x[0] + 2*x[1] + 1*x[2];
    double check2 = 2*x[0] - 4*x[1] + 2*x[2];  
    double check3 = -1*x[0] - 2*x[1] + 7*x[2];
    fprintf(datFile, "Equation 1: %.6f (should be -10)\n", check1);
    fprintf(datFile, "Equation 2: %.6f (should be -5)\n", check2);
    fprintf(datFile, "Equation 3: %.6f (should be 10)\n", check3);

    fclose(datFile);

    // Print to console
    printf("Circuit Analysis Complete!\n");
    printf("Branch Currents:\n");
    printf("I1 = %.10f A\n", x[0]);
    printf("I2 = %.10f A\n", x[1]);
    printf("I3 = %.10f A\n", x[2]);
    printf("\n");
    printf("Results written to main.dat\n");

    return 0;
}
