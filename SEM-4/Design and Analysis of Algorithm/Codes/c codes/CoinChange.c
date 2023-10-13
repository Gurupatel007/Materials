#include <stdio.h>
#include <limits.h>

int min(int a, int b) {
    return (a < b) ? a : b;
}

void printCoinsUsed(int coins[], int n, int dp[], int amount) {
    printf("Coins used: ");

    while (amount > 0) {
        for (int i = 0; i < n; i++) {
            if (coins[i] <= amount && dp[amount-coins[i]] + 1 == dp[amount]) {
                printf("%d ", coins[i]);
                amount -= coins[i];
                break;
            }
        }
    }

    printf("\n");
}

int minCoins(int coins[], int n, int amount) {
    int dp[amount+1];
    dp[0] = 0;

    for (int i = 1; i <= amount; i++) {
        dp[i] = INT_MAX;
    }

    for (int i = 1; i <= amount; i++) {
        for (int j = 0; j < n; j++) {
            if (coins[j] <= i) {
                int sub_res = dp[i-coins[j]];
                if (sub_res != INT_MAX && sub_res + 1 < dp[i]) {
                    dp[i] = sub_res + 1;
                }
            }
        }
    }

    printCoinsUsed(coins, n, dp, amount);

    return dp[amount];
}

int main() {
    int coins[] = {1,2,4,5}; // available coin denominations
    int num_coins = 4; // number of available coin denominations
    int amount; // the amount for which to make change

    // prompt user for input
    printf("Enter the amount for which to make change: ");
    scanf("%d", &amount);

    // compute minimum number of coins required using dynamic programming
    int num_of_coins = minCoins(coins, num_coins, amount);

    // output the number of coins used to make change
    printf("Minimum number of coins required: %d\n", num_of_coins);

    return 0;
}
