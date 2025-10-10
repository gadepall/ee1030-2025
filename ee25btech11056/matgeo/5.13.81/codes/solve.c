#include <stdio.h>

int main() {

  int count = 0;
  int a, b, c, d, e;

  for (a = 0; a <= 1; a++) {

    for (b = 0; b <= 1; b++) {

      for (c = 0; c <= 1; c++) {

        for (d = 0; d <= 1; d++) {

          for (e = 0; e <= 1; e++) {

            int k1 = a - d;
            int k2 = d - e;

            int a[3][3] = {{0, 1, c}, {0, k1, k2}, {1, b, e}};

            int c = a[0][1] * a[1][2] - a[0][2] * a[1][1];

            if (c == (-1) || c == 1) {
              count++;
            }
          }
        }
      }
    }
  }

  printf("The number of possible matrices is : %d\n", count);

  return 0;
}
