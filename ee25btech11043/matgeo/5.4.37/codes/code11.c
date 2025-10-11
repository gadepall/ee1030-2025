#include <stdio.h>
#include <math.h> // For fabs() for determinant check

// Function to calculate the determinant of a 3x3 matrix
double calculateDeterminant(double matrix[3][3]) {
    return matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
           matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
           matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]);
}

// Function to calculate the cofactor of a 3x3 matrix
// The cofactor matrix C is where C_ij = (-1)^(i+j) * M_ij
// M_ij is the determinant of the submatrix formed by deleting row i and column j
void calculateCofactor(double matrix[3][3], double cofactor[3][3]) {
    // Cofactor for element (0,0)
    cofactor[0][0] = (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]);
    // Cofactor for element (0,1)
    cofactor[0][1] = -(matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]);
    // Cofactor for element (0,2)
    cofactor[0][2] = (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]);

    // Cofactor for element (1,0)
    cofactor[1][0] = -(matrix[0][1] * matrix[2][2] - matrix[0][2] * matrix[2][1]);
    // Cofactor for element (1,1)
    cofactor[1][1] = (matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]);
    // Cofactor for element (1,2)
    cofactor[1][2] = -(matrix[0][0] * matrix[2][1] - matrix[0][1] * matrix[2][0]);

    // Cofactor for element (2,0)
    cofactor[2][0] = (matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]);
    // Cofactor for element (2,1)
    cofactor[2][1] = -(matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0]);
    // Cofactor for element (2,2)
    cofactor[2][2] = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]);
}

// Function to transpose a matrix (to get the adjoint from the cofactor matrix)
void transposeMatrix(double matrix[3][3], double transpose[3][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            transpose[j][i] = matrix[i][j]; // Swap i and j
        }
    }
}

// Main function to find the inverse of a 3x3 matrix
// The inverse is stored in the 'inverse' parameter
// Returns 0 if successful, 1 if determinant is zero (matrix is singular)
int findInverse(double matrix[3][3], double inverse[3][3]) {
    double det = calculateDeterminant(matrix);

    // If determinant is zero, inverse does not exist
    if (fabs(det) < 1e-9) { // Using a small epsilon for floating-point comparison
        printf("Error: Determinant is zero. Inverse does not exist.\n");
        return 1; // Indicate error
    }

    double cofactor_matrix[3][3];
    calculateCofactor(matrix, cofactor_matrix);

    double adjoint_matrix[3][3];
    transposeMatrix(cofactor_matrix, adjoint_matrix); // Adjoint is the transpose of the cofactor matrix

    // Calculate the inverse: A_inv = (1/det) * adj(A)
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            inverse[i][j] = adjoint_matrix[i][j] / det;
        }
    }
    return 0; // Indicate success
}