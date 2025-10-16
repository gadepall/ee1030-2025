#include "eigen.h"
#include <stdio.h>
#include <stdlib.h>

// Helper function to multiply an n x n matrix by an n x 1 vector.
void matrix_vector_mult(const double* matrix, const double* vector, double* result, int n) {
    for (int i = 0; i < n; i++) {
        result[i] = 0.0;
        for (int j = 0; j < n; j++) {
            // matrix[i * n + j] is used to access the (i, j) element
            // of the flattened 2D array.
            result[i] += matrix[i * n + j] * vector[j];
        }
    }
}

// Helper function to multiply a vector by a scalar.
void scalar_vector_mult(double scalar, const double* vector, double* result, int n) {
    for (int i = 0; i < n; i++) {
        result[i] = scalar * vector[i];
    }
}

// Main verification function exposed to Python.
void perform_verification(
    double* Q, double* R, double* R_inv, double* x, double lambda, int n,
    double* q_rx_result,
    double* lambda_rx_result,
    double* q_rinvx_result,
    double* lambda_rinvx_result
) {
    // Allocate memory for intermediate calculation results.
    double* Rx = (double*)malloc(n * sizeof(double));
    double* R_inv_x = (double*)malloc(n * sizeof(double));

    if (!Rx || !R_inv_x) {
        // Handle memory allocation failure
        fprintf(stderr, "Failed to allocate memory in C function.\n");
        if (Rx) free(Rx);
        if (R_inv_x) free(R_inv_x);
        return;
    }

    // --- Perform calculations for options a) and b) ---
    // 1. Calculate Rx = R * x
    matrix_vector_mult(R, x, Rx, n);
    // 2. Calculate Q(Rx) = Q * (R * x)
    matrix_vector_mult(Q, Rx, q_rx_result, n);
    // 3. Calculate λ(Rx) = λ * (R * x)
    scalar_vector_mult(lambda, Rx, lambda_rx_result, n);

    // --- Perform calculations for options c) and d) ---
    // 1. Calculate R_inv_x = R⁻¹ * x
    matrix_vector_mult(R_inv, x, R_inv_x, n);
    // 2. Calculate Q(R⁻¹x) = Q * (R⁻¹ * x)
    matrix_vector_mult(Q, R_inv_x, q_rinvx_result, n);
    // 3. Calculate λ(R⁻¹x) = λ * (R⁻¹ * x)
    scalar_vector_mult(lambda, R_inv_x, lambda_rinvx_result, n);

    // Free the allocated memory for intermediate results.
    free(Rx);
    free(R_inv_x);
}

