#include <stdio.h>

int main() {
    // Coefficient matrix A
    double A[2][2] = {{2, 3}, {4, 6}};
    // Right-hand side vector B
    double B[2] = {8, 7};

    // Compute determinant
    double det = A[0][0]*A[1][1] - A[0][1]*A[1][0];

    if(det != 0) {
        // If determinant is non-zero, solve using Cramer's rule
        double x = (B[0]*A[1][1] - B[1]*A[0][1]) / det;
        double y = (A[0][0]*B[1] - A[1][0]*B[0]) / det;
        printf("Unique solution:\n");
        printf("x = %.2lf\n", x);
        printf("y = %.2lf\n", y);
    } else {
        // Determinant is zero, check for consistency
        if((A[0][0]*B[1] - A[1][0]*B[0] != 0) || (A[0][1]*B[1] - A[1][1]*B[0] != 0)) {
            printf("The system is inconsistent. No solution exists.\n");
        } else {
            printf("The system has infinitely many solutions.\n");
        }
    }

    return 0;
}