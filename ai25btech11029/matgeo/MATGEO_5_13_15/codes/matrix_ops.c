#include <stdio.h>
#include "matrix_ops.h"

void compute_adj(double A[2][2], double Adj[2][2]) {
    Adj[0][0] = A[1][1];
    Adj[0][1] = -A[0][1];
    Adj[1][0] = -A[1][0];
    Adj[1][1] = A[0][0];
}

void transpose(double A[2][2], double AT[2][2]) {
    AT[0][0] = A[0][0];
    AT[0][1] = A[1][0];
    AT[1][0] = A[0][1];
    AT[1][1] = A[1][1];
}

void multiply(double A[2][2], double B[2][2], double Result[2][2]) {
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++) {
            Result[i][j] = 0;
            for (int k = 0; k < 2; k++)
                Result[i][j] += A[i][k] * B[k][j];
        }
}

void print_matrix(double M[2][2]) {
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++)
            printf("%8.3f ", M[i][j]);
        printf("\n");
    }
}

