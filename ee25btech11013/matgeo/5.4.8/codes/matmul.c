#include <stdio.h>


void matmul(double* A, double* B, double* C) {
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            double sum = 0.0;
            for (int k = 0; k < 2; k++) {
                sum += A[i*2 + k] * B[k*2 + j];
            }
            C[i*2 + j] = sum;
        }
    }
}
