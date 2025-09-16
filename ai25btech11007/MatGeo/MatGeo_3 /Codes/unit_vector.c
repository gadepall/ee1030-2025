#include <stdio.h>

// Custom sqrt function using Newton-Raphson method
double mySqrt(double n) {
    double x = n;
    double root;
    int i;

    if (n == 0) return 0;

    // Iterate to improve accuracy
    for (i = 0; i < 20; i++) {
        root = 0.5 * (x + (n / x));
        x = root;
    }
    return root;
}

int main() {
    // Given vectors a = (1, -7, 7), b = (3, -2, 2)
    double a[3] = {1, -7, 7};
    double b[3] = {3, -2, 2};
    double n[3];   // cross product
    double magnitude, unit[3];

    // Cross product: n = a × b
    n[0] = a[1]*b[2] - a[2]*b[1]; // i component
    n[1] = a[2]*b[0] - a[0]*b[2]; // j component
    n[2] = a[0]*b[1] - a[1]*b[0]; // k component

    // Magnitude of vector n using custom sqrt
    magnitude = mySqrt(n[0]*n[0] + n[1]*n[1] + n[2]*n[2]);

    // Unit vector = n / |n|
    unit[0] = n[0] / magnitude;
    unit[1] = n[1] / magnitude;
    unit[2] = n[2] / magnitude;

    // Output results
    printf("Vector perpendicular to both a and b: (%.2f, %.2f, %.2f)\n", n[0], n[1], n[2]);
    printf("Unit vector: (%.6f, %.6f, %.6f)\n", unit[0], unit[1], unit[2]);

    return 0;
}
