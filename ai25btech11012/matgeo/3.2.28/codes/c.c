#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/3.2.28/codes/libs/geofun.h"
#include "/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/3.2.28/codes/libs/matfun.h"



int main() 
{
    double AB = 5.0;     // given side
    double angleA = 45.0 * M_PI / 180.0; // convert to radians
    double b, a;
    int possible = 0;

    for (b = 0.1; b < 5.0; b += 0.01) {  // try possible AC lengths
        a = 5.0 - b; // since a+b = 5
        double lhs = a*a;
        double rhs = b*b + AB*AB - 2*AB*b*cos(angleA);

        if (fabs(lhs - rhs) < 1e-3) {
            possible = 1;
            break;
        }
    }
 FILE *file = fopen("values.dat", "w");

    // Check if the file was opened successfully
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write the values to the file
    fprintf(file, "AB: %.2f cm\n", AB);
    fprintf(file, "Angle A: %.2f degrees\n", angleA);
    
    // Close the file
    fclose(file);

    printf("Values have been written to values.dat\n");
     if (possible)
        printf("Triangle can be constructed.\n");
    else
        printf("Triangle cannot be constructed.\n");


    return 0;
}

