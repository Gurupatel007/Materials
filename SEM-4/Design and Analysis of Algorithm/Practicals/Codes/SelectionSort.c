#include <stdio.h>
#include <time.h>
void selection_sort(int[], int);
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
    selection_sort(a, n);
    end = clock();
    printf("\nAfter selection sort, elements are: ");
    for (i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
    time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    printf("\nTime taken by selection sort for random unsorted array: %lf", time_taken);
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
    selection_sort(a, n);
    end = clock();
    printf("\nAfter selection sort, elements are: ");
    for (i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
    time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    printf("\nTime taken by selection sort for sorted array: %lf", time_taken);
}
void selection_sort(int a[], int n)
{
    int i, j, min, temp;
    for (i = 0; i < n - 1; i++)
    {
        min = i;
        for (j = i + 1; j < n; j++)
        {
            if (a[min] > a[j])
            {
                min = j;
            }
        }
        if (min != i)
        {
            temp = a[i];
            a[i] = a[min];
            a[min] = temp;
        }
    }
}
