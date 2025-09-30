#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <dlfcn.h>

// Function to perform matrix-vector multiplication
void matrix_vector_mult(double A[3][3], double x[3], double result[3]) {
    for(int i = 0; i < 3; i++) {
        result[i] = 0.0;
        for(int j = 0; j < 3; j++) {
            result[i] += A[i][j] * x[j];
        }
    }
}

// Function to find maximum absolute value in vector
double find_max_abs(double x[3]) {
    double max = fabs(x[0]);
    for(int i = 1; i < 3; i++) {
        if(fabs(x[i]) > max) {
            max = fabs(x[i]);
        }
    }
    return max;
}

// Function to normalize vector by dividing by maximum element
void normalize_vector(double x[3], double normalized[3], double max_val) {
    for(int i = 0; i < 3; i++) {
        normalized[i] = x[i] / max_val;
    }
}

// Function to calculate Rayleigh quotient
double rayleigh_quotient(double A[3][3], double y[3]) {
    double Ay[3];
    matrix_vector_mult(A, y, Ay);
    
    double numerator = 0.0;
    double denominator = 0.0;
    
    for(int i = 0; i < 3; i++) {
        numerator += y[i] * Ay[i];
        denominator += y[i] * y[i];
    }
    
    return numerator / denominator;
}

// Power method implementation (exported function for shared library)
double power_method_iterations(double A[3][3], double x0[3], double result_vector[3], int *iterations) {
    double x1[3], y1[3], x2[3], y2[3];
    double max_x1, max_x2;
    
    // First iteration: x1 = A * x0
    matrix_vector_mult(A, x0, x1);
    
    // Normalize x1 to get y1
    max_x1 = find_max_abs(x1);
    normalize_vector(x1, y1, max_x1);
    
    // Second iteration: x2 = A * y1
    matrix_vector_mult(A, y1, x2);
    
    // Normalize x2 to get y2
    max_x2 = find_max_abs(x2);
    normalize_vector(x2, y2, max_x2);
    
    // Copy final normalized vector to result
    for(int i = 0; i < 3; i++) {
        result_vector[i] = y2[i];
    }
    
    *iterations = 2;
    
    // Calculate eigenvalue using Rayleigh quotient
    return rayleigh_quotient(A, y2);
}

int main() {
    // Define the matrix A
    double A[3][3] = {
        {15.0, 4.0, 3.0},
        {10.0, 12.0, 6.0},
        {20.0, 4.0, 2.0}
    };
    
    // Initial vector x0
    double x0[3] = {1.0, 1.0, 1.0};
    
    // Variables for iterations
    double x1[3], y1[3], x2[3], y2[3];
    double max_x1, max_x2;
    
    printf("Power Method Implementation\\n");
    printf("===========================\\n");
    
    printf("Matrix A:\\n");
    for(int i = 0; i < 3; i++) {
        printf("[");
        for(int j = 0; j < 3; j++) {
            printf("%6.1f", A[i][j]);
            if(j < 2) printf(", ");
        }
        printf("]\\n");
    }
    
    printf("\\nInitial vector x0: [%.1f, %.1f, %.1f]\\n", x0[0], x0[1], x0[2]);
    
    // First iteration: x1 = A * x0
    matrix_vector_mult(A, x0, x1);
    printf("\\nIteration 1:\\n");
    printf("x1 = A * x0 = [%.1f, %.1f, %.1f]\\n", x1[0], x1[1], x1[2]);
    
    // Normalize x1 to get y1
    max_x1 = find_max_abs(x1);
    normalize_vector(x1, y1, max_x1);
    printf("max(|x1|) = %.1f\\n", max_x1);
    printf("y1 = x1/%.1f = [%.8f, %.8f, %.8f]\\n", max_x1, y1[0], y1[1], y1[2]);
    
    // Second iteration: x2 = A * y1
    matrix_vector_mult(A, y1, x2);
    printf("\\nIteration 2:\\n");
    printf("x2 = A * y1 = [%.8f, %.8f, %.8f]\\n", x2[0], x2[1], x2[2]);
    
    // Normalize x2 to get y2
    max_x2 = find_max_abs(x2);
    normalize_vector(x2, y2, max_x2);
    printf("max(|x2|) = %.8f\\n", max_x2);
    printf("y2 = x2/%.8f = [%.8f, %.8f, %.8f]\\n", max_x2, y2[0], y2[1], y2[2]);
    
    // Calculate eigenvalue using Rayleigh quotient
    double eigenvalue = rayleigh_quotient(A, y2);
    printf("\\nApproximate eigenvalue (Rayleigh quotient): %.8f\\n", eigenvalue);
    
    // Write results to main.dat file
    FILE *dat_file = fopen("main.dat", "w");
    if(dat_file != NULL) {
        fprintf(dat_file, "Matrix A:\\n");
        for(int i = 0; i < 3; i++) {
            for(int j = 0; j < 3; j++) {
                fprintf(dat_file, "%.1f ", A[i][j]);
            }
            fprintf(dat_file, "\\n");
        }
        fprintf(dat_file, "Initial vector:\\n");
        fprintf(dat_file, "%.1f %.1f %.1f\\n", x0[0], x0[1], x0[2]);
        fprintf(dat_file, "Iteration 1 result:\\n");
        fprintf(dat_file, "%.1f %.1f %.1f\\n", x1[0], x1[1], x1[2]);
        fprintf(dat_file, "Normalized y1:\\n");
        fprintf(dat_file, "%.8f %.8f %.8f\\n", y1[0], y1[1], y1[2]);
        fprintf(dat_file, "Iteration 2 result:\\n");
        fprintf(dat_file, "%.8f %.8f %.8f\\n", x2[0], x2[1], x2[2]);
        fprintf(dat_file, "Final normalized y2:\\n");
        fprintf(dat_file, "%.8f %.8f %.8f\\n", y2[0], y2[1], y2[2]);
        fprintf(dat_file, "Approximate eigenvalue:\\n");
        fprintf(dat_file, "%.8f\\n", eigenvalue);
        fclose(dat_file);
        printf("\\nResults saved to main.dat\\n");
    }
    
    return 0;
}