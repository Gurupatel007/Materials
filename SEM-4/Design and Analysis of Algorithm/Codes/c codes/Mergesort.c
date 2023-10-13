#include <stdio.h>

// function to merge two subarrays into a single sorted array
void merge(int arr[], int left[], int right[], int left_size, int right_size) {
    int i = 0, j = 0, k = 0;

    // merge the two subarrays into a single sorted array
    while (i < left_size && j < right_size) {
        if (left[i] <= right[j]) {
            arr[k++] = left[i++];
        } else {
            arr[k++] = right[j++];
        }
    }

    // copy any remaining elements from the left subarray
    while (i < left_size) {
        arr[k++] = left[i++];
    }

    // copy any remaining elements from the right subarray
    while (j < right_size) {
        arr[k++] = right[j++];
    }
}

// function to perform Merge sort
void mergeSort(int arr[], int n) {
    if (n < 2) {
        return;
    }

    int mid = n / 2; // find the middle index of the array

    // create left and right subarrays
    int left[mid], right[n - mid];
    for (int i = 0; i < mid; i++) {
        left[i] = arr[i];
    }
    for (int i = mid; i < n; i++) {
        right[i - mid] = arr[i];
    }

    // recursively sort the left and right subarrays
    mergeSort(left, mid);
    mergeSort(right, n - mid);

    // merge the sorted subarrays into a single sorted array
    merge(arr, left, right, mid, n - mid);
}

int main() {
    int arr[] = {5, 2, 8, 3, 1}; // array to be sorted
    int n = sizeof(arr) / sizeof(int); // size of the array

    // sort the array using Merge sort
    mergeSort(arr, n);

    // output the sorted array
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
