#include <stdio.h>

// function to perform insertion sort
void insertionSort(int arr[], int n) {
    int i, key, j;

    // iterate through the array
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;

        // move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while (j >= 0 && arr[j] > key) {
            arr[j+1] = arr[j];
            j = j-1;
        }
        arr[j+1] = key;
    }
}

int main() {
    int arr[] = {5, 2, 8, 3, 1}; // array to be sorted
    int n = sizeof(arr) / sizeof(int); // size of the array

    // sort the array using insertion sort
    insertionSort(arr, n);

    // output the sorted array
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
