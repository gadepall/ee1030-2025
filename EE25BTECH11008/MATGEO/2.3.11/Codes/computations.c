#include <stdio.h>
#include <math.h>

double find_angle(int A[3], int B[3]) {
    int dot = 0;
    double a_mag = 0;
    double b_mag = 0;
    for (int i=0; i<3; i++) {
        dot += A[i]*B[i];
        a_mag += A[i]*A[i];
        b_mag += B[i]*B[i];
    }
    a_mag = pow(a_mag, 0.5);
    b_mag = pow(b_mag, 0.5);
    double cos_theta = dot/(a_mag*b_mag);
    // numerical safety
    if (cos_theta > 1.0) {
        cos_theta = 1.0; 
    }
    if (cos_theta < -1.0) {
        cos_theta = -1.0;
    }
    return acos(cos_theta);
}
