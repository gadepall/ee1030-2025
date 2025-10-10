#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/4.4.8/codes/libs/geofun.h"
#include "/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/4.4.8/codes/libs/matfun.h"


// Function to compute cross product
void crossProduct(int a[3], int b[3], int result[3]) {
    result[0] = a[1]*b[2] - a[2]*b[1];
    result[1] = a[2]*b[0] - a[0]*b[2];
    result[2] = a[0]*b[1] - a[1]*b[0];
}

int main() {
    // Normals of the two given planes
    int n1[3] = {1, 2, 3};
    int n2[3] = {3, 3, 1};

    // Point through which plane passes
    int P[3] = {-1, 3, 2};

    // Required normal
    int n[3];
    crossProduct(n1, n2, n);

    // Equation: n1*(x-x0) + n2*(y-y0) + n3*(z-z0) = 0
    int d = -(n[0]*P[0] + n[1]*P[1] + n[2]*P[2]);
    FILE* file;
    file = fopen("values.dat","w");

    fprintf(file,"Equation of the plane: %dx + %dy + %dz + %d = 0\n", n[0], n[1], n[2], d);
    fclose(file);
    printf("Results have been written to values.dat\n");

    return 0;
}

