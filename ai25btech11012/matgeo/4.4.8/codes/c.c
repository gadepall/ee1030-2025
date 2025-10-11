#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/4.4.8/codes/libs/geofun.h"
#include "/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/4.4.8/codes/libs/matfun.h"

// Function to compute determinant of 3x3 matrix
int determinant(int a[3][3]) {
    int det;
    det = a[0][0]*(a[1][1]*a[2][2] - a[1][2]*a[2][1])
        - a[0][1]*(a[1][0]*a[2][2] - a[1][2]*a[2][0])
        + a[0][2]*(a[1][0]*a[2][1] - a[1][1]*a[2][0]);
    return det;
}

int main() {
    int x;
    for(x=-10; x<=10; x++) {
        int mat[3][3] = {
            {x-3, 5-2, -1-1},
            {4-3, 5-2, 5-1},
            {4-3, 2-2, -2-1}
        };
        if(determinant(mat) == 0) {
            FILE*file;
	    file = fopen("values.dat","w");
	    fprintf(file,"%d",x);
	    fclose(file);
	    printf("Results have been written to values.dat\n");
        }
    }
    return 0;
}

