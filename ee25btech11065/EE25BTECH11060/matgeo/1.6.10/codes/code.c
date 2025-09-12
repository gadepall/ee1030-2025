 
#include <stdio.h>

int main(){
    double Ax = 1, Ay = -2, Az = -8;
    double Bx = 5, By = 0, Bz = -2;
    double Cx = 11, Cy = 3, Cz = 7;

    double kx = (Bx - Ax) / (Cx - Bx);
    double ky = (By - Ay) / (Cy - By);
    double kz = (Bz - Az) / (Cz - Bz);

    printf("%lf",kx);

    return 0;

}
