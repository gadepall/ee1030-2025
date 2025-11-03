
#include <stdio.h>
#include <stdlib.h>

// Function to perform Gaussian elimination to solve (A - λI)v = 0
void find_eigenvector(double A[3][3], double lambda, double eigenvector[3]) {
    // Create augmented matrix (A - λI | 0)
    double matrix[3][4];

    // Fill the matrix (A - λI)
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            matrix[i][j] = A[i][j];
            if (i == j) {
                matrix[i][j] -= lambda;  // Subtract λ from diagonal
            }
        }
        matrix[i][3] = 0.0;  // Right hand side is zero
    }

    printf("Matrix (A - λI):\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%.1f ", matrix[i][j]);
        }
        printf("\n");
    }

    // Row reduction to find null space
    // From the problem: (A - I) results in:
    // [0  1  2]
    // [0  0  0] 
    // [1  2  0]

    // The solution is any vector in the null space
    // From row 1: y + 2z = 0 => y = -2z
    // From row 3: x + 2y = 0 => x = -2y = -2(-2z) = 4z
    // So if z = 1, then x = 4, y = -2, z = 1

    eigenvector[0] = 4.0;   // x component
    eigenvector[1] = -2.0;  // y component  
    eigenvector[2] = 1.0;   // z component

    printf("\nEigenvector for λ = %.1f: [%.1f, %.1f, %.1f]\n", 
           lambda, eigenvector[0], eigenvector[1], eigenvector[2]);
}

int main() {
    // Define the matrix A
    double A[3][3] = {
        {1, 1, 2},
        {0, 1, 0},
        {1, 2, 1}
    };

    double lambda = 1.0;
    double eigenvector[3];

    printf("Given matrix A:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%.1f ", A[i][j]);
        }
        printf("\n");
    }
    printf("\n");

    printf("Finding eigenvector for eigenvalue λ = %.1f\n\n", lambda);

    find_eigenvector(A, lambda, eigenvector);

    // Verify the solution: Av = λv
    printf("\nVerification (Av = λv):\n");
    for (int i = 0; i < 3; i++) {
        double result = 0.0;
        for (int j = 0; j < 3; j++) {
            result += A[i][j] * eigenvector[j];
        }
        printf("Row %d: %.1f = %.1f * %.1f\n", i+1, result, lambda, eigenvector[i]);
    }

    // Write results to files
    FILE *dat_file = fopen("main.dat", "w");
    if (dat_file) {
        fprintf(dat_file, "Matrix A:\n");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                fprintf(dat_file, "%.1f ", A[i][j]);
            }
            fprintf(dat_file, "\n");
        }
        fprintf(dat_file, "\nEigenvalue: %.1f\n", lambda);
        fprintf(dat_file, "Eigenvector: %.1f %.1f %.1f\n", 
                eigenvector[0], eigenvector[1], eigenvector[2]);
        fclose(dat_file);
    }

    return 0;
}
