#include <stdio.h>
#include <math.h>


// Analyze the system: returns code (0=unique,1=no solution,2=infinitely many)
int analyze_system(double p, double q, double r, double *D_out, double *E_out){
double D = p*q - 11.0*p*r + 10.0*q*r;
double E = (p*r - 10.0*q*r) / 9.0;
if(D_out) *D_out = D;
if(E_out) *E_out = E;
const double tol = 1e-12;
if(fabs(D) > tol) return 0; // unique
if(fabs(E) > tol) return 1; // inconsistent
return 2; // infinitely many
}


// Parametric solution (only valid if analyze_system returns 2)
void parametric_solution(double t, double *x, double *y, double *z){
if(x) *x = 10.0 * t + 10.0/9.0;
if(y) *y = -11.0 * t - 1.0/9.0;
if(z) *z = t;
}


// Row reduction for 3x4 augmented matrix
void row_reduce_3x4(const double A_in[3][4], double A_out[3][4]){
int i,j;
for(i=0;i<3;i++){
for(j=0;j<4;j++){
A_out[i][j] = A_in[i][j];
}
}
// R2 <- R2 - 10 R1
for(j=0;j<4;j++){
A_out[1][j] -= 10.0 * A_out[0][j];
}
// R3 <- R3 - (qr) R1, qr = A_in[2][0]
double qr = A_in[2][0];
for(j=0;j<4;j++){
A_out[2][j] -= qr * A_out[0][j];
}
// s = (pr-qr)/90 ; pr = A_in[2][1]
double pr = A_in[2][1];
double s = (pr - qr) / 90.0;
for(j=0;j<4;j++){
A_out[2][j] -= s * A_out[1][j];
}
}
