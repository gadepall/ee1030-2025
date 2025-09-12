#include <stdio.h>

void cross_product(double a[3], double b[3], double result[3]) {
    result[0] = a[1]*b[2] - a[2]*b[1];
    result[1] = a[2]*b[0] - a[0]*b[2];
    result[2] = a[0]*b[1] - a[1]*b[0];
}

double find_p() {
    double a[3] = {2, 6, 27};
    double p = 27.0 / 2.0;
    double b[3] = {1, 3, p};
    double res[3];
    cross_product(a, b, res);

    if(res[0] == 0 && res[1] == 0 && res[2] == 0) {
        return p;
    }
    return -1;
}

