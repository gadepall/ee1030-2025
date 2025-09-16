#include<stdio.h>
#include<math.h>

float dotfinder(float a1, float a2, float a3, float b1, float b2, float b3){

    float dot_product;
    float mod1;
    float mod2;
    float cosval;
    float angle;
    float result;

    dot_product = a1*b1 + a2*b2 + a3*b3;

    mod1 = sqrt(pow(a1,2) + pow(a2,2) + pow(a3,2));
    mod2 = sqrt(pow(b1,2) + pow(b2,2) + pow(b3,2));

    cosval = dot_product/(mod1 * mod2);

    angle = acos(cosval);   // angle between vectors

    result = dot_product;   // return a·b value

    return result;
}