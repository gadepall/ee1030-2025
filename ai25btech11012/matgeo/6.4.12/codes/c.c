#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/6.4.12/codes/libs/geofun.h"
#include "/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/6.4.12/codes/libs/matfun.h"



// Function to compute cross product of two vectors
void cross(double a[3], double b[3], double result[3]) {
    result[0] = a[1]*b[2] - a[2]*b[1];
    result[1] = a[2]*b[0] - a[0]*b[2];
    result[2] = a[0]*b[1] - a[1]*b[0];
}

// Function to compute dot product
double dot(double a[3], double b[3]) {
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
}

// Function to compute magnitude of vector
double magnitude(double a[3]) {
    return sqrt(dot(a,a));
}

int main() {
    // Line 1: r = (1,2,1) + λ(1,-1,1)
    double a1[3] = {1,2,1};
    double d1[3] = {1,-1,1};

    // Line 2: r = (2,-1,-1) + μ(2,-1,2)
    double a2[3] = {2,-1,-1};
    double d2[3] = {2,-1,2};

    // Compute (a2 - a1)
    double diff[3] = {a2[0]-a1[0], a2[1]-a1[1], a2[2]-a1[2]};

    // Compute d1 x d2
    double cross_d1d2[3];
    cross(d1, d2, cross_d1d2);

    // Compute numerator = |(a2 - a1) . (d1 x d2)|
    double numerator = fabs(dot(diff, cross_d1d2));

    // Compute denominator = |d1 x d2|
    double denominator = magnitude(cross_d1d2);

    // Distance
    double distance = numerator / denominator;

    
   FILE *file;
	file = fopen("values.dat", "w");

	if (file == NULL) {
		printf("Error opening file!\n");
		return 1;
	}
	fprintf(file, "shortest distance : %lf" , distance);
	
	

	fclose(file);
	printf("Results have been written to values.dat\n");

	
	return 0; 

    
}

