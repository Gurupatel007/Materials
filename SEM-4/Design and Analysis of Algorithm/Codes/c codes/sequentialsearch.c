#include <stdio.h>

// function to perform sequential search and count the number of steps executed
int sequentialSearch(int arr[], int n, int key, int *steps) {
    *steps = 0; // initialize the step count to 0
    for (int i = 0; i < n; i++) {
        (*steps)++; // increment the step count for each comparison
        if (arr[i] == key) {
            return i; // return the index of the key if found
        }
    }
    return -1; // return -1 if the key is not found
}

int main() {
    int arr[] = {1, 2, 3, 4, 5}; // array to search
    int n = sizeof(arr) / sizeof(int); // size of the array
    int key = 3; // key to search for
    int steps; // variable to store the number of steps executed

    // search for the key in the array
    int index = sequentialSearch(arr, n, key, &steps);

    // output the results
    if (index != -1) {
        printf("Key found at index %d\n", index);
    } else {
        printf("Key not found\n");
    }
    printf("Steps executed: %d\n", steps);

    return 0;
}
