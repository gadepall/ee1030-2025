#include <stdio.h>

// Function to compute dot product of two vectors
int dot(int a[3], int b[3]) {
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
}

// Function to calc determinant
int determinant3x3(int M[3][3]) {
    int det = M[0][0]*(M[1][1]*M[2][2] - M[1][2]*M[2][1])
            - M[0][1]*(M[1][0]*M[2][2] - M[1][2]*M[2][0])
            + M[0][2]*(M[1][0]*M[2][1] - M[1][1]*M[2][0]);
    return det;
}

int check_coplanar(int a[3], int b[3], int c[3]) {
    int G[3][3] = {
        { dot(a,a), dot(a,b), dot(a,c) },
        { dot(b,a), dot(b,b), dot(b,c) },
        { dot(c,a), dot(c,b), dot(c,c) }
    };
    int det = determinant3x3(G);
    return det == 0; // returns 1 if coplanar, 0 otherwise
}

