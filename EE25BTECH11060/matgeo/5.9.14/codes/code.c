#include <stdio.h>
int main() {
    double mat[2][3] = {
        {5, -4, 40},
        {5, -8, -80}
    };

    for (int j = 0; j < 3; j++) {
        mat[1][j] = mat[1][j] - mat[0][j];
    }
    for (int j = 0; j < 3; j++) {
        mat[1][j] = mat[1][j] / -4;
    }
    for (int j = 0; j < 3; j++) {
        mat[0][j] = mat[0][j] + 4 * mat[1][j];
    }

    for (int j = 0; j < 3; j++) {
        mat[0][j] = mat[0][j] / 5;
    }

    // Solution
    double c = mat[0][2];
    double a = mat[1][2];

    printf("Solution:\n");
    printf("Number of children (c) = %.0f\n", c);
    printf("Amount (a) = %.0f\n", a);

    return 0;
}
