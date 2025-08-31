#include <stdio.h>

typedef struct { double x,y,z; } Point;

void save_points() {
    Point pts[4]={{-1,2,1},{1,-2,5},{4,-7,8},{2,-3,4}};
    FILE *f=fopen("points.dat","w");
    for(int i=0;i<4;i++)
        fprintf(f,"%f %f %f\n",pts[i].x,pts[i].y,pts[i].z);
    fclose(f);
}

int main() {
    save_points();
    return 0;
}

