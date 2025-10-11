#include <stdio.h>
#include "matrix_ops.h"

int main() {
    double a = 13.0 / 5.0;
    double b = 13.0;

    double A[2][2] = { {5*a, -b}, {3, 2} };
    double AT[2][2], AA_T[2][2], Adj[2][2];

    transpose(A, AT);
    multiply(A, AT, AA_T);
    compute_adj(A, Adj);

    printf("Matrix A:\n");
    print_matrix(A);

    printf("\nTranspose A^T:\n");
    print_matrix(AT);

    printf("\nProduct AA^T:\n");
    print_matrix(AA_T);

    printf("\nAdjugate of A:\n");
    print_matrix(Adj);

    printf("\n5a + b = %.3f\n", 5*a + b);
    return 0;
}

