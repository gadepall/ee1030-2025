#include <stdio.h>

int main() {
  FILE *fp;

  // -------------------
  // Question 5.5.16
  // -------------------


  fp = fopen("points.dat", "w");
  fprintf(fp, "%d,%d,%d\n", 2, -3, 5); // A
  fprintf(fp, "%d,%d,%d\n", 3, -2, -4); // B
  fprintf(fp, "%d,%d,%d\n", 1, 1, -2); // C
  fprintf(fp, "%f,%f,%f\n", 27/35, -2/35, 13/7); // P
  fclose(fp);
  return 0;
}
