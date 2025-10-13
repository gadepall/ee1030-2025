#include <stdio.h>

int main() {
  FILE *fp;

  // -------------------
  // Question 2.9.15
  // -------------------


  fp = fopen("points.dat", "w");
  fprintf(fp, "%d,%d,%d\n", 2, 0, 0);  // A
  fprintf(fp, "%d,%d,%d\n", 6, 1, 0);  // B
  fprintf(fp, "%d,%d,%d\n", 2, 6, 0);  // C1
  fprintf(fp, "%d,%d,%d\n", 22/3, -14/3, 0);  // C2
  fclose(fp);
  return 0;
}
