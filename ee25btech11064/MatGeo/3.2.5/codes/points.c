#include <stdio.h>

int main() {
  FILE *fp;

  // -------------------
  // Question 3.2.5
  // -------------------


  fp = fopen("points.dat", "w");
  fprintf(fp, "%f,%f,%f\n", 2.25, 3.31, 0.00);  // A
  fprintf(fp, "%d,%d,%d\n", 0, 0, 0);   // B
  fprintf(fp, "%d,%d,%d\n", 6, 0, 0); // C
  fclose(fp);
  return 0;
}
