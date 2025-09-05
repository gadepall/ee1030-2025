#include <stdio.h>
#include <math.h>

// Function to compute x-coordinate of equidistant point
double equidistant_point(double ax, double ay, double bx, double by) {
    // Norm squared of A and B
    double normA2 = ax*ax + ay*ay;
    double normB2 = bx*bx + by*by;

    double denom = 2 * (ax - bx);

    
    double x = (normA2 - normB2) / denom;
    return x;
}

