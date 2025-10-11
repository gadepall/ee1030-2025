#include <stdio.h>
#include <math.h>

typedef struct {
    double x, y, z;
} Vector;

// Function to add two vectors
Vector add(Vector v1, Vector v2) {
    Vector result = {v1.x + v2.x, v1.y + v2.y, v1.z + v2.z};
    return result;
}

// Function to calculate dot product
double dot(Vector v1, Vector v2) {
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z;
}

// Function to calculate the magnitude of a vector
double magnitude(Vector v) {
    return sqrt(v.x * v.x + v.y * v.y + v.z * v.z);
}

// Function to scale a vector by a scalar
Vector scale(Vector v, double scalar) {
    Vector result = {v.x * scalar, v.y * scalar, v.z * scalar};
    return result;
}

int main() {
    // Given vectors
    Vector a = {2, 2, 1};
    Vector b = {1, 3, 1};
    Vector c = {1, 0, 1};
    
    // Step 1: compute b + c
    Vector b_plus_c = add(b, c);
    
    // Step 2: compute dot product of (b+c) with a
    double dot_product = dot(b_plus_c, a);
    
    // Step 3: compute magnitude of a
    double mag_a = magnitude(a);
    
    // Step 4: compute scalar k
    double k = dot_product / mag_a;
    
    // Step 5: compute the projection vector
    Vector projection = scale(a, k / mag_a);
    
    // Print the results
    printf("Projection of (b + c) on a is:\n");
    printf("x = %.2f\ny = %.2f\nz = %.2f\n", projection.x, projection.y, projection.z);
    
    return 0;
}
