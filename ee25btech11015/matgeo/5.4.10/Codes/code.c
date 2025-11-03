#include <stdio.h>

// Compute determinant of 3x3 matrix
float determinant(float A[3][3]) {
    return A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1])
         - A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0])
         + A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0]);
}

// Function to compute inverse of 3x3 matrix
int matrix_inverse(float A[3][3], float inverse[3][3]) {
    float det = determinant(A);
    if (det == 0) return 0; // singular, no inverse

    float adj[3][3];

    // Cofactor matrix
    adj[0][0] =  (A[1][1]*A[2][2] - A[1][2]*A[2][1]);
    adj[0][1] = -(A[1][0]*A[2][2] - A[1][2]*A[2][0]);
    adj[0][2] =  (A[1][0]*A[2][1] - A[1][1]*A[2][0]);

    adj[1][0] = -(A[0][1]*A[2][2] - A[0][2]*A[2][1]);
    adj[1][1] =  (A[0][0]*A[2][2] - A[0][2]*A[2][0]);
    adj[1][2] = -(A[0][0]*A[2][1] - A[0][1]*A[2][0]);

    adj[2][0] =  (A[0][1]*A[1][2] - A[0][2]*A[1][1]);
    adj[2][1] = -(A[0][0]*A[1][2] - A[0][2]*A[1][0]);
    adj[2][2] =  (A[0][0]*A[1][1] - A[0][1]*A[1][0]);

    // Transpose adjoint and divide by determinant → inverse
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            inverse[i][j] = adj[j][i] / det;
        }
    }
    return 1;
}
