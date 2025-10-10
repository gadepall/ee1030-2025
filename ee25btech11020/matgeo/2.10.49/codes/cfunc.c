#include <stdio.h>
#include <math.h>

double* solve_q2_10_49(double A[3], double B[3], double C[3]) {
    static double result[3];  
    double A_dot_C = A[0]*C[0] + A[1]*C[1] + A[2]*C[2];
    double B_dot_C = B[0]*C[0] + B[1]*C[1] + B[2]*C[2];
    double a = 1.0;
    double b = -(A_dot_C / B_dot_C);
    double P[3];
    for (int i = 0; i < 3; i++) {
        P[i] = a*A[i] + b*B[i];
    }
    double norm = sqrt(P[0]*P[0] + P[1]*P[1] + P[2]*P[2]);
    for (int i = 0; i < 3; i++) {
        result[i] = P[i] / norm;
    }
    return result;
}

