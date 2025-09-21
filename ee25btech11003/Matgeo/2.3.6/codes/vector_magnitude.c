#include <stdio.h>
#include <math.h>

// Function to calculate the magnitude of vectors
float findMagnitude(float angle_deg, float dot_product) {
    // Convert angle from degrees to radians
    float angle_rad = angle_deg * M_PI / 180.0;

    // Using formula: dot_product = r^2 * cos(theta)
    // => r = sqrt(dot_product / cos(theta))
    float magnitude = sqrt(dot_product / cos(angle_rad));

    return magnitude;
}

