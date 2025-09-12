#include <stdio.h>
#include <stdlib.h>

double *normal(double p[]) {

  double o[3] = {0, 0, 0};

  double *n = malloc(3 * sizeof(double));

  if (n == NULL)
    return NULL;

  n[0] = p[0] - o[0];
  n[1] = p[1] - o[1];
  n[2] = p[2] - o[2];

  return n;
}
