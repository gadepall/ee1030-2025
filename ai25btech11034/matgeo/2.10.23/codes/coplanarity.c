#include <stdio.h>

// Function to check if A, B, D are coplanar
// Returns 1 if coplanar, 0 otherwise
int is_coplanar(double A[3], double B[3], double D[3]) {
    double cross[3];
    // Cross product B × D
    cross[0] = B[1]*D[2] - B[2]*D[1];
    cross[1] = B[2]*D[0] - B[0]*D[2];
    cross[2] = B[0]*D[1] - B[1]*D[0];

    // Dot product A · (B × D)
    double scalar_triple = A[0]*cross[0] + A[1]*cross[1] + A[2]*cross[2];

    return (scalar_triple == 0.0);
}

