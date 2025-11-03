#include <stdio.h>
#include <stdlib.h>

// ---------------- Matrix Multiplication ----------------
// A: a×b, B: b×c  =>  C: a×c
void matmul(double *A, double *B, double *C, int a, int b, int c) {
    for (int i = 0; i < a; i++) {
        for (int j = 0; j < c; j++) {
            *(C + i*c + j) = 0;
            for (int k = 0; k < b; k++) {
                *(C + i*c + j) += (*(A + i*b + k)) * (*(B + k*c + j));
            }
        }
    }
}

// ---------------- Transpose ----------------
// A: m×n, AT: n×m
void transpose(double *A, double *AT, int m, int n) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            *(AT + j*m + i) = *(A + i*n + j);
        }
    }
}

// ---------------- Determinant (recursive, for n×n) ----------------
double det(double *A, int n) {
    if (n == 1) return *A;
    double D = 0;
    double *temp = malloc((n-1)*(n-1)*sizeof(double));
    int sign = 1;

    for (int f = 0; f < n; f++) {
        int subi = 0;
        for (int i = 1; i < n; i++) {
            int subj = 0;
            for (int j = 0; j < n; j++) {
                if (j == f) continue;
                temp[subi*(n-1)+subj] = *(A + i*n + j);
                subj++;
            }
            subi++;
        }
        D += sign * (*(A + 0*n + f)) * det(&temp[0], n - 1);
        sign = -sign;
    }
    free(temp);
    return D;
}

// ---------------- Adjugate ----------------
void adj(double *A, double *Adj, int n) {
    if (n == 1) {
        *Adj = 1;
        return;
    }

    double *temp = malloc((n-1)*(n-1)*sizeof(double));
    int sign;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int subi = 0;
            for (int row = 0; row < n; row++) {
                if (row == i) continue;
                int subj = 0;
                for (int col = 0; col < n; col++) {
                    if (col == j) continue;
                    temp[subi*(n-1)+subj] = *(A + row*n + col);
                    subj++;
                }
                subi++;
            }
            sign = ((i + j) % 2 == 0) ? 1 : -1;
            *(Adj + j*n + i) = sign * det(&temp[0], n - 1);
        }
    }
    free(temp);
}

// ---------------- Print Matrix ----------------
void printMat(double *A, int r, int c) {
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            printf("%8.3f ", *(A + i*c + j));
        }
        printf("\n");
    }
    printf("\n");
}
