#ifndef MATRIX_OPS_H
#define MATRIX_OPS_H

void compute_adj(double A[2][2], double Adj[2][2]);
void transpose(double A[2][2], double AT[2][2]);
void multiply(double A[2][2], double B[2][2], double Result[2][2]);
void print_matrix(double M[2][2]);

#endif

