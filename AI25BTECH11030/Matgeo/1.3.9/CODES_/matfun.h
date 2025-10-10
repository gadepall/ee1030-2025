#ifndef MATFUN_H
#define MATFUN_H

double** createMat(int rows, int cols);
double** Matmul(double **A, double **B, int r1, int c1, int c2);
void freeMat(double **mat, int rows);

#endif

