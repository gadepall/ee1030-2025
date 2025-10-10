// cross.c
#include <stdio.h>

// Function to compute 2D cross product of two vectors
double cross(double u[2], double v[2]) {
    return u[0] * v[1] - u[1] * v[0];
}

