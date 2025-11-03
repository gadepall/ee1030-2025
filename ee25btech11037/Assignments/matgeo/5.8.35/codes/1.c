#include <stdio.h>

#define N 3

void solve_system(float A[N][N+1]) {
    int i, j, k;
    
    
    for (i = 0; i < N; i++) {
        
        float pivot = A[i][i];
        if (pivot == 0.0f) {
            printf("Matrix is singular or requires row swapping!\n");
            return;
        }
        for (j = 0; j <= N; j++) {
            A[i][j] /= pivot;
        }

        for (k = 0; k < N; k++) {
            if (k != i) {
                float factor = A[k][i];
                for (j = 0; j <= N; j++) {
                    A[k][j] -= factor * A[i][j];
                }
            }
        }
    }}
