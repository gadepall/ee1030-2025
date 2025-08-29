#include <stdio.h>
#include <math.h>

// Function to calculate distance
float distance(float a, float b) {
    float x1 = a, y1 = b;
    float x2 = -a, y2 = -b;

    float dist = sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1));
    return dist;
}

