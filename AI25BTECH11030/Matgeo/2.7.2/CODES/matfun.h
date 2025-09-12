#ifndef MATFUN_H
#define MATFUN_H

// Function to create a rows x cols matrix (2D array) dynamically
double** createMat(int rows, int cols);

// Function to subtract two matrices A and B of size rows x cols
double** Matsub(double** A, double** B, int rows, int cols);

// Function to free a matrix created by createMat
void freeMat(double** mat, int rows);

#endif // MATFUN_H

