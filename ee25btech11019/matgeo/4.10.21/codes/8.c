#include <stdio.h>

// This function finds intersection point of given lines
// Line 1: through A(0, -1, -1) and B(4, 5, 1)
// Line 2: through C(3, 9, 4) and D(-4, 4, 4)
void intersection_point(double *x, double *y, double *z)
{
    // Given points
    double A[3] = {0, -1, -1};
    double B[3] = {4, 5, 1};

    // Direction vector of first line = B - A
    double AB[3];
    AB[0] = B[0] - A[0];
    AB[1] = B[1] - A[1];
    AB[2] = B[2] - A[2];

    // Second line points (C, D)
    double C[3] = {3, 9, 4};
    double D[3] = {-4, 4, 4};

    // Direction vector of second line = D - C
    double CD[3];
    CD[0] = D[0] - C[0];
    CD[1] = D[1] - C[1];
    CD[2] = D[2] - C[2];

    // We already know from solving z = -1 + 2λ = 4 → λ = 2.5
    double lambda = 2.5;

    // Substitute λ in first line
    *x = A[0] + lambda * AB[0];
    *y = A[1] + lambda * AB[1];
    *z = A[2] + lambda * AB[2];
}

