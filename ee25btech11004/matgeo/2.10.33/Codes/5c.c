#include<stdio.h>
#include<math.h>

float norm(float a, float b, float c){

float answer;
answer = pow(a,2) + pow(b,2) + pow(c,2);
answer = sqrt(answer);

return answer;

}