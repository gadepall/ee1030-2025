#include<stdio.h>

void make_data(double *points){
    double n = 2;
    points[0] = 5;
    points[1] = -8;
    points[2] = -1;
    points[3] = 3;
    points[4] = -4.8;
    points[5] = -0.6;
    points[6] = 2;
}

void processing(double rA, double rB, double n, double X, double Y){
    if(rA==rB&&rB==n){
        printf("Unique solution exists for the given system of linear equations.\n");
        printf("The solution for the given system of linear equations is: x=%.2lf, y=%.2lf", X, Y);
    }
    else if(rA==rB&&rA!=n){
        printf("Infinite solutions exist for the given system of linear equations in 2 variables.");
    }
    else{
        printf("No solution exists for the given system of linear equations in 2 variables");
    }
}
