#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "libs/matfun.h"
#include "libs/geofun.h"

int main() {
    double **k, **M, **C;
    int x1 = -4, x2 = 0, y1 = 0, y2 = 6;

    // Create matrices
    M = createMat(2, 2);
    k = createMat(2, 1);
    C = createMat(2, 1);


    M[0][1] = x1; 
    M[1][1] = y1; 

    M[0][0] = x2;  
    M[1][0] = y2;  
 
    k[0][0] = 3.0 / 4;  // weight for B (column 0)
    k[1][0] = 1.0 / 4;  // weight for A (column 1)

    // Matrix multiplication: C = M * k
    C = Matmul(M, k, 2, 2, 1);

    // Write result to file
    FILE *file = fopen("values.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(file, "x\ty\t of C\n");
    fprintf(file, "%.02lf\t%.02lf\n", C[0][0], C[1][0]);  // x and y of C

    fclose(file);
    printf("Results have been written to values.dat\n");

    // Free memory
    freeMat(M, 2);
    freeMat(k, 2);
    freeMat(C, 2);

    return 0;
}