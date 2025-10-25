#ifndef MATFUN_H
#define MATFUN_H

// Solve 2x2 system Ax = b
int solve_2x2(double A[4], double b[2], double x[2]);

// Calculate distance between two points
double distance(double x1, double y1, double x2, double y2);

// Solve the main problem
int solve_problem(double center[2], double *radius);

#endif
