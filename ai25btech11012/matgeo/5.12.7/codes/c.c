#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/5.12.7/codes/libs/geofun.h"
#include "/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/5.12.7/codes/libs/matfun.h"


int main() {
    double a, b;
    printf("Enter values of a and b: ");
    scanf("%lf %lf", &a, &b);

    // Coefficient matrix determinant
    double D = a*a + b*b;

    if (D == 0) {
        printf("No unique solution (determinant = 0).\n");
        return 0;
    }

    // Right-hand side values
    double rhs1 = -(a + 4*b);
    double rhs2 = 4*a - b;

    // Determinants for Cramer's rule
    double Dx = rhs1*a - (-b)*rhs2;
    double Dy = a*rhs2 - b*rhs1;

    // Solutions
    double x = Dx / D;
    double y = Dy / D;
     FILE *file;
	file = fopen("values.dat", "w");

	if (file == NULL) {
		printf("Error opening file!\n");
		return 1;
	}
	fprintf(file, "x\ty\n");
	fprintf(file, "%lf\t", x);
	fprintf(file, "%lf\t", y);
	

	fclose(file);
	printf("Results have been written to values.dat\n");

	
	return 0; 


}

