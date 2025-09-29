#include "matfun.h"

// Calculate dot product of two 3D vectors
double dot_product(const double a[3], const double b[3]) {
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
}

// Compute the foot of the perpendicular from point P to the Y-axis
void foot_of_perpendicular_to_Y_axis(const double P[3], double Q[3]) {
    // Direction vector of Y-axis
    double m[3] = {0.0, 1.0, 0.0};
    double m_norm_sq = dot_product(m, m);

    // dot product of m and P
    double dp = dot_product(m, P);

    // projection scalar
    double scalar = dp / m_norm_sq;

    // Q = scalar * m
    Q[0] = scalar * m[0];
    Q[1] = scalar * m[1];
    Q[2] = scalar * m[2];
}

