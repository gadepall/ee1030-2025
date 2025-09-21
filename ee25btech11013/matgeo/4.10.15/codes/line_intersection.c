#include <stdio.h>

int line_intersection(double p1[3], double d1[3],
                      double p2[3], double d2[3],
                      double intersection[3]) {
    double A[2][2] = {
        { d1[0], -d2[0] },
        { d1[1], -d2[1] }
    };
    double b[2] = { p2[0] - p1[0], p2[1] - p1[1] };

    double det = A[0][0]*A[1][1] - A[0][1]*A[1][0];
    if(det == 0) {
        return -1; // Parallel or skew
    }

    double lam = (b[0]*A[1][1] - b[1]*A[0][1]) / det;


    for(int i = 0; i < 3; i++) {
        intersection[i] = p1[i] + lam*d1[i];
    }

    return 0;
}
