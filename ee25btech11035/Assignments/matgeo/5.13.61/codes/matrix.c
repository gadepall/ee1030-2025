#include <stdio.h>

#define N 3   // matrix size

// Multiply two N×N matrices: C = A * B
void matmul(double A[N][N], double B[N][N], double C[N][N]) {
    double temp[N][N] = {0};
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            temp[i][j] = 0;
            for (int k = 0; k < N; k++) {
                temp[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            C[i][j] = temp[i][j];
}

// Compute P^power - I
void computeQ(double P[N][N], int power, double Q[N][N]) {
    double result[N][N];
    double temp[N][N];

    // Initialize result = I
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            result[i][j] = (i == j) ? 1 : 0;

    // Copy P to temp
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            temp[i][j] = P[i][j];

    // Exponentiation by squaring (efficient)
    while (power > 0) {
        if (power % 2 == 1)
            matmul(result, temp, result);
        matmul(temp, temp, temp);
        power /= 2;
    }

    // Subtract I: Q = result - I
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            Q[i][j] = result[i][j] - ((i == j) ? 1 : 0);
}

// Function to compute ratio = (q31 + q32)/q21
double getRatio(double P[N][N], int power) {
    double Q[N][N];
    computeQ(P, power, Q);
    return (Q[2][0] + Q[2][1]) / Q[1][0];
}
