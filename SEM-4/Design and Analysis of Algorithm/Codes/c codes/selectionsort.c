#include <stdio.h>

// function to perform selection sort
void selectionSort(int arr[], int n) {
    int i, j, minIndex, temp;

    // iterate through the array
    for (i = 0; i < n-1; i++) {
        minIndex = i; // set the minimum index to the current index

        // find the index of the minimum element in the unsorted portion of the array
        for (j = i+1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }

        // swap the minimum element with the current element
        temp = arr[i];
        arr[i] = arr[minIndex];
        arr[minIndex] = temp;
    }
}

int main() {
    int arr[] = {5, 2, 8, 3, 1}; // array to be sorted
    int n = sizeof(arr) / sizeof(int); // size of the array

    // sort the array using selection sort
    selectionSort(arr, n);

    // output the sorted array
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
