#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// function to swap two elements in an array
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// function to partition the array
int partition(int arr[], int low, int high) {
    int pivot = arr[high]; // choose the last element as the pivot
    int i = low - 1; // index of smaller element

    for (int j = low; j <= high - 1; j++) {
        // if the current element is smaller than or equal to the pivot
        if (arr[j] <= pivot) {
            i++; // increment index of smaller element
            swap(&arr[i], &arr[j]); // swap arr[i] and arr[j]
        }
    }

    swap(&arr[i + 1], &arr[high]); // swap arr[i + 1] and arr[high]
    return i + 1; // return the partition index
}

// function to perform Randomized Quicksort
void randomizedQuicksort(int arr[], int low, int high) {
    if (low < high) {
        // generate a random number between low and high
        srand(time(NULL));
        int random = low + rand() % (high - low + 1);

        // swap the randomly chosen element with the last element
        swap(&arr[random], &arr[high]);

        // partition the array and get the partition index
        int pi = partition(arr, low, high);

        // recursively sort the left and right subarrays
        randomizedQuicksort(arr, low, pi - 1);
        randomizedQuicksort(arr, pi + 1, high);
    }
}

int main() {
    int arr[] = {5, 2, 8, 3, 1}; // array to be sorted
    int n = sizeof(arr) / sizeof(int); // size of the array

    // sort the array using Randomized Quicksort
    randomizedQuicksort(arr, 0, n - 1);

    // output the sorted array
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
