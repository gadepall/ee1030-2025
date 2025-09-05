#include <stdio.h>

int main() {
    int x1 = 5, y1 = 4;
    int x2 = 7, y2;   // y2 = k
    int x3 = 9, y3 = -2;
    int k;

    // Equation: x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2) = 0
    // Substituting values
    // 5(k - (-2)) + 7((-2) - 4) + 9(4 - k) = 0
    // Solve manually inside program:

    // Simplified form: -4k + 4 = 0 => k = 1
    k = 1;

    printf("The value of k is: %d\n", k);

    return 0;
}