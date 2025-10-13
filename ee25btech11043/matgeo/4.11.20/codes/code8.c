#include <math.h> // For M_PI, atan2, sqrt

// Function to calculate the intersection point of a line with the XZ plane
// Line passes through (x1, y1, z1) and (x2, y2, z2)
// Intersection point is stored in (ix, iy, iz)
void findIntersectionAndAngle(
    double x1, double y1, double z1,
    double x2, double y2, double z2,
    double *ix, double *iy, double *iz,
    double *angle_degrees) {

    // Direction vector of the line (L = B - A)
    double Lx = x2 - x1;
    double Ly = y2 - y1;
    double Lz = z2 - z1;

    // For a point to be on the XZ plane, its y-coordinate must be 0.
    // Parametric equation of the line: P(t) = A + t * L
    // P(t) = (x1 + t*Lx, y1 + t*Ly, z1 + t*Lz)

    // Set the y-coordinate to 0:
    // y1 + t*Ly = 0
    // t*Ly = -y1
   
    double t = -y1 / Ly;
    

    // Calculate the intersection point coordinates
    *ix = x1 + t * Lx;
    *iy = y1 + t * Ly; // This should be 0 or close to 0
    *iz = z1 + t * Lz;

    // Calculate the angle with the XZ plane
    // The normal vector to the XZ plane is (0, 1, 0)
    // The angle theta between a line with direction vector L and a plane with normal vector N
    // is given by sin(theta) = |L . N| / (||L|| * ||N||)
    // N = (0, 1, 0), ||N|| = 1
    // L . N = (Lx * 0) + (Ly * 1) + (Lz * 0) = Ly
    // ||L|| = sqrt(Lx^2 + Ly^2 + Lz^2)

    double dot_product = Ly; // L . N
    double magnitude_L = sqrt(Lx * Lx + Ly * Ly + Lz * Lz);

        double sin_theta = fabs(dot_product) / magnitude_L;
        double angle_radians = asin(sin_theta);
        *angle_degrees = angle_radians * 180.0 / M_PI;
}