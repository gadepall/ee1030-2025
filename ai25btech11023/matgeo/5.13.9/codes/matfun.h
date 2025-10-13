
#include <stdlib.h>

// Create a m x n matrix dynamically (double array)
double *createMat(int m, int n);

// Print a matrix (m x n)
void printMat(double *p, int m, int n);

// Multiply matrices a (m x n) and b (n x p), returns new matrix (m x p)
double *Matmul(double *a, double *b, int m, int n, int p);

// Add matrices a and b (both m x n), returns new matrix (m x n)
double *Matadd(double *a, double *b, int m, int n);

// Subtract matrix b from a (both m x n), returns new matrix (m x n)
double *Matsub(double *a, double *b, int m, int n);

// Compute norm of vector of length m
double Matnorm(double *a, int m);

// Determinant of 2x2 matrix a
double Matdet(double *a);

