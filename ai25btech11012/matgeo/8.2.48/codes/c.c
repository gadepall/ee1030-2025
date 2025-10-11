
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/4.13.81/codes/libs/geofun.h"
#include "/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/4.13.81/codes/libs/matfun.h"
int main() {
    // Focus coordinates
    double Fx = -1, Fy = -2;

    // Directrix coefficients: x - 2y + 3 = 0
    double n1 = 1, n2 = -2, c = -3;

    // Eccentricity for parabola
    double e = 1;

    // Compute norm squared of directrix normal
    double n_norm2 = n1*n1 + n2*n2;

    // Compute V matrix
    double V[2][2];
    V[0][0] = n_norm2 - e*e*n1*n1;
    V[0][1] = 0 - e*e*n1*n2;
    V[1][0] = 0 - e*e*n2*n1;
    V[1][1] = n_norm2 - e*e*n2*n2;

    // Compute u vector
    double u[2];
    u[0] = c*e*e*n1 - n_norm2*Fx;
    u[1] = c*e*e*n2 - n_norm2*Fy;

    // Compute f scalar
    double f_val = n_norm2*(Fx*Fx + Fy*Fy) - c*c*e*e;

    // Print the quadratic form
     FILE *file;
	file = fopen("values.dat", "w");
    fprintf(file,"Equation of the parabola in quadratic form:\n");
    fprintf(file,"%.0fx^2 + %.0fxy + %.0fy^2 + %.0fx + %.0fy + %.0f = 0\n",
           V[0][0], V[0][1]+V[1][0], V[1][1], 2*u[0], 2*u[1], f_val);
    fclose(file);
	printf("Results have been written to values.dat\n");


    return 0;
}

