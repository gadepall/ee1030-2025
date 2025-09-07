#include<stdio.h>

int solve(float a, float b) {
    float A[2] = {3*a + 1, -3};
    float B[2] = {8*a, 5};
    float P[2] = {9*a - 2, -b};
    int ratio = 3;

    if (((A[0]+ratio*B[0])/(ratio+1) == P[0]) && ((A[1]+ratio*B[1])/(ratio+1) == P[1])) {
        return 1;
    }
    return 0;
}
