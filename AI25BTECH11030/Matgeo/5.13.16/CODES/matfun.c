// matfun.c
#include "matfun.h"

// Calculates foot of perpendicular from point P to line QR
void foot_of_perpendicular(const double *P, const double *Q, const double *R, double *foot) {
    double QR[2] = {R[0]-Q[0], R[1]-Q[1]};
    double QP[2] = {P[0]-Q[0], P[1]-Q[1]};
    double dot_QP_QR = QP[0]*QR[0] + QP[1]*QR[1];
    double dot_QR_QR = QR[0]*QR[0] + QR[1]*QR[1];
    double t = dot_QP_QR / dot_QR_QR;
    foot[0] = Q[0] + t * QR[0];
    foot[1] = Q[1] + t * QR[1];
}

// Combines two altitudes to determine orthocenter
void orthocenter(const double *A, const double *B, const double *C, double *O) {
    double footA[2], footB[2];
    foot_of_perpendicular(A, B, C, footA);
    foot_of_perpendicular(B, A, C, footB);

    double a1 = footA[1] - A[1];
    double b1 = A[0] - footA[0];
    double c1 = a1 * A[0] + b1 * A[1];

    double a2 = footB[1] - B[1];
    double b2 = B[0] - footB[0];
    double c2 = a2 * B[0] + b2 * B[1];

    double det = a1 * b2 - a2 * b1;
    if (det == 0) { // parallel lines
        O[0] = O[1] = 0.0;
        return;
    }
    O[0] = (c1 * b2 - c2 * b1) / det;
    O[1] = (a1 * c2 - a2 * c1) / det;
}

