#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libs/matfun.h"

int main() {

    /* This code calculates 30 degrees west of south */
    
    // Create 2x2 rotation matrix
    // double **R = createMat(2, 2); 
    // R[0][0] = cos(-M_PI/6);  R[0][1] = -sin(-M_PI/6);
    // R[1][0] = sin(-M_PI/6);  R[1][1] =  cos(-M_PI/6);
    double **R = rotMat(-M_PI/6);
    
    // Create 2x1 south vector (column vector)
    double **v = createMat(2, 1);
    v[0][0] = 0;
    v[1][0] = -1;

    // Multiply: (2x2) * (2x1) = (2x1)
    double **rotated = Matmul(R, v, 2, 2, 1);

    // Print result
    printf("Rotated vector: (%.4f, %.4f)\n", rotated[0][0], rotated[1][0]);
    
    FILE *fp = fopen("var.dat", "w");
    if (fp != NULL) {
        fprintf(fp, "%.4f\n%.4f\n", rotated[0][0], rotated[1][0]);
        fclose(fp);
    } else {
        printf("Error opening file for writing.\n");
    }
    
    return 0;
}
