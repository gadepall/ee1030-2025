#include <stdio.h>
#include<math.h>
int main() {

float c= 31.4;
float r = c/(M_PI*2);

float a= M_PI*r*r;

printf("\n\n If the circumference of a circle is 3.14cm then its Radius is %.1f cm and its Area is %.2f cm2. \n\n" , r ,a);


return 0;
}
