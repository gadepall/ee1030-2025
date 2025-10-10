#include <stdio.h>
#include <math.h>

int main() {
    // Direction ratios of the line
    double dx = 2, dy = 3, dz = 6;
    
    // Normal vector of the plane
    double nx = 10, ny = 2, nz = -11;
    
    // Dot product of d and n
    double dot = dx * nx + dy * ny + dz * nz;
    
    // Magnitudes of d and n
    double mag_d = sqrt(dx*dx + dy*dy + dz*dz);
    double mag_n = sqrt(nx*nx + ny*ny + nz*nz);
    
    // Calculate the cosine of angle phi between d and n
    double cos_phi = fabs(dot) / (mag_d * mag_n);
    
    // Calculate phi in radians
    double phi = acos(cos_phi);
    
    // Angle between line and plane
    double theta = (M_PI / 2) - phi;
    
    // Convert to degrees
    double angle_degrees = theta * (180.0 / M_PI);
    
    printf("The angle between the line and the plane is: %.2f degrees\n", angle_degrees);
    
    return 0;
}
