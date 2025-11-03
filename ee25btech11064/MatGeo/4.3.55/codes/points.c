#include <stdio.h>

int main() {
  FILE *fp;

  // -------------------
  // Question 4.3.55
  // -------------------


  fp = fopen("points.dat", "w");
  fprintf(fp, "%d,%d,%d\n", 2, 5, -3);  // R
  fprintf(fp, "%d,%d,%d\n", -2, -3, 5);   // S
  fprintf(fp, "%d,%d,%d\n", 5, 3, -3); // T
  fclose(fp);
  return 0;
}
