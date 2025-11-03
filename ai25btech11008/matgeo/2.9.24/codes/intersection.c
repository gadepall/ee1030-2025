#include <stdio.h>
#include <math.h>

int main() {
    // Line: r = r0 + lambda*v
    double r0[3] = {-1, -2, -3};
    double v[3] = {3, 4, 3};

    // Plane: n . r = ±||n|| d
    double n[3] = {1, 1, 3};
    double d = 4.0 / sqrt(11.0);

    // Compute plane constants
    double plane_pos =  sqrt(n[0]*n[0] + n[1]*n[1] + n[2]*n[2]) * d;  // +4
    double plane_neg = -plane_pos;                                     // -4

    // Function to compute dot product
    double dot(double a[3], double b[3]) {
        return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
    }

    // Compute lambda for positive plane
    double lambda1 = (plane_pos - dot(n, r0)) / dot(n, v);
    double lambda2 = (plane_neg - dot(n, r0)) / dot(n, v);

    // Compute intersection points
    double point1[3], point2[3];
    for(int i=0; i<3; i++){
        point1[i] = r0[i] + lambda1 * v[i];
        point2[i] = r0[i] + lambda2 * v[i];
    }

    // Print results
    printf("Intersection points:\n");
    printf("Point 1: (%f, %f, %f)\n", point1[0], point1[1], point1[2]);
    printf("Point 2: (%f, %f, %f)\n", point2[0], point2[1], point2[2]);

    return 0;
}

