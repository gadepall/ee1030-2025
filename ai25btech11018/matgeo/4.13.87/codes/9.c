#include <stdio.h>

// This function calculates the value of mu
double solve_mu() {
    // Coordinates of point P(3, 2, 6)
    double px = 3.0;
    double py = 2.0;
    double pz = 6.0;

    // Components of the starting point of the line: (1, -1, 2)
    double rx = 1.0;
    double ry = -1.0;
    double rz = 2.0;

    // Components of the direction vector of the line: (-3, 1, 5)
    double vx = -3.0;
    double vy = 1.0;
    double vz = 5.0;

    // Normal vector components of the plane: (1, -4, 3)
    double nx = 1.0;
    double ny = -4.0;
    double nz = 3.0;

    // The vector PQ is calculated as Q - P, where Q = r + mu*v
    // PQ = ( (rx + mu*vx) - px, (ry + mu*vy) - py, (rz + mu*vz) - pz )
    // PQ = ( (1 + mu*(-3)) - 3, (-1 + mu*1) - 2, (2 + mu*5) - 6 )
    // PQ = ( -2 - 3*mu, -3 + mu, -4 + 5*mu )

    // The condition for PQ to be parallel to the plane is that its dot product
    // with the plane's normal vector n is zero.
    // PQ . n = 0
    // (-2 - 3*mu)*nx + (-3 + mu)*ny + (-4 + 5*mu)*nz = 0
    
    // ((-2 - 3*mu)*1) + ((-3 + mu)*-4) + ((-4 + 5*mu)*3) = 0
    // -2 - 3*mu + 12 - 4*mu - 12 + 15*mu = 0
    // Collect mu terms: (-3 - 4 + 15)*mu = 8*mu
    // Collect constant terms: -2 + 12 - 12 = -2
    // So, 8*mu - 2 = 0
    // 8*mu = 2
    // mu = 2 / 8
    
    // The coefficients of the linear equation for mu: A*mu + B = 0
    // A = vx*nx + vy*ny + vz*nz - (dot product of direction vector with normal vector)
    double A = vx * nx + vy * ny + vz * nz;
    
    // B = (rx - px)*nx + (ry - py)*ny + (rz - pz)*nz - (dot product of position vector PQ with normal vector)
    double B = (rx - px) * nx + (ry - py) * ny + (rz - pz) * nz;

    // Solve for mu
    double mu = -B / A;
    
    return mu;
}

int main() {
    double result = solve_mu();
    printf("The value of mu is: %f\n", result);
    return 0;
}
