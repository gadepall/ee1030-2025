#include <stdio.h>

int main() {
  FILE *fp;

  // -------------------
  // Question 4.13.68
  // -------------------


  fp = fopen("points.dat", "w");
  fprintf(fp, "%d,%d,%d\n", 5, 4, 0);  // n1 c1
  fprintf(fp, "%d,%d,%d\n", 1, 2, 10);   // n2 c2
  fprintf(fp, "%d,%d,%d\n", 2, 1, -5); // n3 c3
  fclose(fp);
  return 0;
}
