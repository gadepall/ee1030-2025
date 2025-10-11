#include <stdio.h>

int main() {
  FILE *fp;

  // -------------------
  // Question 1.11.1
  // -------------------


  fp = fopen("points.dat", "w");
  fprintf(fp, "%d,%d,%d\n", 3, 3, 3);  // 1
  fprintf(fp, "%d,%d,%d\n", -3, -3, -3);   // 2
  fclose(fp);
  return 0;
  }