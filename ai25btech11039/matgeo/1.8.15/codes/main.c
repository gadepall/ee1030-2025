#include <stdio.h>
#include <math.h>
int main() {
    int x1=-3,y1=-14;
    int y2=-5;
    int a;
    double d;
    for(a=-100;a<=100;a++) {
        d = sqrt(pow(x1-a,2)+pow(y1-y2,2));
        if(fabs(d-9.0)<1e-6) {
            printf("a = %d\n",a);
        }
    }
    return 0;
}
