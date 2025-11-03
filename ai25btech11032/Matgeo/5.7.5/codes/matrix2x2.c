// All matrices are 2x2, flattened in row-major order:
// [a11, a12,
//  a21, a22]

void mat2_mul(const double *A, const double *B, double *C) {
    // C = A * B
    double a11 = A[0], a12 = A[1], a21 = A[2], a22 = A[3];
    double b11 = B[0], b12 = B[1], b21 = B[2], b22 = B[3];

    C[0] = a11*b11 + a12*b21; // c11
    C[1] = a11*b12 + a12*b22; // c12
    C[2] = a21*b11 + a22*b21; // c21
    C[3] = a21*b12 + a22*b22; // c22
}

void mat2_square(const double *A, double *C) {
    // C = A^2
    mat2_mul(A, A, C);
}

