#include <stdio.h>

// Function to compute 3a + 2b and return direction ratios
void compute_vector_sum(double a_i, double a_j, double a_k, 
                       double b_i, double b_j, double b_k,
                       double *result_i, double *result_j, double *result_k) {
    // Calculate 3a + 2b
    *result_i = 3 * a_i + 2 * b_i;
    *result_j = 3 * a_j + 2 * b_j;
    *result_k = 3 * a_k + 2 * b_k;
}

// Function to print vector components
void print_vector(const char *name, double i, double j, double k) {
    printf("%s = %.1fi + %.1fj + %.1fk\n", name, i, j, k);
}
