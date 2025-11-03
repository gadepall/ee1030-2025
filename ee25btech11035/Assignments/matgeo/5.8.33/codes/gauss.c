#include <stdio.h>

// The only change needed is here:
#define N 2

void solve_system(float A[N][N+1]) {
    int i, j, k;
    
    // The loops now correctly iterate for a 2x2 system since N=2
    for (i = 0; i < N; i++) {
        
        // Find the pivot element
        float pivot = A[i][i];
        if (pivot == 0.0f) {
            printf("Matrix is singular or requires row swapping!\n");
            return;
        }
        
        // Normalize the pivot row (make the pivot element 1)
        for (j = 0; j <= N; j++) {
            A[i][j] /= pivot;
        }

        // Eliminate the variable in the other rows
        for (k = 0; k < N; k++) {
            if (k != i) { // Don't perform the operation on the pivot row itself
                float factor = A[k][i];
                for (j = 0; j <= N; j++) {
                    A[k][j] -= factor * A[i][j];
                }
            }
        }
    }
}