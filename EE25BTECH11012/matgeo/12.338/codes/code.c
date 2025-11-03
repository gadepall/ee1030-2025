#include <stdio.h>
#include <stdbool.h>

// Define a 2x2 matrix structure
typedef struct {
    double elements[2][2];
} Matrix2x2;

// Function to print a 2x2 matrix
void printMatrix(Matrix2x2 m) {
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            printf("%8.2f", m.elements[i][j]);
        }
        printf("\n");
    }
}

// Function to check if a 2x2 matrix is symmetric
// A matrix A is symmetric if A = A^T (its transpose)
// For a 2x2 matrix, this just means element [0][1] must equal element [1][0]
bool isSymmetric(Matrix2x2 m) {
    if (m.elements[0][1] == m.elements[1][0]) {
        return true;
    }
    return false;
}

// Function to calculate the determinant of a 2x2 matrix
// For a matrix [[a, b], [c, d]], the determinant is ad - bc
double determinant(Matrix2x2 m) {
    return (m.elements[0][0] * m.elements[1][1]) - (m.elements[0][1] * m.elements[1][0]);
}

int main() {
    // Example 1: A real symmetric matrix that IS invertible
    Matrix2x2 matrixA = {
        {{3.0, 1.0}, {1.0, 2.0}}
    };

    printf("## Matrix A ##\n");
    printMatrix(matrixA);
    printf("Is symmetric? %s\n", isSymmetric(matrixA) ? "Yes" : "No");

    double detA = determinant(matrixA);
    printf("Determinant: %.2f\n", detA);
    printf("Is invertible? %s\n\n", (detA != 0) ? "Yes" : "No");


    // Example 2: A real symmetric matrix that is NOT invertible
    Matrix2x2 matrixB = {
        {{2.0, 4.0}, {4.0, 8.0}}
    };

    printf("## Matrix B ##\n");
    printMatrix(matrixB);
    printf("Is symmetric? %s\n", isSymmetric(matrixB) ? "Yes" : "No");

    double detB = determinant(matrixB);
    printf("Determinant: %.2f\n", detB);
    printf("Is invertible? %s\n", (detB != 0) ? "Yes" : "No");
    return 0;
}
