#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/1.11.14/codes/libs/geofun.h"
#include "/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/1.11.14/codes/libs/matfun.h"



int main() {
    double a[3], b[3], c[3], magnitude, unit[3];

    a[0]=4;a[1]=-1;a[2]=1;
    b[0]=2;b[1]=-2;b[2]=1;

    

    // Compute a+b
    for (int i = 0; i < 3; i++)
    { c[i] = a[i] + b[i];}

    // Compute magnitude of (a+b)
    magnitude = sqrt(c[0]*c[0] + c[1]*c[1] + c[2]*c[2]);

    if (magnitude == 0)
    {
        printf("The vector (a+b) is zero, unit vector cannot be defined.\n");
        return 0;
    }

    // Compute unit vector
    for (int i = 0; i < 3; i++)
    { unit[i] = c[i] / magnitude;}

    FILE *file;
	file = fopen("values.dat", "w");

	if (file == NULL) {
		printf("Error opening file!\n");
		return 1;
	}
	fprintf(file, "x\ty\tz\n");
	fprintf(file, "%lf\t", unit[0]);
	fprintf(file, "%lf\t", unit[1]);
	fprintf(file, "%lf\t", unit[2]);
	

	fclose(file);
	printf("Results have been written to values.dat\n");

	
	return 0;


}

