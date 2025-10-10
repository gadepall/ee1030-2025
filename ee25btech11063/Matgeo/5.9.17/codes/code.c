#include <stdio.h>

void solve2x2(double aug[2][3], int *x, int *y) {
    // Gaussian elimination for 2x2 system
    // aug is 2x3 augmented matrix

    // Step 1: make leading coefficient of first row = 1
    if (aug[0][0] != 0) {
        double factor = aug[0][0];
        aug[0][0] /= factor;
        aug[0][1] /= factor;
        aug[0][2] /= factor;
    }

    // Step 2: eliminate below
    double factor = aug[1][0];
    aug[1][0] -= factor * aug[0][0];
    aug[1][1] -= factor * aug[0][1];
    aug[1][2] -= factor * aug[0][2];

    // Step 3: make pivot in row 2 equal to 1
    if (aug[1][1] != 0) {
        factor = aug[1][1];
        aug[1][0] /= factor;
        aug[1][1] /= factor;
        aug[1][2] /= factor;
    }

    // Step 4: eliminate above row 2
    factor = aug[0][1];
    aug[0][0] -= factor * aug[1][0];
    aug[0][1] -= factor * aug[1][1];
    aug[0][2] -= factor * aug[1][2];

    // Now solution is in aug[0][2], aug[1][2]
    *x = (int)(aug[0][2] + 0.5); // rounding
    *y = (int)(aug[1][2] + 0.5);
}

int main() {
    int a, b, c, d, result;

    double aug1[2][3] = {
        {2,  1,  4},
        {1, -2, -3}
    };
    solve2x2(aug1, &a, &b);

    
    double aug2[2][3] = {
        {5, -1, 11},
        {4,  3, 24}
    };
    solve2x2(aug2, &c, &d);

    
    result = a + b - c + 2 * d;

  
    FILE *fp = fopen("answer.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    fprintf(fp, "%d\n", result);
    fclose(fp);

    return 0;
}

