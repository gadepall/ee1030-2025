#ifndef MATFUN_H
#define MATFUN_H

// Multiply 3x1 vector by scalar
void mat_scalar_mul(const double in[3], double scalar, double out[3]);

// Subtract 3x1 vectors: out = a - b
void mat_subtract(const double a[3], const double b[3], double out[3]);

// Compute Euclidean norm of 3x1 vector
double mat_norm(const double v[3]);

// Solve y-coordinate on Y-axis given point P and distance
// Outputs two possible y values in roots array
void solve_y_coordinate(const double P[3], double distance, double roots[2]);

#endif
