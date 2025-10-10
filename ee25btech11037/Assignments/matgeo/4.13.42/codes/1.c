#include <math.h>
#include<stdio.h>

#define PI 3.14159265358979323846

void compute_vectors(double alpha_deg, double theta_deg, double* P, double* Q) {
    double alpha = alpha_deg * (PI / 180.0);
    double theta = theta_deg * (PI / 180.0);

    // Compute P
    P[0] = cos(theta);
    P[1] = sin(theta);

    // Rotation matrix R
    double R[2][2] = {
        {cos(alpha), sin(alpha)},
        {-sin(alpha), cos(alpha)}
    };

    // Compute Q = R * P
    Q[0] = R[0][0] * P[0] + R[0][1] * P[1];
    Q[1] = R[1][0] * P[0] + R[1][1] * P[1];
}

