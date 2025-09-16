#include <stdio.h>
// Section formula for a point dividing line AB in ratio m:n
int main(){
void section_formula(float *P, float *A, float *B, int m, int n, int k){
    for (int i = 0; i < k ; i++) {
        P[i] = (m*B[i] + n*A[i])/(m+n);
    }
}

// Area of triangle given 3 points in 2D
float triangle_area(float *A, float *B, float *C){
    float det = (B[0]-A[0])*(C[1]-A[1]) - (B[1]-A[1])*(C[0]-A[0]);
    if(det < 0) det = -det;
    return 0.5f * det;
}
}