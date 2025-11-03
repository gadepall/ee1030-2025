#include <stdio.h>
#include <math.h>

int check_solvability(double b1, double b2, double b3) {
    double cond = 3*b1 + b2 + 2*b3;
    if (fabs(cond) < 1e-9) {
        return 1;  
    } else {
        return 0;  
    }
}

