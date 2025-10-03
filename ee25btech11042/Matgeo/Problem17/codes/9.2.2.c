#include <math.h>

void get_conic_data(double* data_out) {
    // Let a = 1 for the purpose of generating concrete values
    double a = 1.0;

    // Parabola: y^2 - 6ax = 0 => V1=[[0,0],[0,1]], u1=[-3a,0]
    data_out[0] = 0.0;  data_out[1] = 0.0;
    data_out[2] = 0.0;  data_out[3] = 1.0;
    data_out[4] = -3.0 * a; data_out[5] = 0.0;

    // Circle: x^2 + y^2 - 16a^2 = 0 => V2=[[1,0],[0,1]], u2=[0,0], f2=-16a^2
    // Storing V2 and u2 in the format requested
    data_out[6] = 1.0; data_out[7] = 0.0;
    data_out[8] = 0.0; data_out[9] = 1.0;
    data_out[10] = 0.0; data_out[11] = 0.0;

    // Solution Points: (2a, 2*sqrt(3)*a) and (2a, -2*sqrt(3)*a)
    data_out[12] = 2.0 * a; data_out[13] = 2.0 * sqrt(3.0) * a;
    data_out[14] = 2.0 * a; data_out[15] = -2.0 * sqrt(3.0) * a;
}
