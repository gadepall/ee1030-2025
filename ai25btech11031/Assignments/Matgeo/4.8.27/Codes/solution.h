  #ifndef PLANE_H
  #define PLANE_H

  #include <stdio.h>

  // Function to compute cross product of two vectors
  void cross_product(double a1, double b1, double c1,
                     double a2, double b2, double c2,
                     double *rx, double *ry, double *rz) {
      *rx = b1*c2 - c1*b2;
      *ry = c1*a2 - a1*c2;
      *rz = a1*b2 - b1*a2;
  }

  // Function to compute dot product of two vectors
  double dot_product(double a1, double b1, double c1,
                     double a2, double b2, double c2) {
      return a1*a2 + b1*b2 + c1*c2;
  }

  // Function to print plane equation given normal and point
  void plane_equation(double nx, double ny, double nz,
                      double x0, double y0, double z0) {
      double rhs = dot_product(nx, ny, nz, x0, y0, z0);
      printf("\nEquation of required plane: %.2lf*x + %.2lf*y + %.2lf*z = %.2lf\n",
             nx, ny, nz, rhs);
  }

  #endif

