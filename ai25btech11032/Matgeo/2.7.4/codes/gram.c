#include <stdio.h>

// Dot product of two 3D vectors
double dot_product(double a[3], double b[3]) {
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
}

// Build Gram matrix from three 3D vectors
void gram_matrix(double a[3], double b[3], double c[3], double G[3][3]) {
    G[0][0] = dot_product(a,a);
    G[0][1] = dot_product(a,b);
    G[0][2] = dot_product(a,c);

    G[1][0] = dot_product(b,a);
    G[1][1] = dot_product(b,b);
    G[1][2] = dot_product(b,c);

    G[2][0] = dot_product(c,a);
    G[2][1] = dot_product(c,b);
    G[2][2] = dot_product(c,c);
}

// Determinant of a 3x3 matrix
double det3(double M[3][3]) {
    return M[0][0]*(M[1][1]*M[2][2] - M[1][2]*M[2][1])
         - M[0][1]*(M[1][0]*M[2][2] - M[1][2]*M[2][0])
         + M[0][2]*(M[1][0]*M[2][1] - M[1][1]*M[2][0]);
}

