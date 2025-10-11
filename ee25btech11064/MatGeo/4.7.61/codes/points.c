#include <stdio.h>

int main() {
  FILE *fp;

  // -------------------
  // Question 4.7.61
  // -------------------


  fp = fopen("points.dat", "w");
  fprintf(fp, "%d,%d,%d\n", 2, -3, 4);  // n
  fclose(fp);
  return 0;
}
