// File: transform.c
#include <stdio.h>

void matvec2x2(double mat[2][2], double vec[2], double result[2]) {
    for (int i = 0; i < 2; i++) {
        result[i] = 0;
        for (int j = 0; j < 2; j++) {
            result[i] += mat[i][j] * vec[j];
        }
    }
}

void matvec3x3(double mat[3][3], double vec[3], double result[3]) {
    for (int i = 0; i < 3; i++) {
        result[i] = 0;
        for (int j = 0; j < 3; j++) {
            result[i] += mat[i][j] * vec[j];
        }
    }
}

