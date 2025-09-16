#include <math.h>

// Function to compute angle (in radians) between two 3D vectors
double angle_between(double ax, double ay, double az,
                     double bx, double by, double bz) {
    double dot = ax*bx + ay*by + az*bz;

    double mag_a = sqrt(ax*ax + ay*ay + az*az);
    double mag_b = sqrt(bx*bx + by*by + bz*bz);

    if (mag_a == 0.0 || mag_b == 0.0) {
        return -1.0;  // invalid
    }

    double cos_theta = dot / (mag_a * mag_b);
    if (cos_theta > 1.0) cos_theta = 1.0;
    if (cos_theta < -1.0) cos_theta = -1.0;

    return acos(cos_theta);
}
