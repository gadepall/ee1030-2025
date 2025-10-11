#include <stdio.h>

// Function to check if C and D are perpendicular
// Returns 1 if perpendicular, 0 otherwise
int is_perpendicular(double C[3], double D[3]) {
    double dot = C[0]*D[0] + C[1]*D[1] + C[2]*D[2];
    return (dot == 0.0);
}

