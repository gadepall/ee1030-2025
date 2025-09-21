
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// Function to compute cross product of two 3D vectors
void cross_product(double a[3], double b[3], double result[3]) {
    result[0] = a[1] * b[2] - a[2] * b[1];
    result[1] = a[2] * b[0] - a[0] * b[2];
    result[2] = a[0] * b[1] - a[1] * b[0];
}

// Function to compute dot product of two 3D vectors
double dot_product(double a[3], double b[3]) {
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
}

// Function to compute vector magnitude
double vector_magnitude(double v[3]) {
    return sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2]);
}

int main() {
    // Define vectors from the problem
    // First plane is determined by vectors i and i+j
    double v1[3] = {1, 0, 0};  // i vector
    double v2[3] = {1, 1, 0};  // i + j vector

    // Second plane is determined by vectors i-j and i+k
    double v3[3] = {1, -1, 0}; // i - j vector
    double v4[3] = {1, 0, 1};  // i + k vector

    // Calculate normal vectors for both planes
    double n1[3], n2[3], n3[3];

    // n1 = v1 × v2 (normal to first plane)
    cross_product(v1, v2, n1);
    printf("Normal vector n1: [%.1f, %.1f, %.1f]\n", n1[0], n1[1], n1[2]);

    // n2 = v3 × v4 (normal to second plane)
    cross_product(v3, v4, n2);
    printf("Normal vector n2: [%.1f, %.1f, %.1f]\n", n2[0], n2[1], n2[2]);

    // n3 = n1 × n2 (direction of line of intersection)
    cross_product(n1, n2, n3);
    printf("Intersection line direction n3: [%.1f, %.1f, %.1f]\n", n3[0], n3[1], n3[2]);

    // Vector a is parallel to the line of intersection
    double a[3] = {n3[0], n3[1], n3[2]};
    printf("Vector a: [%.1f, %.1f, %.1f]\n", a[0], a[1], a[2]);

    // Given vector u = i - 2j + 2k
    double u[3] = {1, -2, 2};
    printf("Vector u: [%.1f, %.1f, %.1f]\n", u[0], u[1], u[2]);

    // Calculate angle between a and u
    double dot_au = dot_product(a, u);
    double mag_a = vector_magnitude(a);
    double mag_u = vector_magnitude(u);

    double cos_theta = dot_au / (mag_a * mag_u);
    double theta_radians = acos(cos_theta);
    double theta_degrees = theta_radians * 180.0 / M_PI;

    printf("\nCalculations:\n");
    printf("a·u = %.1f\n", dot_au);
    printf("|a| = %.3f\n", mag_a);
    printf("|u| = %.1f\n", mag_u);
    printf("cos(θ) = %.3f\n", cos_theta);
    printf("θ = %.1f degrees\n", theta_degrees);

    // Save all vectors to vector.dat file
    FILE *file = fopen("vector.dat", "w");
    if (file != NULL) {
        fprintf(file, "v1 %.1f %.1f %.1f\n", v1[0], v1[1], v1[2]);
        fprintf(file, "v2 %.1f %.1f %.1f\n", v2[0], v2[1], v2[2]);
        fprintf(file, "v3 %.1f %.1f %.1f\n", v3[0], v3[1], v3[2]);
        fprintf(file, "v4 %.1f %.1f %.1f\n", v4[0], v4[1], v4[2]);
        fprintf(file, "n1 %.1f %.1f %.1f\n", n1[0], n1[1], n1[2]);
        fprintf(file, "n2 %.1f %.1f %.1f\n", n2[0], n2[1], n2[2]);
        fprintf(file, "n3 %.1f %.1f %.1f\n", n3[0], n3[1], n3[2]);
        fprintf(file, "a %.1f %.1f %.1f\n", a[0], a[1], a[2]);
        fprintf(file, "u %.1f %.1f %.1f\n", u[0], u[1], u[2]);
        fclose(file);
        printf("\nVectors saved to vector.dat\n");
    }

    return 0;
}
