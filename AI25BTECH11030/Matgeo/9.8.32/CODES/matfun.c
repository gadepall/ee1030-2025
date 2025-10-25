#include "matfun.h"
#include <math.h>

// Solve 2x2 system Ax = b using simple method
int solve_2x2(double A[4], double b[2], double x[2]) {
    // A = [a11, a12, a21, a22]  (row-major)
    double det = A[0]*A[3] - A[1]*A[2];
    
    if (fabs(det) < 1e-10) return 0;  // No solution
    
    x[0] = (b[0]*A[3] - b[1]*A[1]) / det;
    x[1] = (A[0]*b[1] - A[2]*b[0]) / det;
    
    return 1;  // Success
}

// Calculate distance between two points
double distance(double x1, double y1, double x2, double y2) {
    double dx = x1 - x2;
    double dy = y1 - y2;
    return sqrt(dx*dx + dy*dy);
}

// Solve the circle-parabola problem
int solve_problem(double center[2], double *radius) {
    // System: 4cx + 6cy = 19, cx + 4cy = 18
    double A[4] = {4.0, 6.0, 1.0, 4.0};
    double b[2] = {19.0, 18.0};
    
    if (!solve_2x2(A, b, center)) return 0;
    
    // Calculate radius from center to (0,1)
    *radius = distance(center[0], center[1], 0.0, 1.0);
    
    return 1;
}
