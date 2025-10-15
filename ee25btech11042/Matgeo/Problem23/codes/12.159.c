#include <stdio.h>

// Function to calculate the determinant of a 3x3 matrix
// The matrix is passed as a flattened array of 9 doubles.
double determinant_3x3(double mat[9]) {
    // Create a mutable 2D array from the flattened input for easier access
    double m[3][3];
    int k = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            m[i][j] = mat[k++];
        }
    }

    double det = 1.0;

    // --- Gaussian Elimination to create an Upper Triangular Matrix ---

    // Step 1: Eliminate the first element of row 2 and row 3
    // Operation: R2 -> R2 - (m[1][0] / m[0][0]) * R1
    double factor1 = m[1][0] / m[0][0];
    for (int i = 0; i < 3; i++) {
        m[1][i] = m[1][i] - factor1 * m[0][i];
    }

    // Operation: R3 -> R3 - (m[2][0] / m[0][0]) * R1
    double factor2 = m[2][0] / m[0][0];
    for (int i = 0; i < 3; i++) {
        m[2][i] = m[2][i] - factor2 * m[0][i];
    }

    // Step 2: Eliminate the second element of row 3
    // Operation: R3 -> R3 - (m[2][1] / m[1][1]) * R2
    double factor3 = m[2][1] / m[1][1];
    for (int i = 1; i < 3; i++) {
        m[2][i] = m[2][i] - factor3 * m[1][i];
    }
    
    // The determinant is the product of the diagonal elements
    det = m[0][0] * m[1][1] * m[2][2];

    return det;
}
