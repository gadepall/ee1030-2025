// intersection.c
#include <stdio.h>

void find_intersection(double *result) {
    double P[3] = {4, -3, -4};
    double Q[3] = {3, -2, 2};
    double n[3] = {2, 1, 1};
    double c = 6;

    double d[3];
    for (int i = 0; i < 3; i++) d[i] = Q[i] - P[i];

    // Compute t = (c - n·P) / (n·d)
    double num = c - (n[0]*P[0] + n[1]*P[1] + n[2]*P[2]);
    double den = n[0]*d[0] + n[1]*d[1] + n[2]*d[2];
    double t = num / den;

    // Compute intersection point
    for (int i = 0; i < 3; i++)
        result[i] = P[i] + t * d[i];
}

