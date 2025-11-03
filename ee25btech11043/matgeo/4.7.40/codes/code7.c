#include <stdio.h>
#include <math.h>

// Function to find the foot of the perpendicular and the perpendicular distance
// from a point (x0, y0, z0) to a line
// (x - x1)/a = (y - y1)/b = (z - z1)/c
void find_perpendicular_details(
    double x0, double y0, double z0, // Point P
    double x1, double y1, double z1, // Point on the line L
    double a, double b, double c,    // Direction ratios of the line L
    double *foot_x, double *foot_y, double *foot_z, // Output: Foot of perpendicular
    double *distance // Output: Perpendicular distance
) {
    // Vector PL (P - L)
    double PL_x = x0 - x1;
    double PL_y = y0 - y1;
    double PL_z = z0 - z1;

    // Direction vector of the line L (D)
    double D_x = a;
    double D_y = b;
    double D_z = c;

    // Calculate projection of PL onto D: t = (PL . D) / ||D||^2
    double dot_product = PL_x * D_x + PL_y * D_y + PL_z * D_z;
    double magnitude_D_squared = D_x * D_x + D_y * D_y + D_z * D_z;

    double t = dot_product / magnitude_D_squared;

    // Foot of the perpendicular F = L + t * D
    *foot_x = x1 + t * D_x;
    *foot_y = y1 + t * D_y;
    *foot_z = z1 + t * D_z;

    // Perpendicular vector PF = F - P
    double PF_x = *foot_x - x0;
    double PF_y = *foot_y - y0;
    double PF_z = *foot_z - z0;

    // Perpendicular distance = ||PF||
    *distance = sqrt(PF_x * PF_x + PF_y * PF_y + PF_z * PF_z);
}