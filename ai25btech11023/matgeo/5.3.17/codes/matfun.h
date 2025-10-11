#include <stdlib.h>
#include <math.h>


// Allocates a double pointer for an m x n matrix
double **createMat(int m, int n);

// Frees memory of an m x n matrix
void freeMat(double **a, int m);

// Prints an m x n matrix to stdout
void printMat(double **a, int m, int n);

// Solves a 2x2 system Ax = b; result in x[0], x[1]
void solve2x2(double **A, double *b, double *x);

