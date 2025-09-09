#include <stdio.h>
#include <math.h>

int main() {
    // Normal vector of plane n = (2, -3, 6)
    double n[3] = {2.0, -3.0, 6.0};
    
    // Direction vector of x-axis a = (1, 0, 0)
    double a[3] = {1.0, 0.0, 0.0};
    
    // Dot product n · a
    double dot = n[0]*a[0] + n[1]*a[1] + n[2]*a[2];
    
    // Magnitudes ||n|| and ||a||
    double mag_n = sqrt(n[0]*n[0] + n[1]*n[1] + n[2]*n[2]);
    double mag_a = sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2]);
    
    // cos(theta) = (n · a) / (||n|| ||a||)
    double cos_theta = dot / (mag_n * mag_a);
    
    // theta = arccos(cos(theta)) in degrees
    double theta = acos(cos_theta) * 180.0 / M_PI;
    
    // Angle between plane and x-axis = 90° - theta
    double alpha = 90.0 - theta;
    
    printf("cos(theta) = %lf\n", cos_theta);
    printf("theta (angle between n and x-axis) = %lf degrees\n", theta);
    printf("alpha (angle between plane and x-axis) = %lf degrees\n", alpha);
    
    return 0;
}
