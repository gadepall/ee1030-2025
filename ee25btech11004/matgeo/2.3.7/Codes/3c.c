#include<stdio.h>
#include<math.h>






float anglefinder(float x1, float y1, float z1, float x2, float y2, float z2){


float dot_product;
float mod1;
float mod2;
float cosval;
float angle;

dot_product = x1*x2 + y1*y2 + z1*z2;

mod1 = pow(x1,2) + pow(y1,2) + pow(z1,2);
    
mod2 = pow(x2,2) + pow(y2,2) + pow(z2,2);
    
mod1 = sqrt(mod1);
mod2 = sqrt(mod2);
    
    
cosval = dot_product/(mod1 * mod2);

angle= asin(cosval);


return angle;
}
