#include<stdio.h>
typedef struct {
    double x, y, z;
} Vector;

typedef struct {
    double a, b, c, d;
} Plane;

Plane find_plane_from_point_and_normal(Vector point, Vector normal) {
    Plane result;
    result.a = normal.x;
    result.b = normal.y;
    result.c = normal.z;
    result.d = (normal.x * point.x) + (normal.y * point.y) + (normal.z * point.z);
    return result;
}


