#ifndef MATRIX_SOLVER_H
#define MATRIX_SOLVER_H

// Function to multiply two 2x2 matrices
void multiply_matrix(int A[2][2], int B[2][2], int result[2][2]);

// Function to add identity matrix to a 2x2 matrix
void add_identity(int M[2][2]);

// Function to compute scalar k such that A^2 + I = kA
int compute_scalar_k(int A[2][2]);

// Utility function to print a 2x2 matrix
void print_matrix(int M[2][2]);

#endif

