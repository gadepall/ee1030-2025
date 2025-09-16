#include <stdio.h>
#include <math.h>

// Your existing function
void get_unit_vectors(double result[6]) {
    double a[3] = {1, 1, 1};
    double b[3] = {1, 2, 3};
    double sum[3], cross[3], mag;
    int i;
    for(i=0;i<3;i++) sum[i]=a[i]+b[i];
    cross[0] = sum[1]*b[2] - sum[2]*b[1];
    cross[1] = sum[2]*b[0] - sum[0]*b[2];
    cross[2] = sum[0]*b[1] - sum[1]*b[0];
    mag = sqrt(cross[0]*cross[0] + cross[1]*cross[1] + cross[2]*cross[2]);
    if (mag == 0.0) {
        for(i=0;i<6;i++) result[i]=-999; // error
        return;
    }
    for(i=0;i<3;i++) {
        result[i] = cross[i]/mag;     // positive unit vector
        result[i+3] = -cross[i]/mag;  // negative unit vector
    }
}


