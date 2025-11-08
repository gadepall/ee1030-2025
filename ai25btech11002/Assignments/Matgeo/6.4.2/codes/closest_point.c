#include <stdio.h>
// Function to calculate lambda and mu
// Inputs: arrays A1[3], d1[3], A2[3], d2[3]
// Outputs: lambda and mu via pointers
void calc_lambda_mu(double A1[3], double d1[3], double A2[3], double d2[3], double* lambda, double* mu) {
    double D1D1=0, D1D2=0, D2D2=0;
    double RHS1=0, RHS2=0;

    double A2_minus_A1[3];
    for(int i=0;i<3;i++)
        A2_minus_A1[i] = A2[i] - A1[i];

    // Dot products
    for(int i=0;i<3;i++){
        D1D1 += d1[i]*d1[i];
        D1D2 += d1[i]*d2[i];
        D2D2 += d2[i]*d2[i];
        RHS1 += d1[i]*A2_minus_A1[i];
        RHS2 += d2[i]*A2_minus_A1[i];
    }

    // Solve 2x2 system:
    // [D1D1  -D1D2][lambda] = [RHS1]
    // [-D1D2  D2D2][mu    ] = [RHS2]

    double det = D1D1*D2D2 - D1D2*D1D2;
    if(det==0){
        *lambda = 0;
        *mu = 0;
        return; // lines are parallel or ill-conditioned
    }

    *lambda = (RHS1*D2D2 + RHS2*D1D2)/det;
    *mu     = (RHS2*D1D1 + RHS1*D1D2)/det;
}

