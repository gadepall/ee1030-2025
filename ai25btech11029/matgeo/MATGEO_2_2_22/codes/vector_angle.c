#include <math.h>
#include "vector_angle.h"

double dot_product(Vector a, Vector b) {
    return a.x * b.x + a.y * b.y + a.z * b.z;
}

double magnitude(Vector v) {
    return sqrt(v.x * v.x + v.y * v.y + v.z * v.z);
}

double angle_between(Vector a, Vector b) {
    return acos(dot_product(a, b) / (magnitude(a) * magnitude(b)));
}

