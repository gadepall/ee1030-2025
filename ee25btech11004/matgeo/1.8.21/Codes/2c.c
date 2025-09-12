#include<stdio.h>
#include<math.h>

float xfinder (float x1, float y1, float x2, float y2){

float norm1 = x1*x1 + y1*y1;
float norm2 = x2*x2 + y2*y2;

float denominator = x1 - x2;



float xcoord = (norm1 - norm2)/(2 * denominator);

return xcoord;
}