#ifndef MATFUN_H
#define MATFUN_H

void vector_subtract(const double *A, const double *B, double *C, int n);
double dot_product(const double *A, const double *B, int n);
void scalar_multiply(const double *A, double *B, double scalar, int n);

#endif
