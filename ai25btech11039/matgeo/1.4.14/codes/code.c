#include <stdio.h>
#include <math.h>

int main() {
    double A[2] = {-6, 10};
    double B[2] = {-4, 6};
    double C[2] = {3, -8};
    
    double AB[2] = {A[0]-B[0], A[1]-B[1]};
    double BC[2] = {B[0]-C[0], B[1]-C[1]};
    
    double dot = AB[0]*BC[0] + AB[1]*BC[1];
    double norm2 = BC[0]*BC[0] + BC[1]*BC[1];
    double k = dot / norm2;
    
    double AB_len = sqrt((A[0]-B[0])*(A[0]-B[0]) + (A[1]-B[1])*(A[1]-B[1]));
    double AC_len = sqrt((A[0]-C[0])*(A[0]-C[0]) + (A[1]-C[1])*(A[1]-C[1]));
    
    printf("k = %.3f\n", k);
    printf("AB:BC = 2:7\n");
    printf("AB/AC = %.3f\n", AB_len/AC_len);
    
    return 0;
}
