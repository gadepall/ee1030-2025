#include <math.h>
#include <stdio.h>

void ellipse(double *c, double *e, double f1[], double f2[], double vert[],
             double n[]) {

  n[0] = f1[0] - f2[0];
  n[1] = f1[1] - f2[1];

  double mod = sqrt(n[0] * n[0] + n[1] * n[1]);

  n[0] /= mod;
  n[1] /= mod;

  *e = f1[1] / vert[1];

  double k = (*e) * (*e);

  *c = f1[1] / (k);
}
