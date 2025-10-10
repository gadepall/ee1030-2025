// VectorLib.c
#include <math.h>
#include "VectorLib.h"

Vector3D createVector(double x, double y, double z) {
    Vector3D v = {x, y, z};
    return v;
}

double dotProduct(Vector3D a, Vector3D b) {
    return a.x*b.x + a.y*b.y + a.z*b.z;
}

double magnitude(Vector3D v) {
    return sqrt(v.x*v.x + v.y*v.y + v.z*v.z);
}

double angleBetween(Vector3D a, Vector3D b) {
    double dot = dotProduct(a, b);
    double magA = magnitude(a);
    double magB = magnitude(b);
    return acos(dot / (magA * magB));
}

