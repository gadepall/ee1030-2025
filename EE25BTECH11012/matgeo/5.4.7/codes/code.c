#include <stdio.h>
#include <stdlib.h> // For exit()

// A function to print a 2x2 matrix
void printMatrix(double mat[2][2]) {
    for (int i = 0; i < 2; i++) {
        printf(" |");
        for (int j = 0; j < 2; j++) {
            // %.2f prints the float with 2 decimal places
            printf("%8.2f", mat[i][j]);
        }
        printf(" |\n");
    }
}

int main() {
    // The original matrix from the question
    double matrix[2][2] = {
        {2.0, 2.0},
        {4.0, 3.0}
    };

    printf("Original Matrix A:\n");
    printMatrix(matrix);

    // --- Step 1: Check if the inverse exists (determinant != 0) ---
    // Determinant = ad - bc
    double det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];
    if (det == 0) {
        printf("\nInverse does not exist because the determinant is zero.\n");
        return 1; // Exit with an error
    }

    // --- Step 2: Create an augmented matrix [A|I] ---
    // 'I' is the 2x2 identity matrix
    double augmented[2][4];
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            augmented[i][j] = matrix[i][j]; // Copy matrix A
        }
    }
    // Append the identity matrix
    augmented[0][2] = 1.0;
    augmented[0][3] = 0.0;
    augmented[1][2] = 0.0;
    augmented[1][3] = 1.0;

    // --- Step 3: Apply Gauss-Jordan elimination ---
    // Goal: Transform the left side of the augmented matrix into the identity matrix.

    // Make the first element of the first row (pivot) equal to 1
    // R1 -> R1 / 2
    double pivot1 = augmented[0][0];
    for (int j = 0; j < 4; j++) {
        augmented[0][j] /= pivot1;
    }

    // Make the first element of the second row equal to 0
    // R2 -> R2 - 4 * R1
    double factor1 = augmented[1][0];
    for (int j = 0; j < 4; j++) {
        augmented[1][j] -= factor1 * augmented[0][j];
    }

    // Make the second element of the second row (pivot) equal to 1
    // R2 -> R2 / -1
    double pivot2 = augmented[1][1];
    for (int j = 0; j < 4; j++) {
        augmented[1][j] /= pivot2;
    }

    // Make the second element of the first row equal to 0
    // R1 -> R1 - 1 * R2
    double factor2 = augmented[0][1];
    for (int j = 0; j < 4; j++) {
        augmented[0][j] -= factor2 * augmented[1][j];
    }

    // --- Step 4: Extract the inverse matrix ---
    // The inverse is now on the right side of the augmented matrix
    double inverse[2][2];
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            inverse[i][j] = augmented[i][j + 2];
        }
    }

    printf("\nFound Inverse Matrix A⁻¹:\n");
    printMatrix(inverse);

    return 0;
}