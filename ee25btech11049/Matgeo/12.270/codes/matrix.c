#include <stdio.h>

// This function multiplies two 2x2 matrices (A and B) and stores the
// transpose of the result in the `result` matrix.
// Matrices are passed as pointers to 1D arrays of size 4 (row-major order).
void multiply_and_transpose(double* A, double* B, double* result) {
    double product[4];

    // Perform matrix multiplication: C = A * B
    // C[0,0] = A[0,0]*B[0,0] + A[0,1]*B[1,0]
    product[0] = A[0] * B[0] + A[1] * B[2];
    // C[0,1] = A[0,0]*B[0,1] + A[0,1]*B[1,1]
    product[1] = A[0] * B[1] + A[1] * B[3];
    // C[1,0] = A[1,0]*B[0,0] + A[1,1]*B[1,0]
    product[2] = A[2] * B[0] + A[3] * B[2];
    // C[1,1] = A[1,0]*B[0,1] + A[1,1]*B[1,1]
    product[3] = A[2] * B[1] + A[3] * B[3];

    // Transpose the product matrix and store it in the result
    // result[0,0] = product[0,0]
    result[0] = product[0];
    // result[0,1] = product[1,0]
    result[1] = product[2];
    // result[1,0] = product[0,1]
    result[2] = product[1];
    // result[1,1] = product[1,1]
    result[3] = product[3];
}

