#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to write matrix to binary file
void write_matrix_to_file(double matrix[2][2], const char* filename) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        printf("Error opening file for writing\n");
        return;
    }

    // Write matrix dimensions first
    int rows = 2, cols = 2;
    fwrite(&rows, sizeof(int), 1, file);
    fwrite(&cols, sizeof(int), 1, file);

    // Write matrix data
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            fwrite(&matrix[i][j], sizeof(double), 1, file);
        }
    }

    fclose(file);
}

// Function to calculate eigenvalues of 2x2 matrix
void calculate_eigenvalues(double matrix[2][2], double eigenvalues[2]) {
    // For 2x2 matrix A = [[a, b], [c, d]]
    // Characteristic polynomial: λ² - (a+d)λ + (ad-bc) = 0
    // Using quadratic formula: λ = [(a+d) ± √((a+d)² - 4(ad-bc))] / 2

    double a = matrix[0][0];
    double b = matrix[0][1];
    double c = matrix[1][0];
    double d = matrix[1][1];

    double trace = a + d;          // sum of diagonal elements
    double determinant = a*d - b*c; // determinant

    double discriminant = trace*trace - 4*determinant;

    if (discriminant >= 0) {
        eigenvalues[0] = (trace + sqrt(discriminant)) / 2.0;
        eigenvalues[1] = (trace - sqrt(discriminant)) / 2.0;
    } else {
        // Complex eigenvalues - store real part only
        eigenvalues[0] = trace / 2.0;
        eigenvalues[1] = trace / 2.0;
    }
}

int main() {
    // Define the matrix A = [[1, -1], [2, -2]]
    double A[2][2] = {{1, -1}, {2, -2}};

    printf("Matrix A:\n");
    printf("[%.3f %.3f]\n", A[0][0], A[0][1]);
    printf("[%.3f %.3f]\n", A[1][0], A[1][1]);

    // Calculate eigenvalues
    double eigenvalues[2];
    calculate_eigenvalues(A, eigenvalues);

    printf("\nEigenvalues:\n");
    printf("λ₁ = %.3f\n", eigenvalues[0]);
    printf("λ₂ = %.3f\n", eigenvalues[1]);

    // Write matrix to binary file
    write_matrix_to_file(A, "main.dat");

    // Write eigenvalues to a separate binary file for verification
    FILE *eigen_file = fopen("eigenvalues.dat", "w");
    if (eigen_file != NULL) {
        fwrite(eigenvalues, sizeof(double), 2, eigen_file);
        fclose(eigen_file);
    }

    printf("\nMatrix data written to main.dat\n");
    printf("Eigenvalues written to eigenvalues.dat\n");

    return 0;
}
