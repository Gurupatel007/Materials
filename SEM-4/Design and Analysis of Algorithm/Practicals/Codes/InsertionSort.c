#include <stdio.h>
#include <time.h>
void insertion_sort(int[], int);
void main()
{
    int a[10000], n, i;
    time_t t;
    double time_taken;
    clock_t start, end;
    printf("Enter number of elements: ");
    scanf("%d", &n);
    srand((unsigned)time(&t));
    for (i = 0; i < n; i++)
    {
        a[i] = rand() % 1000;
    }
    printf("Random generated %d elements are: ", n);
    for (i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
    start = clock();
    insertion_sort(a, n);
    end = clock();
    printf("\nAfter insertion sort, elements are: ");
    for (i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
    time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    printf("\nTime taken by insertion sort for random unsorted array: %lf", time_taken);
    for (i = 0; i < n; i++)
    {
        a[i] = i + 1;
    }
    printf("\nSorted %d elements are: ", n);
    for (i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
    start = clock();
    insertion_sort(a, n);
    end = clock();
    printf("\nAfter insertion sort, elements are: ");
    for (i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
    time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    printf("\nTime taken by insertion sort for sorted array: %lf", time_taken);
}
void insertion_sort(int a[], int n)
{
    int i, j, temp;
    for (i = 1; i < n; i++)
    {
        temp = a[i];
        j = i - 1;
        while (j >= 0 && a[j] > temp)
        {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = temp;
    }
}
