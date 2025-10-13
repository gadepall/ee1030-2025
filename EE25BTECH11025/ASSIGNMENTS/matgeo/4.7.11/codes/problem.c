#include <stdio.h>

int vector1[2]={3, -2};
int constant1[1]={5};
int vector2[2]={3, 2};
int constant2[1]={5};

void give_data(double *points){
    points[0] = vector1[0];points[1] = vector1[1];
    points[2] = constant1[0];
    points[3] = vector2[0]; points[4] = vector2[1];
    points[5] = constant2[0];
}

void give_findata(double *points2){ 
    double finalvector1[2]; double finalvector2[2]; 
    double finalconstant1; double finalconstant2;
    for(int i = 0; i<2; i++){
        finalvector1[i] = vector1[i] - vector2[i];
        finalvector2[i] = vector1[i] + vector2[i];
    }  
    finalconstant1 = constant1[0] - constant2[0];
    finalconstant2 = constant1[0] + constant2[0];
    points2[0] = finalvector1[0];points2[1] = finalvector1[1];
    points2[2] = finalconstant1;
    points2[3] = finalvector2[0]; points2[4] = finalvector2[1];
    points2[5] = finalconstant2;

    
}


 