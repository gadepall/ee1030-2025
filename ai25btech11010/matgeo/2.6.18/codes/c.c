#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "/home/dhanush-kumar-a/ee1030-2025/ai25btech11010/matgeo/1.11.12/codes/libs/matfun.h"

int main() {
    // Step 1: Create triangle vertices as 2x1 matrices
    double **A = createMat(2,1);
    double **B = createMat(2,1);
    double **C = createMat(2,1);

    A[0][0] = -1; A[1][0] = 0;
    B[0][0] = 1;  B[1][0] = 3;
    C[0][0] = 3;  C[1][0] = 2;

    // Step 2: Compute vectors AB and AC using matrix subtraction
    double **AB = Matsub(B, A, 2, 1);
    double **AC = Matsub(C, A, 2, 1);

    // Step 3: Create rotated row vector [AB_y, -AB_x] for cross product
    double **rotAB = createMat(1,2);
    rotAB[0][0] = AB[1][0];   // AB_y
    rotAB[0][1] = -AB[0][0];  // -AB_x

    // Step 4: Area = 0.5 * |rotAB * AC|
    double **prod = Matmul(rotAB, AC, 1, 2, 1); // 1x1 matrix
    double area = 0.5 * fabs(prod[0][0]);

    // Step 5: Save results to files
    FILE *fp_points = fopen("points.dat", "w");
    if(fp_points != NULL){
        fprintf(fp_points, "Vertex\tX\tY\n");
        fprintf(fp_points, "A\t%.2f\t%.2f\n", A[0][0], A[1][0]);
        fprintf(fp_points, "B\t%.2f\t%.2f\n", B[0][0], B[1][0]);
        fprintf(fp_points, "C\t%.2f\t%.2f\n", C[0][0], C[1][0]);
        fclose(fp_points);
    }

    FILE *fp_area = fopen("area.dat", "w");
    if(fp_area != NULL){
        fprintf(fp_area, "%.2f\n", area);
        fclose(fp_area);
    }

    // Step 6: Free memory
    for(int i=0;i<2;i++){
        free(A[i]); free(B[i]); free(C[i]);
        free(AB[i]); free(AC[i]);
    }
    free(A); free(B); free(C);
    free(AB); free(AC);
    free(rotAB[0]); free(rotAB);
    free(prod[0]); free(prod);

    return 0;
}
