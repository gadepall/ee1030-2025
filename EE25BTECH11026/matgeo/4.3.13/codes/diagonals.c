#include <stdio.h>

void diagonal_equations(double vertices[4][2], double n1[2], double *c1, double n2[2], double *c2) {
    // A, B, C, D are the vertices
    double *A = vertices[0];
    double *B = vertices[1];
    double *C = vertices[2];
    double *D = vertices[3];

    // Diagonal AC
    double dx1 = C[0] - A[0];
    double dy1 = C[1] - A[1];
    n1[0] = dy1;
    n1[1] = -dx1;
    *c1 = n1[0]*A[0] + n1[1]*A[1];

    // Diagonal BD
    double dx2 = D[0] - B[0];
    double dy2 = D[1] - B[1];
    n2[0] = dy2;
    n2[1] = -dx2;
    *c2 = n2[0]*B[0] + n2[1]*B[1];
}

