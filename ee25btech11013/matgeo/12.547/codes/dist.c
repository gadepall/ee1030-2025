#include <math.h>

double projection(const double *u1, const double *u2, const double *P, double *P_proj) {
    double U_TU[2][2], invU[2][2], UTP[2], coeff[2];

    // Compute Gram matrix U^T U
    U_TU[0][0] = u1[0]*u1[0] + u1[1]*u1[1] + u1[2]*u1[2];
    U_TU[0][1] = u1[0]*u2[0] + u1[1]*u2[1] + u1[2]*u2[2];
    U_TU[1][0] = U_TU[0][1];
    U_TU[1][1] = u2[0]*u2[0] + u2[1]*u2[1] + u2[2]*u2[2];

    // Inverse of 2x2 matrix
    double det = U_TU[0][0]*U_TU[1][1] - U_TU[0][1]*U_TU[1][0];
    invU[0][0] =  U_TU[1][1]/det;
    invU[0][1] = -U_TU[0][1]/det;
    invU[1][0] = -U_TU[1][0]/det;
    invU[1][1] =  U_TU[0][0]/det;

    // Compute U^T P
    UTP[0] = u1[0]*P[0] + u1[1]*P[1] + u1[2]*P[2];
    UTP[1] = u2[0]*P[0] + u2[1]*P[1] + u2[2]*P[2];

    // Compute coefficients
    coeff[0] = invU[0][0]*UTP[0] + invU[0][1]*UTP[1];
    coeff[1] = invU[1][0]*UTP[0] + invU[1][1]*UTP[1];

    // Compute projection point
    for(int i=0;i<3;i++)
        P_proj[i] = coeff[0]*u1[i] + coeff[1]*u2[i];

    // Compute distance
    double dist = 0.0;
    for(int i=0;i<3;i++)
        dist += (P[i] - P_proj[i]) * (P[i] - P_proj[i]);
    return sqrt(dist);
}
