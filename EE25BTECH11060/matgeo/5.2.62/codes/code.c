#include <stdio.h>
int main() {
    int n = 3;
    double a[3][4] = {
        {3, -2, 3, 8},
        {2, 1, -1, 1},
        {4, -3, 2, 4}
    };
    // Forward elimination
    for (int i = 0; i < n; i++) {
        // Normalize row
        double pivot = a[i][i];
        for (int j = i; j <= n; j++)
            a[i][j] /= pivot;

        // Eliminate column
        for (int k = 0; k < n; k++) {
            if (k != i) {
                double factor = a[k][i];
                for (int j = i; j <= n; j++)
                    a[k][j] -= factor * a[i][j];
            }
        }
    }

    printf("Solution:\n");
    for (int i = 0; i < n; i++) {
        printf("x%d = %lf\n", i+1, a[i][n]);
    }

    return 0;
}