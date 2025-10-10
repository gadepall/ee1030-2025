// main.c
#include <stdio.h>

// function declaration
int find_x(int Ax, int Ay, int Bx, int By, int Cx, int Cy, int Dy);

int main() {
    int Ax=1, Ay=3, Bx=-1, By=2, Cx=2, Cy=5, Dy=4;
    int x = find_x(Ax, Ay, Bx, By, Cx, Cy, Dy);

    printf("The value of x is: %d\n", x);

    // save coordinates to file for Python
    FILE *fp = fopen("coords.dat","w");
    fprintf(fp,"%d %d\n",Ax,Ay);
    fprintf(fp,"%d %d\n",Bx,By);
    fprintf(fp,"%d %d\n",x,Dy);
    fprintf(fp,"%d %d\n",Cx,Cy);
    fclose(fp);

    return 0;
}
