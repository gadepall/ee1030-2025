#include <stdio.h>

typedef struct {
    double x, y, z;
} Vec3;

// Cross product
Vec3 cross(Vec3 a, Vec3 b) {
    Vec3 res;
    res.x = a.y*b.z - a.z*b.y;
    res.y = a.z*b.x - a.x*b.z;
    res.z = a.x*b.y - a.y*b.x;
    return res;
}

// Dot product
double dot(Vec3 a, Vec3 b) {
    return a.x*b.x + a.y*b.y + a.z*b.z;
}

// Subtraction
Vec3 sub(Vec3 a, Vec3 b) {
    Vec3 res = {a.x-b.x, a.y-b.y, a.z-b.z};
    return res;
}

// Addition
Vec3 add(Vec3 a, Vec3 b) {
    Vec3 res = {a.x+b.x, a.y+b.y, a.z+b.z};
    return res;
}

// Scalar multiply
Vec3 mul(Vec3 a, double s) {
    Vec3 res = {a.x*s, a.y*s, a.z*s};
    return res;
}

/*
   Function: find_intersection
   Input: points A, B, C (plane), P, Q (line)
   Output: intersection point (returned as Vec3)
*/
Vec3 find_intersection(Vec3 A, Vec3 B, Vec3 C, Vec3 P, Vec3 Q) {
    // Plane normal
    Vec3 AB = sub(B, A);
    Vec3 AC = sub(C, A);
    Vec3 n = cross(AB, AC);

    // Plane constant
    double d = -dot(n, A);

    // Line direction
    Vec3 d_line = sub(Q, P);

    // Solve n.(P + t*d_line) + d = 0
    double t = -(dot(n, P) + d) / dot(n, d_line);

    // Intersection point
    Vec3 inter = add(P, mul(d_line, t));
    return inter;
}

// Example usage (can be removed when used with Python)
int main() {
    Vec3 A = {2, 5, -3};
    Vec3 B = {-2, -3, 5};
    Vec3 C = {5, 3, -3};
    Vec3 P = {3, 1, 5};
    Vec3 Q = {-1, -3, -1};

    Vec3 inter = find_intersection(A, B, C, P, Q);
    printf("Intersection: (%.3f, %.3f, %.3f)\n", inter.x, inter.y, inter.z);

    return 0;
}
