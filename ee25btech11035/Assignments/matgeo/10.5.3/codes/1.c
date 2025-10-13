#include<stdio.h>
#include <math.h>

#define M_PI 3.14159265358979323846

void calculate_tangent_points(double radius, double angle_deg, double* h, double* poc1, double* poc2) {
    // The half-angle in radians
    double theta = (angle_deg / 2.0) * (M_PI / 180.0);

    // Calculate the distance of the intersection point h from the origin.
    // We place h on the positive x-axis for simplicity.
    double dist_h = radius / sin(theta);
    h[0] = dist_h;
    h[1] = 0.0;

    // The coordinates of the points of contact are derived from the geometry
    // of the right-angled triangle formed by the origin, h, and the point of contact.
    poc1[0] = radius * sin(theta);
    poc1[1] = radius * cos(theta);
    
    poc2[0] = radius * sin(theta);
    poc2[1] = -radius * cos(theta);
}