// lin_solver.c
#include <stdio.h>

void solve2x2(double A[2][2], double b[2], double result[2]) {
    double det = A[0][0]*A[1][1] - A[0][1]*A[1][0];
    if (det == 0) {
        result[0] = result[1] = 0;
        return;
    }
    result[0] = (b[0]*A[1][1] - b[1]*A[0][1]) / det;
    result[1] = (A[0][0]*b[1] - A[1][0]*b[0]) / det;
}
