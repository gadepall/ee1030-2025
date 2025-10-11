#include <stdio.h>
#include <math.h>

//Solving for x-coordinate of Point of Intersection

double POI_x(double a1, double b1, double c1, double a2, double b2, double c2){
   
    double x = (b1*c2-b2*c1)/(a1*b2-a2*b1);
   
    return x;
}

//Solving for y-coordinate of point of intersection

double POI_y(double a1, double b1, double c1, double a2, double b2, double c2){
   
    double y = (a2*c1-a1*c2)/(a1*b2-a2*b1);
   
    return y;
}


