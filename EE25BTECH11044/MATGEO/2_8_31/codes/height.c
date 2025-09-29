#include <stdio.h>
#include <math.h>

// Function to compute norm of a 2D vector
double norm(double v[2]) {
    return sqrt(v[0]*v[0] + v[1]*v[1]);
}

// Function to compute dot product of two 2D vectors
double dot(double a[2], double b[2]) {
    return a[0]*b[0] + a[1]*b[1];
}

int main() {
    // Points A, B, C
    double A[2] = {1, -2};
    double B[2] = {2, 3};
    double C[2] = {-3, 2}; // since a = -3 from earlier

    // Base vector u = AB
    double u[2] = {B[0] - A[0], B[1] - A[1]};
    // Vector v = AC
    double v[2] = {C[0] - A[0], C[1] - A[1]};

    // Compute projection of v onto u: ( (v·u) / (u·u) ) * u
    double uu = dot(u,u);
    double vu = dot(v,u);
    double proj[2] = {(vu/uu)*u[0], (vu/uu)*u[1]};

    // Compute perpendicular component w = v - proj
    double w[2] = {v[0] - proj[0], v[1] - proj[1]};

    // Height = norm of w
    double h = norm(w);

    printf("Height of parallelogram (AB as base) = %lf\n", h);

    return 0;
}
