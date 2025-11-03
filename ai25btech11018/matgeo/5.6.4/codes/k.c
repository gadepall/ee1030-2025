#include <stdio.h>

// Function to multiply two 2x2 matrices (A * A)
void multiply_matrices(double result[2][2], double A[2][2], double B[2][2]) {
    result[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0];
    result[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1];
    result[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0];
    result[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1];
}

// Function to multiply a 2x2 matrix by a scalar
void scalar_multiply(double result[2][2], double matrix[2][2], double k) {
    result[0][0] = k * matrix[0][0];
    result[0][1] = k * matrix[0][1];
    result[1][0] = k * matrix[1][0];
    result[1][1] = k * matrix[1][1];
}

// Function to subtract two 2x2 matrices with a scalar multiplication
void subtract_matrices(double result[2][2], double A[2][2], double I[2][2]) {
    result[0][0] = A[0][0] - 2 * I[0][0];
    result[0][1] = A[0][1] - 2 * I[0][1];
    result[1][0] = A[1][0] - 2 * I[1][0];
    result[1][1] = A[1][1] - 2 * I[1][1];
}

int main() {
    // Define the matrix A and the identity matrix I
    double A[2][2] = {{3.0, -2.0}, {4.0, -2.0}};
    double I[2][2] = {{1.0, 0.0}, {0.0, 1.0}};

    // Calculate A^2
    double A_squared[2][2];
    multiply_matrices(A_squared, A, A);

    // Solve for k using one element of the matrix equation
    // Equating the (0,0) elements: (A^2)[0][0] = k*A[0][0] - 2*I[0][0]
    // A^2[0][0] = k*3 - 2*1
    // A_squared[0][0] + 2 = 3*k
    double k_numerator = A_squared[0][0] + 2.0;
    double k_denominator = A[0][0];
    
    double k_val = k_numerator / k_denominator;

    // Verify the solution with another element for consistency
    // Equating the (1,1) elements: (A^2)[1][1] = k*A[1][1] - 2*I[1][1]
    // A^2[1][1] = k*(-2) - 2*1
    // A^2[1][1] + 2 = -2*k
    double k_val_check = (A_squared[1][1] + 2.0) / A[1][1];

    printf("Calculated value of k from (0,0) element: %.2f\n", k_val);
    printf("Calculated value of k from (1,1) element: %.2f\n\n", k_val_check);

    // Print the final result and verify the equation
    printf("The value of k that satisfies A^2 = kA - 2I is k = %.2f\n", k_val);
    
    return 0;
}