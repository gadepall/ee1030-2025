#ifndef MATFUN_H
#define MATFUN_H

// Create m x n matrix
double **createMat(int m, int n);

// Generate m x m identity matrix
double **Mateye(int m);

// Scale an m x n matrix by factor k
double **Matscale(double **a, int m, int n, double k);

// Add two m x n matrices
double **Matadd(double **a, double **b, int m, int n);

#endif // MATFUN_H
