#include <stdio.h>
#include <math.h>
typedef struct {
    double x, y, z;
} Vector;
Vector cross(Vector a, Vector b) {
    Vector result;
    result.x = a.y * b.z - a.z * b.y;
    result.y = a.z * b.x - a.x * b.z;
    result.z = a.x * b.y - a.y * b.x;
    return result;
}
double dot(Vector a, Vector b) {
    return a.x * b.x + a.y * b.y + a.z * b.z;
}
void check_conditions(Vector a, Vector b, Vector c, int *results) {
    Vector ab = cross(a, b);
    Vector bc = cross(b, c);
    Vector ca = cross(c, a);
    results[0] = (ab.x==0 && ab.y==0 && ab.z==0 &&
                  bc.x==0 && bc.y==0 && bc.z==0 &&
                  ca.x==0 && ca.y==0 && ca.z==0);
    results[1] = ((ab.x==bc.x && ab.y==bc.y && ab.z==bc.z) &&
                  (bc.x==ca.x && bc.y==ca.y && bc.z==ca.z) &&
                  !(ab.x==0 && ab.y==0 && ab.z==0));
    Vector ac = cross(a, c);
    results[2] = ((ab.x==bc.x && ab.y==bc.y && ab.z==bc.z) &&
                  (bc.x==ac.x && bc.y==ac.y && bc.z==ac.z) &&
                  !(ab.x==0 && ab.y==0 && ab.z==0));
    results[3] = (fabs(dot(ab, bc)) < 1e-9 &&
                  fabs(dot(bc, ca)) < 1e-9 &&
                  fabs(dot(ca, ab)) < 1e-9);
}
void out_data(double *points){
    double A[3] = {1, 0, 0};
    double B[3] = {-0.5, sqrt(3)/2, 0};
    double C[3] = {-0.5, -sqrt(3)/2, 0};
    points[0] = A[0];
    points[1] = A[1];
    points[2] = A[2];
    points[3] = B[0];
    points[4] = B[1];
    points[5] = B[2];
    points[6] = C[0];
    points[7] = C[1];
    points[8] = C[2];
}
