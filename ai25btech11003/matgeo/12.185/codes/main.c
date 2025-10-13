#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define ROWS 5
#define COLS 6

// Compute rank via Gaussian elimination
int compute_rank(double A[ROWS][COLS]) {
    int rank = 0;
    double M[ROWS][COLS];
    // Copy matrix
    for(int i=0;i<ROWS;i++)
        for(int j=0;j<COLS;j++)
            M[i][j] = A[i][j];

    int row = 0;
    for(int col = 0; col < COLS && row < ROWS; col++) {
        // Find pivot
        int sel = row;
        for(int i = row; i < ROWS; i++)
            if(fabs(M[i][col]) > fabs(M[sel][col]))
                sel = i;
        if(fabs(M[sel][col]) < 1e-9) continue;

        // Swap to current row
        for(int j = col; j < COLS; j++)
            { double tmp = M[row][j]; M[row][j] = M[sel][j]; M[sel][j] = tmp; }

        // Normalize and eliminate
        double inv = 1.0 / M[row][col];
        for(int j = col; j < COLS; j++)
            M[row][j] *= inv;
        for(int i = 0; i < ROWS; i++) {
            if(i == row) continue;
            double factor = M[i][col];
            for(int j = col; j < COLS; j++)
                M[i][j] -= factor * M[row][j];
        }
        row++;
    }
    rank = row;
    return rank;
}

// Exposed API for Python via ctypes
int get_rank() {
    double Q[ROWS][COLS] = {
        {1,0,0,0,2,3},
        {0,1,0,0,4,5},
        {0,0,1,0,6,7},
        {0,0,0,1,8,9},
        {0,0,0,0,0,0}
    };
    return compute_rank(Q);
}

int main() {
    int r = get_rank();
    FILE *fp = fopen("main.dat","w");
    if(!fp) { perror("main.dat"); return EXIT_FAILURE; }
    fprintf(fp, "%d\n", r);
    fclose(fp);
    return EXIT_SUCCESS;
}

