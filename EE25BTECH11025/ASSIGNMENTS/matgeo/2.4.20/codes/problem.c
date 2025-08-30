#include <stdio.h>

// Function to calculate dot product of two vectors
double dot_product(double a[], double b[], int size) {
    double result = 0.0;
    for(int i = 0; i < size; i++) {
        result += a[i] * b[i];
    }
    return result;
}

// Wrapper for Python to access
double solve_lambda(double b[]) {
    // a = [2, lambda, 1]
    double a[3];
    double lambda;
    // Equation: 2*b[0] + lambda*b[1] + 1*b[2] = 0
    // => lambda = -(2*b[0] + 1*b[2]) / b[1]
    lambda = -(2*b[0] + 1*b[2]) / b[1];
    return lambda;
}

