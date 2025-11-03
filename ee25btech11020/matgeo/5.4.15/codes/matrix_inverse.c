#include <stdio.h>

int inverse2x2(double mat[4], double inv[4]) {
    double a = mat[0], b = mat[1];
    double c = mat[2], d = mat[3];

    double det = a*d - b*c;
    if(det == 0.0) {
        return -1;  // not invertible
    }

    inv[0] =  d / det;
    inv[1] = -b / det;
    inv[2] = -c / det;
    inv[3] =  a / det;

    return 0; // success
}

