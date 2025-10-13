#include<stdio.h>

float slopee(float x1, float y1, float x2, float y2){

    float slope = (y1 - y2)/(x1-x2);
    return slope;
}