#ifndef TRIANGLE_H
#define TRIANGLE_H

// Function to compute cross product of two 3D vectors
void cross_product(const double a[3], const double b[3], double result[3]);

// Function to compute magnitude of a 3D vector
double magnitude(const double v[3]);

// Function to compute area of triangle OAB
double triangle_area(const double OA[3], const double OB[3]);

#endif

