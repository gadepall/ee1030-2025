#include <stdio.h>

int solve_2x2(double A[4], double b[2], double x[2]) {
    double det = A[0]*A[3] - A[1]*A[2]; 

    if (det == 0.0) {
        return -1; 
    }

    x[0] = (b[0]*A[3] - b[1]*A[1]) / det;
    x[1] = (A[0]*b[1] - A[2]*b[0]) / det;

    return 0; 
}
