#include <stdio.h>

void find_projection(double *A, double *B, double *C, double *D, double *projection){

double AB[3];
for (int i = 0; i < 3; i++) {
    AB[i] = B[i] - A[i];
}
double CD[3];
for (int i=0; i<3; i++){
    CD[i] = D[i] - C[i];
}

double dot_product = 0.0;
for (int i=0; i<3; i++) {
    dot_product += AB[i]*CD[i];
}

double mag_square = 0.0;
for (int i=0; i<3; i++) {
mag_square += CD[i]*CD[i];
}

if (mag_square == 0) {
        projection[0] = 0;
        projection[1] = 0;
        projection[2] = 0;
        return;
    }
for (int i=0; i<3; i++){
    projection[i] = (dot_product/mag_square)*CD[i];
}

}
