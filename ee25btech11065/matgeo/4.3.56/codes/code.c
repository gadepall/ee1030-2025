#include <stdio.h>

typedef struct {
    double x, y, z;
} Vector;

typedef struct {
    double a, b, c, d;
} Plane;

Vector subtract_vectors(Vector v1, Vector v2) {
    Vector result;
    result.x = v1.x - v2.x;
    result.y = v1.y - v2.y;
    result.z = v1.z - v2.z;
    return result;
}

Vector cross_product(Vector v1, Vector v2) {
    Vector result;
    result.x = v1.y * v2.z - v1.z * v2.y;
    result.y = v1.z * v2.x - v1.x * v2.z;
    result.z = v1.x * v2.y - v1.y * v2.x;
    return result;
}

double dot_product(Vector v1, Vector v2) {
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z;
}

Plane find_plane_equation(Vector p1, Vector p2, Vector p3) {
    Vector m1 = subtract_vectors(p2, p1);
    Vector m2 = subtract_vectors(p3, p1);
    Vector normal = cross_product(m1, m2);
    double d = dot_product(normal, p1);

    Plane result;
    result.a = normal.x;
    result.b = normal.y;
    result.c = normal.z;
    result.d = d;
    return result;
}

