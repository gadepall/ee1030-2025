#include<stdio.h>

float findK(int px, int py, int ax, int by)
{
    float rhs=(by-py)*(by-py) - (ax-px)*(ax-px);
    float num= rhs + px*px - py*py;
    float den=2*(px-py);
    
    return num/den;
}

