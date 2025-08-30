#include <stdio.h>
#include <math.h>

// Distance between two points A(x1,y1) and B(x2,y2)
double distance(double A[2], double B[2]) {
    return sqrt( (B[0]-A[0])*(B[0]-A[0]) + (B[1]-A[1])*(B[1]-A[1]) );
}
