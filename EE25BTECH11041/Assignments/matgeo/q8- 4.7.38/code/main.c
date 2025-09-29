#include <stdio.h>

// Function to compute coefficients of required plane
// Plane form: Ax + By + Cz + D = 0
// Returns coefficients via array coeff[4]
void find_plane(double coeff[4]) {
    // Plane 1: x - 2y + 3z - 4 = 0
    double A1 = 1, B1 = -2, C1 = 3, D1 = -4;

    // Plane 2: -2x + y + z + 5 = 0
    double A2 = -2, B2 = 1, C2 = 1, D2 = 5;

    // Required plane = pi1 + λ*pi2
    // (A1 + λA2)x + (B1 + λB2)y + (C1 + λC2)z + (D1 + λD2) = 0

    // Condition: intercept on X = intercept on Y → A = B
    // So: A1 + λA2 = B1 + λB2
    double lambda = (B1 - A1) / (A2 - B2);

    double A = A1 + lambda * A2;
    double B = B1 + lambda * B2;
    double C = C1 + lambda * C2;
    double D = D1 + lambda * D2;

    coeff[0] = A;
    coeff[1] = B;
    coeff[2] = C;
    coeff[3] = D;
}

