// VectorLib.h
#ifndef VECTORLIB_H
#define VECTORLIB_H

typedef struct {
    double x;
    double y;
    double z;
} Vector3D;

Vector3D createVector(double x, double y, double z);
double dotProduct(Vector3D a, Vector3D b);
double magnitude(Vector3D v);
double angleBetween(Vector3D a, Vector3D b);

#endif
