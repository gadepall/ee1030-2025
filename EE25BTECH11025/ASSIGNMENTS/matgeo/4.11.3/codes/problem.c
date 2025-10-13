#include <stdio.h>

void get_data(double *out_data){
    double P0[3] = {2.0, -1.0, 2.0};
    double P1[3] = {5.0,  3.0, 4.0};
    double Q1[3] = {2.0, 0.0, 3.0};
    double Q2[3] = {1.0, 1.0, 5.0};
    double Q3[3] = {3.0, 2.0, 4.0};
    double u[3], v[3], n[3];
    for(int i=0;i<3;i++){
        u[i] = Q2[i] - Q1[i];
        v[i] = Q3[i] - Q1[i];
    }
    n[0] = u[1]*v[2] - u[2]*v[1];
    n[1] = u[2]*v[0] - u[0]*v[2];
    n[2] = u[0]*v[1] - u[1]*v[0];
    double dir[3];
    for(int i=0;i<3;i++) dir[i] = P1[i] - P0[i];
    double numerator = 0.0, denominator = 0.0, rhs = 0.0;
    for(int i=0;i<3;i++){
        rhs += n[i] * Q1[i];
        numerator += n[i] * P0[i];
        denominator += n[i] * dir[i];
    }
    double t;
    if (denominator == 0.0) {
        if (numerator == rhs) t = 0.0;
        else {
            t = 0.0/0.0;
        }
    } else {
        t = (rhs - numerator) / denominator;
    }
    double X[3];
    for(int i=0;i<3;i++) X[i] = P0[i] + t * dir[i];
    out_data[0] = P0[0]; out_data[1] = P0[1]; out_data[2] = P0[2];
    out_data[3] = P1[0]; out_data[4] = P1[1]; out_data[5] = P1[2];
    out_data[6] = Q1[0]; out_data[7] = Q1[1]; out_data[8] = Q1[2];
    out_data[9] = Q2[0]; out_data[10]= Q2[1]; out_data[11]= Q2[2];
    out_data[12]= Q3[0]; out_data[13]= Q3[1]; out_data[14]= Q3[2];
    out_data[15]= X[0];  out_data[16]= X[1];  out_data[17]= X[2];
}


 