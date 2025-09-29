#include <stdio.h>

// Structure to represent a 3D point
typedef struct {
    int x;
    int y;
    int z;
} Point;

// Function to compute the normal vector PQ and plane equation
void findPlaneEquation(Point P, Point Q) {
    // Compute normal vector PQ = Q - P
    int a = Q.x - P.x;
    int b = Q.y - P.y;
    int c = Q.z - P.z;
    
    // Compute d using point Q
    int d = -(a * Q.x + b * Q.y + c * Q.z);
    
    // Print the equation of the plane
    printf("Equation of the plane: %dx + %dy + %dz + %d = 0\n", a, b, c, d);
}
