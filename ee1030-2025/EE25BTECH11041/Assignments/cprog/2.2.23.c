#include <stdio.h>
// 2.2.23 
// question : (11/2) *(3/10)

float pdt( float a ,float b){
return a*b;
}



int main(){
float a = 11.0/2.0 , b = 3.0/10.0;
float answer = pdt(a, b); 

printf(" (11/2)*(3/10) = %f", answer);
return 0;
}
