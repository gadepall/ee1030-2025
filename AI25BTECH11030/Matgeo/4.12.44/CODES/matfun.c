#include "matfun.h"

void vector_subtract(const double *A, const double *B, double *C, int n) {
    for(int i = 0; i < n; i++) {
        C[i] = A[i] - B[i];
    }
}

double dot_product(const double *A, const double *B, int n) {
    double sum = 0;
    for(int i = 0; i < n; i++) {
        sum += A[i] * B[i];
    }
    return sum;
}

void scalar_multiply(const double *A, double *B, double scalar, int n) {
    for(int i = 0; i < n; i++) {
        B[i] = A[i] * scalar;
    }
}
