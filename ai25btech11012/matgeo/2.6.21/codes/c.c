#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/2.6.21/codes/libs/geofun.h"
#include "/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/2.6.21/codes/libs/matfun.h"



int main() {
    double A[2], B[2], C[2];
    double AB[2], AC[2]; 
    double area;

    A[0]=3;A[1]=8;B[0]=-4;B[1]=2;C[0]=5;C[1]=1;

    // Vectors AB and AC
    for(int i = 0; i < 2; i++) 
    {
        AB[i] = B[i] - A[i];
        AC[i] = C[i] - A[i];
    }

    

    // Magnitude of cross product
    double magnitude = AB[0]*AC[0] + AB[1]*AC[1];

    // Area of triangle
    area = 0.5 * magnitude;

    printf("Area of the triangle = %.4lf\n", area);

    return 0;
}

