#include <stdio.h>
#include <math.h>

void solve_quad(double a, double b, double c, double sols[2]){
   
    double D = b*b - 4*a*c;
   
    sols[0] = (-b+pow(D,0.5))/(2*a);
    sols[1] = (-b-pow(D,0.5))/(2*a);
   
}

