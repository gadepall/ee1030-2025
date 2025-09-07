#include <stdio.h>

int main() {
  FILE *fp;

  // -------------------
  // Question 1.6.6 (a)
  // -------------------
  int k_a = 4; // Final answer
  printf("Q1.6.6 (a): k = %d\n", k_a);

  fp = fopen("points_a.dat", "w");
  fprintf(fp, "%d,%d,%d\n", 7, -2, 0);  // A
  fprintf(fp, "%d,%d,%d\n", 5, 1, 0);   // B
  fprintf(fp, "%d,%d,%d\n", 3, k_a, 0); // C
  fclose(fp);

  // -------------------
  // Question 1.6.6 (b)
  // -------------------
  int k_b = 3; // Final answer
  printf("Q1.6.6 (b): k = %d\n", k_b);

  fp = fopen("points_b.dat", "w");
  fprintf(fp, "%d,%d,%d\n", 8, 1, 0);    // A
  fprintf(fp, "%d,%d,%d\n", k_b, -4, 0); // B
  fprintf(fp, "%d,%d,%d\n", 2, -5, 0);   // C
  fclose(fp);

  return 0;
}
