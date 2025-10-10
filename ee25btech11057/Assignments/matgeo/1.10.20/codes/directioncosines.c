#include <stdio.h>
#include <math.h>


// Function to compute direction cosines between two 3D points
void direction_cosines(double x1, double y1, double z1,
double x2, double y2, double z2,
double *l, double *m, double *n) {
double dx = x2 - x1;
double dy = y2 - y1;
double dz = z2 - z1;
double mag = sqrt(dx*dx + dy*dy + dz*dz);


*l = dx / mag;
*m = dy / mag;
*n = dz / mag;
}


// For testing in C directly
int main() {
double l, m, n;
direction_cosines(-2,4,-5, 1,2,3, &l,&m,&n);
printf("Direction cosines: (%lf, %lf, %lf)\n", l, m, n);
return 0;
}
