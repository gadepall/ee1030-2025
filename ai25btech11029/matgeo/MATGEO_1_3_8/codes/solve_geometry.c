// solve_geometry.c
#include <stdio.h>
#include "geometry_utils.h"

int main() {
    Point A = {-1, -1}, B = {-1, 6}, C = {3, 6}, D = {3, -1};
    Point P = midpoint(A, B);
    Point Q = midpoint(B, C);
    Point R = midpoint(C, D);
    Point S = midpoint(D, A);

    Point diag1_mid = midpoint(P, R);
    Point diag2_mid = midpoint(Q, S);

    printf("Midpoint of PR: (%.2f, %.2f)\n", diag1_mid.x, diag1_mid.y);
    printf("Midpoint of QS: (%.2f, %.2f)\n", diag2_mid.x, diag2_mid.y);

    return 0;
}

