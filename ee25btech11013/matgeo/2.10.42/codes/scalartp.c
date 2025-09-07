#include <stdio.h>

typedef struct {
    double x, y, z;
} Vector;


Vector createVector(double x, double y, double z) {
    Vector v = {x, y, z};
    return v;
}

Vector subtract(Vector u, Vector v) {
    return createVector(u.x - v.x, u.y - v.y, u.z - v.z);
}

Vector scale(Vector u, double k) {
    return createVector(k*u.x, k*u.y, k*u.z);
}

Vector cross(Vector u, Vector v) {
    return createVector(
        u.y*v.z - u.z*v.y,
        u.z*v.x - u.x*v.z,
        u.x*v.y - u.y*v.x
    );
}

double dot(Vector u, Vector v) {
    return u.x*v.x + u.y*v.y + u.z*v.z;
}


double triple(Vector u, Vector v, Vector w) {
    return dot(u, cross(v, w));
}

Vector twominus(Vector a, Vector b) {
    return subtract(scale(a, 2), b); 
}


double computeX(Vector a, Vector b, Vector c) {
    Vector v1 = twominus(a, b);
    Vector v2 = twominus(b, c);
    Vector v3 = twominus(c, a);
    return triple(v1, v2, v3);
}


__attribute__((visibility("default"))) 
double computeX_py(double ax, double ay, double az,
                   double bx, double by, double bz,
                   double cx, double cy, double cz) {
    Vector a = createVector(ax, ay, az);
    Vector b = createVector(bx, by, bz);
    Vector c = createVector(cx, cy, cz);
    return computeX(a, b, c);
}
