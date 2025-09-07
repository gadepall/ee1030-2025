#include <stdio.h>
#include<math.h>

float findk(int qx, int qy, int rx, int ry){
    int num, den;
    num = ((rx*rx) + (ry*ry)) - ((qx*qx) + (qy*qy));
    den = 2*(2*(rx - qx) + (ry - qy));
    float k = num/den;
    return k;
    // coordinates of point P will be (2k, k)
}
