#include <stdio.h>
#include <math.h>

typedef struct {
    double x, y, z;
} Vector;

double dot(Vector a, Vector b) {
    return a.x*b.x + a.y*b.y + a.z*b.z;
}

Vector cross(Vector a, Vector b) {
    Vector r;
    r.x = a.y*b.z - a.z*b.y;
    r.y = a.z*b.x - a.x*b.z;
    r.z = a.x*b.y - a.y*b.x;
    return r;
}

int main() {
    // Choose simple unit vectors
    Vector a = {sqrt(3)/2, 0.5, 0}; // unit vector
    Vector d = {sqrt(3)/2, 0.5, 0}; // parallel to a
    Vector b = {0, 1, 0};           // unit vector
    Vector c = {0, 1, 0};           // parallel to b

    // Compute
    Vector axb = cross(a, b);
    Vector cxd = cross(c, d);
    double lhs = dot(axb, cxd);
    double ac  = dot(a, c);

    printf("(a × b) · (c × d) = %.2f\n", lhs);
    printf("a · c = %.2f\n", ac);

    if (fabs(lhs - 1.0) < 1e-6 && fabs(ac - 0.5) < 1e-6) {
        printf("Condition satisfied: a || d and b || c\n");
    }

    return 0;
}