#include <stdio.h>

int main() {
  FILE *fp;

  // -------------------
  // Question 1.6.14
  // -------------------


  fp = fopen("points.dat", "w");
  fprintf(fp, "%d,%d,%d\n", 3, 1, 0);  // A
  fprintf(fp, "%d,%d,%d\n", 12, -2, 0);   // B
  fprintf(fp, "%d,%d,%d\n", 0, 2, 0); // C
  fclose(fp);
  return 0;
  }