#include <stdio.h>
#include <math.h>

// Function to compute new intercepts after rotation
// Inputs: a, b, theta
// Outputs: p, q (via pointers)
void line_intercepts_after_rotation(double a, double b, double theta, double *p, double *q) {
    // vector [1/a, 1/b]
    double m[2] = {1.0/a, 1.0/b};

    // Rotation matrix
    double P[2][2] = {
        {cos(theta), -sin(theta)},
        {sin(theta),  cos(theta)}
    };

    // Multiply m @ P
    double m_new[2];
    m_new[0] = m[0]*P[0][0] + m[1]*P[1][0];
    m_new[1] = m[0]*P[0][1] + m[1]*P[1][1];

    // Return intercepts
    *p = 1.0 / m_new[0];
    *q = 1.0 / m_new[1];
}

// Function to check options (returns index of true option)
int check_options(double a, double b, double p, double q, double eps) {
    double optA = fabs((a*a + b*b) - (p*p + q*q)) < eps;
    double optB = fabs((1.0/(a*a) + 1.0/(b*b)) - (1.0/(p*p) + 1.0/(q*q))) < eps;
    double optC = fabs((a*a + p*p) - (b*b + q*q)) < eps;
    double optD = fabs((1.0/(a*a) + 1.0/(p*p)) - (1.0/(b*b) + 1.0/(q*q))) < eps;

    if(optA) return 1;
    if(optB) return 2;
    if(optC) return 3;
    if(optD) return 4;
    return 0; // none true
}

