#include<stdio.h>
#include<math.h>
double calculate_lambda(double xp, double xq, double xr) {
    
    return (xp - xr) / (xr - xq);
}