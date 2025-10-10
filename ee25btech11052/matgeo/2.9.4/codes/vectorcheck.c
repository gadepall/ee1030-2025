#include <stdio.h>
#include <math.h>

double magnitude(double b[3]) {
    return sqrt(b[0]*b[0] + b[1]*b[1] + b[2]*b[2]);
}

int solve_vector(double b[3]) {
    // Given: a = (1,1,1), a·b = 1, a×b = (0,1,-1)
    // From constraints: b₃ = 0, b₂ = 0, b₁ = 1
    b[0] = 1.0;
    b[1] = 0.0;
    b[2] = 0.0;
    
    return 1;
}

int verify_solution(double b[3]) {
    double a[3] = {1.0, 1.0, 1.0};
    
    // Check dot product: a·b = 1
    double dot = a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
    if (fabs(dot - 1.0) > 1e-9) return 0;
    
    // Check cross product: a×b = (0,1,-1)
    double cross[3];
    cross[0] = a[1]*b[2] - a[2]*b[1];  // should be 0
    cross[1] = a[2]*b[0] - a[0]*b[2];  // should be 1
    cross[2] = a[0]*b[1] - a[1]*b[0];  // should be -1
    
    if (fabs(cross[0] - 0.0) > 1e-9 || 
        fabs(cross[1] - 1.0) > 1e-9 || 
        fabs(cross[2] + 1.0) > 1e-9) return 0;
    
    return 1;
}