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
    // Normals of planes P1 and P2
    double n1[3] = {2, 1, -1};
    double n2[3] = {1, 2, 1};

    // Cross product for direction of intersection line
    double d[3];
    d[0] = n1[1]*n2[2] - n1[2]*n2[1];
    d[1] = n1[2]*n2[0] - n1[0]*n2[2];
    d[2] = n1[0]*n2[1] - n1[1]*n2[0];

  
    // Angle between planes
    double dot = n1[0]*n2[0] + n1[1]*n2[1] + n1[2]*n2[2];
    double mag1 = sqrt(n1[0]*n1[0] + n1[1]*n1[1] + n1[2]*n1[2]);
    double mag2 = sqrt(n2[0]*n2[0] + n2[1]*n2[1] + n2[2]*n2[2]);
    double angle = acos(fabs(dot)/(mag1*mag2)) * 180.0 / M_PI;
   
    // Plane P3: passes through (4,2,-2), normal = d
    double A = d[0], B = d[1], C = d[2];
    double x0 = 4, y0 = 2, z0 = -2;
    double D = -(A*x0 + B*y0 + C*z0); // plane equation Ax+By+Cz+D=0
    
    // Distance of point (2,1,1) from P3
    double xp = 2, yp = 1, zp = 1;
    double dist = fabs(A*xp + B*yp + C*zp + D)/sqrt(A*A + B*B + C*C);
  
    FILE *file;
	file = fopen("values.dat", "w");
       fprintf(file, "angle between plane = %.2f \n",angle);
       fprintf(file,"equation of P3 : %.2fx + %.2fy + %.2fz + %.2f = 0\n",A,B,C,D);
       fprintf(file,"Distance = %.5f",dist);
	fclose(file);
	printf("Results have been written to values.dat\n");


    return 0;
}

