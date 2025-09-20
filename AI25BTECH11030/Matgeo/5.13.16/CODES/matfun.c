#include "matfun.h"

void line_equation(const double P[2], const double Q[2], const double R[2], double *a, double *b, double *c) {
    double dx = R[0] - Q[0];
    double dy = R[1] - Q[1];
    *a = -dy;
    *b = dx;
    *c = (*a)*P[0] + (*b)*P[1];
}

void solve_2x2(double a1, double b1, double c1, double a2, double b2, double c2, double sol[2]) {
    double det = a1*b2 - a2*b1;
    sol[0] = (b2*c1 - b1*c2) / det;
    sol[1] = (a1*c2 - a2*c1) / det;
}

void compute_orthocentre(const double A[2], const double B[2], const double C[2], double O[2]) {
    double a1, b1, c1, a2, b2, c2;
    line_equation(A, B, C, &a1, &b1, &c1);
    line_equation(B, A, C, &a2, &b2, &c2);
    solve_2x2(a1, b1, c1, a2, b2, c2, O);
}

