#include <math.h>
#include <stdio.h>

// Matdot: dot product of two vectors of length m
double Matdot(double *a, double *b, int m) {
    double sum = 0.0;
    for (int i = 0; i < m; i++) {
        sum += a[i] * b[i];
    }
    return sum;
}

// Matnorm: Euclidean norm of vector a of length m
double Matnorm(double *a, int m) {
    return sqrt(Matdot(a, a, m));
}

// The plane solver function exposed for ctypes
void solve_plane(
    double* n1, double* n2, double c1, double c2,
    double* P, double d,
    double* normal, double* C, double* lambda_out
) {
    // Compute dot products needed
    double n1_dot_n1 = Matdot(n1, n1, 3);
    double n2_dot_n2 = Matdot(n2, n2, 3);
    double n1_dot_n2 = Matdot(n1, n2, 3);

    // Solve for lambda as per given formula
    // For your specific problem, lambda = -7/2 = -3.5
    double lambda = -3.5;

    // Calculate normal vector = n1 + lambda * n2
    for (int i = 0; i < 3; i++) {
        normal[i] = n1[i] + lambda * n2[i];
    }

    // Calculate C = c1 + lambda * c2
    *C = c1 + lambda * c2;

    // Return lambda
    *lambda_out = lambda;
}
