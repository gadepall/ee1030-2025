#include<stdio.h>

void collinear(double A[2]){
    double B[2]={-5,7};
    double C[2]={-4,5};
    double M[2][2]={A[0]-C[0],A[1]-C[1],B[0]-C[0],B[1]-C[1]};

    int j;

    // Make the pivot in row 1, col 0 to 1
    if (M[0][0] != 0) {
        double pivot = M[0][0];
        for (j = 0; j < 2; j++) {
            M[0][j] /= pivot;
        }
    }

    // Eliminate below pivot (row 2, col 0)
    if (M[1][0] != 0) {
        double factor = M[1][0];
        for (j = 0; j < 2; j++) {
            M[1][j] -= factor*M[0][j];
        }
    }

    if(M[1][0]==0 && M[1][1]==0){
        printf("The point is collinear with the other points");
    }
    else{
        printf("The point is not collinear with the other points");
    }
}