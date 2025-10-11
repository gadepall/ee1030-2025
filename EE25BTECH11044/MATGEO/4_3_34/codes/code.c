#include <stdio.h>

int main() {
    // Augmented matrix for the system:
    // 2u - 3v = 1
    // 4u - 5v = 1
    double A[2][3] = {
        {2, -3, 1},
        {4, -5, 1}
    };

    // Step 1: R2 -> R2 - 2R1
    A[1][0] = A[1][0] - 2*A[0][0];
    A[1][1] = A[1][1] - 2*A[0][1];
    A[1][2] = A[1][2] - 2*A[0][2];

    // Step 2: R1 -> R1 + 3R2
    A[0][0] = A[0][0] + 3*A[1][0];
    A[0][1] = A[0][1] + 3*A[1][1];
    A[0][2] = A[0][2] + 3*A[1][2];

    // Step 3: R1 -> R1 / 2
    A[0][0] /= 2;
    A[0][1] /= 2;
    A[0][2] /= 2;

    // Now matrix is in reduced row echelon form
    double u = A[0][2];
    double v = A[1][2];

    // Back substitute to find a, b
    double a = 1.0 / u;
    double b = 1.0 / v;

    printf("u = %lf, v = %lf\n", u, v);
    printf("a = %lf, b = %lf\n", a, b);

    return 0;
}
