#ifndef REFLECTION_H
#define REFLECTION_H

#include <stdio.h>

// Function to compute reflection of a point (x,y,z)
// across the plane x+y+z=1.
// The result is stored in (alpha, beta, gamma).
void reflect_point(double x, double y, double z,
                                 double *alpha, double *beta, double *gamma) {
    double n[3] = {1.0, 1.0, 1.0};   // Normal vector
    double d = 1.0;                  // Plane constant
    double norm_sq = 3.0;            // ||n||^2 = 1^2+1^2+1^2 = 3

    // Dot product n.q
    double dot = n[0]*x + n[1]*y + n[2]*z;

    // Reflection formula: s = q - 2((n.q - d)/||n||^2) * n
    *alpha = x - 2.0*(dot - d)/norm_sq * n[0];
    *beta  = y - 2.0*(dot - d)/norm_sq * n[1];
    *gamma = z - 2.0*(dot - d)/norm_sq * n[2];
}

#endif

