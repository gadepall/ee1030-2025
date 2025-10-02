#include <stdio.h>

int inverse(double* mat, double* result) {
    double a = mat[0], b = mat[1], c = mat[2], d = mat[3];
    double det = a*d - b*c;
    if(det == 0) return 0;
    
    result[0] =  d/det;
    result[1] = -b/det;
    result[2] = -c/det;
    result[3] =  a/det;
    return 1;
}
