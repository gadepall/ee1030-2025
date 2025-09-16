#include <stdio.h>
#include <math.h>

double angleWithYAxis(double vx, double vy, double vz) {
    double e2y = 1.0;
    double dot = vy * e2y;
    double magv = sqrt(vx*vx + vy*vy + vz*vz);
    double mage2 = 1.0;
    double cosTheta = dot / (magv * mage2);
    double thetaRad = acos(cosTheta);
    double thetaDeg = thetaRad * 180.0 / M_PI;
    return thetaDeg;
}

int main() {
    double vx = 1, vy = -1, vz = 2;
    double theta = angleWithYAxis(vx, vy, vz);
    printf("Angle with positive Y-axis = %.2f degrees\n", theta);
    return 0;
}
