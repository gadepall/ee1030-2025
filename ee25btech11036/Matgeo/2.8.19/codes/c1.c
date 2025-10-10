#include <stdio.h>

double scalar_triple(double a[3], double b[3], double c[3]) {
    return a[0]*(b[1]*c[2] - b[2]*c[1])
         - a[1]*(b[0]*c[2] - b[2]*c[0])
         + a[2]*(b[0]*c[1] - b[1]*c[0]);
}
