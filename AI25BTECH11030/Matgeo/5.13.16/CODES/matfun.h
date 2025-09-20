#ifndef MATFUN_H
#define MATFUN_H

void compute_orthocentre(const double A[2], const double B[2], const double C[2], double O[2]);

void line_equation(const double P[2], const double Q[2], const double R[2], double *a, double *b, double *c);

void solve_2x2(double a1, double b1, double c1, double a2, double b2, double c2, double sol[2]);

#endif

