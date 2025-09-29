#include <stdio.h>
#include <math.h>

typedef struct { double x, y, z; } Vec;

Vec cross(Vec a, Vec b) {
    Vec c = {
        a.y*b.z - a.z*b.y,
        a.z*b.x - a.x*b.z,
        a.x*b.y - a.y*b.x
    };
    return c;
}

double norm(Vec v) {
    return sqrt(v.x*v.x + v.y*v.y + v.z*v.z);
}

Vec scale(Vec v, double s) {
    Vec r = { v.x * s, v.y * s, v.z * s };
    return r;
}

int main(void) {
    // Given vectors
    Vec a = {1, 1, 0};
    Vec b = {0, 1, 1};

    // Vector perpendicular to both is a × b
    Vec n = cross(a, b);
    double m = norm(n);

    // If cross product is zero, vectors are parallel -> infinitely many unit normals
    const double EPS = 1e-12;
    if (m < EPS) {
        printf("Number of unit vectors perpendicular to both: infinite\n");
        return 0;
    }

    // Two unit vectors: ± (a × b) / ||a × b||
    Vec u = scale(n, 1.0 / m);
    Vec v = scale(u, -1.0);

    printf("Number of unit vectors perpendicular to both: 2\n");
    printf("u1 = (%.6f, %.6f, %.6f)\n", u.x, u.y, u.z);
    printf("u2 = (%.6f, %.6f, %.6f)\n", v.x, v.y, v.z);

    return 0;
}