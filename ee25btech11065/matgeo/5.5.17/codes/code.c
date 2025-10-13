#include <stdio.h>

void inverse3x3(double A[3][3], double inv[3][3]);
void multiply3x3_3x1(double A[3][3], double B[3], double result[3]);
void printVector(double v[3]);

int main() {
    double A[3][3] = {
        {1, 1, 1},
        {0, 1, 3},
        {1, -2, 1}
    };
    double b[3] = {6, 11, 0};
    double A_inv[3][3];
    double x[3];

    inverse3x3(A, A_inv);
    multiply3x3_3x1(A_inv, b, x);

    printf("Solution:\n");
    printf("x = %.6lf\n", x[0]);
    printf("y = %.6lf\n", x[1]);
    printf("z = %.6lf\n", x[2]);

    return 0;
}

void inverse3x3(double A[3][3], double inv[3][3]) {
    double det =
          A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1])
        - A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0])
        + A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0]);

    if(det == 0) {
        printf("Matrix is singular, no inverse.\n");
        return;
    }

    double invDet = 1.0 / det;

    inv[0][0] =  (A[1][1]*A[2][2] - A[1][2]*A[2][1]) * invDet;
    inv[0][1] = -(A[0][1]*A[2][2] - A[0][2]*A[2][1]) * invDet;
    inv[0][2] =  (A[0][1]*A[1][2] - A[0][2]*A[1][1]) * invDet;

    inv[1][0] = -(A[1][0]*A[2][2] - A[1][2]*A[2][0]) * invDet;
    inv[1][1] =  (A[0][0]*A[2][2] - A[0][2]*A[2][0]) * invDet;
    inv[1][2] = -(A[0][0]*A[1][2] - A[0][2]*A[1][0]) * invDet;

    inv[2][0] =  (A[1][0]*A[2][1] - A[1][1]*A[2][0]) * invDet;
    inv[2][1] = -(A[0][0]*A[2][1] - A[0][1]*A[2][0]) * invDet;
    inv[2][2] =  (A[0][0]*A[1][1] - A[0][1]*A[1][0]) * invDet;
}

void multiply3x3_3x1(double A[3][3], double B[3], double result[3]) {
    for(int i = 0; i < 3; i++) {
        result[i] = 0;
        for(int j = 0; j < 3; j++) {
            result[i] += A[i][j] * B[j];
        }
    }
}

