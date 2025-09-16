#include <math.h>
double norm(double *P, int m) {
    double sum_of_squares = 0.0;
    int i;
    for (i = 0; i < m; i++) {
        sum_of_squares += P[i] * P[i];
    }
    return sqrt(sum_of_squares);
}

