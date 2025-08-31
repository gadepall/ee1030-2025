#include <stdio.h>

int main() {
    double A[3] = {3, -5, 7};
    double B[3] = {-1, 7, -6};
    double G[3] = {1, 1, 1};
    double C[3];

    for (int i = 0; i < 3; i++)
        C[i] = 3 * G[i] - A[i] - B[i];

    printf("C = (%lf, %lf, %lf)\n", C[0], C[1], C[2]);
}
