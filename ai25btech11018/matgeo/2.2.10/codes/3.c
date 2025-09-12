#include <stdio.h>
#include <math.h>

// Function to compute dot product of two vectors
double dot(double v1[3], double v2[3]) {
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2];
}

// Function to compute magnitude of vector
double magnitude(double v[3]) {
    return sqrt(dot(v, v));
}

int main() {
    // Given vectors A and B
    double A[3] = {3, -2, 2};
    double B[3] = {1, 0, -2};
    double d1[3], d2[3];
    double cos_theta, theta;

 // Compute diagonals
    for (int i = 0; i < 3; i++) {
        d1[i] = A[i] + B[i]; // A + B
        d2[i] = A[i] - B[i]; // A - B
    }

    // Compute cosine of angle
    cos_theta = dot(d1, d2) / (magnitude(d1) * magnitude(d2));

    // Clamp value to [-1, 1] for numerical stability
    if (cos_theta > 1.0) cos_theta = 1.0;
    if (cos_theta < -1.0) cos_theta = -1.0;

    // Angle in radians
    theta = acos(cos_theta);

  

  // Convert to degrees
    theta = theta * 180.0 / M_PI;

    // Ensure acute angle
    if (theta > 90.0) {
        theta = 180.0 - theta;
    }

    printf("The acute angle between diagonals is: %.2f degrees\n", theta);

    return 0;
}
