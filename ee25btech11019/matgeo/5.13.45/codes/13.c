#include <stdio.h>

// Function to find determinant of 3x3 matrix
double determinant3x3(double A[3][3]) {
    return A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1])
         - A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0])
         + A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0]);
}

// Function to find inverse of 3x3 matrix
void inverse3x3(double A[3][3], double invA[3][3]) {
    double det = determinant3x3(A);
    if (det == 0) {
        printf("Matrix is singular, inverse not possible.\n");
        return;
    }

    invA[0][0] = (A[1][1]*A[2][2] - A[1][2]*A[2][1]) / det;
    invA[0][1] = (A[0][2]*A[2][1] - A[0][1]*A[2][2]) / det;
    invA[0][2] = (A[0][1]*A[1][2] - A[0][2]*A[1][1]) / det;

    invA[1][0] = (A[1][2]*A[2][0] - A[1][0]*A[2][2]) / det;
    invA[1][1] = (A[0][0]*A[2][2] - A[0][2]*A[2][0]) / det;
    invA[1][2] = (A[0][2]*A[1][0] - A[0][0]*A[1][2]) / det;

    invA[2][0] = (A[1][0]*A[2][1] - A[1][1]*A[2][0]) / det;
    invA[2][1] = (A[0][1]*A[2][0] - A[0][0]*A[2][1]) / det;
    invA[2][2] = (A[0][0]*A[1][1] - A[0][1]*A[1][0]) / det;
}

// Function for matrix multiplication (3x3)
void multiply3x3(double A[3][3], double B[3][3], double result[3][3]) {
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            result[i][j]=0;
            for(int k=0;k<3;k++){
                result[i][j]+=A[i][k]*B[k][j];
            }
        }
    }
}

// Function to compute R = P * Q * P^-1
void computeR(double P[3][3], double Q[3][3], double R[3][3]) {
    double Pinv[3][3];
    double temp[3][3];

    inverse3x3(P, Pinv);
    multiply3x3(P, Q, temp);
    multiply3x3(temp, Pinv, R);
}
