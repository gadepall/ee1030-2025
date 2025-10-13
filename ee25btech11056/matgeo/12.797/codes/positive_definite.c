#include <math.h>
#include <stdio.h>

// Function to check both statements (I) and (II)
int check_statements(double A[][10], int n) {
  int i, j;
  double B[10][10];
  double det;

  // --- Step 1: Check if A is symmetric ---
  for (i = 0; i < n; i++) {
    for (j = 0; j < n; j++) {
      if (fabs(A[i][j] - A[j][i]) > 1e-6)
        return 0; // Not symmetric → both fail
    }
  }

  // --- Step 2: Check Statement (I) ---
  // There exists c >= 0 such that A + cI is positive definite
  int statement_I = 0;
  for (double c = 0; c <= 100; c += 1.0) {
    // Form B = A + cI
    for (i = 0; i < n; i++) {
      for (j = 0; j < n; j++) {
        if (i == j)
          B[i][j] = A[i][j] + c;
        else
          B[i][j] = A[i][j];
      }
    }

    // Check positive definiteness using leading principal minors
    int positive = 1;
    if (n >= 1) {
      det = B[0][0];
      if (det <= 0)
        positive = 0;
    }
    if (n >= 2 && positive) {
      det = B[0][0] * B[1][1] - B[0][1] * B[1][0];
      if (det <= 0)
        positive = 0;
    }
    if (n >= 3 && positive) {
      det = B[0][0] * (B[1][1] * B[2][2] - B[1][2] * B[2][1]) -
            B[0][1] * (B[1][0] * B[2][2] - B[1][2] * B[2][0]) +
            B[0][2] * (B[1][0] * B[2][1] - B[1][1] * B[2][0]);
      if (det <= 0)
        positive = 0;
    }

    if (positive) {
      statement_I = 1;
      break;
    }
  }

  // --- Step 3: Check Statement (II) ---
  // If A is symmetric and positive definite, then there exists B s.t. A = B^2
  // For symmetric PD matrices, this is always true
  int statement_II = 1;
  // But we must check if A is actually positive definite
  int positive_A = 1;
  if (n >= 1) {
    det = A[0][0];
    if (det <= 0)
      positive_A = 0;
  }
  if (n >= 2 && positive_A) {
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0];
    if (det <= 0)
      positive_A = 0;
  }
  if (n >= 3 && positive_A) {
    det = A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1]) -
          A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0]) +
          A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]);
    if (det <= 0)
      positive_A = 0;
  }

  if (!positive_A)
    statement_II = 0;

  // --- Step 4: Final Decision ---
  if (statement_I && statement_II)
    return 1;
  else
    return 0;
}
