#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

// Function declarations
void solve_matrix_problem();
double dot_product(double *a, double *b, int n);
void vector_add(double *a, double *b, double *result, int n);
void vector_scale(double *a, double scalar, double *result, int n);
void vector_subtract(double *a, double *b, double *result, int n);
double vector_norm_squared(double *a, int n);

// Export function for Python interface
double calculate_norm_squared() {
    // Unit eigenvectors (orthonormal basis)
    double u[3] = {1.0, 0.0, 0.0};  // eigenvector for eigenvalue -1
    double v[3] = {0.0, 1.0, 0.0};  // eigenvector for eigenvalue 1
    double w[3] = {0.0, 0.0, 1.0};  // eigenvector for eigenvalue 2

    // From the theoretical solution:
    // x = 2v + w - u
    double x[3];
    double temp1[3], temp2[3];

    vector_scale(v, 2.0, temp1, 3);       // 2v
    vector_add(temp1, w, temp2, 3);       // 2v + w
    vector_subtract(temp2, u, x, 3);      // x = 2v + w - u

    // y = u - v - (1/2)w
    double y[3];
    vector_subtract(u, v, temp1, 3);      // u - v
    vector_scale(w, 0.5, temp2, 3);       // (1/2)w
    vector_subtract(temp1, temp2, y, 3);  // y = u - v - (1/2)w

    // Calculate x + y
    double x_plus_y[3];
    vector_add(x, y, x_plus_y, 3);

    // Calculate |x + y|²
    double norm_squared = vector_norm_squared(x_plus_y, 3);

    return norm_squared;
}

void solve_matrix_problem() {
    printf("Matrix Eigenvalue Problem Solution\n");
    printf("==================================\n");

    // Given eigenvalues: -1, 1, 2
    double eigenvalues[3] = {-1.0, 1.0, 2.0};

    printf("Eigenvalues: λ1 = %.1f, λ2 = %.1f, λ3 = %.1f\n", 
           eigenvalues[0], eigenvalues[1], eigenvalues[2]);

    // Unit eigenvectors (orthonormal basis)
    double u[3] = {1.0, 0.0, 0.0};  // eigenvector for eigenvalue -1
    double v[3] = {0.0, 1.0, 0.0};  // eigenvector for eigenvalue 1
    double w[3] = {0.0, 0.0, 1.0};  // eigenvector for eigenvalue 2

    printf("\nUnit eigenvectors:\n");
    printf("u = [%.1f, %.1f, %.1f] (eigenvalue = %.1f)\n", u[0], u[1], u[2], eigenvalues[0]);
    printf("v = [%.1f, %.1f, %.1f] (eigenvalue = %.1f)\n", v[0], v[1], v[2], eigenvalues[1]);
    printf("w = [%.1f, %.1f, %.1f] (eigenvalue = %.1f)\n", w[0], w[1], w[2], eigenvalues[2]);

    printf("\nGiven conditions:\n");
    printf("Mx = u + 2(v + w)\n");
    printf("M²y = u - (v + 2w)\n");

    printf("\nFrom the theoretical solution:\n");

    // x = 2v + w - u (from solving Mx = u + 2(v + w))
    double x[3];
    double temp1[3], temp2[3];

    vector_scale(v, 2.0, temp1, 3);       // 2v
    vector_add(temp1, w, temp2, 3);       // 2v + w
    vector_subtract(temp2, u, x, 3);      // x = 2v + w - u

    printf("x = 2v + w - u = [%.1f, %.1f, %.1f]\n", x[0], x[1], x[2]);

    // y = u - v - (1/2)w (from solving M²y = u - (v + 2w))
    double y[3];
    vector_subtract(u, v, temp1, 3);      // u - v
    vector_scale(w, 0.5, temp2, 3);       // (1/2)w
    vector_subtract(temp1, temp2, y, 3);  // y = u - v - (1/2)w

    printf("y = u - v - (1/2)w = [%.1f, %.1f, %.1f]\n", y[0], y[1], y[2]);

    // Calculate x + y
    double x_plus_y[3];
    vector_add(x, y, x_plus_y, 3);

    printf("\nx + y = [%.1f, %.1f, %.1f]\n", x_plus_y[0], x_plus_y[1], x_plus_y[2]);

    // Calculate |x + y|²
    double norm_squared = vector_norm_squared(x_plus_y, 3);

    printf("\n|x + y|² = %.2f\n", norm_squared);
    printf("\nAnswer: Option (a) 1.25\n");
}

double dot_product(double *a, double *b, int n) {
    double result = 0.0;
    for (int i = 0; i < n; i++) {
        result += a[i] * b[i];
    }
    return result;
}

void vector_add(double *a, double *b, double *result, int n) {
    for (int i = 0; i < n; i++) {
        result[i] = a[i] + b[i];
    }
}

void vector_scale(double *a, double scalar, double *result, int n) {
    for (int i = 0; i < n; i++) {
        result[i] = a[i] * scalar;
    }
}

void vector_subtract(double *a, double *b, double *result, int n) {
    for (int i = 0; i < n; i++) {
        result[i] = a[i] - b[i];
    }
}

double vector_norm_squared(double *a, int n) {
    return dot_product(a, a, n);
}

int main() {
    solve_matrix_problem();
    return 0;
}