void find_eigenvector(double A[2][2], double eigenvalue, double eigenvector[2]) {
    double B[2][2];
    B[0][0] = A[0][0] - eigenvalue;
    B[0][1] = A[0][1];
    B[1][0] = A[1][0];
    B[1][1] = A[1][1] - eigenvalue;

    eigenvector[0] = -B[0][1];
    eigenvector[1] = B[0][0];
}

// Wrapper function to be called from Python
void get_eigenvectors(double A[2][2], double eigenvalues[2], double out_vec1[2], double out_vec2[2]) {
    find_eigenvector(A, eigenvalues[0], out_vec1);
    find_eigenvector(A, eigenvalues[1], out_vec2);
}
