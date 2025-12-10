#include <stdio.h>

// Define a structure to hold the components of a 3D vector.
// This will be used for normal vectors and the direction vector.
typedef struct {
    double x;
    double y;
    double z;
} Vector3D;

// Define a structure to hold the coefficients of a plane equation (ax + by + cz + d = 0).
typedef struct {
    double a;
    double b;
    double c;
    double d;
} Plane;

/**
 * @brief Calculates the direction vector of the line of intersection between two planes.
 * * The direction vector is the cross product of the normal vectors of the two planes.
 * * @param p1 The first plane.
 * @param p2 The second plane.
 * @return Vector3D The direction vector of the intersection line.
 */
Vector3D find_intersection_direction(Plane p1, Plane p2) {
    // The normal vectors are derived from the coefficients of the planes.
    Vector3D n1 = {p1.a, p1.b, p1.c};
    Vector3D n2 = {p2.a, p2.b, p2.c};
    
    // Calculate the cross product of the two normal vectors.
    Vector3D direction_vector;
    direction_vector.x = (n1.y * n2.z) - (n1.z * n2.y);
    direction_vector.y = (n1.z * n2.x) - (n1.x * n2.z);
    direction_vector.z = (n1.x * n2.y) - (n1.y * n2.x);
    
    return direction_vector;
}
