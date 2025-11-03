#include <stdio.h>

int main() {
  FILE *fp;

  // -------------------
  // Question 2.5.32
  // -------------------


  fp = fopen("points.dat", "w");
  fprintf(fp, "%d,%d,%d\n", 7, 10, 0);  // A
  fprintf(fp, "%d,%d,%d\n", -2, 5, 0);   // B
  fprintf(fp, "%d,%d,%d\n", 3, 4, 0); // C
  fclose(fp);
  return 0;
}
