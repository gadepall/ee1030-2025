#include <stdio.h>

int det3(int m[3][3]) {
    return m[0][0]*m[1][1]*m[2][2]
         + m[0][1]*m[1][2]*m[2][0]
         + m[0][2]*m[1][0]*m[2][1]
         - m[0][2]*m[1][1]*m[2][0]
         - m[0][0]*m[1][2]*m[2][1]
         - m[0][1]*m[1][0]*m[2][2];
}

void compute_counts(int counts[7]) {
    int mat[3][3];
    for (int i = 0; i < 7; i++) counts[i] = 0;

    for (int mask = 0; mask < (1<<9); mask++) {
        for (int i = 0; i < 9; i++) {
            mat[i/3][i%3] = (mask >> i) & 1;
        }
        int d = det3(mat);
        counts[d+3]++;
    }
}

