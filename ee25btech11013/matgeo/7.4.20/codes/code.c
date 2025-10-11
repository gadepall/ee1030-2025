#include <stdio.h>
#include <math.h>

int xcenter(int c, int p, int m, int n){
    return (m*c + n*p)/(m+n);
}

int ycenter(int c, int p, int m, int n){
    return (m*c + n*p)/(m+n);
}
double dist(int x1, int y1, int x2, int y2){
    return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
}