#include <stdio.h>

// function to solve the fractional knapsack problem
double fractionalKnapsack(double weight[], double value[], int n, double capacity) {
    double totalValue = 0.0;

    // calculate value-to-weight ratios for each item
    double ratios[n];
    for (int i = 0; i < n; i++) {
        ratios[i] = value[i] / weight[i];
    }

    // fill knapsack with items that have the highest value-to-weight ratios
    while (capacity > 0) {
        // find the item with the highest value-to-weight ratio
        int maxIndex = 0;
        double maxValue = 0.0;
        for (int i = 0; i < n; i++) {
            if (ratios[i] > maxValue) {
                maxValue = ratios[i];
                maxIndex = i;
            }
        }

        if (weight[maxIndex] <= capacity) {
            // add the entire item to the knapsack
            totalValue += value[maxIndex];
            capacity -= weight[maxIndex];
            ratios[maxIndex] = 0.0; // mark item as used
        } else {
            // add a fraction of the item to the knapsack
            double fraction = capacity / weight[maxIndex];
            totalValue += fraction * value[maxIndex];
            capacity = 0;
        }
    }

    return totalValue;
}

int main() {
    int n; // number of items
    double capacity; // knapsack capacity

    // prompt user for input
    printf("Enter the number of items: ");
    scanf("%d", &n);

    double weight[n]; // array to store the weights of each item
    double value[n]; // array to store the values of each item

    // prompt user for input for each item
    for (int i = 0; i < n; i++) {
        printf("Enter the weight and value of item %d: ", i+1);
        scanf("%lf %lf", &weight[i], &value[i]);
    }

    // prompt user for input for knapsack capacity
    printf("Enter the knapsack capacity: ");
    scanf("%lf", &capacity);

    // solve the fractional knapsack problem using greedy approach
    double totalValue = fractionalKnapsack(weight, value, n, capacity);

    // output the maximum total value that can be carried in the knapsack
    printf("Maximum total value that can be carried in the knapsack: %.2lf\n", totalValue);

    return 0;
}
