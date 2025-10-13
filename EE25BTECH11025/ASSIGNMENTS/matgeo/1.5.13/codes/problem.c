#include<stdio.h>

void get_data(double *out_data){
    double A[2] = {-1.0, -4.0};
    double B[2] = {5.0, -6.0};

    double lambda = (0-A[0])/(B[0]-A[0]);

    double Px = A[0] + lambda*(B[0] - A[0]);
    double Py = A[1] + lambda*(B[1] - A[1]);

    out_data[0] = Px;
    out_data[1] = Py;
    out_data[2] = A[0];
    out_data[3] = A[1];
    out_data[4] = B[0];
    out_data[5] = B[1];
}
