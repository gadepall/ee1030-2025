#include <stdio.h>
// 2.2.127
// question: (-3/4) * (1/7)
float pdt(float a, float b){
return a*b;
}



int main(){
float a = -3.0/4.0;
float b = 1.0/7.0;
float answer = pdt(a, b);
printf("(-3/4) * (1/7) = %f", answer);
return 0;
}
