#ifndef VECTOROPS_H
#define VECTOROPS_H

// Function to compute cross product of two vectors
void cross(int a[3], int b[3], int result[3]) {
    result[0] = a[1]*b[2] - a[2]*b[1];
    result[1] = a[2]*b[0] - a[0]*b[2];
    result[2] = a[0]*b[1] - a[1]*b[0];
}

// Function to compute dot product of two vectors
int dot(int a[3], int b[3]) {
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
}

#endif
