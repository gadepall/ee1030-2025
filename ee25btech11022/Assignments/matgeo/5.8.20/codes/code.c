#include <stdio.h>

void solve_ages(double *minu, double *sonu) {
    double A[2][2] = {{1, -3}, {1, -2}};
    double B[2] = {-10, 10};
    double det = A[0][0]*A[1][1] - A[1][0]*A[0][1];

    // Inverse matrix elements
    double invA[2][2] = {{A[1][1]/det, -A[0][1]/det},
                         {-A[1][0]/det, A[0][0]/det}};

    // Multiply invA by B
    *minu = invA[0][0]*B[0] + invA[0][1]*B[1];
    *sonu = invA[1][0]*B[0] + invA[1][1]*B[1];
}

