#include <stdio.h>
//3.2.39

void compare(float a, float b){
    if (a > b){
    printf("-5/11>5/-11\n");
    }

    else if (a < b) {
        printf("-5/11<5/-11\n");
    }
    else {
	printf("-5/11=5/-11\n");
    }
}
int main() {
    float a = -5.0 / 11.0;
    float b = 5.0 / -11.0;

    compare(a,b);

    return 0;
}


