#include <stdio.h>
#include <math.h>

// Function to compute determinant of 3x3 matrix
double det3(double M[3][3]) {
    return M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
         - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
         + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]);
}

// Function to compute inverse of 3x3 matrix
int inverse3(double M[3][3], double inv[3][3]) {
    double d = det3(M);
    if (fabs(d) < 1e-9) return 0; // singular

    inv[0][0] =  (M[1][1]*M[2][2]-M[1][2]*M[2][1])/d;
    inv[0][1] = -(M[0][1]*M[2][2]-M[0][2]*M[2][1])/d;
    inv[0][2] =  (M[0][1]*M[1][2]-M[0][2]*M[1][1])/d;

    inv[1][0] = -(M[1][0]*M[2][2]-M[1][2]*M[2][0])/d;
    inv[1][1] =  (M[0][0]*M[2][2]-M[0][2]*M[2][0])/d;
    inv[1][2] = -(M[0][0]*M[1][2]-M[0][2]*M[1][0])/d;

    inv[2][0] =  (M[1][0]*M[2][1]-M[1][1]*M[2][0])/d;
    inv[2][1] = -(M[0][0]*M[2][1]-M[0][1]*M[2][0])/d;
    inv[2][2] =  (M[0][0]*M[1][1]-M[0][1]*M[1][0])/d;

    return 1;
}

// Helper to compare matrices with tolerance
int equal(double A[3][3], double B[3][3], double tol) {
    for (int i=0;i<3;i++) {
        for (int j=0;j<3;j++) {
            if (fabs(A[i][j]-B[i][j])>tol) return 0;
        }
    }
    return 1;
}

// Main checker function: returns option number (1–4), or 0 if none
int check_matrices(double A[3][3], double B[3][3]) {
    double Ainv[3][3], Binv[3][3];
    if (!inverse3(A, Ainv)) return 0;
    if (!inverse3(B, Binv)) return 0;

    // Build 6B and (1/6)A
    double sixB[3][3], one6A[3][3];
    for (int i=0;i<3;i++) {
        for (int j=0;j<3;j++) {
            sixB[i][j] = 6*B[i][j];
            one6A[i][j] = A[i][j]/6.0;
        }
    }

    if (equal(Ainv, B, 1e-9)) return 1;
    if (equal(Ainv, sixB, 1e-9)) return 2;
    if (equal(Binv, B, 1e-9)) return 3;
    if (equal(Binv, one6A, 1e-9)) return 4;

    return 0;
}
