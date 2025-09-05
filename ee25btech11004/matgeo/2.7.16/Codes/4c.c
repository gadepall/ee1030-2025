#include<stdio.h>
#include<math.h>

int crossprod(float a0, float a1, float a2, float b0, float b1, float b2){

float modA = sqrt(pow(a0,2)+pow(a1,2)+pow(a2,2));
float modB = sqrt(pow(b0,2)+pow(b1,2)+pow(b2,2));

float dotprod = a0*b0 + a1*b1 + a2*b2;

float mod = sqrt(pow(modA,2)*pow(modB,2) - pow(dotprod,2));

return mod;
}