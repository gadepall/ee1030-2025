#include <stdio.h>
#include <math.h>
#define N 3  // Number of variables
int main() {
    int i, j, k;
    float a[N][N+1], ratio;
    float x[N];

    // Augmented matrix input
    // System:
    // x + y + z = 6
    // x + 2z = 7
    // 3x + y + z = 12

    a[0][0] = 1; a[0][1] = 1; a[0][2] = 1; a[0][3] = 6;
    a[1][0] = 1; a[1][1] = 0; a[1][2] = 2; a[1][3] = 7;
    a[2][0] = 3; a[2][1] = 1; a[2][2] = 1; a[2][3] = 12;

    // Forward Elimination
    for (i = 0; i < N-1; i++) {
        if (a[i][i] == 0.0) {
            printf("Mathematical Error!\n");
            return 0;
        }
        for (j = i+1; j < N; j++) {
            ratio = a[j][i] / a[i][i];
            for (k = 0; k <= N; k++) {
                a[j][k] -= ratio * a[i][k];
            }
        }
    }

    // Back Substitution
    x[N-1] = a[N-1][N] / a[N-1][N-1];

    for (i = N-2; i >= 0; i--) {
        x[i] = a[i][N];
        for (j = i+1; j < N; j++) {
            x[i] -= a[i][j] * x[j];
        }
        x[i] /= a[i][i];
    }

    // Display solution
    printf("Solution:\n");
    for (i = 0; i < N; i++) {
        printf("x[%d] = %.2f\n", i+1, x[i]);
    }

    return 0;
}
