#include <math.h>

// Define a structure for a 3D vector to pass data
// between Python and C.
typedef struct {
    double x, y, z;
} Vector;

// Helper function to calculate the cross product of two vectors.
Vector cross_product(Vector a, Vector b) {
    Vector result;
    result.x = a.y * b.z - a.z * b.y;
    result.y = a.z * b.x - a.x * b.z;
    result.z = a.x * b.y - a.y * b.x;
    return result;
}

// Helper function to calculate the magnitude (length) of a vector.
double magnitude(Vector a) {
    return sqrt(a.x * a.x + a.y * a.y + a.z * a.z);
}

// Helper function to normalize a vector (convert it to a unit vector).
Vector normalize(Vector a) {
    double mag = magnitude(a);
    Vector result = {0, 0, 0};
    // Avoid division by zero for safety
    if (mag > 1e-9) { 
        result.x = a.x / mag;
        result.y = a.y / mag;
        result.z = a.z / mag;
    }
    return result;
}

// This is the main function that will be exposed to Python.
// It calculates AD' based on the geometric constraints.
__attribute__((visibility("default")))
Vector calculate_ad_prime(Vector ab, Vector ad) {
    // 1. Find the normal to the parallelogram's plane (AB x AD).
    Vector normal_vec = cross_product(ab, ad);

    // 2. Find a vector in the plane that is perpendicular to AB.
    // This is achieved by the cross product of the normal and AB.
    Vector ad_perp_direction = cross_product(normal_vec, ab);

    // 3. Normalize this perpendicular vector to get a pure direction.
    Vector ad_prime_unit = normalize(ad_perp_direction);

    // 4. The final AD' must have the same length as the original AD.
    double ad_mag = magnitude(ad);

    // 5. Scale the unit direction vector by the correct magnitude.
    Vector ad_prime;
    ad_prime.x = ad_prime_unit.x * ad_mag;
    ad_prime.y = ad_prime_unit.y * ad_mag;
    ad_prime.z = ad_prime_unit.z * ad_mag;
    
    return ad_prime;
}
