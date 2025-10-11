#include <stdio.h>

int main() {
    int i, j, k;
    int A[3][3] = {
        {2, -1, 1},
        {-1, 2, -1},
        {1, -1, 2}
    };
    
    int A2[3][3] = {0};
    int temp[3][3] = {0};
    float Ainv[3][3];

    for(i = 0; i < 3; i++) {
        for(j = 0; j < 3; j++) {
            for(k = 0; k < 3; k++) {
                A2[i][j] += A[i][k] * A[k][j];
            }
        }
    }

    for(i = 0; i < 3; i++) {
        for(j = 0; j < 3; j++) {
            temp[i][j] = A2[i][j] - 6*A[i][j];
            if(i == j) temp[i][j] += 9;
        }
    }

    for(i = 0; i < 3; i++) {
        for(j = 0; j < 3; j++) {
            Ainv[i][j] = temp[i][j] / 4.0;
        }
    }

    printf("The inverse matrix A^{-1} is:\n");
    for(i = 0; i < 3; i++) {
        for(j = 0; j < 3; j++) {
            printf("%6.2f ", Ainv[i][j]);
        }
        printf("\n");
    }

    return 0;
}
