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

float find_norm(double **p, int n);

int write_points(double x1, double y1, double z1, double x2, double y2, double z2, double x3, double y3, double z3, int npts){
    int m = 3;
    int n = 1;

    double **R = createMat(m, n);
    double **O = createMat(m, n);
    double **T = createMat(m, n);
    double **S = createMat(m, n);
    double **origin = createMat(m, n);

    for(int i = 0; i<3; i++)
        origin[i][0] = 0; 
    

    R[0][0] = x2;
    R[1][0] = y2;
    R[2][0] = z2;

    O[0][0] = x1;
    O[1][0] = y1;
    O[2][0] = z1;

    T[0][0] = x1+x2+x3;
    T[1][0] = y1+y2+y3;
    T[2][0] = z1+z2+z3;

    S[0][0] = x3;
    S[1][0] = y3;
    S[2][0] = z3;

    FILE *p_file;
    p_file = fopen("plot.dat", "w");
    if(p_file == NULL)
        printf("Error opening one of the data files\n");

    point_gen(p_file, origin, O, m, n, npts);
    point_gen(p_file, origin, R, m, n, npts);
    point_gen(p_file, origin, S, m, n, npts);
    point_gen(p_file, origin, T, m, n, npts);

    float k = find_norm(T, m);
    freeMat(R, m);
    freeMat(O, m);
    freeMat(T, m);
    freeMat(S, m);
    freeMat(origin, m);

    fclose(p_file);
    return k;
}

float find_norm(double **p, int n){
    return sqrt(Matmul(transposeMat(p, n, 1), p, 1, n, 1)[0][0]);
}
