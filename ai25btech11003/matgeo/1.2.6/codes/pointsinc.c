#include <stdio.h>
#include <math.h>

int main() {
    double theta = 60.0; 
    double A[2] = {-2.00, 8.00};
    double B[2] = {-1.00, 7.00};
    double D[2] = {0.00, -1.25};
    double C[2] = {1.00, 3.00};
    double E[2] = {3.00, -1.00};
   
    printf("Point A: (%.2f, %.2f)\n", A[0], A[1]);
    printf("Point B: (%.2f, %.2f)\n", B[0], B[1]);
    printf("Point C: (%.2f, %.2f)\n", C[0], C[1]);
    printf("Point D: (%.2f, %.2f)\n", D[0], D[1]);
    printf("Point E: (%.2f, %.2f)\n", E[0], E[1]);
    return 0;
}
