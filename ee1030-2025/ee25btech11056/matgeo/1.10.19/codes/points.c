#include <stdio.h>

int main() {
  FILE *fp;

  // Endpoint of the vector with direction ratios (2, -1, -2)
  int x = 2, y = -1, z = -2;

  // Save origin and endpoint into file
  fp = fopen("points.dat", "w");
  fprintf(fp, "%d,%d,%d\n", 0, 0, 0); // Origin
  fprintf(fp, "%d,%d,%d\n", x, y, z); // Endpoint
  fclose(fp);

  return 0;
}
