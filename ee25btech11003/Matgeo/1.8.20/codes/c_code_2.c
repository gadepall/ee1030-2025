#include <stdio.h>


float perpendicularSlope(float x1, float y1, float x2, float y2) {
    float slope,pslope;

    
    if (x2 - x1 == 0) {
        
        return 0.0;  
    }

    if (y2 - y1 == 0) {
        return 9999999.0;
    }
    
    slope = ((y2 - y1) / (x2 - x1));
    
    pslope = (-1/slope);

    return pslope;
}
