#ifndef COPLANAR_H
#define COPLANAR_H

#include <stdio.h>

typedef struct {
    double x;
    double y;
    double z;
} Point;

// Function to compute vector b-a
Point vector(Point a, Point b) {
    Point res = {b.x - a.x, b.y - a.y, b.z - a.z};
    return res;
}

// Cross product
Point cross(Point u, Point v) {
    Point res = {
        u.y * v.z - u.z * v.y,
        u.z * v.x - u.x * v.z,
        u.x * v.y - u.y * v.x
    };
    return res;
}

// Dot product
double dot(Point u, Point v) {
    return u.x * v.x + u.y * v.y + u.z * v.z;
}

// Function to compute value of x for coplanarity
double solve_for_x(Point A, Point C, Point D) {
    // AC and AD vectors
    Point AC = vector(A, C);
    Point AD = vector(A, D);

    // Cross product AC × AD
    Point cross_prod = cross(AC, AD);

    // Scalar triple product condition:
    // (1, x-2, 4) ⋅ (cross_prod) = 0
    // => coeff_x * x + constant = 0
    double coeff_x = cross_prod.y;
    double constant = cross_prod.x + (-2)*cross_prod.y + 4*cross_prod.z;

    return -constant / coeff_x;
}

#endif

