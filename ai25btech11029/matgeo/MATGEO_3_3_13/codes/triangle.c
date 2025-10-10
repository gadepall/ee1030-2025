#include <math.h>
#include "triangle.h"

#define DEG2RAD(x) ((x) * M_PI / 180.0)

Point solve_point_A(double BC, double angle_B_deg, double angle_C_deg) {
    double angle_B = DEG2RAD(angle_B_deg);
    double angle_C = DEG2RAD(angle_C_deg);

    // Matrix setup
    double M[2][2] = {
        {cos(angle_C), cos(angle_B)},
        {sin(angle_C), -sin(angle_B)}
    };
    double rhs[2] = {BC, 0};

    // Gaussian elimination to solve for c
    double factor = M[1][0] / M[0][0];
    M[1][1] -= factor * M[0][1];
    rhs[1] -= factor * rhs[0];

    double sqrt2 = sqrt(2.0);
    double sqrt3 = sqrt(3.0);
    double c = (-7.0 * sqrt3 * sqrt2) / (-1.0 + sqrt3);


    // Compute point A from direction of angle B
    Point A;
    A.x = c * cos(angle_B);
    A.y = c * sin(angle_B);
    return A;
}

