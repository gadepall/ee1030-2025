#include <stdio.h>
#include <math.h>

// cross product of two 3D vectors
void cross(double u[3], double v[3], double result[3]) {
    result[0] = u[1]*v[2] - u[2]*v[1];
    result[1] = u[2]*v[0] - u[0]*v[2];
    result[2] = u[0]*v[1] - u[1]*v[0];
}

// dot product
double dot(double u[3], double v[3]) {
    return u[0]*v[0] + u[1]*v[1] + u[2]*v[2];
}

// magnitude of a 3D vector
double magnitude(double v[3]) {
    return sqrt(dot(v, v));
}

int main(void) {
    // Example vectors satisfying (a×b)×(c×d)=0
    double a[3] = {1, 0, 0};
    double b[3] = {0, 1, 0};
    double c[3] = {2, 0, 0};
    double d[3] = {0, 2, 0};

    double n1[3], n2[3];
    cross(a, b, n1);
    cross(c, d, n2);

    double angle = acos(dot(n1, n2) / (magnitude(n1) * magnitude(n2)));

    printf("Angle between the two planes (radians): %f\n", angle);
    printf("Angle between the two planes (degrees): %f\n", angle * 180.0 / M_PI);

    return 0;
}