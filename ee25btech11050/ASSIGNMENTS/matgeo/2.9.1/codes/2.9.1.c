#include <stdio.h>
#include <math.h>

// Output: out[0]=Rx, out[1]=Ry, out[2]=Sx, out[3]=Sy, out[4]=area, out[5]=diagonal, out[6]=Cx, out[7]=Cy, out[8]=K
void solve_from_pdf(double* out) {
    // Points from PDF
    double P[2] = {-200, 0};
    double Q[2] = {200, 0};
    double A[2] = {200, 800};

    // Side vector PQ
    double X[2] = {Q[0] - P[0], Q[1] - P[1]}; // [400, 0]
    // Rotate X by 90 deg anticlockwise to get Y (QR)
    double Y[2] = {0 - X[1], X[0]};           // [0, 400]

    // R = Q + Y = [200 + 0, 0 + 400] = [200, 400]
    double R[2] = {Q[0] + Y[0], Q[1] + Y[1]};

    // Z = Y, PS parallel to QR, so Z = [0, 400]
    // S = P + Z = [-200, 0 + 400] = [-200, 400]
    double S[2] = {P[0] + Y[0], P[1] + Y[1]};

    // Area and diagonal
    double x = sqrt(X[0]*X[0] + X[1]*X[1]);   // 400
    double area = x * x;
    double diag = x * sqrt(2);

    // Point C from PDF, lying on x-axis, with collinearity
    double C[2] = {-600, 0}; // from matrix rank/collinearity in PDF

    // K for S dividing CA in K:1
    // S = (K*A + C)/(K+1) --> solve for K using x or y (use y)
    double K = (S[1] - C[1]) / (A[1] - S[1]);

    out[0] = R[0];
    out[1] = R[1];
    out[2] = S[0];
    out[3] = S[1];
    out[4] = area;
    out[5] = diag;
    out[6] = C[0];
    out[7] = C[1];
    out[8] = K;
}







