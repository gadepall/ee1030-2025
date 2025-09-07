#include <stdio.h>

// Function to compute P and Q points
void compute_points(double *Px, double *Py, double *Pz, double *Qx, double *Qy, double *Qz) {
    // Given data
    double A[3] = {6, 7, 4};
    double AB[3] = {3, -1, 1};
    double C[3] = {0, -9, 2};
    double CD[3] = {-3, 2, 4};

    // Solve equations (precomputed λ = -2, μ = -3)
    double lambda = -2, mu = -3;

    // Point P = A + λ*AB
    *Px = A[0] + lambda * AB[0];
    *Py = A[1] + lambda * AB[1];
    *Pz = A[2] + lambda * AB[2];

    // Point Q = C + μ*CD
    *Qx = C[0] + mu * CD[0];
    *Qy = C[1] + mu * CD[1];
    *Qz = C[2] + mu * CD[2];
}
