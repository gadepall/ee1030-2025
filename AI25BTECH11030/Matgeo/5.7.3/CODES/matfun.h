#ifndef MATFUNH
#define MATFUNH

#define SIZE 3

void matmult(double A[SIZE][SIZE], double B[SIZE][SIZE], double res[SIZE][SIZE]);
void matscalarmult(double scalar, double A[SIZE][SIZE], double res[SIZE][SIZE]);
void matadd(double A[SIZE][SIZE], double B[SIZE][SIZE], double res[SIZE][SIZE]);
void matsub(double A[SIZE][SIZE], double B[SIZE][SIZE], double res[SIZE][SIZE]);
void matidentity(double I[SIZE][SIZE]);
void compute_inverse(double A[SIZE][SIZE], double A_inv[SIZE][SIZE]);

#endif

