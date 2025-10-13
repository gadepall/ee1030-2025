#include <stdio.h>

int main() {
    // Coefficients of equations:
    // Equation 1: 4x + 2y = 7
    // Equation 2: 2x +  y = 6
    int a1 = 4, b1 = 2, c1 = 7;
    int a2 = 2, b2 = 1, c2 = 6;

    // File pointer
    FILE *fp;
    fp = fopen("solution.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Calculate determinants
    int det  = a1*b2 - a2*b1;   // determinant of coefficients
    int detx = c1*b2 - c2*b1;   // determinant replacing x-column
    int dety = a1*c2 - a2*c1;   // determinant replacing y-column

    if (det != 0) {
        // Unique solution exists
        double x = (double)detx / det;
        double y = (double)dety / det;
        fprintf(fp, "The system has a unique solution: x = %.2f, y = %.2f\n", x, y);
    }
    else {
        if (detx == 0 && dety == 0) {
            // Infinite solutions
            fprintf(fp, "The system has infinite number of solutions.\n");
        } else {
            // No solution
            fprintf(fp, "The system has no solution.\n");
        }
    }

    fclose(fp);
    return 0;
}

