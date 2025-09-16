#include <stdio.h>

double calculate_determinant(double* matrix) {
    // Calculates the determinant of a 3x3 matrix using the standard formula.
    // The matrix is passed as a 9-element array in row-major order.
    // Matrix layout corresponds to:
    // [ matrix[0], matrix[1], matrix[2] ]
    // [ matrix[3], matrix[4], matrix[5] ]
    // [ matrix[6], matrix[7], matrix[8] ]

    double det = matrix[0] * (matrix[4] * matrix[8] - matrix[5] * matrix[7]) -
                 matrix[1] * (matrix[3] * matrix[8] - matrix[5] * matrix[6]) +
                 matrix[2] * (matrix[3] * matrix[7] - matrix[4] * matrix[6]);

    return det;
}

