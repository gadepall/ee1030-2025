// vector_angle.c
#include <math.h>

// This function returns the angle (in degrees) between two 3D vectors
double angle_between_vectors(double* a, double* b) {
    double dot = a[0]*b[0] + a[1]*b[1] + a[2]*b[2];

    double mag_a = sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2]);
    double mag_b = sqrt(b[0]*b[0] + b[1]*b[1] + b[2]*b[2]);

    double cos_theta = dot / (mag_a * mag_b);

    // Clamp cos_theta to [-1, 1] to avoid acos domain errors
    if (cos_theta > 1.0) cos_theta = 1.0;
    if (cos_theta < -1.0) cos_theta = -1.0;

    double angle_rad = acos(cos_theta);
    double angle_deg = angle_rad * (180.0 / M_PI);

    return angle_deg;
}

