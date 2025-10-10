#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/1.6.27/codes/libs/geofun.h"
#include "/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/1.6.27/codes/libs/matfun.h"

int main()
{
    // Points A, B, C
    int A[3] = {-4, 6, 10};
    int B[3] = {2, 4, 6};
    int C[3] = {14, 0, -2};

    // Vectors AB and BC
    int AB[3], BC[3];
    for(int i = 0; i < 3; i++)
    {
        AB[i] = B[i] - A[i];
        BC[i] = C[i] - B[i];
    }

    // Check proportionality: AB × BC = 0 for collinearity
    int cross[3];
    cross[0] = AB[1]*BC[2] - AB[2]*BC[1];
    cross[1] = AB[2]*BC[0] - AB[0]*BC[2];
    cross[2] = AB[0]*BC[1] - AB[1]*BC[0];


     FILE *file;
	file = fopen("values.dat", "w");

    if(cross[0] == 0 && cross[1] == 0 && cross[2] == 0)
        fprintf(file, "Points are collienear");

    
	fclose(file);
	("Results have been written to values.dat\n");
printf
	
	return 0; 


}

