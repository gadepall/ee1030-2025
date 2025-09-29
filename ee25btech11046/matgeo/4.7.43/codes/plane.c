#include <stdio.h>
#include <math.h>
double perp_distance_withoutsign(double *D, double *P, double k) {
    double sum = 0, norm1 = 0,  norm = 0;
    for (int i=0; i<3; i++) {
        sum += D[i]*P[i];
        norm1 += D[i]*D[i];
    }
    sum -= k;
    norm = sqrt(norm1);
    return sum/norm;
}
void function(double *D, double k, double *P1, double *P2) {
    if ((perp_distance_withoutsign(D, P1, k))*(perp_distance_withoutsign(D, P2, k))<0) {
        printf("They lie on the opposite side of the plane.\n");            
    }
    else {
        printf("They lie on the the same side of the plane.\n");
    }
}
