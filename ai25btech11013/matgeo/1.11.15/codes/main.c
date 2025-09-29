#include <stdio.h>

// Function declarations
void compute_vector_sum(double a_i, double a_j, double a_k, 
                       double b_i, double b_j, double b_k,
                       double *result_i, double *result_j, double *result_k);
void print_vector(const char *name, double i, double j, double k);

int main() {
    // Given vectors
    double a_i = 1.0, a_j = 1.0, a_k = -2.0;  // a = i + j - 2k
    double b_i = 2.0, b_j = -4.0, b_k = 5.0;  // b = 2i - 4j + 5k
    
    // Result vector
    double result_i, result_j, result_k;
    
    // Compute 3a + 2b
    compute_vector_sum(a_i, a_j, a_k, b_i, b_j, b_k, 
                      &result_i, &result_j, &result_k);
    
    // Print results
    printf("Vector Operations:\n");
    printf("==================\n");
    print_vector("a", a_i, a_j, a_k);
    print_vector("b", b_i, b_j, b_k);
    print_vector("3a + 2b", result_i, result_j, result_k);
    
    printf("\nDirection ratios of 3a + 2b:\n");
    printf("x-component: %.1f\n", result_i);
    printf("y-component: %.1f\n", result_j);
    printf("z-component: %.1f\n", result_k);
    
    return 0;
}
