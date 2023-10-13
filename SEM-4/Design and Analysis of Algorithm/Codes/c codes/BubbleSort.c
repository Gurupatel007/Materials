#include <stdio.h>

// function to perform bubble sort
void bubbleSort(int arr[], int n) {
    int i, j, temp;

    // iterate through the array
    for (i = 0; i < n-1; i++) {
        // iterate through the unsorted portion of the array
        for (j = 0; j < n-i-1; j++) {
            // swap adjacent elements if they are in the wrong order
            if (arr[j] > arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main() {
    int arr[] = {5, 2, 8, 3, 1}; // array to be sorted
    int n = sizeof(arr) / sizeof(int); // size of the array

    // sort the array using bubble sort
    bubbleSort(arr, n);

    // output the sorted array
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
