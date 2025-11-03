#include <stdio.h>

// Function to find point dividing line in ratio m:n
// flag = 1 for internal, -1 for external
void sectionFormula(float Px, float Py, float Qx, float Qy, int m, int n, int flag,
                    float *Rx, float *Ry) {
    if(flag == 1) { // internal
        *Rx = (m*Qx + n*Px) / (float)(m+n);
        *Ry = (m*Qy + n*Py) / (float)(m+n);
    }
    else if(flag == -1) { // external
        *Rx = (m*Qx - n*Px) / (float)(m-n);
        *Ry = (m*Qy - n*Py) / (float)(m-n);
    }
}
