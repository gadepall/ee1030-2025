#include <math.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

/* --- Helper Function --- */
// Calculates the Euclidean norm (magnitude) of a 3D vector.
static inline double calculate_norm(const double vec[3]) {
    return sqrt(vec[0] * vec[0] + vec[1] * vec[1] + vec[2] * vec[2]);
}

/* --- Core Logic Function --- */
// This function is "exported" so it can be called from other programs.
#ifdef __cplusplus
extern "C" {
#endif

double get_angle_between_lines() {
    // Direction ratios derived from solving the system of equations.
    double d1_ratios[] = {0.0, 1.0, -1.0};
    double d2_ratios[] = {1.0, 0.0, -1.0};
    double d1_cosines[3], d2_cosines[3];

    // Calculate the magnitude (norm) of each direction ratio vector.
    double norm_d1 = calculate_norm(d1_ratios);
    double norm_d2 = calculate_norm(d2_ratios);

    // Calculate the direction cosines by normalizing the vectors.
    for (int i = 0; i < 3; ++i) {
        d1_cosines[i] = d1_ratios[i] / norm_d1;
        d2_cosines[i] = d2_ratios[i] / norm_d2;
    }

    // Calculate the dot product of the two direction cosine vectors.
    double cos_theta = 0.0;
    for (int i = 0; i < 3; ++i) {
        cos_theta += d1_cosines[i] * d2_cosines[i];
    }
    
    // Calculate the angle in radians and convert to degrees.
    double angle_rad = acos(cos_theta);
    return angle_rad * (180.0 / M_PI);
}

#ifdef __cplusplus
}
#endif


