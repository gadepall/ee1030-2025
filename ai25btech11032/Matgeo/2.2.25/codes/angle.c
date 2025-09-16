#include <math.h>

// Function to compute angle in DEGREES between two vectors
double compute_angle_deg(double d1[3], double d2[3]) {
    // Dot product (matrix multiplication style)
    double dot = d1[0]*d2[0] + d1[1]*d2[1] + d1[2]*d2[2];

    // Norms
    double norm1 = sqrt(d1[0]*d1[0] + d1[1]*d1[1] + d1[2]*d1[2]);
    double norm2 = sqrt(d2[0]*d2[0] + d2[1]*d2[1] + d2[2]*d2[2]);

    // cos(theta)
    double cos_theta = dot / (norm1 * norm2);

    // Clamp for numerical safety
    if (cos_theta > 1.0) cos_theta = 1.0;
    if (cos_theta < -1.0) cos_theta = -1.0;

    // Return angle in degrees
    return acos(cos_theta) * (180.0 / M_PI);
}
