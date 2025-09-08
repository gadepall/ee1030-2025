#include <stdio.h>
#include <math.h>

#define PI 3.14159265358979323846

// Vector struct
typedef struct {
    double x, y, z;
} Vector3;

// Dot product of two vectors
double dotProduct(Vector3 a, Vector3 b) {
    return a.x * b.x + a.y * b.y + a.z * b.z;
}

// Normalize a vector to unit length
Vector3 normalize(Vector3 v) {
    double length = sqrt(dotProduct(v, v));
    Vector3 result = {v.x / length, v.y / length, v.z / length};
    return result;
}

// Create vector from direction cosines (angles in degrees)
Vector3 fromDirectionCosines(double angle_x_deg, double angle_y_deg) {
    double a = cos(angle_x_deg * PI / 180.0);
    double b = cos(angle_y_deg * PI / 180.0);

    // Since a^2 + b^2 + c^2 = 1, solve for c
    double c_squared = 1.0 - (a*a + b*b);
    double c = 0.0;
    if (c_squared >= 0) {
        c = sqrt(c_squared);
    } else {
        printf("Warning: angles do not form a valid unit vector.\n");
    }

    Vector3 v = {a, b, c};
    return normalize(v);
}

int main() {
    // Angles given in the problem
    double angle_x = 30.0;   // degrees
    double angle_y = 120.0;  // degrees

    Vector3 direction = fromDirectionCosines(angle_x, angle_y);

    printf("Unit direction vector:\n");
    printf("x = %.6f\n", direction.x);
    printf("y = %.6f\n", direction.y);
    printf("z = %.6f\n", direction.z);

    // Compute angle with z-axis
    Vector3 e_z = {0.0, 0.0, 1.0};
    double cos_gamma = dotProduct(direction, e_z);
    double gamma_deg = acos(cos_gamma) * 180.0 / PI;

    printf("Angle with z-axis = %.2f degrees\n", gamma_deg);

    return 0;
}
