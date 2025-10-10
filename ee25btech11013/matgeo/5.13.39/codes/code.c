#include <stdio.h>


int determinant(int n, int mat[n][n]){
    int det = mat[0][0]*(mat[1][1]*mat[2][2] - mat[1][2]*mat[2][1])
            - mat[0][1]*(mat[1][0]*mat[2][2] - mat[1][2]*mat[2][0])
            + mat[0][2]*(mat[1][0]*mat[2][1] - mat[1][1]*mat[2][0]);
    return det;
}

int solution(int a1, int b1, int c1, int alpha){
    return ((c1-a1*alpha)/b1);
}
