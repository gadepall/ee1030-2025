#include <stdio.h>

struct Vector {
    int x, y, z;
};

// Function to compute cross product
struct Vector cross(struct Vector a, struct Vector b) {
    struct Vector result;
    result.x = a.y*b.z - a.z*b.y;
    result.y = a.z*b.x - a.x*b.z;
    result.z = a.x*b.y - a.y*b.x;
    return result;
}

int main() {
    // Point P0 through which plane passes
    struct Vector P0 = {3, 2, 0};

    // Direction vector of line
    struct Vector v = {1, 5, 4};

    // A point on the line
    struct Vector P1 = {3, 6, 4};

    // Vector from P0 to P1
    struct Vector w = {P1.x - P0.x, P1.y - P0.y, P1.z - P0.z};

    // Normal vector = v × w
    struct Vector n = cross(v, w);

    // Plane equation: n1(x-x0) + n2(y-y0) + n3(z-z0) = 0
    int D = -(n.x*P0.x + n.y*P0.y + n.z*P0.z);

    printf("Equation of the plane: %dx + %dy + %dz + %d = 0\n", n.x, n.y, n.z, D);

    return 0;
}