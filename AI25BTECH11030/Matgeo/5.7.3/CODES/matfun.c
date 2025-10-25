#include <stdio.h>
#include "matfun.h"

void matmult(double A[SIZE][SIZE], double B[SIZE][SIZE], double res[SIZE][SIZE]) {
    for(int i=0; i<SIZE; i++) {
        for(int j=0; j<SIZE; j++) {
            res[i][j] = 0.0;
            for(int k=0; k<SIZE; k++) {
                res[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

void matscalarmult(double scalar, double A[SIZE][SIZE], double res[SIZE][SIZE]) {
    for(int i=0; i<SIZE; i++) {
        for(int j=0; j<SIZE; j++) {
            res[i][j] = scalar * A[i][j];
        }
    }
}

void matadd(double A[SIZE][SIZE], double B[SIZE][SIZE], double res[SIZE][SIZE]) {
    for(int i=0; i<SIZE; i++) {
        for(int j=0; j<SIZE; j++) {
            res[i][j] = A[i][j] + B[i][j];
        }
    }
}

void matsub(double A[SIZE][SIZE], double B[SIZE][SIZE], double res[SIZE][SIZE]) {
    for(int i=0; i<SIZE; i++) {
        for(int j=0; j<SIZE; j++) {
            res[i][j] = A[i][j] - B[i][j];
        }
    }
}

void matidentity(double I[SIZE][SIZE]) {
    for(int i=0; i<SIZE; i++) {
        for(int j=0; j<SIZE; j++) {
            I[i][j] = (i == j) ? 1.0 : 0.0;
        }
    }
}

void compute_inverse(double A[SIZE][SIZE], double A_inv[SIZE][SIZE]) {
    double A2[SIZE][SIZE], negA2[SIZE][SIZE];
    double sixA[SIZE][SIZE], neg5I[SIZE][SIZE];
    double temp[SIZE][SIZE], I[SIZE][SIZE];

    matmult(A, A, A2);
    matscalarmult(-1, A2, negA2);
    matscalarmult(6, A, sixA);

    matidentity(I);
    matscalarmult(-5, I, neg5I);

    matadd(negA2, sixA, temp);
    matadd(temp, neg5I, temp);

    matscalarmult(1.0/11.0, temp, A_inv);
}

