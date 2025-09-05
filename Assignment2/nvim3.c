#include <stdio.h>

int main() {
    float costPrice = 10000;    
    float profitPercent = 20;  
    float sellingPrice;

    
    sellingPrice = costPrice + (costPrice * profitPercent / 100);

    
    printf("Selling Price = ₹%.2f\n", sellingPrice);

    return 0;
}