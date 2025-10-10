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
  int a1=3, b1 = -1, c1 = 8;
  int a2 = 6 , b2, c2=16;
  int r = a2/a1;

  b2 = r*b1;
  int k = -1*r;

  FILE *file;
   file = fopen("values.dat","w");

   fprintf(file,"r = %d",k);

   fclose(file);
   printf("Results have been written to values.dat\n");
   return 0;


}
