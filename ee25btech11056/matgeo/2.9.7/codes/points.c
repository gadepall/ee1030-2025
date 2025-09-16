#include <math.h>
#include <stdio.h>

// Function to compute dot product
double dot(double u[3], double v[3]) {
  return u[0] * v[0] + u[1] * v[1] + u[2] * v[2];
}

// Function to compute determinant of 3x3 matrix
double det3(double M[3][3]) {
  return M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) -
         M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0]) +
         M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]);
}

// Function to compute box product using Gram matrix
double box_product() {
  double a[3] = {2, 1, 3};
  double b[3] = {-1, 2, 1};
  double c[3] = {3, 1, 2};

  double G[3][3] = {{dot(a, a), dot(a, b), dot(a, c)},
                    {dot(b, a), dot(b, b), dot(b, c)},
                    {dot(c, a), dot(c, b), dot(c, c)}};

  double detG = det3(G);

  // Negative since left-handed system
  double box = -sqrt(detG);

  return box;
}
