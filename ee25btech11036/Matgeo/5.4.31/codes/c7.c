#include <stdio.h>

// Function to compute inverse of a 2x2 matrix
// Input: double A[2][2]
// Output: double Inv[2][2]
// Returns: 0 if successful, -1 if singular
int inverse2x2(const double A[2][2], double Inv[2][2]) {
    double det = A[0][0]*A[1][1] - A[0][1]*A[1][0];

    if (det == 0.0) {
        return -1; // singular matrix
    }

    double invDet = 1.0 / det;

    Inv[0][0] =  A[1][1] * invDet;
    Inv[0][1] = -A[0][1] * invDet;
    Inv[1][0] = -A[1][0] * invDet;
    Inv[1][1] =  A[0][0] * invDet;

    return 0;
}

// For testing purpose (can be removed when used as .so)
#ifdef TEST_MAIN
int main() {
    double A[2][2] = { {1, 2}, {4, 2} };
    double Inv[2][2];

    if (inverse2x2(A, Inv) == 0) {
        printf("Inverse matrix:\n");
        printf("%lf %lf\n", Inv[0][0], Inv[0][1]);
        printf("%lf %lf\n", Inv[1][0], Inv[1][1]);
    } else {
        printf("Matrix is singular!\n");
    }

    return 0;
}
#endif

