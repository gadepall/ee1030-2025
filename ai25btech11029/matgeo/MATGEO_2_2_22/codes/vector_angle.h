#ifndef VECTOR_ANGLE_H
#define VECTOR_ANGLE_H

typedef struct {
    double x;
    double y;
    double z;
} Vector;

double dot_product(Vector a, Vector b);
double magnitude(Vector v);
double angle_between(Vector a, Vector b);

#endif

