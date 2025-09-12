#include <stdio.h>
#include <math.h>

// Function to compute determinant of 3x3 matrix
double determinant(double a[3][3]) {
    return a[0][0]*(a[1][1]*a[2][2] - a[1][2]*a[2][1])
         - a[0][1]*(a[1][0]*a[2][2] - a[1][2]*a[2][0])
         + a[0][2]*(a[1][0]*a[2][1] - a[1][1]*a[2][0]);
}

int main() {
    // Two planes:
    // Plane P: 3x+2y+3z=16
    // Plane S: x+y+z=7

    // Solve intersection line between P and S
    // Choose basis for S: let
    // a = (1,-1,0), b = (1,0,-1) → both satisfy x+y+z=0
    // So general point on S: (7,0,0) + s*a + t*b

    // Constraint from P: 3x+2y+3z = 14 or 18 (distance condition)
    // Pick "14" first.

    // Solve quickly: Intersection point
    double u[3] = {2,3,2};
    double v[3] = {-2,3,6};
    double w[3] = {-2,7,2};

    // Put in matrix
    double M[3][3] = {
        {u[0], v[0], w[0]},
        {u[1], v[1], w[1]},
        {u[2], v[2], w[2]}
    };

    // Determinant
    double det = determinant(M);
    double V = fabs(det);
    double result = (80.0/3.0) * V;

    printf("Chosen vectors:\n");
    printf("u = (%.2lf, %.2lf, %.2lf)\n", u[0], u[1], u[2]);
    printf("v = (%.2lf, %.2lf, %.2lf)\n", v[0], v[1], v[2]);
    printf("w = (%.2lf, %.2lf, %.2lf)\n", w[0], w[1], w[2]);
    printf("Determinant = %.2lf\n", det);
    printf("Volume V = %.2lf\n", V);
    printf("Final (80/3)*V = %.2lf\n", result);

    return 0;
}

