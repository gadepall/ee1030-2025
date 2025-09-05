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
     fprintf(p_file, "%lf, %lf, %lf\n", output[0][0], output[1][0], output[2][0]);
     freeMat(output, rows);
    }
}

void calculate_unit(double **R, int npts);

void write_points(double x1, double y1, double z1, int npts){
    int m = 3;
    int n = 1;

    double **R = createMat(m, n);
    double **O = createMat(m, n);

    R[0][0] = x1;
    R[1][0] = y1;
    R[2][0] = z1;

    O[0][0] = 0;
    O[1][0] = 0;
    O[2][0] = 0;

    FILE *p_file;
    p_file = fopen("plot.dat", "w");
    if(p_file == NULL){
        printf("Error opening data file\n");
    }

    point_gen(p_file, O, R, m, n, npts);
    calculate_unit(R, npts);

    freeMat(R, m);
    freeMat(O, m);

    fclose(p_file);
}

void calculate_unit(double **R, int npts){
    double **X = Matunit(R, 3);
    double **O = createMat(3, 1);

    for(int i = 0; i<3; i++){
        O[i][0] = 0;
    }

    FILE *p_file;
    p_file = fopen("plot2.dat", "w");
    if(p_file == NULL){
        printf("Error opening data file\n");
    }

    point_gen(p_file, O, X, 3, 1, npts);

    freeMat(X, 3);
    freeMat(O, 3);

    fclose(p_file);
}
