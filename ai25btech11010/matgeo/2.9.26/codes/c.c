#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "/home/dhanush-kumar-a/ee1030-2025/ai25btech11010/matgeo/2.9.26/codes/libs/matfun.h"

int main() {
    double alpha, beta;
    printf("Enter alpha (in radians): ");
    scanf("%lf", &alpha);
    printf("Enter beta (in radians): ");
    scanf("%lf", &beta);

    // Step 1: Create 3x3 rotation matrices
    double **F_alpha = createMat(3,3);
    double **F_minus_beta = createMat(3,3);
    double **F_alpha_minus_beta = createMat(3,3);

    // Fill the matrices manually
    F_alpha[0][0] = cos(alpha);  F_alpha[0][1] = -sin(alpha); F_alpha[0][2] = 0;
    F_alpha[1][0] = sin(alpha);  F_alpha[1][1] =  cos(alpha); F_alpha[1][2] = 0;
    F_alpha[2][0] = 0;           F_alpha[2][1] = 0;           F_alpha[2][2] = 1;

    F_minus_beta[0][0] = cos(-beta);  F_minus_beta[0][1] = -sin(-beta); F_minus_beta[0][2] = 0;
    F_minus_beta[1][0] = sin(-beta);  F_minus_beta[1][1] =  cos(-beta); F_minus_beta[1][2] = 0;
    F_minus_beta[2][0] = 0;           F_minus_beta[2][1] = 0;           F_minus_beta[2][2] = 1;

    F_alpha_minus_beta[0][0] = cos(alpha - beta);  F_alpha_minus_beta[0][1] = -sin(alpha - beta); F_alpha_minus_beta[0][2] = 0;
    F_alpha_minus_beta[1][0] = sin(alpha - beta);  F_alpha_minus_beta[1][1] =  cos(alpha - beta); F_alpha_minus_beta[1][2] = 0;
    F_alpha_minus_beta[2][0] = 0;                  F_alpha_minus_beta[2][1] = 0;                  F_alpha_minus_beta[2][2] = 1;

    // Step 2: Multiply f(alpha) * f(-beta)
    double **lhs = Matmul(F_alpha, F_minus_beta, 3, 3, 3);

    // Step 3: Compare lhs with f(alpha - beta)
    int equal = 1;
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            if(fabs(lhs[i][j] - F_alpha_minus_beta[i][j]) > 1e-9){
                equal = 0;
                break;
            }
        }
        if(!equal) break;
    }

    // Step 4: Print results
    if(equal){
        printf("\nVerified: f(alpha) * f(-beta) = f(alpha - beta)\n");
    } else {
        printf("\nNot equal!\n\nLHS =\n");
        printMat(lhs, 3, 3);
        printf("\nRHS =\n");
        printMat(F_alpha_minus_beta, 3, 3);
    }

    // Step 5: Free memory
    for(int i=0;i<3;i++){
        free(F_alpha[i]); free(F_minus_beta[i]); free(F_alpha_minus_beta[i]);
        free(lhs[i]);
    }
    free(F_alpha); free(F_minus_beta); free(F_alpha_minus_beta); free(lhs);

    return 0;
}
