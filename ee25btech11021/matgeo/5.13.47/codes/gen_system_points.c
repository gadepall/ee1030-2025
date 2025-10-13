// gen_system_points.c
#include <stdio.h>

void gen_system_points(double *A, double *B) {
    // Coefficient matrix (3x3)
    double tempA[9] = {
         1,  1, -1,   // Eqn 1
         1, -1,  1,   // Eqn 2
        -1,  1,  1    // Eqn 3
    };
    // RHS vector
    double tempB[3] = {1, 1, 1};

    for (int i = 0; i < 9; i++) A[i] = tempA[i];
    for (int i = 0; i < 3; i++) B[i] = tempB[i];
}

