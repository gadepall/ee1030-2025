#include <math.h> // Required for sqrt() and fabs()

// Define a small constant for floating-point comparisons
#define EPSILON 1e-9

// Structure to represent a 3D vector
typedef struct {
    double x;
    double y;
    double z;
} Vector3D;

/**
 * @brief Calculates the magnitude (length) of a 3D vector.
 * @param v The input Vector3D.
 * @return The magnitude of the vector.
 */
double vector_magnitude(Vector3D v) {
    return sqrt(v.x * v.x + v.y * v.y + v.z * v.z);
}

/**
 * @brief Checks if the sum vector (a + b) bisects the angle between vectors a and b.
 *        Based on the mathematical proof, this is true if and only if ||a|| == ||b||.
 *        Uses a tolerance (EPSILON) for floating-point comparison.
 * @param a The first vector.
 * @param b The second vector.
 * @return 1 (true) if ||a|| is approximately equal to ||b||, 0 (false) otherwise.
 */
int does_sum_bisect_angle(Vector3D a, Vector3D b) {
    double mag_a = vector_magnitude(a);
    double mag_b = vector_magnitude(b);

    // Compare magnitudes with a small tolerance for floating-point numbers.
    // If the absolute difference is less than EPSILON, consider them equal.
    if (fabs(mag_a - mag_b) < EPSILON) {
        return 1; // Magnitudes are approximately equal.
    } else {
        return 0; // Magnitudes are not equal.
    }
}
