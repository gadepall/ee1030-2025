#include <stdio.h>

/*
 * Calculates the inverse of a 2x2 matrix.
 *
 * @param matrix_in A pointer to a 4-element float array representing the input matrix [a, b, c, d].
 * @param matrix_out A pointer to a 4-element float array where the inverse will be stored.
 * @return 1 on success, 0 if the matrix is singular (no inverse exists).
 */
int get_inverse(float* matrix_in, float* matrix_out) {
    // The matrix is represented as:
    // [ matrix_in[0]  matrix_in[1] ]
    // [ matrix_in[2]  matrix_in[3] ]

    // Calculate the determinant: ad - bc
    float determinant = (matrix_in[0] * matrix_in[3]) - (matrix_in[1] * matrix_in[2]);

    // If the determinant is zero, the inverse does not exist.
    if (determinant == 0) {
        return 0; // Return 0 to indicate failure
    }

    // Calculate the inverse using the formula:
    // inverse = (1/determinant) * [ d -b ]
    //                             [ -c a ]
    matrix_out[0] = matrix_in[3] / determinant;
    matrix_out[1] = -matrix_in[1] / determinant;
    matrix_out[2] = -matrix_in[2] / determinant;
    matrix_out[3] = matrix_in[0] / determinant;

    return 1; // Return 1 to indicate success
}


