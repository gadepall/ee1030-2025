#include <stdio.h>

float add(float a, float b);
float div(float a, float b);

int main(void) {
float a = 2.0, b = 3.0, c = 5.0;
printf("%f\n",div(add(a,b),c));
}


float add(float a, float b) {
return a+b;
}


float div(float a, float b) {
return a/b;
}
