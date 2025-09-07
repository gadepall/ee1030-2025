#include <stdio.h>

// Function to return relation value  (0 => COLLINEAR)
int relation(int a, int b) {
    return b - 2*a;   // For A(1,2), O(0,0), C(a,b): collinear <=> b - 2a = 0
}

int main(void) {
    // Given points: A(1,2) and O(0,0)
    int x1 = 0, y1 = 0;   // O
    int x2 = 1, y2 = 2;   // A

    // Step 1: Compute slope of line through O and A
    float m = (float)(y2 - y1) / (x2 - x1);

    printf("Step 1: Compute slope using two points O(0,0) and A(1,2):\n");
    printf("        m = (y2 - y1) / (x2 - x1) = (%d - %d) / (%d - %d) = %.2f\n\n",
           y2, y1, x2, x1, m);

    // Step 2: Point-slope form using point O(0,0)
    printf("Step 2: Equation using point-slope form (through O):\n");
    printf("        (y - %d) = m (x - %d)\n", y1, x1);
    printf("        => y = m x\n\n");

    // Step 3: Substitute m = 2 (from Step 1)
    printf("Step 3: With m = %.0f, the line is:  y = 2x\n\n", m);

    // Step 4: Final relation for C(a,b) lying on this line
    printf("Step 4: Substitute C(a,b) into y = 2x  =>  b = 2a\n");
    printf("Final Relation: b - 2a = 0\n\n");

    // (Optional) quick test: uncomment to verify with numbers
    // int a = 3, b = 6;
    // printf("Test with a=%d, b=%d -> residual (b - 2a) = %d\n", a, b, relation(a,b));

    return 0;
}

