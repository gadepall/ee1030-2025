#include <stdio.h>

void trisec(double k, double x1, double y1, double x2, double y2, double* a, double* b){
    *a= (x1+k*x2)/(1+k);
    *b= (y1+k*y2)/(1+k);
}