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

int check_perpendicularity(double **p1, double **p2, int m, int n);

int write_points(double x1, double y1, double z1, double x2, double y2, double z2, double x3, double y3, double z3, double x4, double y4, double z4, int npts){
    int m = 3;
    int n = 1;

    double **R = createMat(m, n);
    double **O = createMat(m, n);
    double **T = createMat(m, n);
    double **S = createMat(m, n);

    R[0][0] = x2;
    R[1][0] = y2;
    R[2][0] = z2;

    O[0][0] = x1;
    O[1][0] = y1;
    O[2][0] = z1;

    T[0][0] = x4;
    T[1][0] = y4;
    T[2][0] = z4;

    S[0][0] = x3;
    S[1][0] = y3;
    S[2][0] = z3;

    FILE *p_file;
    FILE *p_file_2;
    p_file = fopen("plot.dat", "w");
    p_file_2 = fopen("plot2.dat", "w");
    if(p_file == NULL || p_file_2 == NULL){
        printf("Error opening one of the data files\n");
    }

    point_gen(p_file, O, R, m, n, npts);
    point_gen(p_file_2, S, T, m, n, npts);

    int k = check_perpendicularity(Matsub(R, O, m, n), Matsub(T, S, m, n), m, n);
    freeMat(R, m);
    freeMat(O, m);
    freeMat(T, m);
    freeMat(S, m);

    fclose(p_file);
    fclose(p_file_2);
    return k;
}

int check_perpendicularity(double **p1, double **p2, int m, int n){
    return Matmul(transposeMat(p1, m, n), p2, n, m, n)[0][0];
}
