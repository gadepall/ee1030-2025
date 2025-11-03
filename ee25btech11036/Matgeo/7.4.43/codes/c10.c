#include <stdio.h>
#include <math.h>

typedef struct {
    double x, y;
} Vec;

// Vector subtraction
Vec sub(Vec a, Vec b) {
    Vec r = {a.x - b.x, a.y - b.y};
    return r;
}

// Midpoint
Vec midpoint(Vec a, Vec b) {
    Vec r = {(a.x + b.x)/2.0, (a.y + b.y)/2.0};
    return r;
}

// Dot product
double dot(Vec a, Vec b) {
    return a.x*b.x + a.y*b.y;
}

// Norm
double norm(Vec a) {
    return sqrt(dot(a,a));
}

// Circle center (midpoint of AC)
Vec circle_center(Vec A, Vec C) {
    return midpoint(A, C);
}

// Midpoint of DC
Vec midpoint_DC(Vec D, Vec C) {
    return midpoint(D, C);
}

