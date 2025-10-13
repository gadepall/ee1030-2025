#include <stdio.h>
#include <math.h>

#define SIZE 3

// Function to display an augmented matrix [A|I]
void display(float mat[SIZE][2*SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < 2*SIZE; j++) {
            printf("%10.6f ", mat[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

int main() {
    // Augmented matrix [A|I] for A = {{3,0,-1},{2,3,0},{0,4,1}}
    float mat[SIZE][2*SIZE] = {
        {3.0f, 0.0f, -1.0f, 1.0f, 0.0f, 0.0f},
        {2.0f, 3.0f,  0.0f, 0.0f, 1.0f, 0.0f},
        {0.0f, 4.0f,  1.0f, 0.0f, 0.0f, 1.0f}
    };

    printf("Initial augmented matrix [A | I]:\n");
    display(mat);

    // Gauss-Jordan elimination
    for (int i = 0; i < SIZE; i++) {
        // Pivot element
        float pivot = mat[i][i];
        if (fabs(pivot) < 1e-6) {
            printf("Matrix is singular and cannot be inverted.\n");
            return 1;
        }

        // Normalize pivot row
        for (int j = 0; j < 2*SIZE; j++) {
            mat[i][j] /= pivot;
        }

        // Eliminate column entries in other rows
        for (int r = 0; r < SIZE; r++) {
            if (r != i) {
                float factor = mat[r][i];
                for (int c = 0; c < 2*SIZE; c++) {
                    mat[r][c] -= factor * mat[i][c];
                }
            }
        }

        printf("After step %d:\n", i+1);
        display(mat);
    }

    // Extract inverse from right half
    printf("Inverse matrix A^{-1}:\n");
    for (int i = 0; i < SIZE; i++) {
        for (int j = SIZE; j < 2*SIZE; j++) {
            // Round if close to integer
            float v = mat[i][j];
            if (fabs(v - roundf(v)) < 1e-6f)
                printf("%6.0f ", roundf(v));
            else
                printf("%8.6f ", v);
        }
        printf("\n");
    }

    return 0;
}

