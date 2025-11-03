#include <stdio.h>

void foot_of_perpendicular(double A[3], double B[3], double C[3], double foot[3]) {
    double d[3] = {C[0] - B[0], C[1] - B[1], C[2] - B[2]};
    double AB[3] = {A[0] - B[0], A[1] - B[1], A[2] - B[2]};

    double dot = AB[0]*d[0] + AB[1]*d[1] + AB[2]*d[2];
    double mag_sq = d[0]*d[0] + d[1]*d[1] + d[2]*d[2];
    double t = dot / mag_sq;

    for (int i = 0; i < 3; i++)
        foot[i] = B[i] + t * d[i];
}

void image_point(double A[3], double foot[3], double image[3]) {
    for (int i = 0; i < 3; i++)
        image[i] = 2 * foot[i] - A[i];
}

