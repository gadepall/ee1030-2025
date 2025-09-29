#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include "libs/matfun.h"
#include "libs/geofun.h"

void point_gen(FILE *p_file, double **A, double **B, int rows, int cols, int npts){
    for(int i = 0; i <= npts; i++){
     double **output = Matadd(A, Matscale(Matsub(B, A, rows, cols), rows, cols, (double)i/npts), rows, cols);
     fprintf(p_file, "%lf, %lf\n", output[0][0], output[1][0]);
     freeMat(output, rows);
    }
}

void write_points(double x1, double y1, double x2, double y2, double x3, double y3, double x4, double y4, int npts){
    int m = 2;
    int n = 1;

    double **A = createMat(m, n);
    double **B = createMat(m, n);
    double **C = createMat(m, n);
    double **D = createMat(m, n);

    B[0][0] = x2;
    B[1][0] = y2;

    A[0][0] = x1;
    A[1][0] = y1;

    C[0][0] = x3;
    C[1][0] = y3;

    D[0][0] = x4;
    D[1][0] = y4;

    FILE *p_file;
    p_file = fopen("plot.dat", "w");
    if(p_file == NULL)
        printf("Error opening one of the data files\n");

    point_gen(p_file, A, B, m, n, npts);
    point_gen(p_file, B, C, m, n, npts);
    point_gen(p_file, C, D, m, n, npts);
    point_gen(p_file, D, A, m, n, npts);
    point_gen(p_file, B, D, m, n, npts);

    freeMat(A, m);
    freeMat(B, m);
    freeMat(C, m);
    freeMat(D, m);

    fclose(p_file);
}
