#include <stdio.h>
int main() {
    int i, j, k;
    double a[3][3] = {
        {1, 4, -7},  // a + 4b = -7
        {2, 5, -8},  // 2a + 5b = -8
        {3, 6, -9}   // 3a + 6b = -9
    };
    double factor;
    // Forward elimination
    for (i = 0; i < 2; i++) { // only first 2 rows, since 2 variables
        for (j = i+1; j < 3; j++) {
            if(a[i][i] != 0){
                factor = a[j][i] / a[i][i];
                for (k = i; k < 3; k++) {
                    a[j][k] -= factor * a[i][k];
                }
            }
        }
    }
    // Back substitution
    double b_val, a_val;
    if(a[1][1] != 0){
        b_val = a[1][2] / a[1][1];
        a_val = (a[0][2] - 4*b_val) / 1;
        printf("Solution: a = %.2lf, b = %.2lf\n", a_val, b_val);
    } else {
        printf("No unique solution exists.\n");
    }
    return 0;
}
