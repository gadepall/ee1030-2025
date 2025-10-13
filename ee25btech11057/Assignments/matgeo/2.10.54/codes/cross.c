#include <stdio.h>

// Function to compute cross product of two vectors
void cross(double u[3], double v[3], double result[3]) {
    result[0] = u[1]*v[2] - u[2]*v[1];
    result[1] = u[2]*v[0] - u[0]*v[2];
    result[2] = u[0]*v[1] - u[1]*v[0];
}

int main() {
    // Example unit vectors at 120° apart in the xy-plane
    double a[3] = {1.0, 0.0, 0.0};
    double b[3] = {-0.5, 0.86602540378, 0.0};   // cos120, sin120
    double c[3] = {-0.5, -0.86602540378, 0.0};  // cos240, sin240

    double ab[3], bc[3], ca[3];

    cross(a, b, ab);
    cross(b, c, bc);
    cross(c, a, ca);

    printf("a × b = (%lf, %lf, %lf)\n", ab[0], ab[1], ab[2]);
    printf("b × c = (%lf, %lf, %lf)\n", bc[0], bc[1], bc[2]);
    printf("c × a = (%lf, %lf, %lf)\n", ca[0], ca[1], ca[2]);

    return 0;
}

