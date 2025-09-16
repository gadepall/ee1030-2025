#include <stdio.h>
#include <math.h>

typedef struct { double x, y, z; } V3;

static inline double dot(V3 a, V3 b){ 
    return a.x*b.x + a.y*b.y + a.z*b.z; 
}
static inline double norm(V3 a){ 
    return sqrt(dot(a,a)); 
}

int main(void){
    V3 a, b, c;
    scanf("%lf %lf %lf %lf %lf %lf", &a.x, &a.y, &a.z, &b.x, &b.y, &b.z);

    // Compute c = sqrt(3)*a - b
    c.x = sqrt(3)*a.x - b.x;
    c.y = sqrt(3)*a.y - b.y;
    c.z = sqrt(3)*a.z - b.z;

    printf("Norm of c = %lf\n", norm(c));

    double theta = acos(dot(a,b)/(norm(a)*norm(b)));
    printf("Angle (radians) = %lf\n", theta);
    printf("Angle (degrees) = %lf\n", theta*180.0/M_PI);

    return 0;
}
