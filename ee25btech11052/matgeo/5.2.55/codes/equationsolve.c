#include <stdio.h>
#include <math.h>

double determinant2x2(double a[2][2]) {
    return a[0][0] * a[1][1] - a[0][1] * a[1][0];
}

int inverse2x2(double a[2][2], double inv[2][2]) {
    double det = determinant2x2(a);
    if (fabs(det) < 1e-9) return 0; // singular matrix
    
    inv[0][0] = a[1][1] / det;
    inv[0][1] = -a[0][1] / det;
    inv[1][0] = -a[1][0] / det;
    inv[1][1] = a[0][0] / det;
    
    return 1;
}

void matrix_multiply2x2(double a[2][2], double b[2], double result[2]) {
    result[0] = a[0][0] * b[0] + a[0][1] * b[1];
    result[1] = a[1][0] * b[0] + a[1][1] * b[1];
}

int solve_system(double A[2][2], double b[2], double result[2]) {
    double A_inv[2][2];
    
    if (!inverse2x2(A, A_inv)) return 0;
    
    matrix_multiply2x2(A_inv, b, result);
    return 1;
}