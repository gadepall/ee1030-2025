#include <stdio.h>

void inverse(double (*matrix)[3]) {
    double I[3][3] = {
        {1,0,0},
        {0,1,0},
        {0,0,1}
    };
   
    double pivot = matrix[0][0];
    for(int i = 0; i < 3; i++) {
        matrix[0][i] /= pivot;
        I[0][i] /= pivot;
    }
   
   
    double factor = matrix[1][0];
    for(int i = 0; i < 3; i++) {
        matrix[1][i] -= factor * matrix[0][i];
        I[1][i] -= factor * I[0][i];
    }
   
    factor = matrix[2][0];
    for(int i = 0; i < 3; i++) {
        matrix[2][i] -= factor * matrix[0][i];
        I[2][i] -= factor * I[0][i];
    }
   
   
    pivot = matrix[1][1];
    for(int i = 0; i < 3; i++) {
        matrix[1][i] /= pivot;
        I[1][i] /= pivot;
    }
   

    factor = matrix[0][1];
    for(int i = 0; i < 3; i++) {
        matrix[0][i] -= factor * matrix[1][i];
        I[0][i] -= factor * I[1][i];
    }

    factor = matrix[2][1];
    for(int i = 0; i < 3; i++) {
        matrix[2][i] -= factor * matrix[1][i];
        I[2][i] -= factor * I[1][i];
    }
   

    pivot = matrix[2][2];
    for(int i = 0; i < 3; i++) {
        matrix[2][i] /= pivot;
        I[2][i] /= pivot;
    }
   
   
    factor = matrix[0][2];
    for(int i = 0; i < 3; i++) {
        matrix[0][i] -= factor * matrix[2][i];
        I[0][i] -= factor * I[2][i];
    }

    factor = matrix[1][2];
    for(int i = 0; i < 3; i++) {
        matrix[1][i] -= factor * matrix[2][i];
        I[1][i] -= factor * I[2][i];
    }

    for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        matrix[i][j] = I[i][j];
    }
}

}
