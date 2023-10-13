#include <stdio.h>

void printCoinsUsed(int coins[], int n, int amount) {
    printf("Coins used: ");

    for (int i = n-1; i >= 0; i--) {
        while (amount >= coins[i]) {
            printf("%d ", coins[i]);
            amount -= coins[i];
        }
    }

    printf("\n");
}

int minCoins(int coins[], int n, int amount) {
    int num_of_coins = 0;

    for (int i = n-1; i >= 0; i--) {
        while (amount >= coins[i]) {
            num_of_coins++;
            amount -= coins[i];
        }
    }

    printCoinsUsed(coins, n, amount);

    return num_of_coins;
}

int main() {
    int coins[] = {1, 5, 10, 25}; // available coin denominations
    int num_coins = 4; // number of available coin denominations
    int amount; // the amount for which to make change

    // prompt user for input
    printf("Enter the amount for which to make change: ");
    scanf("%d", &amount);

    // compute minimum number of coins required using greedy approach
    int num_of_coins = minCoins(coins, num_coins, amount);

    // output the number of coins used to make change
    printf("Minimum number of coins required: %d\n", num_of_coins);

    return 0;
}
