#include <stdio.h>
#include <math.h>

// Function to calculate angle between two 3D vectors
double angle_between_lines(double v1[3], double v2[3]) {
    double dot = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2];
    double mag1 = sqrt(v1[0]*v1[0] + v1[1]*v1[1] + v1[2]*v1[2]);
    double mag2 = sqrt(v2[0]*v2[0] + v2[1]*v2[1] + v2[2]*v2[2]);

    if (mag1 == 0 || mag2 == 0) {
        return -1; // invalid case
    }

    double cos_theta = dot / (mag1 * mag2);

    if (cos_theta > 1) cos_theta = 1;
    if (cos_theta < -1) cos_theta = -1;

    return acos(cos_theta); // radians
}

