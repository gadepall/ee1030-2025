#include <stdio.h>
#include <math.h>
int main(void){
    double Ax=1, Ay=-1, Bx=-4, By=6, Cx=-3, Cy=-5;
    // 2D cross product z-component of (AB × AC)
    double ABx = Bx-Ax, ABy = By-Ay;
    double ACx = Cx-Ax, ACy = Cy-Ay;
    double z = ABx*ACy - ABy*ACx;
    double area = fabs(z)/2.0;
    printf("Area = %.0f\n", area);  // 24
    return 0;
}
