#include <stdio.h>

/**
 * @file compile_time_lu.c
 * @brief Analyzes LU factorization at compile time using the preprocessor.
 *
 * The logic to determine the truthiness of statements P and Q is resolved
 * before the program is compiled. The runtime executable only contains the
 * final, pre-determined answer.
 */

// --- Matrix P Definition ---
// A = [[P_00, P_01], [P_10, P_11]]
#define P_00 0
#define P_01 5
#define P_10 0
#define P_11 7

// --- Matrix Q Definition ---
// A = [[Q_00, Q_01], [Q_10, Q_11]]
#define Q_00 0
#define Q_01 0
#define Q_10 2
#define Q_11 5

// --- COMPILE-TIME ANALYSIS ---
// The preprocessor will evaluate these #if statements.

// Analyze Statement P: "P has infinitely many LU factorizations"
// This is TRUE if A[0][0] is 0 AND A[1][0] is 0, leading to 0 = 0.
#if P_00 == 0 && P_10 == 0
  #define P_IS_TRUE 1
#else
  #define P_IS_TRUE 0
#endif

// Analyze Statement Q: "Q has no LU factorization"
// This is TRUE if A[0][0] is 0 AND A[1][0] is not 0, leading to 0 = non-zero.
#if Q_00 == 0 && Q_10 != 0
  #define Q_IS_TRUE 1
#else
  #define Q_IS_TRUE 0
#endif


int main() {
    printf("This conclusion was determined entirely at COMPILE TIME.\n");
    printf("The running program is just printing the pre-calculated result.\n\n");

    // The preprocessor uses the P_IS_TRUE and Q_IS_TRUE macros
    // to select ONLY ONE of the following printf statements to
    // include in the final compiled program.
    #if P_IS_TRUE && Q_IS_TRUE
      printf("Conclusion: Both P and Q are TRUE. The correct option is (b).\n");
    #elif P_IS_TRUE && !Q_IS_TRUE
      printf("Conclusion: P is TRUE and Q is FALSE. The correct option is (a).\n");
    #elif !P_IS_TRUE && Q_IS_TRUE
      printf("Conclusion: P is FALSE and Q is TRUE. The correct option is (c).\n");
    #else
      printf("Conclusion: Both P and Q are FALSE. The correct option is (d).\n");
    #endif
    return 0;
}