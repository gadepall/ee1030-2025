#include <stdio.h>

typedef struct {
    double x, y, z;
} Vec3;

// Function to return points and direction vectors for lines
void get_lines(Vec3* P1, Vec3* d1, Vec3* P2, Vec3* d2, Vec3* P3, Vec3* d3) {
    // Line 1
    P1->x = 1; P1->y = -1; P1->z = 0;
    d1->x = 2; d1->y = -1; d1->z = 3;

    // Line 2
    P2->x = 0; P2->y = 2; P2->z = -1;
    d2->x = 4; d2->y = -2; d2->z = 6;

    // Line 3
    P3->x = 2; P3->y = 1; P3->z = 2;
    d3->x = 3; d3->y = 1; d3->z = 5;
}

