#include <stdio.h>
#include <math.h>

// Structure to represent a 3D vector
typedef struct {
    double x, y, z;
} Vector3D;

// Function to compute dot product of two vectors
double dotProduct(Vector3D a, Vector3D b) {
    return a.x * b.x + a.y * b.y + a.z * b.z;
}

// Function to compute squared norm of a vector
double normSquared(Vector3D v) {
    return v.x * v.x + v.y * v.y + v.z * v.z;
}

// Function to compute division ratio k
double computeDivisionRatio(Vector3D A, Vector3D B, Vector3D P) {
    Vector3D A_minus_P = {A.x - P.x, A.y - P.y, A.z - P.z};
    Vector3D P_minus_B = {P.x - B.x, P.y - B.y, P.z - B.z};
    
    double numerator = dotProduct(A_minus_P, P_minus_B);
    double denominator = normSquared(P_minus_B);
    
    return numerator / denominator;
}

