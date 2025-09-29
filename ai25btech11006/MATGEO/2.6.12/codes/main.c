#include <stdio.h>
#include <math.h>

// Function to compute magnitude of a vector
double magnitude(double v[3]) {
    return sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
}

// Function to compute cross product
void cross_product(double a[3], double b[3], double result[3]) {
    result[0] = a[1]*b[2] - a[2]*b[1];
    result[1] = a[2]*b[0] - a[0]*b[2];
    result[2] = a[0]*b[1] - a[1]*b[0];
}

int main() {
    double a[3] = {3, 1, 2};
    double b[3] = {2, -2, 4};
    double cross[3];

    // Compute cross product
    cross_product(a, b, cross);

    // Compute magnitudes
    double mag_a = magnitude(a);
    double mag_b = magnitude(b);
    double mag_cross = magnitude(cross);

    // Compute sine of angle
    double sine_theta = mag_cross / (mag_a * mag_b);

    printf("sin(theta) = %lf\n", sine_theta);

    return 0;
}

