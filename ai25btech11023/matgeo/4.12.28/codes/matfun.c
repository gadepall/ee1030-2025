#include <stdlib.h>
#include <stdio.h>
#include <math.h>

// Matrix creation (flat double array)
double* createMat(int m, int n) {
    double* arr = (double*) malloc(m * n * sizeof(double));
    return arr;
}

// Print matrix for debugging
void printMat(double* arr, int m, int n) {
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            printf("%lf ", arr[i*n + j]);
        }
        printf("\n");
    }
}

// Dot product of two vectors of length m
double Matdot(double* a, double* b, int m) {
    double dot = 0;
    for (int i = 0; i < m; i++) {
        dot += a[i] * b[i];
    }
    return dot;
}

// Subtract two vectors (length m)
void Matsub(double* a, double* b, double* result, int m) {
    for (int i = 0; i < m; i++) {
        result[i] = a[i] - b[i];
    }
}

// Add two vectors (length m)
void Matadd(double* a, double* b, double* result, int m) {
    for (int i = 0; i < m; i++) {
        result[i] = a[i] + b[i];
    }
}

// Scale a vector
void Matscale(double* a, double* result, int m, double k) {
    for (int i = 0; i < m; i++) {
        result[i] = a[i] * k;
    }
}
