#include <stdio.h>

// function to swap two elements
void swap(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

// function to partition the array
int partition(int arr[], int low, int high) {
    int pivot = arr[high]; // choose pivot element
    int i = low - 1; // index of smaller element

    for (int j = low; j <= high - 1; j++) {
        // if current element is smaller than or equal to pivot
        if (arr[j] <= pivot) {
            i++; // increment index of smaller element
            swap(&arr[i], &arr[j]); // swap arr[i] and arr[j]
        }
    }
    swap(&arr[i + 1], &arr[high]); // swap arr[i + 1] and arr[high]
    return i + 1;
}

// function to perform Quick sort
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        // partition the array and get the index of the pivot element
        int pi = partition(arr, low, high);

        // recursively sort the elements before and after the pivot element
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main() {
    int arr[] = {5, 2, 8, 3, 1}; // array to be sorted
    int n = sizeof(arr) / sizeof(int); // size of the array

    // sort the array using Quick sort
    quickSort(arr, 0, n - 1);

    // output the sorted array
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
