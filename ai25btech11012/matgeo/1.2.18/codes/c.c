#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/1.2.18/codes/libs/geofun.h"
#include "/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/1.2.18/codes/libs/matfun.h"


int main()
{
   int x1=6,x2=8,x3=9,y1=1,y2=2,y3=4,y4=3,x4=0;

   int M[2][4];

   M[0][0] = x1;
   M[1][0] = y1;
   M[0][1] = x2;
   M[1][1] = y2;
   M[0][2] = x3;
   M[1][2] = y3;
   M[0][3] = x4;
   M[1][3] = y4;



   int ABx = M[0][1] - M[0][0];
   M[0][3] = M[0][2] - ABx;


    printf("The value of p is: %d\n", M[0][3]);
    return 0;

}
