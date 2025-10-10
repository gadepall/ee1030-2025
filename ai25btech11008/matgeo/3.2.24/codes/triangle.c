#include <stdio.h>
#include <math.h>

// Function to calculate dot product of two vectors
double dotProduct(double A[], double B[]) {
    return A[0]*B[0] + A[1]*B[1];
}

// Function to calculate magnitude of a vector
double magnitude(double V[]) {
    return sqrt(V[0]*V[0] + V[1]*V[1]);
}

// Function to calculate angle (in degrees) between two vectors
double angleBetweenVectors(double A[], double B[]) {
    double dot = dotProduct(A, B);
    double magA = magnitude(A);
    double magB = magnitude(B);
    double cosTheta = dot / (magA * magB);

    // Clamp cosTheta between -1 and 1 to avoid domain errors in acos due to floating point errors
    if (cosTheta > 1.0) cosTheta = 1.0;
    else if (cosTheta < -1.0) cosTheta = -1.0;

    double angleRad = acos(cosTheta); // angle in radians
    double angleDeg = angleRad * (180.0 / M_PI); // convert to degrees
    return angleDeg;
}

int main() {
    // Vector AB = B - A = (5, 0)
    double AB[2] = {5.0, 0.0};

    // Vector AC = C - A = (3*sqrt(2), 3*sqrt(2))
    double AC[2] = {3.0 * sqrt(2), 3.0 * sqrt(2)};

    double angle = angleBetweenVectors(AB, AC);

    printf("The angle between vectors AB and AC is: %.2f degrees\n", angle);

    return 0;
}

