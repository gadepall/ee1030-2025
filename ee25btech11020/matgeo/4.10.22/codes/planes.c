#include <stdio.h>
#include <math.h>

// Function to solve for the two possible planes
// n1 and n2 are arrays of size 3, c is the constant term
// result is a 2x4 array (two planes, each: a,b,c,d)
void find_planes(double n1[3], double n2[3], double c, double result[2][4]) {
    double n1_dot_n1 = 0, n2_dot_n2 = 0, n1_dot_n2 = 0;
    for(int i=0;i<3;i++){
        n1_dot_n1 += n1[i]*n1[i];
        n2_dot_n2 += n2[i]*n2[i];
        n1_dot_n2 += n1[i]*n2[i];
    }

    // Equation: n1·n1 + 2λ(n1·n2) + λ^2(n2·n2) = 36
    double A = n2_dot_n2;
    double B = 2*n1_dot_n2;
    double C = n1_dot_n1 - 36;

    double disc = B*B - 4*A*C;
    double lambda1 = (-B + sqrt(disc))/(2*A);
    double lambda2 = (-B - sqrt(disc))/(2*A);

    // Plane 1
    for(int i=0;i<3;i++){
        result[0][i] = n1[i] + lambda1*n2[i];
    }
    result[0][3] = -c;

    // Plane 2
    for(int i=0;i<3;i++){
        result[1][i] = n1[i] + lambda2*n2[i];
    }
    result[1][3] = -c;
}

