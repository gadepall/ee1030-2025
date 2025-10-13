#include <stdio.h>
#include <math.h>

// Function to compute dot product of 3D vectors
double dot(double a[3], double b[3]) {
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
}

// Function to compute cross product of 3D vectors
void cross(double a[3], double b[3], double result[3]) {
    result[0] = a[1]*b[2] - a[2]*b[1];
    result[1] = a[2]*b[0] - a[0]*b[2];
    result[2] = a[0]*b[1] - a[1]*b[0];
}

// Function to compute norm (magnitude)
double norm(double v[3]) {
    return sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
}


double find_shortest_distance(double *A_start, double *m1,
                              double *B_start, double *m2,
                              double *pointA, double *pointB)
{
    // Compute dot products
    double m1m1 = dot(m1, m1);
    double m2m2 = dot(m2, m2);
    double m1m2 = dot(m1, m2);

    // Compute RHS vector (A2 - A1)
    double AB[3] = { B_start[0] - A_start[0],
                     B_start[1] - A_start[1],
                     B_start[2] - A_start[2] };

    double rhs1 = dot(AB, m1);
    double rhs2 = dot(AB, m2);

    // Solve for lambda (k1) and mu (k2)
    double det = (m1m1 * (-m2m2)) - (-m1m2 * m1m2);
    double lam = (rhs1 * (-m2m2) - (-m1m2) * rhs2) / det;
    double mu  = (m1m1 * rhs2 - m1m2 * rhs1) / det;

    // Compute points of closest approach
    for (int i = 0; i < 3; i++) {
        pointA[i] = A_start[i] + lam * m1[i];
        pointB[i] = B_start[i] + mu * m2[i];
    }

    // Compute shortest distance
    double diff[3] = { pointB[0] - pointA[0],
                       pointB[1] - pointA[1],
                       pointB[2] - pointA[2] };

    return norm(diff);
}
