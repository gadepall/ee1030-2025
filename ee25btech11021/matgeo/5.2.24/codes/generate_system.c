#include <stdio.h>

// Function to generate coefficient matrix A and RHS vector b
// System:  px + qy = p - q
//          qx - py = p + q
void generate_system(double p, double q, double *A, double *b) {
    // Fill matrix A = [[p, q], [q, -p]]
    A[0] = p;   A[1] = q;
    A[2] = q;   A[3] = -p;

    // Fill vector b = [p - q, p + q]
    b[0] = p - q;
    b[1] = p + q;
}

int main() {
    double p = 2, q = 3;
    double A[4], b[2];
    
    generate_system(p, q, A, b);
    
    printf("Matrix A = [[%lf, %lf], [%lf, %lf]]\n", A[0], A[1], A[2], A[3]);
    printf("Vector b = [%lf, %lf]\n", b[0], b[1]);
    
    return 0;
}

