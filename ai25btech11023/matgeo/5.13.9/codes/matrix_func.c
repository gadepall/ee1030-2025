#include <stdlib.h>
#include <math.h>

#define N 3

// Multiply matrices a (m x n) and b (n x p), returns new matrix (m x p)
double *Matmul(double *a, double *b, int m, int n, int p) {
    double *result = (double *)malloc(m * p * sizeof(double));
    for(int i=0; i<m; i++) {
        for(int j=0; j<p; j++) {
            result[i*p+j] = 0.0;
            for(int k=0; k<n; k++) {
                result[i*p+j] += a[i*n+k] * b[k*p+j];
            }
        }
    }
    return result;
}

// Add matrices a and b (m x n), returns new matrix (m x n)
double *Matadd(double *a, double *b, int m, int n) {
    double *result = (double *)malloc(m * n * sizeof(double));
    for(int i=0; i<m*n; i++) {
        result[i] = a[i] + b[i];
    }
    return result;
}

// Subtract b from a (m x n), returns new matrix (m x n)
double *Matsub(double *a, double *b, int m, int n) {
    double *result = (double *)malloc(m * n * sizeof(double));
    for(int i=0; i<m*n; i++) {
        result[i] = a[i] - b[i];
    }
    return result;
}

// Compute norm of vector length m
double Matnorm(double *a, int m) {
    double sum = 0.0;
    for(int i=0; i<m; i++) {
        sum += a[i]*a[i];
    }
    return sqrt(sum);
}

// Check if two matrices (m x n) are approximately equal
int mat_equal(double *a, double *b, int m, int n) {
    double *diff = Matsub(a, b, m, n);
    double norm_diff = Matnorm(diff, m*n);
    free(diff);
    return (norm_diff < 1e-9);
}

// Determinant for 3x3 matrix
double mat_det_3x3(double *a) {
    return a[0] * (a[4]*a[8] - a[5]*a[7])
         - a[1] * (a[3]*a[8] - a[5]*a[6])
         + a[2] * (a[3]*a[7] - a[4]*a[6]);
}

// Calculate det(P^2 + Q^2) if conditions hold, else return -1
double det_P2_Q2(double *P, double *Q) {
    double *P2 = Matmul(P, P, N, N, N);
    double *Q2 = Matmul(Q, Q, N, N, N);
    double *P3 = Matmul(P2, P, N, N, N);
    double *Q3 = Matmul(Q2, Q, N, N, N);
    double *P2Q = Matmul(P2, Q, N, N, N);
    double *Q2P = Matmul(Q2, P, N, N, N);

    int cond1 = mat_equal(P3, Q3, N, N);
    int cond2 = mat_equal(P2Q, Q2P, N, N);
    int cond3 = !mat_equal(P, Q, N, N);

    double det_sum = -1;
    if(cond1 && cond2 && cond3) {
        double *sum = Matadd(P2, Q2, N, N);
        det_sum = mat_det_3x3(sum);
        free(sum);
    }

    free(P2);
    free(Q2);
    free(P3);
    free(Q3);
    free(P2Q);
    free(Q2P);

    return det_sum;
}
