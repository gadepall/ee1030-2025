#include <stdio.h>

int find_nullity(double k) {
    double scalar = 5 * k * (1 + k + k * k);
    int n = 3;  // 3x3 matrix
    int nullity = 0;

    if (scalar == 0)
        nullity = n;
    else
        nullity = 0;

    return nullity;
}

