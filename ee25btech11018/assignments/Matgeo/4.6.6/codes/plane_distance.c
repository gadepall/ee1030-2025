#include <stdio.h>
#include <math.h>

void plane_from_points(double P1[3], double P2[3], double P3[3], double coeff[4]) {
    coeff[0] = (P2[1]-P1[1])*(P3[2]-P1[2]) - (P2[2]-P1[2])*(P3[1]-P1[1]);
    coeff[1] = (P2[2]-P1[2])*(P3[0]-P1[0]) - (P2[0]-P1[0])*(P3[2]-P1[2]);
    coeff[2] = (P2[0]-P1[0])*(P3[1]-P1[1]) - (P2[1]-P1[1])*(P3[0]-P1[0]);
    coeff[3] = -(coeff[0]*P1[0] + coeff[1]*P1[1] + coeff[2]*P1[2]);
}

void parallel_plane_through_point(double coeff[4], double Q[3], double coeff2[4]) {
    coeff2[0] = coeff[0];
    coeff2[1] = coeff[1];
    coeff2[2] = coeff[2];
    coeff2[3] = -(coeff2[0]*Q[0] + coeff2[1]*Q[1] + coeff2[2]*Q[2]);
}

double norm(double *n) {
    return sqrt(n[0]*n[0] + n[1]*n[1] + n[2]*n[2]);
}

double plane_distance(double *n, double d1, double d2) {
    double num = fabs(d1 - d2);
    double denom = norm(n);
    return num / denom;
}


