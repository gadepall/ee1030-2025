#include <math.h>

// Function to calculate the dot product of two 3D vectors
double dot_product(double v1x, double v1y, double v1z,
                   double v2x, double v2y, double v2z) {
    return v1x * v2x + v1y * v2y + v1z * v2z;
}

// Function to calculate the magnitude of a 3D vector
double magnitude(double vx, double vy, double vz) {
    return sqrt(vx * vx + vy * vy + vz * vz);
}

// Function to calculate the cosines of angles between (A+B+C) and A, B, C
// Arguments:
//   ax, ay, az: Components of vector A
//   bx, by, bz: Components of vector B
//   cx, cy, cz: Components of vector C
//   cos_angle_result: Pointer to an array of 3 doubles to store the results
void calculate_angles_cosines(double ax, double ay, double az,
                              double bx, double by, double bz,
                              double cx, double cy, double cz,
                              double* cos_angle_result) {

    // Calculate the resultant vector R = A + B + C
    double rx = ax + bx + cx;
    double ry = ay + by + cy;
    double rz = az + bz + cz;

    // Calculate magnitudes
    double mag_A = magnitude(ax, ay, az);
    double mag_B = magnitude(bx, by, bz);
    double mag_C = magnitude(cx, cy, cz);
    double mag_R = magnitude(rx, ry, rz);

    // Calculate dot products
    double dot_R_A = dot_product(rx, ry, rz, ax, ay, az);
    double dot_R_B = dot_product(rx, ry, rz, bx, by, bz);
    double dot_R_C = dot_product(rx, ry, rz, cx, cy, cz);

    // Calculate cosines of angles
    // Handle potential division by zero for zero vectors
    if (mag_A > 1e-9 && mag_R > 1e-9) {
        cos_angle_result[0] = dot_R_A / (mag_R * mag_A);
    } else {
        // If A or R is a zero vector, special handling.
        // If both are zero, angle can be considered 0 (cos=1).
        // If one is zero and other non-zero, angle is 90 (cos=0).
        cos_angle_result[0] = (mag_A < 1e-9 && mag_R < 1e-9) ? 1.0 : 0.0;
    }

    if (mag_B > 1e-9 && mag_R > 1e-9) {
        cos_angle_result[1] = dot_R_B / (mag_R * mag_B);
    } else {
        cos_angle_result[1] = (mag_B < 1e-9 && mag_R < 1e-9) ? 1.0 : 0.0;
    }

    if (mag_C > 1e-9 && mag_R > 1e-9) {
        cos_angle_result[2] = dot_R_C / (mag_R * mag_C);
    } else {
        cos_angle_result[2] = (mag_C < 1e-9 && mag_R < 1e-9) ? 1.0 : 0.0;
    }
}
int main() {
    double ax, ay, az;
    double bx, by, bz;
    double cx, cy, cz;
    double cos_angles[3]; // Array to store the 3 cosine results


    // Call the function to calculate the cosines
    calculate_angles_cosines(ax, ay, az, bx, by, bz, cx, cy, cz, cos_angles);

    // Calculate angles in degrees
    double angle_RA_deg = acos(cos_angles[0]) * 180.0 / M_PI;
    double angle_RB_deg = acos(cos_angles[1]) * 180.0 / M_PI;
    double angle_RC_deg = acos(cos_angles[2]) * 180.0 / M_PI;

     return 0;
}