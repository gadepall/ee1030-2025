#include <stdio.h>
#include "matrix_solver.h"

void multiply_matrix(int A[2][2], int B[2][2], int result[2][2]) {
    result[0][0] = A[0][0]*B[0][0] + A[0][1]*B[1][0];
    result[0][1] = A[0][0]*B[0][1] + A[0][1]*B[1][1];
    result[1][0] = A[1][0]*B[0][0] + A[1][1]*B[1][0];
    result[1][1] = A[1][0]*B[0][1] + A[1][1]*B[1][1];
}

void add_identity(int M[2][2]) {
    M[0][0] += 1;
    M[1][1] += 1;
}

int compute_scalar_k(int A[2][2]) {
    int A2[2][2];
    multiply_matrix(A, A, A2);
    add_identity(A2);

    // Assuming A[0][0] ≠ 0 for scalar division
    int k = -A2[0][0] / A[0][0];
    return k;
}

void print_matrix(int M[2][2]) {
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            printf("%d\t", M[i][j]);
        }
        printf("\n");
    }
}

// Optional: main function for testing
int main() {
    int A[2][2] = { {-3, 2}, {1, -1} };
    printf("Matrix A:\n");
    print_matrix(A);

    int k = compute_scalar_k(A);
    printf("Scalar k such that A^2 + I = kA is: %d\n", k);

    return 0;
}

