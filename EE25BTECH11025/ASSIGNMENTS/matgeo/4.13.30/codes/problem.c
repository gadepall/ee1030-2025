#include<stdio.h>
#include<math.h>
double arrP[2] = {1,0};
double arrQ[2] = {-1,0};
double arrR[2] = {2,0};

void give_data(double *points){
    double normal[2];
    for(int i = 0; i<2; i++){
        normal[i] = arrQ[i]+arrR[i]-(2*arrP[i]);
    }
    double k=0;
    for(int i = 0; i<2; i++){
        k+=(pow(arrQ[i],2)+pow(arrR[i],2)-(2*pow(arrP[i],2)))/2;

    }
    points[0] = arrP[0]; points[1] = arrP[1];
    points[2] = arrQ[0]; points[3] = arrQ[1];
    points[4] = arrR[0]; points[5] = arrR[1];
    points[6] = normal[0]; points[7] = normal[1];
    points[8] = k;
}
 