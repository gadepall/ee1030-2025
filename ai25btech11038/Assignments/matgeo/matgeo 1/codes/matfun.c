// matfun.c
#include <stdio.h>

// Compute k using the projection formula
double find_k(double P[3], double Q[3], double R[3]) {
    double RP[3], QP[3];
    double dot = 0.0, norm_sq = 0.0;

    // Compute R-P and Q-P
    for (int i = 0; i < 3; i++) {
        RP[i] = R[i] - P[i];
        QP[i] = Q[i] - P[i];
    }

    // Dot product (Q-P) . (R-P) and ||R-P||^2
    for (int i = 0; i < 3; i++) {
        dot += QP[i] * RP[i];
        norm_sq += RP[i] * RP[i];
    }

    return dot / norm_sq;
}

// Get ratio m:n
void find_ratio(double P[3], double Q[3], double R[3], double *m, double *n) {
    double k = find_k(P, Q, R);
    *m = k;         // from P to Q
    *n = 1.0 - k;   // from Q to R
}
