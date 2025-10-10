#ifndef TRIANGLE_H
#define TRIANGLE_H

typedef struct {
    double x;
    double y;
} Point;

// Solves for point A using linear algebra method
Point solve_point_A(double BC, double angle_B_deg, double angle_C_deg);

#endif

