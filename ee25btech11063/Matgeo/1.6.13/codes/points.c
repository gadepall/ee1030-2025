#include <stdio.h>

int main() {
  FILE *fp;

  // -------------------
  // Question 1.6.13
  // -------------------


  fp = fopen("points.dat", "w");
  fprintf(fp, "%d,%d,%d\n", 0, 5, 0);  // A
  fprintf(fp, "%d,%d,%d\n", 0, -9, 0);   // B
  fprintf(fp, "%d,%d,%d\n", 3, 6, 0); // C
  fclose(fp);
  return 0;
  }
