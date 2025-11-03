#include <stdio.h>

void solve2x2(double A[2][2], double b[2], double result[2]) {
    double det = A[0][0]*A[1][1] - A[1][0]*A[0][1];
    result[0] = (b[0]*A[1][1] - b[1]*A[0][1]) / det; // x
    result[1] = (A[0][0]*b[1] - A[1][0]*b[0]) / det; // y
}

void rhombus_vertex(double n1[2], double c1,
                    double n2[2], double c2,
                    double O[2], double result[2]) {
    double A[2][2] = {{n1[0], n1[1]}, {n2[0], n2[1]}};
    double b[2] = {c1, c2};
    double VA[2];
    solve2x2(A, b, VA);

    double VC[2] = {2*O[0] - VA[0], 2*O[1] - VA[1]};

    double c1p = n1[0]*VC[0] + n1[1]*VC[1];

    double A2[2][2] = {{n1[0], n1[1]}, {n2[0], n2[1]}};
    double b2[2] = {c1p, c2};
    solve2x2(A2, b2, result);
}

