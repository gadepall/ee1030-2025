#include <stdio.h>

void find_fourth_vertex(double A[3], double B[3], double C[3], double D[3]) {
    D[0] = A[0] + C[0] - B[0];
    D[1] = A[1] + C[1] - B[1];
    D[2] = A[2] + C[2] - B[2];
}

